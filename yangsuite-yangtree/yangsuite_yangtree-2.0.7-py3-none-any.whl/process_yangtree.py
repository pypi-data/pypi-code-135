#! /usr/bin/env python
import os
import sys
import json
import configparser
import django
import argparse

from ysfilemanager import merge_user_set
from yangsuite.application import read_prefs
from yangsuite import get_logger, set_base_path
from ysyangtree.context import YSContext


config = read_prefs()
prefs = config[configparser.DEFAULTSECT]

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      prefs.get('settings_module'))
os.environ.setdefault('MEDIA_ROOT',
                      prefs.get('data_path'))
django.setup()
from yangsettree import (
    TreeUserError,
    TreeCacheError,
    TreeContextError,
    generate_key
)
from ysyangtree.ymodels import (
    YSYangModels,
    DEFAULT_INCLUDED_NODETYPES
)


log = get_logger(__file__)


def create_tree_process(owner, setname, modules, repo,
                        ref='',
                        nodes=DEFAULT_INCLUDED_NODETYPES,
                        plugin_name='yangsuite-yangtree',
                        node_callback=None,
                        child_class=None,
                        queue=None):
    """Create tree in separate process for quick release of memory.

    Args:
        owner (str): User name
        setname(str): Name of setname
        modules (dict): A dictionary of modules
        repo(str): User repository
        ref (str): Reference
        nodes (frozenset): Nodes included in tree
        plugin_name (str): Name of plugin
        node_callback (function): Function to call for each node in the tree
            in order to populate additional data into the tree. Must accept
            kwargs ``stmt``, ``node``, and ``parent_data``
            (which may be ``None``), and return ``node``.
        child_class (Object): Custom pyang parser.
        queue (str): JSON file name for temporary storage.
    """
    if modules and queue:
        # Need valid cache entries
        try:
            log.info('Creating new tree for {0}'.format(
                ', '.join([n for n in modules])
            ))
            # YSContext memory gets released after this process ends.
            ctx = YSContext.get_instance(ref, merge_user_set(
                owner, setname
            ))
        except RuntimeError:
            raise TreeUserError("No such user")
        except KeyError:
            raise TreeCacheError('Bad cache reference')
        if ctx is None:
            raise TreeContextError("User context not found")
        models = YSYangModels(ctx, modules, child_class=child_class,
                              included_nodetypes=nodes,
                              node_callback=node_callback)
        supports = {}
        main = {}
        for modtree in models.jstree['data']:
            mod = modtree['text']
            key = generate_key(
                owner, setname, mod, ref, plugin_name, nodes
            )
            if 'children' not in modtree:
                supports[mod] = {'tree': modtree, 'key': key, 'supports': ''}
            else:
                main[mod] = {'tree': modtree, 'key': key}

        for mod, data in supports.items():
            info = data['tree'].get('data')
            if info:
                includes = info.get('belongs-to', [])
                includes += info.get('imports', [])
                for inc in includes:
                    if inc in main:
                        supports[mod]['supports'] = main[inc]['key']

        supports.update(main)
        main = supports

        with open(queue, 'w') as fd:
            json.dump(main, fd)


if __name__ == '__main__':
    breakpoint()

    try:
        config = read_prefs()
        prefs = config[configparser.DEFAULTSECT]
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              prefs.get('settings_module'))
        os.environ.setdefault('MEDIA_ROOT',
                              prefs.get('data_path'))
        parser = argparse.ArgumentParser()
        parser.add_argument('--user', type=str)
        parser.add_argument('--setname', type=str)
        parser.add_argument('--modules', nargs='*')
        parser.add_argument('--ref', type=str)
        parser.add_argument('--repo', type=str)
        parser.add_argument('--nodes', nargs='+')
        parser.add_argument('--plugin_name', type=str,
                            default='yangsuite-yangtree')
        parser.add_argument('--node_callback', type=os.fsencode)
        parser.add_argument('--child_class', type=os.fsencode)
        parser.add_argument('--basepath', type=str)
        args = parser.parse_args()

        django.setup()
        if args.basepath:
            set_base_path(args.basepath)

        print('success')
    except RuntimeError as e:
        print('Error: :404:', str(e), file=sys.stderr)
        print(str(e.output))
        exit(1)
