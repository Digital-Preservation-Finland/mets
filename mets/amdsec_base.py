"""Read and write METS documents"""
from __future__ import unicode_literals

import datetime
from xml_helpers.utils import decode_utf8
from mets.base import _element


def techmd(element_id, created_date=datetime.datetime.utcnow().isoformat(),
           child_elements=None):
    """Return the techMD element"""

    _techmd = _element('techMD')
    _techmd.set('ID', decode_utf8(element_id))
    _techmd.set('CREATED', decode_utf8(created_date))

    if child_elements:
        for elem in child_elements:
            _techmd.append(elem)

    return _techmd


def digiprovmd(element_id, created_date=datetime.datetime.utcnow().isoformat(),
               child_elements=None):
    """Return the digiprovMD element"""

    _digiprovmd = _element('digiprovMD')
    _digiprovmd.set('ID', decode_utf8(element_id))
    _digiprovmd.set('CREATED', decode_utf8(created_date))

    if child_elements:
        for elem in child_elements:
            _digiprovmd.append(elem)

    return _digiprovmd


def amdsec(child_elements=None):
    """Return the amdSec element"""

    _amdsec = _element('amdSec')

    if child_elements:
        for elem in child_elements:
            _amdsec.append(elem)

    return _amdsec
