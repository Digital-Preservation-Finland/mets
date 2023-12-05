"""Test dmdsec.py"""

import lxml.etree as ET

import xml_helpers.utils as u
import mets.structmap_base as m


def test_fptr():
    """test fptr"""
    xml = '<mets:fptr xmlns:mets="http://www.loc.gov/METS/" ' \
          'FILEID="xxx"/>'
    fptr = m.fptr('xxx')
    assert u.compare_trees(fptr, ET.fromstring(xml)) is True


def test_mptr():
    """test mptr"""
    xml = '<mets:mptr xmlns:mets="http://www.loc.gov/METS/" ' \
          'xmlns:xlink="http://www.w3.org/1999/xlink" ' \
          'LOCTYPE="xxx" xlink:href="yyy" xlink:type="äää"/>'
    mptr = m.mptr(loctype='xxx', xlink_href='yyy', xlink_type='äää')
    assert u.compare_trees(mptr, ET.fromstring(xml)) is True


def test_div():
    """test div"""
    xml = '<mets:div xmlns:mets="http://www.loc.gov/METS/" ' \
          'TYPE="xxx"/>'
    div = m.div(type_attr='xxx')
    assert u.compare_trees(div, ET.fromstring(xml)) is True


def test_structmap():
    """test div"""
    xml = '<mets:structMap xmlns:mets="http://www.loc.gov/METS/"/>'
    smap = m.structmap()
    assert u.compare_trees(smap, ET.fromstring(xml)) is True
