#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import io
from os.path import dirname
from os.path import join

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    try:
        with io.open(
            join(dirname(__file__), *names),
            encoding=kwargs.get('encoding', 'utf8')
        ) as fh:
            return fh.read()
    except:
        pass


setup(
    name='code',
    version='0.1.0',
    license='Private',
    description='A data science project package',
    long_description=read('README.md'),
    packages=find_packages('code'),
    package_dir={'': 'code'}
)
