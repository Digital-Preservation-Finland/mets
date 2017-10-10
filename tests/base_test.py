"""Test the `mets.mets` module"""
import os
import lxml.etree as ET
import pytest

import mets.base as m


TESTPATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))


def test_element_with_id():
    """Test the `element_with_admid` method."""
    root = ET.parse(os.path.join(TESTPATH, 'data', 'valid_mets.xml')).getroot()
    techmd = m.element_with_id(root, 'tech003')
    assert techmd.attrib["ID"] == 'tech003'
    dmdsec = m.element_with_id(root, 'dmd008')
    assert dmdsec.attrib["ID"] == 'dmd008'


def test_iter_elements_with_id():
    """Test the `element_with_admid` method."""
    root = ET.parse(os.path.join(TESTPATH, 'data', 'valid_mets.xml')).getroot()
    admid_string = 'dmd010  dmd009 file013'
    results = [x for x in m.iter_elements_with_id(root, admid_string)]
    assert len(results) == 3

    admid_list = ['dmd010', 'dmd009', 'file013', 'tech001']
    results = [x for x in m.iter_elements_with_id(root, admid_list)]
    assert len(results) == 4


def test_get_objid():
    """Test the `mets.get_objid` function.

    :returns: None

    """
    xml = """<mets:mets OBJID="kdk-csc-sip001"
             xmlns:mets="http://www.loc.gov/METS/">
             </mets:mets>"""
    objid = m.get_objid(ET.fromstring(xml))
    assert objid == 'kdk-csc-sip001'


def test_mets():
    """Test METS root generation"""
    mets_tree = ET.tostring(m.mets('xxx', objid='yyy', label='zzz'))
    mets_xml = '<mets:mets ' \
               'xmlns:mets="http://www.loc.gov/METS/" ' \
               'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ' \
               'xsi:schemaLocation="http://www.loc.gov/METS/ http://www.loc.gov/standards/mets/mets.xsd" ' \
               'PROFILE="xxx" OBJID="yyy" LABEL="zzz"/>'
    assert mets_tree == mets_xml


def test_order():
    """Test order function"""
    xml = """<mets:techMD xmlns:mets = "http://www.loc.gov/METS/"/>"""
    assert m.order(ET.fromstring(xml)) == 2


def test_children_order():
    """Test children_order"""
    mets_xml = """<mets:amdSec xmlns:mets = "http://www.loc.gov/METS/">
                  <mets:digiprovMD/></mets:amdSec>"""
    mets_tree_xml = ET.fromstring(mets_xml)
    assert m.children_order(mets_tree_xml) == 1


def test_merge_elements():
    """Merge elements with given tag in elements list"""
    # TODO


def test_mets_ns():
    """Test mets_ns"""
    assert m.mets_ns('xxx') == '{http://www.loc.gov/METS/}xxx'


def test_element():
    """Test METS _element"""
    xml = """<mets:xxx xmlns:mets="http://www.loc.gov/METS/"/>"""
    assert ET.tostring(m._element('xxx')) == xml


def test_subelement():
    """Test METS _subelement"""
    xml = """<mets:xxx xmlns:mets="http://www.loc.gov/METS/"/>"""
    parent_xml = """<mets:mets xmlns:mets = "http://www.loc.gov/METS/"/>"""
    parent = ET.fromstring(parent_xml)
    assert ET.tostring(m._subelement(parent, 'xxx')) == xml

