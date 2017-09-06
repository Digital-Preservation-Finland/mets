"""Read and write METS documents"""

from mets_tools.mets import _element


def fptr(fileid=None):
    """Return the fptr element"""

    _fptr = _element('fptr')
    _fptr.set('FILEID', fileid)

    return _fptr


def mptr(loctype=None, xlink_href=None, xlink_type=None):
    """Return the fptr element"""

    _mptr = _element('mptr')
    _mptr.set('LOCTYPE', loctype)
    _mptr.set('xlink:href', xlink_href)
    _mptr.set('xlink:type', xlink_type)

    return _mptr


def div(type_attr=None, order=None, contentids=None, label=None, orderlabel=None,
        dmdid=None, admid=None,
        div_elements=None, fptr_elements=None, mptr_elements=None):
    """Return the div element"""

    _div = _element('div')
    _div.set('TYPE', type_attr)
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
        _structmap.set('TYPE', type_attr)
    if label:
        _structmap.set('LABEL', label)

    return _structmap

