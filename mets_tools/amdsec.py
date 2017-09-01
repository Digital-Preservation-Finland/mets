"""Read and write METS documents"""

import datetime
import xml.etree.ElementTree as ET
import common_xml_utils.utils
import uuid
import re


def children_order(element):
    return ['{%s}techMD' % METS_NS,
            '{%s}digiprovMD' % METS_NS,].index(element.getchildren()[0].tag)


def get_created_date(mets):
    """Return createdate and modified date from given mets document.

    CREATEDATE
    LASTMODDATE

    :mets: ElementTree document
    :returns: (createdate, modifieddate)

    """

    header = mets.find(mets_ns('metsHdr'))
    create_date = header.get("CREATEDATE")
    last_modified_date = header.get("LASTMODDATE")

    if create_date is not None:
        create_date = dateutil.parser.parse(create_date)
    if last_modified_date is not None:
        last_modified_date = dateutil.parser.parse(last_modified_date)

    return (create_date, last_modified_date)


def techmd(element_id, created_date=datetime.datetime.utcnow().isoformat(),
           child_elements=None):
    """Return the techMD element"""

    _techmd = _element('techMD')
    _techmd.set('ID', element_id)
    _techmd.set('CREATED', created_date)

    if child_elements:
        for element in child_elements:
            _techmd.append(element)

    return _techmd


def digiprovmd(element_id, created_date=datetime.datetime.utcnow().isoformat(),
               child_elements=None):
    """Return the digiprovMD element"""

    _digiprovmd = _element('digiprovMD')
    _digiprovmd.set('ID', element_id)
    _digiprovmd.set('CREATED', created_date)

    if child_elements:
        for element in child_elements:
            _digiprovmd.append(element)

    return _digiprovmd


def amdsec(child_elements=None):
    """Return the amdSec element"""

    _amdsec = _element('amdSec')

    if child_elements:
        for element in child_elements:
            _amdsec.append(element)

    return _amdsec

