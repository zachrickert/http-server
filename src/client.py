# _*_ coding: utf-8 _*_
"""Send msg to serve and gets echo back."""
from __future__ import unicode_literals
import socket
from sys import argv

PORT = 5047


def client(message):
    """Send msg to serve and gets echo back."""
    infos = socket.getaddrinfo('127.0.0.1', PORT)
    stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]
    client_socket = socket.socket(*stream_info[:3])
    client_socket.connect(stream_info[4])

    try:
        message = message.encode('utf8')
    except UnicodeDecodeError:
        pass
    except AttributeError:
        pass

    client_socket.sendall(message)

    client_socket.shutdown(socket.SHUT_WR)

    buffer_length = 8
    message_complete = False
    echo_message = b""
    while not message_complete:
        part = client_socket.recv(buffer_length)
        echo_message += part
        if len(part) < buffer_length:
            message_complete = True

    client_socket.close()

    return echo_message.decode('utf8')

if __name__ == '__main__':
    print(client(argv[1]))
