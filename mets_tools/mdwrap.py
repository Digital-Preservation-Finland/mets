"""Read and write METS documents"""

from mets_tools.mets import _element


def mdwrap(mdtype='PREMIS:OBJECT', othermdtype="",
           mdtypeversion="2.3"):
    elem = _element('mdWrap')
    elem.set('MDTYPE', mdtype)
    elem.set('MDTYPEVERSION', mdtypeversion)
    if mdtype == 'OTHER':
        elem.set('OTHERMDTYPE', othermdtype)
    return elem


def xmldata():
    return _element('xmlData')

