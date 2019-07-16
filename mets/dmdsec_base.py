"""Read and write METS documents"""
from __future__ import unicode_literals

import datetime
from xml_helpers.utils import decode_utf8
from mets.base import _element


def dmdsec(element_id, child_elements=None,
           created_date=datetime.datetime.utcnow().isoformat()):
    """Return the dmdSec element"""

    dmdsec_elem = _element('dmdSec')
    dmdsec_elem.set('ID', decode_utf8(element_id))
    dmdsec_elem.set('CREATED', decode_utf8(created_date))
    if child_elements:
        for elem in child_elements:
            dmdsec_elem.append(elem)

    return dmdsec_elem
