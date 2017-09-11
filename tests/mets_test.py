"""Test the `mets_tools.mets` module"""

import xml.etree.ElementTree as ET
import pytest

import mets_tools.mets as m


def test_get_objid():
    """Test the `mets.get_objid` function.

    :returns: None

    """
    xml = """<mets:mets OBJID="kdk-csc-sip001"
             xmlns:mets="http://www.loc.gov/METS/">
             </mets:mets>"""
    objid = m.get_objid(ET.fromstring(xml))
    assert objid == 'kdk-csc-sip001'

def test_mets_mets():
    """Test METS root generation"""
    mets_tree = ET.tostring(m.mets_mets('xxx', objid='yyy', label='zzz'))
    mets_xml = """<mets:mets
                  xsi:schemaLocation="http://www.loc.gov/METS/ http://www.loc.gov/standards/mets/mets.xsd"
                  xmlns:mets = "http://www.loc.gov/METS/"
                  xmlns:xsi = "http://www.w3.org/2001/XMLSchema-instance"
                  xmlns:xlink = "http://www.w3.org/1999/xlink"
                  PROFILE="xxx" OBJID="yyy" LABEL="zzz"></mets:mets>"""
    mets_tree_xml = ET.tostring(ET.fromstring(mets_xml))
    assert mets_tree == mets_tree_xml


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
    xml = """<mets:xxx xmlns:mets="http://www.loc.gov/METS/" />"""
    assert ET.tostring(m._element('xxx')) == xml


def test_subelement():
    """Test METS _subelement"""
    xml = """<mets:xxx xmlns:mets="http://www.loc.gov/METS/" />"""
    parent_xml = """<mets:mets xmlns:mets = "http://www.loc.gov/METS/"/>"""
    parent = ET.fromstring(parent_xml)
    assert ET.tostring(m._subelement(parent, 'xxx')) == xml

