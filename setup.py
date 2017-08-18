#!/usr/bin/env python

from setuptools import setup

install_requires = [
    'boto3>=1.4.5',
]

classifiers = [
    'Development Status :: 4 - Beta',
    'Topic :: System :: Clustering',
]

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='cwtimer',
    version='0.0.2',
    description='Pythonic timing tracker with reporting to Cloudwatch',
    long_description=long_description,
    author='Xiuming Chen',
    author_email='cc@cxm.cc',
    url='https://github.com/cxmcc/cwtimer',
    py_modules=['cwtimer'],
    install_requires=install_requires,
    keywords=['timer', 'Cloudwatch'],
    classifiers=classifiers,
)
