# _*_ coding: utf-8 _*_
from __future__ import unicode_literals

import pytest


@pytest.fixture
def good_request():
    return 'GET /path/to/index.html HTTP/1.1\r\nHost: www.mysite1.com:80\r\n'


@pytest.fixture
def post_request():
    return 'POST /path/to/index.html HTTP/1.1\r\nHost: www.mysite1.com:80\r\n'


@pytest.fixture
def bad_protocol():
    return 'GET /path/to/index.html HTTP/1\r\nHost: www.mysite1.com:80\r\n'


@pytest.fixture
def bad_host():
    return 'GET /path/to/index.html HTTP/1\r\nAccept-Language: en-us\r\n'


# TEST_CONDITIONS = ['string',  
#     '1', 
#     '1234567', 
#     '12345678', 
#     '123456789',
#     '-'*10000,
#     u'āĕĳœ',
#     ''
#     '12345\t',
#     ]

# VALID_RESPONSE_CODES = ['200', '500']

# CRLF = '\r\n'


# @pytest.mark.parametrize('condition', TEST_CONDITIONS)
# def test_protocol(condition):
#     from client import client
#     assert client(condition).split(' ')[0] == 'HTTP/1.1'


# @pytest.mark.parametrize('condition', TEST_CONDITIONS)
# def test_response_code(condition):
#     from client import client
#     assert client(condition).split(' ')[1] in VALID_RESPONSE_CODES


# @pytest.mark.parametrize('condition', TEST_CONDITIONS)
# def test_crlf(condition):
#     from client import client
#     assert ('').join(list(client(condition))[-2:]) == CRLF


def test_parse_request_good(good_request):
    from server import parse_request
    assert parse_request(good_request) == '/path/to/index.html'


def test_parse_request_post(post_request):
    from server import parse_request
    with pytest.raises(TypeError):
        parse_request(post_request)


def test_parse_bad_protocol(bad_protocol):
    from server import parse_request
    with pytest.raises(ValueError):
        parse_request(bad_protocol)


def test_parse_request_bad_host(bad_host):
    from server import parse_request
    with pytest.raises(ValueError):
        parse_request(bad_host)


def test_resolve_uri_file_found_txt():
    from server import resolve_uri
    assert resolve_uri('text/sample.txt') == ('txt', b'This is a very simple text file.\nJust to show that we can serve it up.\nIt is three lines long.')


def test_resolve_uri_file_not_found():
    from server import resolve_uri
    with pytest.raises(IOError):
        resolve_uri('not/found.txr')


def test_resolve_uri_dir_found():
    from server import resolve_uri
    assert resolve_uri('images/') == ('text', ['JPEG_example.jpg', 'sample_1.png', 'Sample_Scene_Balls.jpg'])


def test_resolve_uri_dir_not_found():
    from server import resolve_uri
    with pytest.raises(IOError):
        resolve_uri('not/found/')
