"""Test mdwrap.py"""
import xml.etree.ElementTree as ET
import pytest

import mets_tools.mdwrap as m

def test_mdwrap():
    """test mdwrap"""
    ET.register_namespace('mets', 'http://www.loc.gov/METS/')
    xml = '<mets:mdWrap xmlns:mets="http://www.loc.gov/METS/" ' \
          'MDTYPE="OTHER" MDTYPEVERSION="8.2" OTHERMDTYPE="ADDML" />'
    wrap = m.mdwrap(mdtype='OTHER', othermdtype='ADDML', mdtypeversion='8.2')
    assert ET.tostring(wrap) == xml

def test_xmldata():
    """test xmldata"""
    ET.register_namespace('mets', 'http://www.loc.gov/METS/')
    xml = '<mets:xmlData xmlns:mets="http://www.loc.gov/METS/" />'
    data = m.xmldata()
    assert ET.tostring(data) == xml
