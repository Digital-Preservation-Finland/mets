"""Test mdwrap.py"""

import os
import lxml.etree as ET

from xml_helpers.utils import xsi_ns, compare_trees
import mets


TESTPATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))


def test_parse_mdwrap():
    """Test the parse_mdwrap """
    root = ET.parse(os.path.join(TESTPATH, 'data', 'valid_mets.xml')).getroot()
    wrap = mets.parse_mdwrap(mets.parse_element_with_id(root, 'tech003'))
    mdtype = mets.parse_wrap_mdtype(wrap)
    xmldata = mets.parse_xmldata(wrap)
    assert mdtype['mdtype'] == 'PREMIS:OBJECT'
    assert xmldata.attrib[xsi_ns('type')] == 'premis:file'


def test_mdwrap():
    """test mdwrap"""
    xml = '<mets:mdWrap xmlns:mets="http://www.loc.gov/METS/" ' \
          'MDTYPE="OTHER" MDTYPEVERSION="8.2" OTHERMDTYPE="ADDML"/>'
    wrap = mets.mdwrap(mdtype='OTHER', othermdtype='ADDML',
                       mdtypeversion='8.2')
    assert compare_trees(wrap, ET.fromstring(xml)) is True


def test_xmldata():
    """test xmldata"""
    xml = '<mets:xmlData xmlns:mets="http://www.loc.gov/METS/"/>'
    data = mets.xmldata()
    assert compare_trees(data, ET.fromstring(xml)) is True
