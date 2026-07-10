"""
Install mets
"""

from setuptools import setup, find_packages


def main():
    """Install mets"""
    setup(
        name='mets',
        packages=find_packages(exclude=['tests', 'tests.*']),
        include_package_data=True,
        setup_requires=["setuptools-scm"],
        use_scm_version={
            "write_to": "mets/_version.py"
        },
        install_requires=[
            'lxml',
            'python-dateutil',
        ]
    )


if __name__ == '__main__':
    main()
