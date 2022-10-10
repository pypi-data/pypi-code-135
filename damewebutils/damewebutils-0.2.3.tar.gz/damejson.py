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

# This program returns a list of broken links in an url

import requests
import argparse
import json
import re
import os

parser = argparse.ArgumentParser()
parser.add_argument("jsonarg", help="url to download json files")
args = parser.parse_args()

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True


m = args.jsonarg
m = re.match(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', args.jsonarg)
# m is an url
if m:
    r = requests.get(args.jsonarg)
    if is_json(r.text):
        print("json file is valid")
    else:
        print("json file is not valid")

if (os.path.isfile(args.jsonarg)):
    with open(args.jsonarg, encoding='utf8') as f:
        text = f.read().strip()
    if is_json(text):
        print("json file is valid")
    else:
        print("json file is not valid")
    
