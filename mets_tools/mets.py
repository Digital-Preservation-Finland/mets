"""Read and write METS documents"""

import datetime
import xml.etree.ElementTree as ET
import common_xml_utils.utils
import uuid
import re

METS_NS = 'http://www.loc.gov/METS/'
XSI_NS = 'http://www.w3.org/2001/XMLSchema-instance'
XLINK = 'http://www.w3.org/1999/xlink'

NAMESPACES = {'mets': METS_NS,
              'xsi': XSI_NS,
              'xlink': XLINK}

def mets_mets(profile, objid=str(uuid.uuid4()), label=None
              namespaces=NAMESPACES):
    """Create METS ElementTree"""

    common_xml_utils.utils.register_namespaces(namespaces)

    mets = _element('mets')
    mets.set('xmlns:' + 'xlink', XLINK)
    mets.set('PROFILE', profile)
    mets.set('OBJID', objid)
    if label:
        mets.set('LABEL', label)

    return mets


def order(element):
    """Return order number for given element in METS schema. This can be
    use for example with sort(). """
    return  ['{%s}dmdSec' % METS_NS,
            '{%s}amdSec' % METS_NS,
            '{%s}techMD' % METS_NS,
            '{%s}digiprovMD' % METS_NS,
            '{%s}fileSec' % METS_NS,
            '{%s}structMap' % METS_NS].index(element.tag)


def merge_elements(tag, elements):
    """Merge elements with given tag in elements list"""
    elements_to_merge = filter(lambda x: x.tag == tag, elements)

    elements_to_merge.sort(key=children_order)
    for element in elements_to_merge[1:]:
        elements_to_merge[0].extend(element.getchildren())

    elements = list(set(elements) - set(elements_to_merge))
    return elements + [elements_to_merge[0]]


def mets_ns(tag, prefix=""):
    """Prefix ElementTree tags with METS namespace.

    object -> {info:lc...premis}object

    :tag: Tag name as string
    :returns: Prefixed tag

    """
    if prefix:
        tag = tag[0].upper() + tag[1:]
        return '{%s}%s%s' % (METS_NS, prefix, tag)
    return '{%s}%s' % (METS_NS, tag)


def get_objid(mets):
    """Return mets:OBJID from given `mets` document

    :mets: ElementTree document
    :returns: objid

    """

    return mets.get("OBJID")


def element(tag, prefix=""):
    """Return _ElementInterface with PREMIS namespace.

    Prefix parameter is useful for adding prefixed to lower case tags. It just
    uppercases first letter of tag and appends it to prefix::

        element = _element('objectIdentifier', 'linking')
        element.tag
        'linkingObjectIdentifier'

    :tag: Tagname
    :prefix: Prefix for the tag (default="")
    :returns: ElementTree element object

    """
    return ET.Element(mets_ns(tag, prefix))


def subelement(parent, tag, prefix=""):
    """Return subelement for the given parent element. Created element is
    appelded to parent element.

    :parent: Parent element
    :tag: Element tagname
    :prefix: Prefix for the tag
    :returns: Created subelement

    """
    return ET.SubElement(parent, mets_ns(tag, prefix))


def namespace(element):
    """return xml element's namespace"""
    m = re.match('\{.*\}', element.tag)
    return m.group(0) if m else ''

