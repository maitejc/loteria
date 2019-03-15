import socket

IP = "127.0.0.1"
PORT = 8081

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.connect((IP, PORT))
except OSError:
    print("Problemas con la conexión")
    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT)) 
except KeyboardInterrupt:
    print("La conexión se ha interrumpido")

print(s.recv(2048).decode("utf-8")) 

