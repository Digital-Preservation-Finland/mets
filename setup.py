"""
Install mets
"""

import os
from setuptools import setup, find_packages


def main():
    """Install mets"""
    setup(
        name='mets',
        packages=find_packages(exclude=['tests', 'tests.*']),
        version='1.0',
        install_requires=["lxml", "dateutils"]
    )


if __name__ == '__main__':
    main()
