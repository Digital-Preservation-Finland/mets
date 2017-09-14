"""Read and write METS documents"""

from mets.mets import _element


def filegrp(use=None, file_elements=None):
    """Return the fileGrp element"""

    _filegrp = _element('fileGrp')
    if use:
        _filegrp.set('USE', use)
    if file_elements:
        for elem in file_elements:
            _filegrp.append(elem)

    return _filegrp


def filesec(filegroup_elements=None):
    """Return the fileSec element"""

    _filesec = _element('fileSec')
    if filegroup_elements:
        for elem in filegroup_elements:
            _filesec.append(elem)

    return _filesec


def file_elem(ID=None, admid_elements=None, loctype=None, xlink_href=None, xlink_type=None,
         groupid=None):
    """Return the file element"""

    _file = _element('file')
    _file.set('ID', ID)
    admids = ' '.join(admid_elements)
    _file.set('ADMID', admids)
    if groupid:
        _file.set('GROUPID', groupid)

    _flocat = _element('FLocat')
    _flocat.set('LOCTYPE', loctype)
    _flocat.set('xlink:href', xlink_href)
    _flocat.set('xlink:type', xlink_type)
    _file.append(_flocat)

    return _file

