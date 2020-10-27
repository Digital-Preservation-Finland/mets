"""
Install mets
"""

import re
from setuptools import setup, find_packages

with open('mets/__init__.py', 'r') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)


def main():
    """Install mets"""
    setup(
        name='mets',
        packages=find_packages(exclude=['tests', 'tests.*']),
        include_package_data=True,
        version=version,
        install_requires=[
            'lxml',
            'python-dateutil',
            'xml_helpers@git+https://gitlab.csc.fi/dpres/xml-helpers.git'
            '@develop'
        ]
    )


if __name__ == '__main__':
    main()
