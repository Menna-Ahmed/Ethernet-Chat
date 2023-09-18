import socket
import threading



port = 1234
FORMAT = 'utf-8'
SIZE = 1024
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
clients = []
names = []


def broadcast(message):
    for client in clients:
        client.send(message)


# Function to handle clients'connections
def handle_client(client):

    while True:
        try:
            message = client.recv(SIZE)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = names[index]
            broadcast(f'{alias} has left the chat room!'.encode(FORMAT))
            names.remove(alias)
            break

def receive():
    while True:
        print(f'Server {SERVER} is running and listening ...')
        client, address = server.accept()
        print(f'connection is established with {str(address)}')
        client.send('alias?'.encode(FORMAT))
        alias = client.recv(SIZE)
        names.append(alias)
        clients.append(client)
        print(f'The name of this client is {alias}'.encode(FORMAT))
        broadcast(f'{alias} has connected to the chat room'.encode(FORMAT))
        client.send('you are now connected!'.encode(FORMAT))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


if __name__ == "__main__":
    receive()