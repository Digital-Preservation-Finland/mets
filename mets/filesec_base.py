"""Read and write METS documents"""

from xml_helpers.utils import decode_utf8, encode_utf8
from mets.base import _element, xlink_ns, XLINK_NS, NAMESPACES


def parse_use(elem):
    """Return the USE attribute from an element."""
    return encode_utf8(elem.attrib.get('USE', '')).strip()


def parse_admid(elem):
    """Return the ADMID attribute from an element."""
    return encode_utf8(elem.attrib.get('ADMID', '')).strip().split()


def parse_href(elem):
    """Return the xlink:href attribute from an element."""
    return encode_utf8(elem.attrib.get('{%s}href' % XLINK_NS)).strip()


def parse_flocats(mets_file):
    """Return the FLocat elements."""
    results = mets_file.xpath('mets:FLocat', namespaces=NAMESPACES)
    return results


def parse_files(mets_root):
    """Return the file elements."""
    results = mets_root.xpath('//mets:file', namespaces=NAMESPACES)
    return results


def parse_streams(mets_file_elem):
    """Return the stream elements."""
    results = mets_file_elem.xpath('./mets:stream', namespaces=NAMESPACES)
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


def file_elem(file_id=None, admid_elements=None, loctype=None,
              xlink_href=None, xlink_type=None, groupid=None,
              use=None):
    """Return the file element"""

    _file = _element('file')
    _file.set('ID', decode_utf8(file_id))
    admids = ' '.join(admid_elements)
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
