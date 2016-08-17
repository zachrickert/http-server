# _*_ coding: utf-8 _*_
import pytest

TEST_CONDITIONS = ['string', 
    '1', 
    '1234567', 
    '12345678', 
    '123456789',
    '-'*10000
    ,'å∫ç∂´ƒ©',
    ]

TEST_CONDITIONS_FAIL = ['', 1, b'1234', '12345\t']


@pytest.mark.parametrize('condition', TEST_CONDITIONS)
def test_client(condition):
    from client import client
    assert client(condition) == condition
