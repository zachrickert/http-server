# _*_ coding: utf-8 _*_
import socket
from sys import argv

PORT = 5023


def client(message):
    buffer_length = 8
    infos = socket.getaddrinfo('127.0.0.1', PORT)
    stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]
    client_socket = socket.socket(*stream_info[:3])
    client_socket.connect(stream_info[4])
    client_socket.sendall(message.encode('utf8'))
    message_complete = False
    echo_message = ""
    while not message_complete:
        part = client_socket.recv(buffer_length)
        echo_message += (part.decode('utf8'))
        if len(part) < buffer_length:
            message_complete = True
        print("this is the echo  '" + echo_message + "'")

if __name__ == '__main__':
    client(argv[1])
