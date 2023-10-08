import socket


HOST = '127.0.0.1'
PORT = 9999
BUFSIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.connect((HOST, PORT))
    print("Enter a message for the server...")
    socket.send(input().encode('utf-8'))
