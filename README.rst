METS Library
============

This repository contains general Python functions for METS XML handling.

Installation
------------

Installation and usage requires Python 2.7, or 3.6 or newer.
The software is tested with Python 3.6 on Centos 7.x release. Python 2.7 support will be removed in the future.

For Python 3.6 or newer, create a virtual environment::
    
    python3 -m venv venv

For Python 2.7, get python-virtualenv software and create a virtual environment::

    sudo yum install python-virtualenv
    virtualenv venv

Run the following to activate the virtual environment::

    source venv/bin/activate

Install the required software with commands::

    pip install --upgrade pip==20.2.4 setuptools  # Only for Python 3.6 or newer
    pip install --upgrade pip setuptools          # Only for Python 2.7
    pip install -r requirements_github.txt
    pip install .

To deactivate the virtual environment, run ``deactivate``.
To reactivate it, run the ``source`` command above.


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
