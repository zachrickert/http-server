# _*_ coding: utf-8 _*_

import socket
from sys import argv


def client(message):
    client_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP
    )


    client_socket.connect(('127.0.0.1', 5000))
    client_socket.sendall(message.encode('utf8'))


if __name__ == '__main__':
    client(argv[1])
