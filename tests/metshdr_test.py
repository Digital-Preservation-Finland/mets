"""Test metshdr.py"""
import lxml.etree as ET
import pytest

import xml_helpers.utils as u
import mets.metshdr_base as m


def test_get_created_date():
    """test metshdr"""
    xml = '<mets:mets xmlns:mets="http://www.loc.gov/METS/">' \
          '<mets:metsHdr CREATEDATE="2017-12-12T12:12:12" '\
          'LASTMODDATE="2017-12-12T12:12:13"/>' \
          '</mets:mets>'
    mets = ET.fromstring(xml)
    (created, modified) = m.get_created_date(mets)

    assert created.strftime('%Y-%m-%dT%H:%M:%S') == '2017-12-12T12:12:12'
    assert modified.strftime('%Y-%m-%dT%H:%M:%S') == '2017-12-12T12:12:13'


def test_agent():
    """test agent"""
    xml = '<mets:agent xmlns:mets="http://www.loc.gov/METS/" ' \
          'ROLE="CREATOR" TYPE="ORGANIZATION">' \
          '<mets:name>zzz</mets:name></mets:agent>'
    hdr = m.agent('zzz')
    assert u.compare_trees(hdr, ET.fromstring(xml)) == True


def test_metshdr():
    """test metshdr"""
    xml = '<mets:metsHdr xmlns:mets="http://www.loc.gov/METS/" ' \
          'CREATEDATE="2017-12-12T12:12:12" ' \
          'RECORDSTATUS="submission">' \
          '<mets:agent ROLE="CREATOR" TYPE="ORGANIZATION">' \
          '<mets:name>zzz</mets:name></mets:agent></mets:metsHdr>'
    hdr = m.metshdr('zzz', create_date='2017-12-12T12:12:12',
                    record_status='submission')
    assert u.compare_trees(hdr, ET.fromstring(xml)) == True

