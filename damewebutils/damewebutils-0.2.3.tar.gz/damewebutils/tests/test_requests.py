#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2019  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with damewebutils; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,


# Summary from https://requests.readthedocs.io/en/master/user/quickstart/

from unittest import TestCase
import requests


class TestRequests(TestCase):

    def test_options(self):
        u = 'https://api.github.com/repositories/1362490/issues/482'
        r = requests.get(u)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.url, u)
        r = requests.post('https://httpbin.org/post', data={'key': 'value'})
        print(r.text)
        j = '{\n "args": {}, \n "data": "", '
        j = '\n "files": {}, \n "form": {\n "key":'
        j = j + '"value"\n }, \n "headers": '
        j = j + '{\n "Accept": "*/*", \n "Accept-Encoding":'
        j = j + '"gzip, deflate", \n "Content-Length": "9", \n "Content-Type":'
        j = j + '"application/x-www-form-urlencoded",'
        j = j + '\n "Host": "httpbin.org", \n'
        j = j + '"User-Agent": "python-requests/2.18.4",'
        j = j + '\n "X-Amzn-Trace-Id": '
        self.assertTrue("x-www-form-urlencoded" in r.text)
        self.assertEqual(r.raise_for_status(), None)
        self.assertEqual('true', r.headers['Access-Control-Allow-Credentials'])
