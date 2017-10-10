"""Test amdsec.py"""
import lxml.etree as ET
import pytest

import mets.amdsec_base as m

def test_techmd():
    """test techmd"""
    xml = '<mets:techMD xmlns:mets="http://www.loc.gov/METS/" ' \
          'ID="xxx" CREATED="2017-12-12T12:12:12"/>'
    tech = m.techmd('xxx', created_date='2017-12-12T12:12:12')
    assert ET.tostring(tech) == xml


def test_digiprovmd():
    """test digiprovmd"""
    xml = '<mets:digiprovMD xmlns:mets="http://www.loc.gov/METS/" ' \
          'ID="xxx" CREATED="2017-12-12T12:12:12"/>'
    tech = m.digiprovmd('xxx', created_date='2017-12-12T12:12:12')
    assert ET.tostring(tech) == xml

def test_amdsec():
    """test amdsec"""
    xml = '<mets:amdSec xmlns:mets="http://www.loc.gov/METS/"/>'
    tech = m.amdsec()
    assert ET.tostring(tech) == xml

