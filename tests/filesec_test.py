"""Test filesec.py"""
import lxml.etree as ET
import pytest

import mets.filesec_base as m

def test_filegrp():
    """test filegrp"""
    xml = '<mets:fileGrp xmlns:mets="http://www.loc.gov/METS/" ' \
          'USE="xxx"/>'
    fgrp = m.filegrp(use='xxx')
    assert ET.tostring(fgrp) == xml


def test_filesec():
    """test filegrp"""
    xml = '<mets:fileSec xmlns:mets="http://www.loc.gov/METS/"/>'
    fsec = m.filesec()
    assert ET.tostring(fsec) == xml


def test_file_element():
    """test file element"""
    xml = '<mets:file xmlns:mets="http://www.loc.gov/METS/" ' \
          'ID="xxx" ADMID="yyy"><mets:FLocat ' \
          'xmlns:xlink="http://www.w3.org/1999/xlink" LOCTYPE="URI" ' \
          'xlink:href="zzz" xlink:type="simple"/></mets:file>'
    felem = m.file_elem(file_id='xxx', admid_elements=['yyy'],
                        loctype='URI', xlink_href='zzz',
                        xlink_type='simple')
    assert ET.tostring(felem) == xml
