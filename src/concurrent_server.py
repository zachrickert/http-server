# _*_ coding: utf-8 _*_
"""Will recieve a message from a client and send back an echo."""
from __future__ import unicode_literals
import socket
from client import PORT
from message import Request, Response
import os
import gevent

HTML_PROTOCOL = 'HTTP/1.1'
CRLF = '\r\n'

PWD = os.path.dirname(__file__)
ROOT = '../webroot'


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
            client_uri = parse_request(recv_message.decode('utf-8'))
        except TypeError as msg:
            reply = response_error(405, str(msg))
        except ValueError as msg:
            reply = response_error(400, str(msg))
        else:
            try:
                resolved = resolve_uri(client_uri)
            except IOError:
                reply = response_error(404, 'file not found')
            else:
                # root_dir = os.path.join(PWD, ROOT)
                reply = response_ok(resolved)
            
        conn.sendall(reply)

        conn.close()
    server_socket.close()


def response_ok(body):
    """Return a http response ok message."""
    my_message = Response(200, body)
    return my_message.send_response()


def response_error(code, phrase):
    """Return an response error by passing in valid error code."""
    my_message = Response(code, phrase)
    return my_message.send_response()


def parse_request(client_request):
    """Parse info from a request.  Raise Errors is bad request."""
    http_request = Request(client_request)
    # print(http_request.protocol, http_request.http_method, http_request.headers)
    if http_request.http_method != 'GET':
        raise TypeError("This server only accomodates get requests.")
    elif http_request.protocol != 'HTTP/1.1':
        raise ValueError("Incorrect Protocol")
    elif not http_request.has_host:
        raise ValueError("No Host found.")
    else:
        return http_request.uri


def resolve_uri(uri):
    # from pdb import set_trace; set_trace()
    webroot = os.path.join(PWD, ROOT)
    relative_uri = os.path.join(webroot, uri.lstrip('/'))
    # ex1 = 'images/JPEG_example.jpg'
    # ex2 = 'text/sample.txt'
    # ex3 = 'text/bad_sample.txt'
    # relative_uri = os.path.join(relative_uri, ex2)
    if os.path.isdir(relative_uri):
        try:
            dir_list = os.listdir(relative_uri)
            response = ('text', dir_list)
        except OSError:
            raise OSError("directroy not found")
    else:
        try:
            with open(relative_uri, 'rb') as target_file:
                content = target_file.read()
        except IOError:
            raise IOError ('file not found')
            # response = (404, 'file not found')
            # return response

        file_type = relative_uri.split('.')[-1]
        response = (file_type, content)
    return response

if __name__ == '__main__':
    from gevent.server import StreamServer
    from gevent.monkey import patch_all
    patch_all()
    server = StreamServer(('127.0.0.1', PORT), server)
    print('Starting echo server on port ' + str(PORT))
    server.serve_forever()
