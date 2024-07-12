"""
This file is used to install the package.
"""

from setuptools import setup


setup(
    name='WebTesting',
    version='0.0.1',
    packages=['Web_tests'],
    install_requires=[
        'selenium',
        'pytest',
        'webdriver_manager',
        ],
)

