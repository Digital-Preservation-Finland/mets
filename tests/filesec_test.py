"""Test filesec.py"""
import lxml.etree as ET

import xml_helpers.utils as u
import mets.filesec_base as m


def test_filegrp():
    """test filegrp"""
    xml = '<mets:fileGrp xmlns:mets="http://www.loc.gov/METS/" ' \
          'USE="xxx"/>'
    fgrp = m.filegrp(use='xxx')
    assert u.compare_trees(fgrp, ET.fromstring(xml)) is True


def test_filesec():
    """test filegrp"""
    xml = '<mets:fileSec xmlns:mets="http://www.loc.gov/METS/"/>'
    fsec = m.filesec()
    assert u.compare_trees(fsec, ET.fromstring(xml)) is True


def test_file_element():
    """test file element"""
    xml = '<mets:file xmlns:mets="http://www.loc.gov/METS/" ' \
          'ID="xxx" ADMID="yyy"><mets:FLocat ' \
          'xmlns:xlink="http://www.w3.org/1999/xlink" LOCTYPE="URI" ' \
          'xlink:href="zzz" xlink:type="simple"/></mets:file>'
    felem = m.file_elem(file_id='xxx', admid_elements=['yyy'],
                        loctype='URI', xlink_href='zzz',
                        xlink_type='simple')
    assert u.compare_trees(felem, ET.fromstring(xml)) is True


def test_parse_streams():
    """test parse_streams"""
    xml = '<mets:file xmlns:mets="http://www.loc.gov/METS/" ' \
          'ID="xxx" ADMID="yyy"><mets:FLocat ' \
          'xmlns:xlink="http://www.w3.org/1999/xlink" LOCTYPE="URI" ' \
          'xlink:href="zzz" xlink:type="simple"/>' \
          '<mets:stream ID="s" ADMID="slink"/>' \
          '</mets:file>'
    felem = ET.fromstring(xml)
    stream = ET.fromstring(
        '<mets:stream xmlns:mets="http://www.loc.gov/METS/" '
        'ID="s" ADMID="slink"/>')
    parsed_stream = m.parse_streams(felem)[0]
    assert u.compare_trees(stream, parsed_stream) is True
