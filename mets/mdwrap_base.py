"""Read and write METS documents"""

from mets.base import _element, METS_NS
from xml_helpers.utils import encode_utf8, decode_utf8

def parse_mdwrap(section):
    return section.find('{%s}mdWrap' % METS_NS)


def parse_xmldata(wrap):
    return wrap.find('{%s}xmlData/*' % METS_NS)


def parse_wrap_mdtype(wrap):
    mdtype = wrap.attrib.get('MDTYPE', None)
    other = wrap.attrib.get('OTHERMDTYPE', None)
    version = wrap.attrib.get('MDTYPEVERSION', None)
    if mdtype is not None:
        mdtype = encode_utf8(mdtype)
    if other is not None:
        other = encode_utf8(other)
    if version is not None:
        version = encode_utf8(version)
    return {'mdtype': mdtype, 'othermdtype': other, 'mdtypeversion': version}


def mdwrap(mdtype, mdtypeversion, othermdtype="",
           child_elements=None):
    mdwrap_e = _element('mdWrap')
    mdwrap_e.set('MDTYPE', decode_utf8(mdtype))
    mdwrap_e.set('MDTYPEVERSION', decode_utf8(mdtypeversion))
    if mdtype == 'OTHER':
        mdwrap_e.set('OTHERMDTYPE', decode_utf8(othermdtype))
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
