"""Read and write METS documents"""

from mets.base import _element, XLINK_NS, xlink_ns


def fptr(fileid=None):
    """Return the fptr element"""

    _fptr = _element('fptr')
    _fptr.set('FILEID', fileid.decode('utf-8'))

    return _fptr


def mptr(loctype=None, xlink_href=None, xlink_type=None):
    """Return the fptr element"""

    _mptr = _element('mptr', ns={'xlink': XLINK_NS})
    _mptr.set('LOCTYPE', loctype.decode('utf-8'))
    _mptr.set(xlink_ns('href'), xlink_href.decode('utf-8'))
    _mptr.set(xlink_ns('type'), xlink_type.decode('utf-8'))

    return _mptr


def div(type_attr=None, order=None, contentids=None, label=None, orderlabel=None,
        dmdid=None, admid=None,
        div_elements=None, fptr_elements=None, mptr_elements=None):
    """Return the div element"""

    _div = _element('div')
    _div.set('TYPE', type_attr.decode('utf-8'))
    if order:
        _div.set('ORDER', order.decode('utf-8'))
    if contentids:
        _div.set('CONTENTIDS', contentids.decode('utf-8'))
    if label:
        _div.set('LABEL', label.decode('utf-8'))
    if orderlabel:
        _div.set('ORDERLABEL', orderlabel.decode('utf-8'))
    if dmdid:
        _div.set('DMDID', ' '.join(dmdid).decode('utf-8'))
    if admid:
        _div.set('ADMID', ' '.join(admid).decode('utf-8'))

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
    #_structMap.append(div_element)
    if type_attr:
        _structmap.set('TYPE', type_attr.decode('utf-8'))
    if label:
        _structmap.set('LABEL', label.decode('utf-8'))

    return _structmap

