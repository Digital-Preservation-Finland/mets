"""Read and write METS documents"""

import datetime
import dateutil.parser
from mets.base import _element, mets_ns


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
        create_date = dateutil.parser.parse(create_date.encode('utf-8'))
    if last_modified_date is not None:
        last_modified_date = dateutil.parser.parse(last_modified_date.encode('utf-8'))

    return (create_date, last_modified_date)


def agent(organisation_name, agent_role='CREATOR',
          agent_type='ORGANIZATION'):
    """Returns METS agent element"""
    metsagent = _element('agent')
    metsagent.set('ROLE', agent_role.decode('utf-8'))
    metsagent.set('TYPE', agent_type.decode('utf-8'))
    _orgname = _element('name')
    _orgname.text = organisation_name.decode('utf-8')
    metsagent.append(_orgname)

    return metsagent


def metshdr(organisation_name, create_date=datetime.datetime.utcnow().isoformat(),
            last_mod_date=None, record_status=None):
    """Return the metsHdr element"""

    _metshdr = _element('metsHdr')
    _metshdr.set('CREATEDATE', create_date.decode('utf-8'))
    if last_mod_date:
        _metshdr.set('LASTMODDATE', last_mod_date.decode('utf-8'))
    _metshdr.set('RECORDSTATUS', record_status.decode('utf-8'))

    _metsagent = agent(organisation_name)

    _metshdr.append(_metsagent)

    return _metshdr

