# coding=utf-8
# Código del Cliente

import socket

HOST = 'localhost'    # La dirección de host con el que vamos a conectar.
PORT = 9999         # Por que puerto vamos a realizar la conexión

# Creamos el socket para el Cliente
sClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Mandamos la petición de conexión al servidor
sClient.connect((HOST, PORT))

# El socket Cliente espera la respuesta con la información del Servidor
data = sClient.recv(4096)

# Se muestra por pantalla la información recibida
print("La hora es: " + data.decode())

# Se cierra el socket
sClient.close()
