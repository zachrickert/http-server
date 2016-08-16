# _*_ coding: utf-8 _*_
import socket
from client import PORT


def server():
    buffer_length = 8
    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP
    )
    # server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    address = ('127.0.0.1', PORT)
    server_socket.bind(address)
    server_socket.listen(1)



    while True:
        conn, addr = server_socket.accept()
        print('conection accepted')
        message_complete = False
        recv_message = ""
        while not message_complete:
            part = conn.recv(buffer_length)
            recv_message += (part.decode('utf8'))
            if len(part) < buffer_length:
                message_complete = True
        print(recv_message)
        conn.sendall(recv_message.encode('utf8'))

if __name__ == '__main__':
    server()
