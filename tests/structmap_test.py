"""Test dmdsec.py"""
import lxml.etree as ET
import pytest

import mets.structmap_base as m

def test_fptr():
    """test fptr"""
    xml = '<mets:fptr xmlns:mets="http://www.loc.gov/METS/" ' \
          'FILEID="xxx"/>'
    fptr = m.fptr('xxx')
    assert ET.tostring(fptr) == xml

def test_mptr():
    """test mptr"""
    xml = '<mets:mptr xmlns:mets="http://www.loc.gov/METS/" ' \
          'xmlns:xlink="http://www.w3.org/1999/xlink" ' \
          'LOCTYPE="xxx" xlink:href="yyy" xlink:type="zzz"/>'
    mptr = m.mptr(loctype='xxx', xlink_href='yyy', xlink_type='zzz')
    assert ET.tostring(mptr) == xml

def test_div():
    """test div"""
    xml = '<mets:div xmlns:mets="http://www.loc.gov/METS/" ' \
          'TYPE="xxx"/>'
    div = m.div(type_attr='xxx')
    assert ET.tostring(div) == xml

def test_structmap():
    """test div"""
    xml = '<mets:structMap xmlns:mets="http://www.loc.gov/METS/"/>'
    smap = m.structmap()
    assert ET.tostring(smap) == xml
