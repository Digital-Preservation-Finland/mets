"""Read and write METS documents"""
from __future__ import unicode_literals

import datetime
from xml_helpers.utils import decode_utf8
from mets.base import _element, current_iso_datetime


def dmdsec(element_id, child_elements=None,
           created_date=None):
    """Return the dmdSec element"""

    if created_date is None:
        created_date = current_iso_datetime()

    dmdsec_elem = _element('dmdSec')
    dmdsec_elem.set('ID', decode_utf8(element_id))
    dmdsec_elem.set('CREATED', decode_utf8(created_date))
    if child_elements:
        for elem in child_elements:
            dmdsec_elem.append(elem)

    return dmdsec_elem
