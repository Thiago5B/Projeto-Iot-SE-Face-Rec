# -*- coding: utf-8 -*-

import os
import cv2
import face_recognition
import numpy as np
import datetime
import mysql.connector

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

# Função para salvar a imagem, encoding e nome no banco de dados
def save_image_and_encoding_to_db(image, encoding, timestamp, name):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Converte a imagem para bytes
        _, buffer = cv2.imencode('.jpg', image)
        image_bytes = buffer.tobytes()

        # Converte o encoding para uma string separada por vírgulas
        encoding_str = ','.join(map(str, encoding))

        # Insere a imagem, encoding e nome no banco de dados
        cursor.execute("INSERT INTO cadastro (data_hora, imagem, encoding, name) VALUES (%s, %s, %s, %s)", 
                       (timestamp, image_bytes, encoding_str, name))
        conn.commit()

    except mysql.connector.Error as error:
        print("Erro ao conectar ou inserir dados no banco de dados:", error)
    
    finally:
        cursor.close()
        conn.close()

# Inicializa a câmera
camera = cv2.VideoCapture(0)

# Define a resolução da câmera para uma mais baixa para melhorar a taxa de quadros
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

name = input("Digite o nome da pessoa: ")

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

    # Desenha retângulos ao redor dos rostos detectados
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # Mostra o quadro capturado
    cv2.imshow('Camera', frame)

    # Aguarda por uma tecla para tirar a foto e salvar no banco de dados
    if cv2.waitKey(1) & 0xFF == ord('q'):
        if face_locations:
            timestamp = datetime.datetime.now()
            for encoding in face_encodings:
                save_image_and_encoding_to_db(frame, encoding, timestamp, name)
            print("Imagem, encoding e nome salvos no banco de dados.")
        else:
            print("Nenhum rosto detectado.")
        break

# Libera a câmera e fecha as janelas
camera.release()
cv2.destroyAllWindows()
