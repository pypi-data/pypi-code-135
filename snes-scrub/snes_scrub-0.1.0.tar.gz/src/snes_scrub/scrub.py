from collections import namedtuple
from functools import reduce
from pkg_resources import resource_filename
import argparse
import hashlib
import os
import sys
import xml.etree.ElementTree as ElementTree

DAT_FILE = 'Nintendo - Super Nintendo Entertainment System (20221002-102033).dat'
DEFAULT_OUTPUT_DIR = 'scrubbed'
EXTENSIONS = ('.sfc', '.swc', '.smc')

Game = namedtuple(
    'Game',
    (
        'name',
        'filename',
        'size',
        'sha1',
    ))

def main():
    args = create_argparser().parse_args()

    if os.path.abspath(args.input) == os.path.abspath(args.output):
        print("Sorry, for safety's sake, we can't write scrubbed files into the same directory we're reading from.")
        sys.exit(1)

    sha_db = parse_dat(resource_filename(__name__, DAT_FILE))
    rom_list = get_rom_file_list(args)

    if len(rom_list) > 0:
        print(f'Found {len(rom_list)} games in {args.input}. Scrubbing into {args.output}...')
        if not os.path.exists(args.output):
            os.makedirs(args.output)
        for filename in rom_list:
            clean_game(filename, sha_db, args)
    else:
        print('No games found.')

    print('Done!')

def create_argparser():
    parser = argparse.ArgumentParser(description='Strip SMC headers and rename SNES ROM files using no-intro.org data and naming conventions')

    parser.add_argument('-i', '--input',
                        metavar='INPUT_DIR',
                        default=os.getcwd(),
                        help=f'the directory to scan for ROM files; defaults to the current directory')
    
    parser.add_argument('-o', '--output',
                        metavar='OUTPUT_DIR',
                        default=os.path.join(os.getcwd(), DEFAULT_OUTPUT_DIR),
                        help=f'the directory to write scrubbed files to; defaults to "{DEFAULT_OUTPUT_DIR}" off the current directory')
    
    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help='print per-file processing info')

    return parser

def parse_game_entry(sha_db, game_xml):
    name = game_xml.attrib['name']
    rom = game_xml.find('./rom')
    sha = rom.attrib['sha1']

    sha_db[sha] = Game(
        name = name,
        filename = rom.attrib['name'],
        size = rom.attrib['size'],
        sha1 = sha,
    )

    return sha_db
    
def parse_dat(file):
    xml = ElementTree.parse(file).getroot()
    sha_db = reduce(parse_game_entry, xml.findall('./game'), {})

    return sha_db

def get_rom_file_list(args):
    files = []

    with os.scandir(args.input) as it:
        for entry in it:
            if entry.is_file() and entry.name.lower().endswith(EXTENSIONS):
                files.append(entry.name)

    return files

def clean_game(filename, sha_db, args):
    source = os.path.join(args.input, filename)

    if args.verbose:
        print(f'Inspecting {source}...')

    game, offset = find_entry(source, sha_db)

    if game:
        target = os.path.join(args.output, game.filename)

        if args.verbose:
            print(f'  Found entry {game.name} using file offset {offset}!')
            print(f'  Copying {source} to {target} from offset {offset}...')

        copy_clean(source, target, offset)
    else:
        if args.verbose:
            print(f'  Could not find a DB entry for {filename}. Skipping.')

def find_entry(filename, sha_db):
    sha = hash_from(filename)

    if sha in sha_db:
        return (sha_db[sha], 0)
    else:
        sha = hash_from(filename, 512)
        if sha in sha_db:
            return (sha_db[sha], 512)

    return (None, None)
    
def hash_from(filename, offset=0):
    with open(filename, 'r+b') as f:
        f.seek(offset)
        hasher = hashlib.sha1()
        hasher.update(f.read())

        return hasher.hexdigest()

def copy_clean(source, target, offset=0):
    with open(source, 'r+b') as s:
        with open(target, 'w+b') as t:
            s.seek(offset)
            t.write(s.read())
