"""Read and write METS documents"""

import datetime
import uuid

import lxml.etree as ET
from xml_helpers.utils import XSI_NS, decode_utf8, xsi_ns

METS_NS = 'http://www.loc.gov/METS/'
XLINK_NS = 'http://www.w3.org/1999/xlink'

NAMESPACES = {'mets': METS_NS,
              'xsi': XSI_NS,
              'xlink': XLINK_NS}


def iter_elements_with_id(root, identifiers, section=None):
    """Iterate all metadata elements under given section with given list of
    IDREFS. If no section is given, IDs are searched everywhere in the
    METS document, which is extremely slow if file is large.

    Identifier parameter can be list or string where values are separated
    with whitespace.

    :root: Root element
    :identifiers: List of IDREFS (list or string)
    :section: "amdSec", "dmdSec", "fileSec", or None
    :returns: Iterable for all references metadata elements

    """
    if isinstance(identifiers, str):
        identifiers = identifiers.split()
    for identifier in identifiers:
        yield parse_element_with_id(root, identifier, section)


def parse_element_with_id(root, identifier, section=None):
    """Return single element with given ID from given section. If no
    section is given, ID is searched from everywhere in the METS, which
    is extremely slow if file is large.

    ID is single unqiue reference to one of the following elements::

        <techMD>, <sourceMD>, <rightsMD>, <digiprovMD>

    :root: Root element
    :identifier: ID as string
    :returns: References element

    """
    identifier = decode_utf8(identifier)

    if section:
        section = decode_utf8(section)

    if section == "amdSec":
        query = f"/mets:mets/mets:amdSec/*[@ID='{identifier}']"
    elif section == "dmdSec":
        query = f"/mets:mets/mets:dmdSec[@ID='{identifier}']"
    elif section == "fileSec":
        query = ("/mets:mets/mets:fileSec/mets:fileGrp/"
                 f"mets:file[@ID='{identifier}']")
    else:
        query = f"//*[@ID='{identifier}']"
    results = root.xpath(query, namespaces=NAMESPACES)
    if len(results) == 1:
        return results[0]
    else:
        return None


def mets(profile='local', objid=None, label=None, namespaces=None,
         child_elements=None):
    """Create METS Element"""

    if namespaces is None:
        namespaces = NAMESPACES

    if objid is None:
        objid = str(uuid.uuid4())

    _mets = _element('mets', ns=namespaces)
    _mets.set(
        xsi_ns('schemaLocation'),
        'http://www.loc.gov/METS/ '
        'http://www.loc.gov/standards/mets/mets.xsd')
    _mets.set('PROFILE', decode_utf8(profile))
    _mets.set('OBJID', decode_utf8(objid))
    if label:
        _mets.set('LABEL', decode_utf8(label))

    if child_elements:
        for elem in child_elements:
            _mets.append(elem)

    return _mets


def order(elem):
    """Return order number for given element in METS schema. This can be
    use for example with sort(). """
    return ['{%s}dmdSec' % METS_NS,
            '{%s}amdSec' % METS_NS,
            '{%s}techMD' % METS_NS,
            '{%s}rightsMD' % METS_NS,
            '{%s}sourceMD' % METS_NS,
            '{%s}digiprovMD' % METS_NS,
            '{%s}fileSec' % METS_NS,
            '{%s}structMap' % METS_NS].index(elem.tag)


def children_order(elem):
    return ['{%s}techMD' % METS_NS,
            '{%s}digiprovMD' % METS_NS].index(elem.getchildren()[0].tag)


def merge_elements(tag, elements):
    """Merge elements with given tag in elements list"""
    elements_to_merge = list(filter(lambda x: x.tag == tag, elements))

    elements_to_merge.sort(key=children_order)
    for elem in elements_to_merge[1:]:
        elements_to_merge[0].extend(elem.getchildren())

    elements = list(set(elements) - set(elements_to_merge))
    return elements + [elements_to_merge[0]]


def mets_ns(tag, prefix=""):
    """Prefix ElementTree tags with METS namespace.

    object -> {http://...}object

    :tag: Tag name as string
    :returns: Prefixed tag

    """
    tag = decode_utf8(tag)

    if prefix:
        prefix = decode_utf8(prefix)
        tag = tag[0].upper() + tag[1:]
        return f'{{{METS_NS}}}{prefix}{tag}'
    return f'{{{METS_NS}}}{tag}'


def xlink_ns(tag):
    """Prefix tags with XLINK namespace.

    object -> {http://...}object

    :tag: Tag name as string
    :returns: Prefixed tag

    """
    return f'{{{XLINK_NS}}}{tag}'


def parse_objid(mets_el):
    """Return mets:OBJID from given `mets` document

    :mets: ElementTree document
    :returns: objid

    """

    return decode_utf8(mets_el.get("OBJID"))


def _element(tag, prefix="", ns=None):
    """Return _ElementInterface with METS namespace.

    Prefix parameter is useful for adding prefixed to lower case tags. It just
    uppercases first letter of tag and appends it to prefix::

        element = _element('objectIdentifier', 'linking')
        element.tag
        'linkingObjectIdentifier'

    :tag: Tagname
    :prefix: Prefix for the tag (default="")
    :returns: ElementTree element object

    """
    if ns is None:
        ns = {}

    ns['mets'] = METS_NS
    return ET.Element(mets_ns(tag, prefix), nsmap=ns)


def _subelement(parent, tag, prefix="", ns=None):
    """Return subelement for the given parent element. Created element is
    appelded to parent element.

    :parent: Parent element
    :tag: Element tagname
    :prefix: Prefix for the tag
    :returns: Created subelement

    """
    if ns is None:
        ns = {}

    ns['mets'] = METS_NS
    return ET.SubElement(parent, mets_ns(tag, prefix), nsmap=ns)


def current_iso_datetime():
    """
    Return the current datetime as a ISO 8601 string with time zone information
    """
    return datetime.datetime.now(datetime.timezone.utc).isoformat()
