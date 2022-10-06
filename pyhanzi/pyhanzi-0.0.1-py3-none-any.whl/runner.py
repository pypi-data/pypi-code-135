#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from argparse import ArgumentParser
import logging
import sys

import pyhanzi
from pyhanzi.compat import PY2

style_map = {
}
func_map = {
}
default_style = '1111'


class NullWriter(object):
    """数据流黑洞，类似 linux/unix 下 /dev/null 的效果。"""
    def write(self, string):
        pass


def get_parser():
    parser = ArgumentParser(description='convert chinese to hanzi.')
    parser.add_argument('-V', '--version', action='version',
                        version='{0} {1}'.format(
                            pyhanzi.__title__, pyhanzi.__version__
                        ))
    # 要执行的函数名称
    parser.add_argument('-f', '--func',
                        help='function name (default: "hanzi")',
                        choices=['hanzi', 'slug'],
                        default='hanzi')

    parser.add_argument('-p', '--separator',
                        help='slug separator (default: "-")',
                        default='-')

    return parser


def main():
    # 禁用除 CRITICAL 外的日志消息
    logging.disable(logging.CRITICAL)

    # read hans from stdin
    if not sys.stdin.isatty():
        pipe_data = sys.stdin.read().strip()
    else:
        pipe_data = ''
    args = sys.argv[1:]
    if pipe_data:
        args.append(pipe_data)

    # 获取命令行选项和参数
    parser = get_parser()
    options = parser.parse_args(args)
    func = getattr(pyhanzi, options.func)
    separator = options.separator

    func_kwargs = {
        'hanzi': {},
    }
    if PY2:
        kwargs = func_kwargs[func.func_name]
    else:
        kwargs = func_kwargs[func.__name__]

    # 重设标准输出流和标准错误流
    # 不输出任何字符，防止污染命令行命令的输出结果
    # 其实主要是为了干掉 jieba 内的 print 语句 ;)
    sys.stdout = sys.stderr = NullWriter()
    result = func(hans, style=style, **kwargs)
    # 恢复默认
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__

    if not result:
        print('')
    elif result and isinstance(result, (list, tuple)):
        if isinstance(result[0], (list, tuple)):
            print(' '.join([','.join(s) for s in result]))
        else:
            print(result)
    else:
        print(result)


if __name__ == '__main__':
    main()
