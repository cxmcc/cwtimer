#!/usr/bin/env python

from setuptools import setup

install_requires = [
    'boto3>=1.4.5',
]

classifiers = [
    'Development Status :: 4 - Beta',
    'Topic :: System :: Clustering',
]

setup(
    name='cwtimer',
    version='0.0.1',
    description='',
    author='Xiuming Chen',
    author_email='cc@cxm.cc',
    url='https://github.com/cxmcc/cwtimer',
    packages=['cwtimer'],
    install_requires=install_requires,
    keywords=['timer', 'Cloudwatch'],
    classifiers=classifiers,
)
