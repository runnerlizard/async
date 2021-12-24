import socket
import selectors

selector = selectors.DefaultSelector()


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # inet - ipv4, sock stream - tcp
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # set option to level socket for reuse address
    server_socket.bind(('localhost', 5001))  # set port
    server_socket.listen()  # order listening signals

    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)  # register
    # server_socket


def accept_connection(serv_socket):
    client_socket, addr = serv_socket.accept()  # getting input and return socket and address
    print('connection from', addr)

    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)  # register
    # client_socket


def send_message(client_socket):
    request = client_socket.recv(4096)  # receiving from client 4 kb
    if request:
        response = 'Hello world\n'.encode()
        client_socket.send(response)  # answering to client
    else:
        selector.unregister(client_socket)
        client_socket.close()


def event_loop():
    while True:
        events = selector.select()  # selectorkey: fileobj, events, data

        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == '__main__':
    server()
    event_loop()
