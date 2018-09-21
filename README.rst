METS Library
============

This repository contains general Python functions for METS XML handling.

Installation
------------

This software is tested with Python 2.7 with Centos 7.x / RHEL 7.x releases.

Install the required software with command::

    pip install -r requirements_github.txt

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
Copyright (C) 2018 CSC - IT Center for Science Ltd.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Lesser General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along
with this program. If not, see <https://www.gnu.org/licenses/>.
