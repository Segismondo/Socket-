

import socket
import sys

HOST= 'localhost'
PORT= 9999

try:
        s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print ('Socket created')
except socket.error:
        print ('Fallo al crear socket: ')
        sys.exit()
try:
        s.bind((HOST, PORT))
except socket.error:
        print ('Error')
        sys.exit()

print ('Puerto establecido correctamente')

import datetime


while 1:
    d=s.recvfrom(1024)
    data= d[0]
    addr= d[1]

    print (data)
    time=datetime.datetime.now().time()
    hora= str(time)
    s.sendto(hora,addr)

s.close()



