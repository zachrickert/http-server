# _*_ coding: utf-8 _*_
"""Classes for the response and the request messages."""
from __future__ import unicode_literals

HTML_PROTOCOL = 'HTTP/1.1'

RESPONSE_CODE = {
    200: '200 OK',
    400: '400 Bad Request',
    404: '404 File not found',
    405: '405 Method Not Allowed',
    500: '500 Internal Server Error'
}

CRLF = '\r\n'
# CRLF = '\\r\\n'

class Response(object):
    """Form a correct http response."""

    def __init__(self, code, body=None):
        """Initialize the response.  Pass in error code."""
        self.code = code
        self.body = body

    def send_response(self):
        """Format reponse for in http protocol."""
        # message = '{0} {1}{2}{3}'.format(
        #     HTML_PROTOCOL,
        #     RESPONSE_CODE[self.code],
        #     CRLF + CRLF,
        #     self.body)
        message = '{0} {1}{2}'.format(
            HTML_PROTOCOL,
            RESPONSE_CODE[self.code],
            CRLF + CRLF)
        message = message.encode('utf-8')
        try:
            message += self.body[1]
        except TypeError:
            if self.code == 200:
                html_list = '<html>'
                for item in self.body[1]:
                    html_list += '<li>{0}'.format(item)
                message += html_list.encode('utf-8')
            else:
                message += self.body.encode('utf-8')

        print(message)
        return message


class Request(object):
    """Parses a request and saves information."""

    def __init__(self, user_request):
        """Initialize request by parsing info out of the request."""
        head_info = user_request.split(CRLF + CRLF)[0]
        head = head_info.split(CRLF)
        first_line = head.pop(0).split(" ")
        self.http_method = first_line[0]
        self.uri = first_line[1]
        self.protocol = first_line[2]
        self.headers = {}
        for header in head:
            try:
                key, value = header.split(':')[0], header.split(':')[1].lstrip()
                self.headers[key] = value
            except IndexError:
                pass

        self.has_host = 'Host' in self.headers
        # print('Method: ' + self.http_method)
        # print('Uri: ' + self.uri)
        # print('Protocol: ' + self.protocol)
        # print('Host: ' + self.headers['Host'])
        
