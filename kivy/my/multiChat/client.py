import socket
import threading

HOST = '127.0.0.1'
PORT = 65456

# {CHAT#1} Create a separate receive handler


def connect():
    global clientSocket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((HOST, PORT))
    return clientSocket

def listen(comming):
    while True:
        message = clientSocket.recv(1024)
        if message.decode('utf-8') == "quit":
            break 
        comming(message)
    
def startlistening(comming):
    clientThread = threading.Thread(target=listen, args=(comming,))
    clientThread.daemon = True
    clientThread.start()
    
def send(message):
    message = message.encode('utf-8')
    clientSocket.send(message)
        # [==end==]