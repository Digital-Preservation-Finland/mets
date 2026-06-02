"""Read and write METS documents"""
from __future__ import annotations

from mets.base import _element, NAMESPACES, current_iso_datetime


def _create_md(name, element_id, created_date=None, child_elements=None):
    """Return a METS metadata block with given name and creation date,
    defaulting to current datetime if none is provided.
    """
    if created_date is None:
        created_date = current_iso_datetime()

    md_el = _element(name)
    md_el.set('ID', element_id)
    md_el.set('CREATED', created_date)

    if child_elements:
        for elem in child_elements:
            md_el.append(elem)

    return md_el


def techmd(element_id, created_date=None, child_elements=None):
    """Return the techMD element"""
    return _create_md(
        "techMD", element_id=element_id,
        created_date=created_date, child_elements=child_elements
    )


def digiprovmd(element_id, created_date=None, child_elements=None):
    """Return the digiprovMD element"""
    return _create_md(
        "digiprovMD", element_id=element_id,
        created_date=created_date, child_elements=child_elements
    )


def amdsec(child_elements=None):
    """Return the amdSec element"""

    _amdsec = _element('amdSec')

    if child_elements:
        for elem in child_elements:
            _amdsec.append(elem)

    return _amdsec


def iter_techmd(root):
    """Iterates all techMD sections in a METS root element.

    :root: Root element
    :returns: Iterable for alla techMD elements
    """
    yield from root.xpath('/mets:mets/mets:amdSec/mets:techMD',
                          namespaces=NAMESPACES)
