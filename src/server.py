# _*_ coding: utf-8 _*_
import socket


def server():
    buffer_length = 8

    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP
    )
    address = ('127.0.0.1', 5006)
    server_socket.bind(address)

    while True:
        server_socket.listen(1)
        conn, addr = server_socket.accept()
        message_complete = False
        recv_messsage = ""
        while not message_complete:
            part = conn.recv(buffer_length)
            recv_messsage += (part.decode('utf8'))
            if len(part) < buffer_length:
                message_complete = True
        print(recv_messsage)

        # server_socket.sendall(recv_messsage.encode('utf8'))


if __name__ == '__main__':
    server()
