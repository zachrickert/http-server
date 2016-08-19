# _*_ coding: utf-8 _*_
import pytest


@pytest.fixture
def good_request():
    return 'GET /path/to/index.html HTTP/1.1\r\nHost: www.mysite1.com:80\r\n'


@pytest.fixture
def bad_request():
    return 'POST /path/to/index.html HTTP/1\r\nNotHost: www.mysite1.com:80\r\n'

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


def test_parse_request_bad(bad_request):
    from server import parse_request
    with pytest.raises(ValueError):
        parse_request(bad_request)
