import socket

# Crear un socket del tipo TCP y vincularlo a un puerto
# Utilizaremos 'localhost', por lo tanto, solo aceptamos conexiones desde la misma máquina
# El puerto podría ser 80, pero como necesita privilegios de root,
# usemos uno por mayor o igual que 8080

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 8080))

# Poner en cola un máximo de 5 solicitudes de conexión TCP

mySocket.listen(5)

# Aceptar conexiones, leer datos entrantes y responder una página HTML (en un bucle)

while True:
    print('Waiting for connections')
    (recvSocket, address) = mySocket.accept()
    print('HTTP request received:')
    print(recvSocket.recv(1024))
    recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n <html><body><h1>Hello World!</h1></body></html> \r\n",'utf-8'))
    recvSocket.close()