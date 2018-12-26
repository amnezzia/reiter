#!/usr/bin/env python
from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='re_iter',
      version='0.1',
      description='Make python generators renewable',
      long_description=long_description,
      author='Misha, Tronc Data Team',
      author_email='mikhail.erekhinsky@gmail.com',
      url='https://github.com/amnezzia/reiter',
      packages=find_packages(exclude=['tests*']),
      install_requires=['pathos',
                        'cranial-common']
      )
