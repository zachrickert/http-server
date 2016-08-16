# _*_ coding: utf-8 _*_

import socket
from sys import argv


def client(message):
    buffer_length = 8

    client_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP
    )

    client_socket.connect(('127.0.0.1', 5006))

    # while True:
    #     client_socket.listen(1)
    #     conn, addr = client_socket.accept()
    #     message_complete = False
    #     echo_messsage = ""
    #     while not message_complete:
    #         part = conn.recv(buffer_length)
    #         echo_messsage += (part.decode('utf8'))
    #         if len(part) < buffer_length:
    #             message_complete = True
    #     print('this is the echo' + echo_messsage)

    client_socket.sendall(message.encode('utf8'))

if __name__ == '__main__':
    client(argv[1])
