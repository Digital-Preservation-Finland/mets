# coding=utf-8
"""Test metshdr.py"""
import lxml.etree as ET

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
          'ROLE="CREATOR" TYPE="ORGANIZATION" OTHERTYPE="abcd">' \
          '<mets:name>zzz</mets:name></mets:agent>'
    hdr = m.agent('zzz', othertype='abcd')
    assert u.compare_trees(hdr, ET.fromstring(xml)) is True


def test_metshdr():
    """test metshdr"""
    xml = u'<mets:metsHdr xmlns:mets="http://www.loc.gov/METS/" ' \
          u'CREATEDATE="2017-12-12T12:12:12" ' \
          u'RECORDSTATUS="submission">' \
          u'<mets:agent ROLE="CREATOR" TYPE="ORGANIZATION">' \
          u'<mets:name>zzz</mets:name></mets:agent>' \
          u'<mets:agent ROLE="ARCHIVIST" TYPE="ORGANIZATION">' \
          u'<mets:name>zzz</mets:name></mets:agent>' \
          u'<mets:agent ROLE="CREATOR" TYPE="OTHER" OTHERTYPE="SOFTWARE">' \
          u'<mets:name>Pekan Paketointipalvelu Öy</mets:name></mets:agent>' \
          u'</mets:metsHdr>'
    hdr = m.metshdr(create_date='2017-12-12T12:12:12',
                    record_status='submission',
                    agents=[
                        m.agent('zzz'),
                        m.agent('zzz', agent_role='ARCHIVIST'),
                        m.agent(u'Pekan Paketointipalvelu Öy',
                                agent_role='CREATOR',
                                agent_type='OTHER',
                                othertype='SOFTWARE')
                    ])
    assert u.compare_trees(hdr, ET.fromstring(xml)) is True
