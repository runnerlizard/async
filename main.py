import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # inet - ipv4, sock stream - tcp
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # set option to level socket for reuse address
server_socket.bind(('localhost', 5001))  # set port
server_socket.listen()  # order listening signals

while True:
    print('Before accept')
    client_socket, addr = server_socket.accept()  # getting input and return socket and address
    print('connection from', addr)
    while True:
        request = client_socket.recv(4096)  # receiving from client 4 kb
        if not request:
            break
        else:
            response = 'Hello world\n'.encode()
            client_socket.send(response)  # answering to client
    print('outside inner loop')
    client_socket.close()
