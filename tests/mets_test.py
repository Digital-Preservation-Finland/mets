"""Test the `preservation.mets` module"""

import pytest


from preservation.workflow.utils import read_xml

from luigi import LocalTarget

import preservation.mets as m


@pytest.fixture
def mets():
    """Return a test mets.xml file

    :returns: METS as ElementTree

    """
    return read_xml(LocalTarget(
        'tests/data/sips/csc_test_valid_sip/mets.xml')).getroot()


def test_find_created_date():
    """Test the `preservation.mets.find_created_date` function

    :returns: None

    """

    (created_date, last_modified_date) = m.get_created_date(mets())

    assert created_date == '2013-11-19T16:40:17'
    assert last_modified_date is None


def test_get_objid():
    """Test the `preservation.mets.get_objid` function.

    :returns: None

    """

    objid = m.get_objid(mets())
    assert objid == 'kdk-csc-sip001'
