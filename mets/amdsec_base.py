"""Read and write METS documents"""
from __future__ import unicode_literals

import datetime
from xml_helpers.utils import decode_utf8
from mets.base import _element, NAMESPACES, current_iso_datetime


def techmd(element_id, created_date=None, child_elements=None):
    """Return the techMD element"""

    if created_date is None:
        created_date = current_iso_datetime()

    _techmd = _element('techMD')
    _techmd.set('ID', decode_utf8(element_id))
    _techmd.set('CREATED', decode_utf8(created_date))

    if child_elements:
        for elem in child_elements:
            _techmd.append(elem)

    return _techmd


def digiprovmd(element_id, created_date=None, child_elements=None):
    """Return the digiprovMD element"""

    if created_date is None:
        created_date = current_iso_datetime()

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


def iter_techmd(root):
    """Iterates all techMD sections in a METS root element.

    :root: Root element
    :returns: Iterable for alla techMD elements
    """
    for techmd_elem in root.xpath('/mets:mets/mets:amdSec/mets:techMD',
                                  namespaces=NAMESPACES):
        yield techmd_elem
