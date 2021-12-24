import socket
from select import select

to_monitor = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # inet - ipv4, sock stream - tcp
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # set option to level socket for reuse address
server_socket.bind(('localhost', 5001))  # set port
server_socket.listen()  # order listening signals


def accept_connection(serv_socket):
    client_socket, addr = serv_socket.accept()  # getting input and return socket and address
    print('connection from', addr)
    to_monitor.append(client_socket)


def send_message(client_socket):
    request = client_socket.recv(4096)  # receiving from client 4 kb
    if request:
        response = 'Hello world\n'.encode()
        client_socket.send(response)  # answering to client
    else:
        client_socket.close()


def event_loop():
    while True:
        print('started loop')
        ready_to_read, _, _ = select(to_monitor, [], [])
        print('get select')
        for sock in ready_to_read:
            if sock is server_socket:
                print('server')
                accept_connection(sock)
            else:
                print('client')
                send_message(sock)


if __name__ == '__main__':
    to_monitor.append(server_socket)
    event_loop()
