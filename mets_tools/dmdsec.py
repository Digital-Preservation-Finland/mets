"""Read and write METS documents"""

import datetime
import uuid
from mets.mets import mets_ns

def dmdSec(child_elements=None, element_id=str(uuid.uuid4()),
        created_date=datetime.datetime.utcnow().isoformat()):
    """Return the dmdSec element"""

    dmdSec = _element('dmdSec')
    dmdSec.set('ID', element_id)
    dmdSec.set('CREATED', created_date)
    mdWrap = _element('mdWrap')
    xmlData = _element('xmlData')
    if child_elements:
        for element in child_elements:
            xmlData.append(element)
            ns = namespace(element)[1:-1]
            if ns in mets_ns.keys():
                mdWrap.set("MDTYPE", mets_ns[ns]['mdtype'])
                if mets_ns[ns]['mdtype'] == 'OTHER':
                    mdWrap.set('OTHERMDTYPE', mets_ns[ns]['othermdtype'])
                mdWrap.set('MDTYPEVERSION', mets_ns[ns]['version'])
            else:
                raise TypeError("Invalid namespace: %s" % ns)
    mdWrap.append(xmlData)
    dmdSec.append(mdWrap)

    return dmdSec

