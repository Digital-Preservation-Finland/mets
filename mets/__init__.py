"""Package version, make functions generally available"""
try:
    from ._version import version as __version__
except ImportError:
    # Package not installed
    __version__ = "unknown"

# flake8 doesn't like these imports, but they are needed for other repos
# flake8: noqa
from mets.base import *
from mets.amdsec_base import *
from mets.dmdsec_base import *
from mets.filesec_base import *
from mets.mdwrap_base import *
from mets.structmap_base import *
from mets.metshdr_base import *
