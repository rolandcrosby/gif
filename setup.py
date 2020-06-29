#!/usr/bin/env python

from setuptools import setup

setup(name='gif',
      version='1.0.2',
      description='command-line porcelain for Gif',
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
