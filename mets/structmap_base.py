"""Read and write METS documents"""

from xml_helpers.utils import decode_utf8
from mets.base import _element, XLINK_NS, xlink_ns


def fptr(fileid=None):
    """Return the fptr element"""

    _fptr = _element('fptr')
    _fptr.set('FILEID', decode_utf8(fileid))

    return _fptr


def mptr(loctype=None, xlink_href=None, xlink_type=None):
    """Return the fptr element"""

    _mptr = _element('mptr', ns={'xlink': XLINK_NS})
    _mptr.set('LOCTYPE', decode_utf8(loctype))
    _mptr.set(xlink_ns('href'), decode_utf8(xlink_href))
    _mptr.set(xlink_ns('type'), decode_utf8(xlink_type))

    return _mptr


def div(type_attr=None, order=None, contentids=None, label=None,
        orderlabel=None, dmdid=None, admid=None, div_elements=None,
        fptr_elements=None, mptr_elements=None):
    """Return the div element"""

    _div = _element('div')
    _div.set('TYPE', decode_utf8(type_attr))
    if order:
        _div.set('ORDER', decode_utf8(order))
    if contentids:
        _div.set('CONTENTIDS', decode_utf8(contentids))
    if label:
        _div.set('LABEL', decode_utf8(label))
    if orderlabel:
        _div.set('ORDERLABEL', decode_utf8(orderlabel))
    if dmdid:
        _div.set(
            'DMDID', ' '.join([decode_utf8(d) for d in dmdid])
        )
    if admid:
        _div.set(
            'ADMID', ' '.join([decode_utf8(a) for a in admid])
        )

    if div_elements:
        for elem in div_elements:
            _div.append(elem)
    if fptr_elements:
        for elem in fptr_elements:
            _div.append(elem)
    if mptr_elements:
        for elem in mptr_elements:
            _div.append(elem)

    return _div


def structmap(type_attr=None, label=None):
    """Return the structmap element"""

    _structmap = _element('structMap')
    # _structMap.append(div_element)
    if type_attr:
        _structmap.set('TYPE', decode_utf8(type_attr))
    if label:
        _structmap.set('LABEL', decode_utf8(label))

    return _structmap
