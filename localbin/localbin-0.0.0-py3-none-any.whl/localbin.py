#!/usr/bin/python3
# PYTHON_ARGCOMPLETE_OK

# localbin
#
# Copyright (C) 2022 Katie Rust (katie@ktpanda.org)
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys
import re
import time
import os
import argparse
import subprocess
import traceback
import json
import shutil
import zipfile
import tempfile
from urllib.request import Request, urlopen

from pathlib import Path

import argcomplete

VERSION = "0.0.0"

CONFIG_PATH = Path('/etc/localbin.json')
CONFIG = {}

def read_config():
    CONFIG.clear()
    try:
        with CONFIG_PATH.open('r', encoding='utf8') as fp:
            CONFIG.update(json.load(fp))
    except FileNotFoundError:
        pass
    except (ValueError, OSError, UnicodeDecodeError) as e:
        print(f'WARNING: Could not read config file {CONFIG_PATH}: {e}', file=sys.stderr)
    CONFIG.setdefault('url', None)
    CONFIG.setdefault('package', None)

def clrdiffline(line):
    if line.startswith('@'):
        clr = '94'
    elif line.startswith('+'):
        clr = '92'
    elif line.startswith('-'):
        clr = '91'
    else:
        clr = '90'
    return f'\033[{clr}m{line}\n'

def do_install(tempdir, manifest_data):
    localbin = Path('/usr/local/bin')
    sudoers = Path('/etc/sudoers.d')

    install_sudoers = set()
    remove_files = []
    files = []

    for script, options in manifest_data.items():
        mode = 0o755
        if options.get('setuid'):
            mode = 0o4755
        if options.get('sudo'):
            install_sudoers.add(script)
        if options.get('delete'):
            remove_files.append(localbin / script)
            continue

        files.append((tempdir / script, localbin / script, mode))

    existing_sudoers = set(f for f in sudoers.iterdir() if f.suffix == '' and f.name.startswith('lbin-'))
    existing_sudoers.update(f for f in sudoers.iterdir() if f.name in install_sudoers)

    for cmd in install_sudoers:
        cmdpath = localbin / cmd
        dest = sudoers / f'lbin-{cmd}'
        existing_sudoers.discard(dest)
        files.append((f'%adm ALL=NOPASSWD:{cmdpath}\n', dest, 0o440))

    difflines = []
    for src, dst, mode in files:
        if isinstance(src, Path):
            proc = subprocess.run(['diff', '-N', '-U3', dst, src], stdout=subprocess.PIPE, check=False, encoding='utf8', errors='replace')
            if proc.stdout:
                difflines.append(f'\033[1m\033[93m=== {dst.name}:\n')
                for line in proc.stdout.strip().split('\n')[2:]:
                    if line.startswith('@'):
                        clr = '94'
                    elif line.startswith('+'):
                        clr = '92'
                    elif line.startswith('-'):
                        clr = '91'
                    else:
                        clr = '90'
                    difflines.append(clrdiffline(line))
                difflines.append('\033[39m\n')
        else:
            try:
                text = dst.read_text(encoding='utf8', errors='replace').strip()
            except OSError:
                text = ''
            src = src.strip()
            if text != src:
                difflines.append(f'\033[1m\033[93m=== {dst.name}:\n')
                if text:
                    for line in text.split('\n'):
                        difflines.append(clrdiffline('-' + line))
                for line in src.split('\n'):
                    difflines.append(clrdiffline('+' + line))
                difflines.append('\033[39m\n')

    remove_files.extend(existing_sudoers)

    remove_files = [path for path in remove_files if path.exists()]

    for path in remove_files:
        difflines.append(f'REMOVE {path}\n')

    if not difflines:
        print('no differences')
        return

    difftxt = ''.join(difflines)
    while True:
        if len(difflines) > 35:
            subprocess.run(['less', '-iSr'], input=difftxt, encoding='utf8', check=True)
        else:
            print(difftxt, end='')

        ans = input('ok? ').lower()
        if ans == 'y':
            break
        if ans == 'n':
            return

    for src, dst, mode in files:
        try:
            if isinstance(src, Path):
                shutil.copy2(src, dst)
            else:
                dst.write_text(src, encoding='utf8')
            os.chmod(dst, mode)
        except IOError as e:
            print(f'Error installing {dst}: {e}')

    for path in remove_files:
        try:
            path.unlink()
        except IOError as e:
            print(f'Error removing {path}: {e}')

def main():
    p = argparse.ArgumentParser(description='Install scripts in /usr/local/bin')
    p.add_argument('-s', '--source', metavar='URL', help='Source URL (base)')
    p.add_argument('-p', '--package', metavar='NAME', help='Package to install from source')
    #p.add_argument(help='')

    argcomplete.autocomplete(p)
    args = p.parse_args()

    os.chdir('/usr/local/bin')

    if os.geteuid() != 0:
        os.execvp('/usr/bin/sudo', ['sudo', sys.executable, '-m', 'localbin'] + sys.argv[1:])
        return

    read_config()

    if not args.package:
        args.package = CONFIG['package']

    if not args.source:
        args.source = CONFIG['url']

        if not args.source:
            print('Source URL not configured! Set the URL with --source.')
            return 1

    if not args.source.endswith('/'):
        args.source += '/'

    write_config = False
    if args.source != CONFIG['url']:
        CONFIG['url'] = args.source
        write_config = True

    if args.package != CONFIG['package']:
        CONFIG['package'] = args.package
        write_config = True

    if write_config:
        config_temp = CONFIG_PATH.with_suffix('.json-tmp')
        with config_temp.open('w', encoding='utf8') as fp:
            json.dump(CONFIG, fp, indent=4)
        config_temp.replace(CONFIG_PATH)

    url = args.source + (args.package or 'default') + '.zip'

    td = tempfile.mkdtemp(prefix='localbin-install')
    try:
        tmppath = Path(td)
        zipf = tmppath / 'package.zip'
        with urlopen(url) as urlf:
            with zipf.open('wb') as tmpzip:
                shutil.copyfileobj(urlf, tmpzip)

        with zipfile.ZipFile(zipf) as zip:
            manifest_data = json.loads(zip.read('manifest.json').decode('utf8'))
            for path, options in manifest_data.items():
                if '/' in path:
                    continue
                if not options.get('delete'):
                    zip.extract(path, td)

        do_install(tmppath, manifest_data)
    finally:
        shutil.rmtree(td)

if __name__ == '__main__':
    sys.exit(main())
