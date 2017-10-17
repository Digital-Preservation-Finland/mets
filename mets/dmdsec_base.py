"""Read and write METS documents"""

import datetime
from mets.base import _element


def dmdsec(element_id, child_elements=None,
           created_date=datetime.datetime.utcnow().isoformat()):
    """Return the dmdSec element"""

    dmdsec_elem = _element('dmdSec')
    dmdsec_elem.set('ID', element_id.decode('utf-8'))
    dmdsec_elem.set('CREATED', created_date.decode('utf-8'))
    if child_elements:
        for elem in child_elements:
            dmdsec_elem.append(elem)

    return dmdsec_elem

