"""Read and write METS documents"""

from mets.base import _element


def mdwrap(mdtype='PREMIS:OBJECT', othermdtype="",
           mdtypeversion="2.3", child_elements=None):
    elem = _element('mdWrap')
    elem.set('MDTYPE', mdtype)
    elem.set('MDTYPEVERSION', mdtypeversion)
    if mdtype == 'OTHER':
        elem.set('OTHERMDTYPE', othermdtype)
    if child_elements:
        for elem in child_elements:
            dmdsec_elem.append(elem)
    return elem


def xmldata(child_elements=None):
    xmldata_e = _element('xmlData')
    if child_elements:
        for elem in child_elements:
            dmdsec_elem.append(elem)
    return xmldata_e
