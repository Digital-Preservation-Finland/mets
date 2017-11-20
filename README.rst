METS Library
============

This repository contains general Python functions for METS XML handling.

Installation
------------

This software is tested with Python 2.7 with Centos 7.x / RHEL 7.x releases.
Support for Python 3 is not planned in recent future.


Install the required software with command::

    pip install -r requirements_dev.txt

Usage
-----

Import the library with::

    import mets

All the functions can now be used with calling mets.<function>.

For example, the div() function in structmap_base.py can be used with::

    div_elem = mets.div(type_attr='xxx')

This creates a METS <div> element to div_elem as lxml.etree.

Please, see the METS documentation for more information:
http://www.loc.gov/standards/mets/

Copyright
---------
All rights reserved to CSC - IT Center for Science Ltd.
