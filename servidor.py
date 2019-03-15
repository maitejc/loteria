import socket
import random

PORT = 8081
IP = "127.0.0.1"
numero_aleatorio =(random.randrange(9))

numeros = IP.split(".")
a = int(numeros[0])
b = int(numeros[1])
c = int(numeros[2])
d = int(numeros[3])
suma = a+b+c+d
resultado = suma % 10

def ganado(clientsocket): 
    send_message =("Has ganado la loteria")
    send_bytes = str.encode(send_message)
    clientsocket.send(send_bytes)
    clientsocket.close() 

def perdido(clientsocket): 
    send_message =("No has ganado la lotería")
    send_bytes = str.encode(send_message)
    clientsocket.send(send_bytes)
    clientsocket.close() 

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
hostname=IP

try:
    serversocket.bind((hostname, PORT))
    serversocket.listen(5) 

    while True:
        print("Esperando conexiones")
        (clientsocket, address) = serversocket.accept()
        if resultado == numero_aleatorio:
            ganado(clientsocket)
        else: 
            perdido(clientsocket)
            
except socket.error:
    print("Problemas con la conexión")
except KeyboardInterrupt:
    print("La conexión se ha interrumpido")

