"""Test the `mets_tools.mets` module"""

import datetime
import xml.etree.ElementTree as ET
import pytest

import dpres_xml_handler.mets as m


def mets():
    """Return an incomplete test METS

    :returns: root Element of ElementTree

    """
    xml = '''<mets:mets OBJID="kdk-csc-sip001"
             xmlns:mets="http://www.loc.gov/METS/">
             <mets:metsHdr CREATEDATE="2013-11-19T16:40:17">
             </mets:metsHdr></mets:mets>'''
    return ET.ElementTree(ET.fromstring(xml)).getroot()


def test_find_created_date():
    """Test the `dpres_xml_handler.mets.find_created_date` function

    :returns: None

    """

    (created_date, last_modified_date) = m.get_created_date(mets())

    assert created_date == datetime.datetime(2013, 11, 19, 16, 40, 17)
    assert last_modified_date is None


def test_get_objid():
    """Test the `dpres_xml_date.mets.get_objid` function.

    :returns: None

    """

    objid = m.get_objid(mets())
    assert objid == 'kdk-csc-sip001'

