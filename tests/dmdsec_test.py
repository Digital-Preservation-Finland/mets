"""Test dmdsec.py"""

import lxml.etree as ET

import xml_helpers.utils as u
import mets.dmdsec_base as m


def test_dmdsec():
    """test dmdsec"""
    xml = '<mets:dmdSec xmlns:mets="http://www.loc.gov/METS/" ' \
          'ID="xxx" CREATED="2017-12-12T12:12:12"/>'
    dmd = m.dmdsec('xxx', created_date='2017-12-12T12:12:12')
    assert u.compare_trees(dmd, ET.fromstring(xml)) is True
