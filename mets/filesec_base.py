"""Read and write METS documents"""
from __future__ import unicode_literals

from xml_helpers.utils import decode_utf8
from mets.base import NAMESPACES, XLINK_NS, _element, xlink_ns


def parse_use(elem):
    """Return the USE attribute from an element."""
    return decode_utf8(elem.attrib.get('USE', '')).strip()


def parse_admid(elem):
    """Return the ADMID attribute from an element."""
    return decode_utf8(elem.attrib.get('ADMID', '')).strip().split()


def parse_href(elem):
    """Return the xlink:href attribute from an element."""
    return decode_utf8(elem.attrib.get('{%s}href' % XLINK_NS)).strip()


def parse_flocats(mets_file):
    """Return the FLocat elements."""
    results = mets_file.xpath('mets:FLocat', namespaces=NAMESPACES)
    return results


def parse_files(xml):
    """Return the file elements from a section of XML data. If the
    xml is a fileGrp, only the file elements from that fileGrp are
    returned.

    :xml: An lxml etree._Element or etree._ElementTree object
    :returns: A list of file elements
    """
    # Try to get the root element of the XML if the type is an ElementTree
    try:
        section = xml.getroot()
    except AttributeError:
        section = xml

    xpath = '/mets:mets/mets:fileSec/mets:fileGrp/mets:file'
    if section.tag == '{http://www.loc.gov/METS/}fileGrp':
        xpath = './mets:file'

    results = section.xpath(xpath, namespaces=NAMESPACES)
    return results


def parse_streams(mets_file_elem):
    """Return the stream elements."""
    results = mets_file_elem.xpath('./mets:stream', namespaces=NAMESPACES)
    return results


def parse_filegrps(mets_root, use=None):
    """Return the fileGrp sections.

    :mets_root: The mets root as an lxml.elementtree
    :use: the USE attribute value of the fileGrp
    :returns: the parsed fileGrp sections as a list of elements
    """
    xpath = '/mets:mets/mets:fileSec/mets:fileGrp'
    if use:
        xpath = xpath + '[@USE="%s"]' % use

    results = mets_root.xpath(xpath, namespaces=NAMESPACES)
    return results


def filegrp(use=None, child_elements=None):
    """Return the fileGrp element"""

    _filegrp = _element('fileGrp')
    if use:
        _filegrp.set('USE', decode_utf8(use))
    if child_elements:
        for elem in child_elements:
            _filegrp.append(elem)

    return _filegrp


def filesec(child_elements=None):
    """Return the fileSec element"""

    _filesec = _element('fileSec')
    if child_elements:
        for elem in child_elements:
            _filesec.append(elem)

    return _filesec


def stream(admid_elements=None):
    """Return the stream element"""
    stream = _element('stream')
    admids = ' '.join([decode_utf8(a) for a in admid_elements])
    stream.set('ADMID', admids)
    return stream


def file_elem(file_id=None, admid_elements=None, loctype=None,
              xlink_href=None, xlink_type=None, groupid=None,
              use=None):
    """Return the file element"""

    _file = _element('file')
    _file.set('ID', decode_utf8(file_id))
    admids = ' '.join([decode_utf8(a) for a in admid_elements])
    _file.set('ADMID', decode_utf8(admids))
    if groupid:
        _file.set('GROUPID', decode_utf8(groupid))
    if use:
        _file.set('USE', decode_utf8(use))

    _flocat = _element('FLocat', ns={'xlink': XLINK_NS})
    _flocat.set('LOCTYPE', decode_utf8(loctype))
    _flocat.set(xlink_ns('href'), decode_utf8(xlink_href))
    _flocat.set(xlink_ns('type'), decode_utf8(xlink_type))
    _file.append(_flocat)

    return _file
