# _*_ coding: utf-8 _*_
"""Will recieve a message from a client and send back an echo."""
from __future__ import unicode_literals
import socket
from client import PORT

HTML_PROTOCOL = 'HTTP/1.1'
RESPONSE_CODE = {
    200: '200 OK',
    500: '500 Internal Server Error'
}
CRLF = '\r\n'


def server():
    """Will recieve a message from a client and send back an echo."""
    buffer_length = 8
    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP
    )
    address = ('127.0.0.1', PORT)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(address)
    server_socket.listen(1)

    while True:
        conn, addr = server_socket.accept()
        print('conection accepted')
        message_complete = False
        recv_message = b""
        while not message_complete:
            part = conn.recv(buffer_length)
            recv_message += part
            if len(part) < buffer_length:
                message_complete = True
        print(recv_message)
        conn.sendall(response_ok())
        conn.close()
    server_socket.close()


def response_ok():
    message = '{0} {1}{2}'.format(HTML_PROTOCOL, RESPONSE_CODE[200], CRLF + CRLF)
    return message.encode('utf8')


def response_error(code, phrase):
    message = '{0} {1}{2}'.format(HTML_PROTOCOL, RESPONSE_CODE[500], CRLF)
    return message.encode('utf8')


def parse_request(request):
    request_as_string = request.encode('utf8')
    head = request_as_string.split(CRLF + CRLF)[0]
    head_as_list = head.split(CRLF)
    first_line = head_as_list[0].split(" ")

    request_type = first_line[0]
    request_uri = first_line[1]
    request_protocol = first_line[2]

    if (request_type == 'GET') and (request_protocol == 'HTTP/1.1') and (head_as_list[1][:4] == 'Host'):
        return request_uri
    else:
        raise ValueError("Please make a request with response type GET protocol HTTP/1.1 and Host on line 2")

if __name__ == '__main__':
    server()
