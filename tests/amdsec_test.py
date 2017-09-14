"""Test amdsec.py"""
import xml.etree.ElementTree as ET
import pytest

import mets.amdsec as m

def test_techmd():
    """test techmd"""
    ET.register_namespace('mets', 'http://www.loc.gov/METS/')
    xml = '<mets:techMD xmlns:mets="http://www.loc.gov/METS/" ' \
          'CREATED="2017-12-12T12:12:12" ID="xxx" />'
    tech = m.techmd('xxx', created_date='2017-12-12T12:12:12')
    assert ET.tostring(tech) == xml


def test_digiprovmd():
    """test digiprovmd"""
    ET.register_namespace('mets', 'http://www.loc.gov/METS/')
    xml = '<mets:digiprovMD xmlns:mets="http://www.loc.gov/METS/" ' \
          'CREATED="2017-12-12T12:12:12" ID="xxx" />'
    tech = m.digiprovmd('xxx', created_date='2017-12-12T12:12:12')
    assert ET.tostring(tech) == xml

def test_amdsec():
    """test amdsec"""
    ET.register_namespace('mets', 'http://www.loc.gov/METS/')
    xml = '<mets:amdSec xmlns:mets="http://www.loc.gov/METS/" />'
    tech = m.amdsec()
    assert ET.tostring(tech) == xml

