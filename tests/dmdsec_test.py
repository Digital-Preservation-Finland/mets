"""Test dmdsec.py"""
import lxml.etree as ET
import pytest

import mets.dmdsec_base as m

def test_dmdsec():
    """test dmdsec"""
    xml = '<mets:dmdSec xmlns:mets="http://www.loc.gov/METS/" ' \
          'ID="xxx" CREATED="2017-12-12T12:12:12"/>'
    dmd = m.dmdsec('xxx', created_date='2017-12-12T12:12:12')
    assert ET.tostring(dmd) == xml

