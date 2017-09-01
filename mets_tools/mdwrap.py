"""Read and write METS documents"""

import datetime
import xml.etree.ElementTree as ET
import common_xml_utils.utils
import uuid
import re


def mdwrap(mdtype='PREMIS:OBJECT', mdtypeversion="2.3"):
    element = _element('mdWrap')
    element.set('MDTYPE', mdtype)
    element.set('MDTYPEVERSION', mdtypeversion)
    return element

def xmldata():
    return _element('xmlData')

