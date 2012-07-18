#!/usr/bin/env python
from setuptools import find_packages, setup

setup(name='txgeonames',
      version='0',
      description='Twisted client for the GeoNames API',
      url='https://github.com/lvh/txgeonames',

      author='Laurens Van Houtven',
      author_email='_@lvh.cc',

      packages=find_packages(),

      install_requires=['twisted'],

      license='ISC',
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Twisted",
        "License :: OSI Approved :: ISC License (ISCL)",
        ])
