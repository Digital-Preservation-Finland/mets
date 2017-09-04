"""Read and write METS documents"""

from mets_tools.mets import element


def fptr(fileid=None):
    """Return the fptr element"""

    _fptr = element('fptr')
    _fptr.set('FILEID', fileid)

    return _fptr


def filegrp(use=None, file_elements=None):
    """Return the fileGrp element"""

    _filegrp = element('fileGrp')
    if use:
        _filegrp.set('USE', use)
    if file_elements:
        for elem in file_elements:
            _filegrp.append(elem)

    return _filegrp


def filesec(filegroup_elements=None):
    """Return the fileSec element"""

    _filesec = element('fileSec')
    if filegroup_elements:
        for elem in filegroup_elements:
            _filesec.append(elem)

    return _filesec


def file_elem(ID=None, admid_elements=None, loctype=None, xlink_href=None, xlink_type=None,
         groupid=None):
    """Return the file element"""

    _file = element('file')
    _file.set('ID', ID)
    admids = ' '.join(admid_elements)
    _file.set('ADMID', admids)
    if groupid:
        _file.set('GROUPID', groupid)

    _flocat = element('FLocat')
    _flocat.set('LOCTYPE', loctype)
    _flocat.set('xlink:href', xlink_href)
    _flocat.set('xlink:type', xlink_type)
    _file.append(_flocat)

    return _file

