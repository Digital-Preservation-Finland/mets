"""Read and write METS documents"""


from mets.base import _element, xlink_ns, XLINK_NS, NAMESPACES, METS_NS


def parse_use(elem):
    return elem.attrib.get('USE', '').encode('utf-8').strip()


def parse_admid(elem):
    return elem.attrib.get('ADMID', '').encode('utf-8').strip().split()


def parse_href(elem):
    return elem.attrib.get('{%s}href' % XLINK_NS).encode('utf-8').strip()


def parse_flocats(mets_file):
    results = mets_file.xpath('mets:FLocat', namespaces=NAMESPACES)
    return results

def parse_files(mets_root):
    results = mets_root.xpath('//mets:file', namespaces=NAMESPACES)
    return results

def filegrp(use=None, child_elements=None):
    """Return the fileGrp element"""

    _filegrp = _element('fileGrp')
    if use:
        _filegrp.set('USE', use.decode('utf-8'))
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
    _file.set('ID', file_id.decode('utf-8'))
    admids = ' '.join(admid_elements)
    _file.set('ADMID', admids.decode('utf-8'))
    if groupid:
        _file.set('GROUPID', groupid.decode('utf-8'))
    if use:
        _file.set('USE', use.decode('utf-8'))

    _flocat = _element('FLocat', ns={'xlink': XLINK_NS})
    _flocat.set('LOCTYPE', loctype.decode('utf-8'))
    _flocat.set(xlink_ns('href'), xlink_href.decode('utf-8'))
    _flocat.set(xlink_ns('type'), xlink_type.decode('utf-8'))
    _file.append(_flocat)

    return _file

