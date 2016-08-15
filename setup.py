# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="http-server",
    description="Build an echo server using Python sockets.",
    version='0.1.0',
    author="Zach Rickert, James Canning",
    author_email="zachrickert@gmail.com",
    license='MIT',
    py_modules=['server', 'client'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']},
)
