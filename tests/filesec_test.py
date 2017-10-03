"""Test filesec.py"""
import xml.etree.ElementTree as ET
import pytest

import mets.filesec_base as m

def test_filegrp():
    """test filegrp"""
    ET.register_namespace('mets', 'http://www.loc.gov/METS/')
    xml = '<mets:fileGrp xmlns:mets="http://www.loc.gov/METS/" ' \
          'USE="xxx" />'
    fgrp = m.filegrp(use='xxx')
    assert ET.tostring(fgrp) == xml


def test_filesec():
    """test filegrp"""
    ET.register_namespace('mets', 'http://www.loc.gov/METS/')
    xml = '<mets:fileSec xmlns:mets="http://www.loc.gov/METS/" />'
    fsec = m.filesec()
    assert ET.tostring(fsec) == xml


def test_file_element():
    """test file element"""
    ET.register_namespace('mets', 'http://www.loc.gov/METS/')
    xml = '<mets:file xmlns:mets="http://www.loc.gov/METS/" ' \
          'ADMID="yyy" ID="xxx"><mets:FLocat LOCTYPE="URI" ' \
          'xlink:href="zzz" xlink:type="simple" ' \
          'xmlns:xlink="http://www.w3.org/1999/xlink" /></mets:file>'
    felem = m.file_elem(file_id='xxx', admid_elements=['yyy'],
                        loctype='URI', xlink_href='zzz',
                        xlink_type='simple')
    assert ET.tostring(felem) == xml
