import os
import sys
import shutil
import pytest


@pytest.mark.parametrize("name", ['duplicate', 'unused_duplicate'])
def test_duplicate(name, tmpdir):
    print(f'{name} {tmpdir}')
    shutil.copy(f'examples/{name}.py', f'{tmpdir}/{name}.py')
    os.system(f'{sys.executable} flake8-start.py {tmpdir}')
    with open(f'{tmpdir}/.flake8') as fh:
        actual = fh.readlines()
    with open(f'examples/{name}.flake8') as fh:
        expected = fh.readlines()
    assert actual == expected
