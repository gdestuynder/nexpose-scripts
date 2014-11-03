#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# Copyright (c) 2014 Mozilla Corporation
# Author: gdestuynder@mozilla.com
import os
from distutils.core import setup
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
setup(
        name = "nexpose-scripts",
        py_modules=[],
        version = "1.0.0",
        author = "Guillaume Destuynder",
        author_email = "gdestuynder@mozilla.com",
        description = ("Rapid7 Nexpose scripts"),
        license = "MPL",
        keywords = "nexpose",
        url = "https://github.com/gdestuynder/nexpose-scripts",
        long_description=read('README.rst'),
        requires=['lxml', 'pnexpose'],
        classifiers=[
"Development Status :: 5 - Production/Stable",
"License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
],
        )
