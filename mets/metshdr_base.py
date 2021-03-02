"""Read and write METS documents"""
from __future__ import unicode_literals

import datetime
import dateutil.parser
from xml_helpers.utils import encode_utf8, decode_utf8
from mets.base import _element, mets_ns, current_iso_datetime


def get_created_date(mets):
    """Return createdate and modified date from given mets document.

    CREATEDATE
    LASTMODDATE

    :mets: ElementTree document
    :returns: (createdate, modifieddate)

    """

    header = mets.find(mets_ns('metsHdr'))
    create_date = header.get("CREATEDATE")
    last_modified_date = header.get("LASTMODDATE")

    if create_date is not None:
        create_date = dateutil.parser.parse(
            decode_utf8(create_date)
        )
    if last_modified_date is not None:
        last_modified_date = dateutil.parser.parse(
            decode_utf8(last_modified_date)
        )

    return (create_date, last_modified_date)


def agent(organisation_name, agent_role='CREATOR',
          agent_type='ORGANIZATION', othertype=None):
    """Returns METS agent element"""
    metsagent = _element('agent')
    metsagent.set('ROLE', decode_utf8(agent_role))
    metsagent.set('TYPE', decode_utf8(agent_type))
    if othertype:
        metsagent.set('OTHERTYPE', othertype)
    _orgname = _element('name')
    _orgname.text = decode_utf8(organisation_name)
    metsagent.append(_orgname)

    return metsagent


def metshdr(create_date=None, last_mod_date=None, record_status=None,
            agents=None):
    """Return the metsHdr element

    :create_date: Creation date
    :last_mod_date: Last modified date
    :record_status: Record status
    :agents: List of agent elements
    :returns: metsHdr element
    """
    if create_date is None:
        create_date = current_iso_datetime()

    _metshdr = _element('metsHdr')
    _metshdr.set('CREATEDATE', decode_utf8(create_date))
    if last_mod_date:
        _metshdr.set('LASTMODDATE', decode_utf8(last_mod_date))
    _metshdr.set('RECORDSTATUS', decode_utf8(record_status))

    # Append each agent element to metsHdr element
    if agents:
        for metsagent in agents:
            _metshdr.append(metsagent)

    return _metshdr
