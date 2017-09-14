"""Test dmdsec.py"""
import xml.etree.ElementTree as ET
import pytest

import mets.dmdsec as m

def test_dmdsec():
    """test dmdsec"""
    ET.register_namespace('mets', 'http://www.loc.gov/METS/')
    xml = '<mets:dmdSec xmlns:mets="http://www.loc.gov/METS/" ' \
          'CREATED="2017-12-12T12:12:12" ID="xxx" />'
    dmd = m.dmdsec('xxx', created_date='2017-12-12T12:12:12')
    assert ET.tostring(dmd) == xml

