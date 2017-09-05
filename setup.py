"""
Install mets-tools
"""

import os
from setuptools import setup, find_packages


def main():
    """Install mets-tools"""
    setup(
        name='mets_tools',
        packages=find_packages(exclude=['tests', 'tests.*']),
        version='1.0')


if __name__ == '__main__':
    main()
