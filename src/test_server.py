# _*_ coding: utf-8 _*_


def test_client():
    from client import client
    from server import server
    client('example_message')
    assert server() == 'example_message'
