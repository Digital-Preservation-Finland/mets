"""Read and write METS documents"""

import datetime
import uuid
from mets_tools.mets import _element
from mets_tools.mdwrap import mdwrap, xmldata
from common_xml_utils.utils import get_namespace


def dmdsec(element_id, child_elements=None,
        created_date=datetime.datetime.utcnow().isoformat()):
    """Return the dmdSec element"""

    dmdsec_elem = _element('dmdSec')
    dmdsec_elem.set('ID', element_id)
    dmdsec_elem.set('CREATED', created_date)
    if child_elements:
        for elem in child_elements:
            dmdsec_elem.append(elem)

    return dmdsec_elem
