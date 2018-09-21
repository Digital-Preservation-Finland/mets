"""
Install mets
"""

from setuptools import setup, find_packages
from version import get_version


def main():
    """Install mets"""
    setup(
        name='mets',
        packages=find_packages(exclude=['tests', 'tests.*']),
        version=get_version(),
        install_requires=["lxml", 'python-dateutil', 'xml_helpers'],
        dependency_links=[('git+https://gitlab.csc.fi/dpres/xml-helpers.git'
                           '@develop#egg=xml_helpers-0')]
    )


if __name__ == '__main__':
    main()
