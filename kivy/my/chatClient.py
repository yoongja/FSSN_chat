import socket
from threading import Thread

HOST = '127.0.0.1'
PORT = 65456

def connet():
    global clientSocket
    
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        if clientSocket.connect((HOST, PORT)) == -1:
                print('> connect() failed and program terminated')
                clientSocket.close()
                return
    except Exception as exceptionObj:
        print('> connect() failed by exception:', exceptionObj)
        return
        
def start_listening(incoming_message_callback):
    Thread(target=listen, args=(incoming_message_callback), daemon=True).start()

def send(message):
    message = message.encode('utf-8')
    clientSocket.send(message)

def listen(incoming_message_callback):
    
    while True:
        message = clientSocket.recv(1024).decode('utf-8')
        incoming_message_callback(message)
        if message.decode('utf-8') == "quit":
            break