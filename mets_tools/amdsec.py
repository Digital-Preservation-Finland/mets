"""Read and write METS documents"""

import datetime
from mets_tools.mets import element


def techmd(element_id, created_date=datetime.datetime.utcnow().isoformat(),
           child_elements=None):
    """Return the techMD element"""

    _techmd = element('techMD')
    _techmd.set('ID', element_id)
    _techmd.set('CREATED', created_date)

    if child_elements:
        for elem in child_elements:
            _techmd.append(elem)

    return _techmd


def digiprovmd(element_id, created_date=datetime.datetime.utcnow().isoformat(),
               child_elements=None):
    """Return the digiprovMD element"""

    _digiprovmd = element('digiprovMD')
    _digiprovmd.set('ID', element_id)
    _digiprovmd.set('CREATED', created_date)

    if child_elements:
        for elem in child_elements:
            _digiprovmd.append(elem)

    return _digiprovmd


def amdsec(child_elements=None):
    """Return the amdSec element"""

    _amdsec = element('amdSec')

    if child_elements:
        for elem in child_elements:
            _amdsec.append(elem)

    return _amdsec
