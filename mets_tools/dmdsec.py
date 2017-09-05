"""Read and write METS documents"""

import datetime
import uuid
from mets_tools.mets import _element
from mets_tools.mdwrap import mdwrap, xmldata
from common_xml_utils.utils import get_namespace


def dmdsec(mdtype_dict,
        child_elements=None, element_id=str(uuid.uuid4()),
        created_date=datetime.datetime.utcnow().isoformat()):
    """Return the dmdSec element"""

    dmdsec_elem = _element('dmdSec')
    dmdsec_elem.set('ID', element_id)
    dmdsec_elem.set('CREATED', created_date)
    xmldata_elem = xmldata()
    if child_elements:
        for elem in child_elements:
            xmldata_elem.append(elem)
            ns = get_namespace(elem)[1:-1]
            if ns in mdtype_dict.keys():
                mdwrap_elem = mdwrap(mdtype_dict[ns]['mdtype'],
                                     mdtype_dict[ns]['othermdtype'],
                                     mdtype_dict[ns]['version'])
            else:
                raise TypeError("Invalid namespace: %s" % ns)
    mdwrap_elem.append(xmldata_elem)
    dmdsec_elem.append(mdwrap_elem)

    return dmdsec_elem

