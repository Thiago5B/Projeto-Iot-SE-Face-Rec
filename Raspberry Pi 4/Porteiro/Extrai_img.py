#-*- coding: utf-8 -*-

import mysql.connector
import cv2
import numpy as np

# Configurações do banco de dados
db_config = {
    'user': 'christv',
    'password': 'icts12345',
    'host': '192.168.50.110',
    'database': 'acesso_casa',
}

def fetch_and_show_image():
    try:
        # Conecta ao banco de dados
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Executa a consulta para obter a última imagem inserida
        cursor.execute("SELECT imagem FROM registros ORDER BY id DESC LIMIT 1")
        result = cursor.fetchone()

        if result:
            # Extrai os bytes da imagem
            image_bytes = result[0]

            # Converte os bytes da imagem para um array NumPy
            np_array = np.frombuffer(image_bytes, dtype=np.uint8)

            # Decodifica o array NumPy em uma imagem
            img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

            # Mostra a imagem usando OpenCV
            cv2.imshow('Imagem Recuperada do Banco de Dados', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Nenhuma imagem encontrada no banco de dados.")

    except mysql.connector.Error as error:
        print("Erro ao conectar ou buscar dados no banco de dados:", error)
    
    finally:
        cursor.close()
        conn.close()

# Executa a função para buscar e mostrar a imagem
fetch_and_show_image()
