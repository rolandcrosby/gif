#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='giphy wht',
      version='1.0.0',
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
      )
