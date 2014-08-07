#!/usr/bin/env python

from setuptools import setup, find_packages

__version__ = '1.0'

# Jenkins will replace __build__ with a unique value.
__build__ = ''

setup(name='insidethehomedeploy',
      version=__version__ + __build__,
      description='insidethehome Deployment Scripts',
      author='Location Labs',
      author_email='info@locationlabs.com',
      url='http://locationlabs.com',
      packages=find_packages(exclude=['*.tests']),
      setup_requires=[
          'nose>=1.0'
      ],
      install_requires=[
          'elmer>=1.2',
          'fabware>=1.0',
      ],
      include_package_data=True
      )
