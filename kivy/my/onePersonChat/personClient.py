import socket

HOST = '127.0.0.1'
PORT = 65456

def connect():
    global clientSocket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((HOST, PORT))
        
def send(message):
    message = message.encode('utf-8')
    clientSocket.send(message)
    
