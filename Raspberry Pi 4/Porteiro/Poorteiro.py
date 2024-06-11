# -*- coding: utf-8 -*-

import os
import cv2
import face_recognition
import numpy as np
import datetime
import mysql.connector
import RPi.GPIO as GPIO
import time

# Configurações do banco de dados
db_config = {
    'user': 'christv',
    'password': 'icts12345',
    'host': '192.168.50.110',
    'database': 'acesso_casa',
}

# Definir variáveis de ambiente para QT
os.environ['QT_PLUGIN_PATH'] = '/home/chrispi/myenv/lib/python3.11/site-packages/cv2/qt/plugins'
os.environ['QT_QPA_PLATFORM'] = 'xcb'

# Configuração da GPIO
GPIO.setwarnings(False)  # Desabilita avisos do GPIO
GPIO.cleanup()  # Limpa qualquer configuração anterior dos pinos GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT ,initial=GPIO.HIGH)  # Usando GPIO 18 para o pulso de 5V

# Função para carregar os encodings e nomes do banco de dados
def load_encodings_from_db():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT name, encoding FROM cadastro")
        rows = cursor.fetchall()
        
        known_encodings = []
        known_names = []

        for row in rows:
            name = row[0]
            encoding_str = row[1]
            encoding = np.array(list(map(float, encoding_str.split(','))))
            known_encodings.append(encoding)
            known_names.append(name)

    except mysql.connector.Error as error:
        print("Erro ao conectar ou recuperar dados do banco de dados:", error)
    
    finally:
        cursor.close()
        conn.close()
    
    return known_encodings, known_names

# Função para salvar a entrada no banco de dados
def save_entry_to_db(image, timestamp, name):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Converte a imagem para bytes
        _, buffer = cv2.imencode('.jpg', image)
        image_bytes = buffer.tobytes()

        # Insere a imagem, timestamp e nome no banco de dados
        cursor.execute("INSERT INTO entradas (data_hora, imagem, name) VALUES (%s, %s, %s)", 
                       (timestamp, image_bytes, name))
        conn.commit()

    except mysql.connector.Error as error:
        print("Erro ao conectar ou inserir dados no banco de dados:", error)
    
    finally:
        cursor.close()
        conn.close()

# Função para enviar um pulso de 5V para a porta GPIO
def send_gpio_pulse():
    GPIO.output(18, GPIO.LOW)
    time.sleep(1)
    GPIO.output(18, GPIO.HIGH)

# Inicializa a câmera
camera = cv2.VideoCapture(0)

# Define a resolução da câmera para uma mais baixa para melhorar a taxa de quadros
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Carrega os encodings e nomes conhecidos do banco de dados
known_encodings, known_names = load_encodings_from_db()

last_saved_time = None
known_person_last_seen = {}

while True:
    # Captura um quadro da câmera
    ret, frame = camera.read()
    if not ret:
        break

    # Redimensiona o quadro para acelerar o processamento de detecção de rostos
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])  # Converte o quadro para RGB

    # Detecta os rostos e seus encodings na imagem redimensionada
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    # Redimensiona novamente as coordenadas dos rostos
    face_locations = [(top * 4, right * 4, bottom * 4, left * 4) for (top, right, bottom, left) in face_locations]

    # Inicializa uma lista de nomes para rostos detectados
    face_names = []

    for face_encoding in face_encodings:
        # Verifica se o rosto detectado corresponde a algum rosto conhecido
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Desconhecido"

        # Usa o primeiro match encontrado
        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]

        face_names.append(name)

        # Salva a entrada no banco de dados se for um rosto conhecido
        if name != "Desconhecido":
            current_time = datetime.datetime.now()
            if name not in known_person_last_seen or (current_time - known_person_last_seen[name]).total_seconds() > 5:
                save_entry_to_db(frame, current_time, name)
                send_gpio_pulse()
                known_person_last_seen[name] = current_time
                print(f"Entrada liberada para {name} as {current_time}")

    # Desenha retângulos ao redor dos rostos detectados e escreve os nomes
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Mostra o quadro capturado
    cv2.imshow('Camera', frame)

    # Aguarda por uma tecla para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera e fecha as janelas
camera.release()
cv2.destroyAllWindows()
GPIO.cleanup()
