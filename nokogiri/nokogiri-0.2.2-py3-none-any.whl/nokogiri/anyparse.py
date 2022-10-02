#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try: 
    import configargparse as argparse
    from configargparse import *
except:
    import argparse
    from argparse import *
from nokogiri.which_env import which_env

class ArgumentParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jupyter_args = list()
    def jupyter_argument(self, args):
        if type(args) == str:
            self.jupyter_args = args.split()
        else:
            self.jupyter_args = args
    def parse_args(self, *args, **kwargs):
        if which_env() == which_env.JUPYTER:
            return self.parse_known_args(self.jupyter_args)[0]
        else:
            return super().parse_args(*args, **kwargs)