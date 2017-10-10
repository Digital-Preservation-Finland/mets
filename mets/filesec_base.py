"""Read and write METS documents"""

from mets.base import _element, xlink_ns, XLINK_NS, NAMESPACES, METS_NS


def parse_use(elem):
    return elem.attrib.get('USE', '').strip()


def parse_admid(elem):
    return split(elem.attrib.get('ADMID', '').strip())


def parse_href(elem):
    return elem.attrib.get('{%s}%s' % XLINK_NS, elem, '').strip()


def mets_files(mets_root):
    return mets_root.findall('./{{0}}fileSec//{{0}}file'.format(METS_NS))


def filegrp(use=None, child_elements=None):
    """Return the fileGrp element"""

    _filegrp = _element('fileGrp')
    if use:
        _filegrp.set('USE', use)
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
    _file.set('ID', file_id)
    admids = ' '.join(admid_elements)
    _file.set('ADMID', admids)
    if groupid:
        _file.set('GROUPID', groupid)
    if use:
        _file.set('USE', use)

    _flocat = _element('FLocat', ns={'xlink': XLINK_NS})
    _flocat.set('LOCTYPE', loctype)
    _flocat.set(xlink_ns('href'), xlink_href)
    _flocat.set(xlink_ns('type'), xlink_type)
    _file.append(_flocat)

    return _file

