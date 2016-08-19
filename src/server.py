# _*_ coding: utf-8 _*_
"""Will recieve a message from a client and send back an echo."""
from __future__ import unicode_literals
import socket
from client import PORT
from message import Request, Response

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

        try:
            parse_request(recv_message.decode('utf-8'))
        except TypeError as msg:
            reply = response_error(405, str(msg))
        except ValueError as msg:
            reply = response_error(400, str(msg))
        else:
            reply = response_ok()

        conn.sendall(reply)
        conn.close()
    server_socket.close()


def response_ok():
    """Return a http response ok message."""
    my_message = Response(200, 'You did it correctly! YOU ROCK!')
    return my_message.send_response()


def response_error(code, phrase):
    """Return an response error by passing in valid error code."""
    my_message = Response(code, phrase)
    return my_message.send_response()


def parse_request(client_request):
    """Parse info from a request.  Raise Errors is bad request."""
    http_request = Request(client_request)

    if http_request.http_method != 'GET':
        raise TypeError("This server only accomodates get requests.")
    if http_request.correct_get_request():
        return http_request.uri
    else:
        raise ValueError("Please make a valid request")

if __name__ == '__main__':
    server()
