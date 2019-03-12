"""
Gets the current version number.
If in a git repository, it is the current git tag.
Otherwise it is the one contained in the PKG-INFO file.

To use this script, simply import it in your setup.py file
and use the results of get_version() as your package version:

    from version import *
 
    setup(
        ...
        version=get_version(),
        ...
    )
"""

__all__ = ('get_version')

import os.path
import re
from subprocess import Popen, PIPE

VERSION_RE = re.compile('^Version: (.+)$', re.M)


def call_git_describe():
    """Calls git describe subprocess."""
    cmd = 'git describe --abbrev --tags --match v[0-9]*'.split()
    print(' '.join(cmd))
    p_obj = Popen(cmd, stdout=PIPE, stderr=PIPE)
    (stdout, _) = p_obj.communicate()
    return stdout.strip()


def write_pkg_info():
    """Create and write package info."""
    if os.path.isfile('PKG-INFO'):
        return

    d_name = os.path.abspath(os.path.dirname(__file__))
    # pylint: disable=broad-except
    # broad-except: Regardless what error takes place, 0.0 is the fallback
    try:
        version = re.match(r".*-v([\d\.]+-[^-]+-g[^/]+)", d_name).group(1)
    except Exception:
        version = '0.0'

    print("%s: Writing version info to '%s'..." % (
        __file__, os.path.abspath('PKG-INFO')))
    f_out = open(os.path.join(d_name, 'PKG-INFO'), 'w')
    f_out.write("Metadata-Version: 1.0\n")
    f_out.write("Name: information-package-tools\n")
    f_out.write("Version: %s\n" % version)
    f_out.write("Summary: UNKNOWN\n")
    f_out.write("Home-page: UNKNOWN\n")
    f_out.write("Author: UNKNOWN\n")
    f_out.write("Author-email: UNKNOWN\n")
    f_out.write("License: UNKNOWN\n")
    f_out.write("Description: UNKNOWN\n")
    f_out.write("Platform: UNKNOWN\n")
    f_out.close()


def get_version():
    """Get version."""
    d_name = os.path.dirname(__file__)

    if os.path.isdir(os.path.join(d_name, '../../.git')):
        # Get the version using "git describe".
        version_git = call_git_describe()

        # PEP 386 compatibility
        if version_git:
            version = "%s-%s" % (
                '.post'.join(version_git.split('-')[:2]),
                '-'.join(version_git.split('-')[2:])
            )

        print("Version number from GIT repository: " + version)
    else:
        write_pkg_info()
        # Extract the version from the PKG-INFO file.
        with open(os.path.join(d_name, 'PKG-INFO')) as f_in:
            version = VERSION_RE.search(f_in.read()).group(1)
        print("Version number from PKG-INFO: " + version)

    return version


if __name__ == '__main__':
    print(get_version())
