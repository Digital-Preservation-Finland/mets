"""Read and write METS documents"""

from mets.base import _element


def mdwrap(mdtype='PREMIS:OBJECT', othermdtype="",
           mdtypeversion="2.3", child_elements=None):
    mdwrap_e = _element('mdWrap')
    mdwrap_e.set('MDTYPE', mdtype)
    mdwrap_e.set('MDTYPEVERSION', mdtypeversion)
    if mdtype == 'OTHER':
        mdwrap_e.set('OTHERMDTYPE', othermdtype)
    if child_elements:
        for elem in child_elements:
            mdwrap_e.append(elem)
    return mdwrap_e


def xmldata(child_elements=None):
    xmldata_e = _element('xmlData')
    if child_elements:
        for elem in child_elements:
            xmldata_e.append(elem)
    return xmldata_e
