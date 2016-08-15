# _*_ coding: utf-8 _*_
import socket

def server():
    buffer_length = 8

    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP
    )
    address = ('127.0.0.1', 5000)
    server_socket.bind(address)
    while True:
        message_complete = False
        recv_messsage = ""
        while not message_complete:
            part = conn.recv(buffer_length)
            recv_message += (part.decode('utf8'))
            if len(part) < buffer_length:
                message_complete = True
                return recv_message

