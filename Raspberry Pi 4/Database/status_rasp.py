
# -*- coding: utf-8 -*-

import psutil
import mysql.connector

# Conectar ao banco de dados
db_config = {
    'user': 'christv',
    'password': 'icts12345',
    'host': '192.168.50.110',
    'database': 'acesso_casa',
}
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Coletar dados do Raspberry Pi
cpu_temperature = 45.0  # Exemplo: temperatura da CPU em Celsius
cpu_usage = psutil.cpu_percent()
ram_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('/').percent

# Inserir dados na tabela raspberry_data
cursor.execute("INSERT INTO raspberry_data (cpu_temperature, cpu_usage, ram_usage, disk_usage) VALUES (%s, %s, %s, %s)", (cpu_temperature, cpu_usage, ram_usage, disk_usage))
conn.commit()

# Fechar conexão com o banco de dados
cursor.close()
conn.close()
