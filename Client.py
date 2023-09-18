import threading
import socket

port = 1234
FORMAT = 'utf-8'
SERVER = '192.168.1.5'
SIZE = 1024
ADDR = (SERVER, port)
alias = input('Choose name >>> ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def client_receive():
    while True:
        try:
            message = client.recv(SIZE).decode(FORMAT)
            if message == "alias?":
                client.send(alias.encode(FORMAT))
            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break


def client_send():
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode(FORMAT))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()