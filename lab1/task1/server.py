import socket
import datetime
import time


HOST = '127.0.0.1'
PORT = 9999
BUFSIZE = 10

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
    serverSocket.bind((HOST, PORT))
    serverSocket.listen()
    print('The server is waiting for connection...')

    clientSocket, clientAddress = serverSocket.accept()
    print(f'Got a connection from {clientAddress}')

    clientAnswer = clientSocket.recv(BUFSIZE)
    print(
        f'Client message: {clientAnswer.decode("utf-8")}  Time: {datetime.datetime.now()}')

    time.sleep(5)

    if len(clientAnswer) >= BUFSIZE:
        clientSocket.send("The message is too long".encode('utf-8'))
    else:
        clientSocket.send(clientAnswer)

    clientSocket.close()
    print(f'{clientAddress} has been disconnected')
