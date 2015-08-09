#!/usr/bin/env python

from setuptools import setup

setup(name='giphy wht',
      version='1.0.1',
      description='Gif viewer on console',
      author='Roland Crosby',
      author_email='roland@rolandcrosby.com',
      url='https://github.com/rolandcrosby/gif',
      entry_points={
          'console_scripts': [
              'gif = gif:main'
          ]
      },
      packages = ['gif'],
      install_requires=['requests'],
      )
