
from ._base import ConfigBase

import _ast
import ast
import sys
import textwrap
import datetime
import typing
# if sys.version_info >= (3, 8):
#    from ast import Str, Num, Bytes, NameConstant  # NOQA


class ConfigPON(ConfigBase):
    suffix = '.pon'

    def load(self) -> typing.Any:
        try:
            data = _loads(self._path.read_text())
        except FileNotFoundError as e:
            print(e)
            data = {}
        if 'glbl' in data and 'global' not in data:
            # cannot have reserved word global in dict(global=....)
            data['global'] = data.pop('glbl')
        return data


# taken from pon.__init__.py
def _loads(node_or_string: typing.Union[_ast.Expression, str], dict_typ: typing.Any=dict, return_ast: bool=False, file_name: typing.Optional[str]=None) -> typing.Any:
    # Safely evaluate an expression node or a string containing a Python
    # expression.  The string or node provided may only consist of the following
    # Python literal structures: strings, bytes, numbers, tuples, lists, dicts,
    # sets, booleans, and None.

    if sys.version_info < (3, 4):
        _safe_names = {'None': None, 'True': True, 'False': False}
    if isinstance(node_or_string, str):
        node_or_string = compile(
            node_or_string,
            '<string>' if file_name is None else file_name,
            'eval',
            _ast.PyCF_ONLY_AST,
        )
    if isinstance(node_or_string, _ast.Expression):
        node_or_string = node_or_string.body  # type: ignore
    else:
        raise TypeError('only string or AST nodes supported')

    def _convert(node: typing.Any, expect_string: bool=False) -> typing.Any:
        if isinstance(node, ast.Str):
            if sys.version_info < (3,):
                return node.s
            return node.s
        elif isinstance(node, ast.Bytes):
            return node.s
        if expect_string:
            pass
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, _ast.Tuple):
            return tuple(map(_convert, node.elts))
        elif isinstance(node, _ast.List):
            return list(map(_convert, node.elts))
        elif isinstance(node, _ast.Set):
            return set(map(_convert, node.elts))
        elif isinstance(node, _ast.Dict):
            return dict_typ(
                (_convert(k, expect_string=False), _convert(v))
                for k, v in zip(node.keys, node.values)
            )
        elif isinstance(node, ast.NameConstant):
            return node.value
        elif sys.version_info < (3, 4) and isinstance(node, ast.Name):
            if node.id in _safe_names:
                return _safe_names[node.id]
        elif (
            isinstance(node, _ast.UnaryOp)
            and isinstance(node.op, (_ast.UAdd, _ast.USub))
            and isinstance(node.operand, (ast.Num, _ast.UnaryOp, _ast.BinOp))
        ):
            operand = _convert(node.operand)
            if isinstance(node.op, _ast.UAdd):
                return +operand
            else:
                return -operand
        elif (
            isinstance(node, _ast.BinOp)
            and isinstance(node.op, (_ast.Add, _ast.Sub, _ast.Mult))
            and isinstance(node.right, (ast.Num, _ast.UnaryOp, _ast.BinOp))
            and isinstance(node.left, (ast.Num, _ast.UnaryOp, _ast.BinOp))
        ):
            left = _convert(node.left)
            right = _convert(node.right)
            if isinstance(node.op, _ast.Add):
                return left + right
            elif isinstance(node.op, _ast.Mult):
                return left * right
            else:
                return left - right
        elif isinstance(node, _ast.Call):
            func_id = getattr(node.func, 'id', None)
            if func_id == 'dict':
                return dict_typ((k.arg, _convert(k.value)) for k in node.keywords)
            elif func_id == 'set':
                return set(_convert(node.args[0]))
            elif func_id == 'date':
                return datetime.date(*[_convert(k) for k in node.args])
            elif func_id == 'datetime':
                return datetime.datetime(*[_convert(k) for k in node.args])
            elif func_id == 'dedent':
                return textwrap.dedent(*[_convert(k) for k in node.args])
        elif isinstance(node, ast.Name):
            return node.s  # type: ignore
        err = SyntaxError('malformed node or string: ' + repr(node))
        err.filename = '<string>'
        err.lineno = node.lineno
        err.offset = node.col_offset
        err.text = repr(node)
        err.node = node  # type: ignore
        raise err

    res = _convert(node_or_string)
    if not isinstance(res, dict_typ):
        raise SyntaxError('Top level must be dict not ' + repr(type(res)))
    if return_ast:
        return res, node_or_string
    return res
