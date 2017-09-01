"""Read and write METS documents"""

import datetime
import xml.etree.ElementTree as ET
import common_xml_utils.utils
import uuid
import re


def fptr(fileid=None):
    """Return the fptr element"""

    _fptr = _element('fptr')
    _fptr.set('FILEID', fileid)

    return _fptr


def filegrp(use=None, file_elements=None):
    """Return the fileGrp element"""

    _filegrp = _element('fileGrp')
    if use:
        _filegrp.set('USE', use)
    if file_elements:
        for element in file_elements:
            _filegrp.append(element)

    return _filegrp


def filesec(filegroup_elements=None):
    """Return the fileSec element"""

    _filesec = _element('fileSec')
    if filegroup_elements:
        for element in filegroup_elements:
            _filesec.append(element)

    return _filesec


def file(id=None, admid_elements=None, loctype=None, xlink_href=None, xlink_type=None,
         groupid=None):
    """Return the file element"""

    _file = _element('file')
    _file.set('ID', id)
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

