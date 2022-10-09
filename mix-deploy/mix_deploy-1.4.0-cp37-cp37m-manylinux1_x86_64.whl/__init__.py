from __future__ import absolute_import
import sys
import subprocess
import os

def get_commit_id():
    file_dir = os.path.dirname(__file__)
    with open(os.path.join(file_dir, 'commit_id.txt'), 'r') as f:
        commit_id = f.readlines()
        commit_id = commit_id[0].strip('\n')
    return commit_id

__commit_id__ = get_commit_id()