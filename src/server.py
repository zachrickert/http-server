# _*_ coding: utf-8 _*_
import socket


def server():
    buffer_length = 8
    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP
    )
    address = ('127.0.0.1', 5015)
    server_socket.bind(address)
    while True:
        server_socket.listen(1)
        conn, addr = server_socket.accept()
        message_complete = False
        recv_message = ""
        while not message_complete:
            part = conn.recv(buffer_length)
            recv_message += (part.decode('utf8'))
            if len(part) < buffer_length:
                message_complete = True
        print(recv_message)
        server_socket.connect(('127.0.0.1', 5016))
        server_socket.sendall(recv_message.encode('utf8'))

if __name__ == '__main__':
    server()
