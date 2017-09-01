"""Read and write METS documents"""

import datetime
import xml.etree.ElementTree as ET
import common_xml_utils.utils
import uuid
import re


def mptr(loctype=None, xlink_href=None, xlink_type=None):
    """Return the fptr element"""

    _mptr = _element('mptr')
    _mptr.set('LOCTYPE', loctype)
    _mptr.set('xlink:href', xlink_href)
    _mptr.set('xlink:type', xlink_type)

    return _mptr


def div(type=None, order=None, contentids=None, label=None, orderlabel=None,
        dmdid=None, admid=None,
        div_elements=None, fptr_elements=None, mptr_elements=None):
    """Return the div element"""

    _div = _element('div')
    _div.set('TYPE', type)
    if order:
        _div.set('ORDER', order)
    if contentids:
        _div.set('CONTENTIDS', contentids)
    if label:
        _div.set('LABEL', label)
    if orderlabel:
        _div.set('ORDERLABEL', orderlabel)
    if dmdid:
        _div.set('DMDID', ' '.join(dmdid))
    if admid:
        _div.set('ADMID', ' '.join(admid))

    if div_elements:
        for element in div_elements:
            _div.append(element)
    if fptr_elements:
        for element in fptr_elements:
            _div.append(element)
    if mptr_elements:
        for element in mptr_elements:
            _div.append(element)

    return _div


def structmap(type=None, label=None):
    """Return the structmap element"""

    _structmap = _element('structMap')
    #_structMap.append(div_element)
    if type:
        _structmap.set('TYPE', type)
    if label:
        _structmap.set('LABEL', label)

    return _structmap

