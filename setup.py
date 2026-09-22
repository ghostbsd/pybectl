#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

__VERSION__ = '0.7'
PROGRAM_VERSION = __VERSION__

setup(
    name="bectl",
    version=PROGRAM_VERSION,
    description="GhostBSD bectl Python module",
    license='BSD',
    author='Eric Turgeon',
    url='https://github.com/GhostBSD/pybectl/',
    package_dir={'': '.'},
    install_requires=['setuptools'],
    py_modules=['bectl']
)
