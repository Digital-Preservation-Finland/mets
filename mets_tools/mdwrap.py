"""Read and write METS documents"""

from mets_tools.mets import element


def mdwrap(mdtype='PREMIS:OBJECT', othermdtype="",
           mdtypeversion="2.3"):
    elem = element('mdWrap')
    elem.set('MDTYPE', mdtype)
    elem.set('MDTYPEVERSION', mdtypeversion)
    if mdtype == 'OTHER':
        elem.set('OTHERMDTYPE', othermdtype)
    return elem


def xmldata():
    return element('xmlData')

