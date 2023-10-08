import socket
import datetime


HOST = '127.0.0.1'
PORT = 9999
BUFSIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
    serverSocket.bind((HOST, PORT))
    serverSocket.listen()
    print('The server is waiting for connection...')

    clientSocket, clientAddress = serverSocket.accept()
    print(f'Got a connection from {clientAddress}')

    clientAnswer = clientSocket.recv(BUFSIZE).decode('utf-8')
    print(f'Client message: {clientAnswer}   Time: {datetime.datetime.now()}')

    print(f'{clientAddress} has been disconnected')
