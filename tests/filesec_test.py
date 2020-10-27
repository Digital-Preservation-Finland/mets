"""Test filesec.py"""
from __future__ import unicode_literals

import lxml.etree as ET

import xml_helpers.utils as u
import mets.filesec_base as m
from mets.base import NAMESPACES


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


def test_parse_files():
    """Tests the parse_files function."""
    xml = '<mets:mets xmlns:mets="http://www.loc.gov/METS/"><mets:fileSec>' \
          '<mets:fileGrp><mets:file/></mets:fileGrp>' \
          '<mets:fileGrp USE="fi-preservation-xml-schemas">' \
          '<mets:file/><mets:file/></mets:fileGrp>' \
          '</mets:fileSec></mets:mets>'

    # All file elements should be returned
    parsed_files = m.parse_files(ET.fromstring(xml))
    assert len(parsed_files) == 3

    # Using the fileSec should yield the same results as the mets root
    parsed_files = m.parse_files(ET.fromstring(xml).xpath(
        './mets:fileSec', namespaces=NAMESPACES)[0])
    assert len(parsed_files) == 3

    # Return only files from one fileGrp
    parsed_files = m.parse_files(ET.fromstring(xml).xpath(
        './mets:fileSec/mets:fileGrp', namespaces=NAMESPACES)[0])
    assert len(parsed_files) == 1


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


def test_parse_filegrps():
    """Tests the parse_filegrps function."""
    xml = '<mets:fileSec xmlns:mets="http://www.loc.gov/METS/">' \
          '<mets:fileGrp><mets:file/></mets:fileGrp>' \
          '<mets:fileGrp USE="fi-preservation-xml-schemas">' \
          '<mets:file/><mets:file/></mets:fileGrp>' \
          '</mets:fileSec>'
    parsed_filegrp = m.parse_filegrps(ET.fromstring(xml))
    assert len(parsed_filegrp) == 2
    filegrp = ET.fromstring(
        '<mets:fileGrp xmlns:mets="http://www.loc.gov/METS/">'
        '<mets:file/></mets:fileGrp>')
    assert u.compare_trees(parsed_filegrp[0], filegrp) is True

    # Now test with returning a specific fileGrp set based on the @USE
    parsed_filegrp = m.parse_filegrps(
        ET.fromstring(xml), use='fi-preservation-xml-schemas')
    assert len(parsed_filegrp) == 1
    filegrp = ET.fromstring(
        '<mets:fileGrp xmlns:mets="http://www.loc.gov/METS/" '
        'USE="fi-preservation-xml-schemas">'
        '<mets:file/><mets:file/></mets:fileGrp>')
    assert u.compare_trees(parsed_filegrp[0], filegrp) is True
