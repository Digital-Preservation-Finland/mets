"""Read and write METS documents"""

from xml_helpers.utils import encode_utf8, decode_utf8
from mets.base import _element, METS_NS


def parse_mdwrap(section):
    """Return the mdWrap element from a metadata section."""
    return section.find('{%s}mdWrap' % METS_NS)


def parse_xmldata(wrap):
    """Return the xmlData element from a metadata section."""
    return wrap.find('{%s}xmlData/*' % METS_NS)


def parse_wrap_mdtype(wrap):
    """Return the MDTYPE, OTHERMDTYPE and MDTYPEVERSION
    attributes from an element.
    """
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
    """Create an mdWrap element with the mandatory
    attributes and append the child elements to the element.

    :mdtype: value for the MDTYPE attribute
    :mdtypeversion: value for the MDTYPEVERSION attribute
    :othermdtype: value for the optional OTHERMDTYPE attribute (use
                  if MDTYPE='OTHER')
    :child_elements: the child elements as a list

    :returns: the mets:mdWrap element as XML
    """
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
    """Create an xmlData element and append the child elements to
    the element.
    """
    xmldata_e = _element('xmlData')
    if child_elements:
        for elem in child_elements:
            xmldata_e.append(elem)
    return xmldata_e
