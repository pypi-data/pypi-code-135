import ast
import abc
import copy
import importlib
import re
import logging
from importlib.metadata import entry_points
from typing import List

from ..node import DrbNode
from ..predicat import Predicate
from ..exceptions import DrbException


class Signature(abc.ABC):
    """
    A signature describes a recognition mechanism for a specific type of DRB
    Item (ItemClass). This recognition mechanism is applied on a DRB Node.
    """

    @abc.abstractmethod
    def matches(self, node: DrbNode) -> bool:
        """
        Allowing to check if the given node match the signature.
        Parameters:
            node (DrbNode): item to check
        Returns:
            bool - ``True`` if the given node match, otherwise ``False``
        """
        raise NotImplementedError

    @abc.abstractmethod
    def to_dict(self) -> dict:
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def get_name():
        return ''


class SignatureAggregator(Signature):
    """
    Allowing to check if a DRB Node match a signature set.
    Parameters:
        signatures List[Signature]: signature list to match
    """

    def __init__(self, signatures: List[Signature]):
        self._signatures = signatures

    def matches(self, node: DrbNode) -> bool:
        if len(self._signatures) == 0:
            return False
        for signature in self._signatures:
            if not signature.matches(node):
                return False
        return True

    def to_dict(self) -> dict:
        data = {}
        for signature in self._signatures:
            for k, v in signature.to_dict().items():
                data[k] = v
        return data

    @staticmethod
    def get_name():
        return 'aggregator'


class NameSignature(Signature):
    """
    Allowing to check if a DRB Node name match a specific regex.
    Parameters:
        regex (str): regex pattern to match
    """

    def __init__(self, regex: str):
        self.__regex = regex

    def matches(self, node: DrbNode) -> bool:
        return re.match(self.__regex, node.name) is not None

    def to_dict(self) -> dict:
        return {self.get_name(): self.__regex}

    @staticmethod
    def get_name():
        return 'name'


class NamespaceSignature(Signature):
    """
    Allowing to check if a DRB Node namespace_uri match a specific regex.
    Parameters:
        regex (str): regex pattern to match
    """

    def __init__(self, regex: str):
        self.__regex = regex

    def matches(self, node: DrbNode) -> bool:
        return re.match(self.__regex, node.namespace_uri) is not None

    def to_dict(self) -> dict:
        return {self.get_name(): self.__regex}

    @staticmethod
    def get_name():
        return 'namespace'


class PathSignature(Signature):
    """
    Allowing to check if a DRB Node path match a specific regex.
    Parameters:
        regex (str): regex pattern to match
    """

    def __init__(self, regex: str):
        self.__regex = regex

    def matches(self, node: DrbNode) -> bool:
        return re.match(self.__regex, node.path.name) is not None

    def to_dict(self) -> dict:
        return {self.get_name(): self.__regex}

    @staticmethod
    def get_name():
        return 'path'


class AttributeSignature(Signature):
    """
    Allowing to check if a DRB Node having a specific attribute and also to
    check its value.
    Parameters:
        name (str): attribute name
    Keyword Arguments:
        namespace (str): attribute namespace
        value (Any): attribute value
    """

    def __init__(self, name: str, **kwargs):
        self.__name = name
        self.__namespace = kwargs.get('namespace', None)
        self.__check_value = 'value' in kwargs.keys()
        self.__value = kwargs.get('value', None)

    def matches(self, node: DrbNode) -> bool:
        try:
            value = node.get_attribute(self.__name, self.__namespace)
            if self.__check_value:
                return self.__value == value
            return True
        except DrbException:
            return False

    def to_dict(self) -> dict:
        data = {'name': self.__name}
        if self.__namespace is not None:
            data['namespace'] = self.__namespace
        if self.__value is not None:
            data['value'] = self.__value
        return data

    @staticmethod
    def get_name():
        return 'attribute'


class AttributesSignature(SignatureAggregator):
    """
    Allowing to check one or several attribute of a node.
    """

    def __init__(self, attributes: list):
        signatures = []
        for data in attributes:
            signatures.append(AttributeSignature(**data))
        super().__init__(signatures)

    def to_dict(self) -> dict:
        return {self.get_name(): [sig.to_dict() for sig in self._signatures]}

    @staticmethod
    def get_name():
        return 'attributes'


class ChildSignature(Signature):
    """
    Allowing to check if a DRB Node having a child matching specific criteria.

    Parameters:
        name (str): child name pattern

    Keyword Arguments:
        namespace (str): child node namespace (default: None)
        namespaceAware (bool): namespace_aware node flag (default: ``False``)
    """

    class _ChildPredicate(Predicate):
        def __init__(self, name: str, ns: str = None, aware: bool = False):
            self.__name = name
            self.__ns = ns
            self.__ns_aware = aware

        def matches(self, node) -> bool:
            match = re.match(self.__name, node.name)
            if match is None:
                return False
            if self.__ns is not None:
                return True if node.namespace_uri == self.__ns else False
            if self.__ns_aware:
                return self.__ns == node.namespace_uri
            return True

    def __init__(self, name: str, **kwargs):
        self.__name = name
        self.__ns = kwargs.get('namespace', None)
        self.__aware = kwargs.get('namespaceAware', False)
        self.__predicate = ChildSignature._ChildPredicate(
            self.__name, self.__ns, self.__aware)

    def matches(self, node: DrbNode) -> bool:
        try:
            n = node[self.__predicate]
            return len(n) > 0
        except DrbException:
            return False

    def to_dict(self) -> dict:
        data = {'name': self.__name}
        if self.__ns is not None:
            data['namespace'] = self.__ns
        if self.__aware:
            data['namespaceAware'] = self.__aware
        return data

    @staticmethod
    def get_name():
        return 'child'


class ChildrenSignature(SignatureAggregator):
    """
    Allowing to check if specific children of a DRB Node match their associated
    criteria.

    Parameters:
        children (list): data list, each data must allow generation of a
                         ChildSignature
    """

    def __init__(self, children: list):
        signatures = []
        for data in children:
            signatures.append(ChildSignature(**data))
        super().__init__(signatures)

    def to_dict(self) -> dict:
        return {self.get_name(): [sig.to_dict() for sig in self._signatures]}

    @staticmethod
    def get_name():
        return 'children'


class ParentSignature(Signature):
    """
    Allowing to check if the parent node match a signature.
    """

    def __init__(self, data: dict):
        raise NotImplementedError

    def matches(self, node: DrbNode) -> bool:
        # TODO
        return False

    def to_dict(self) -> dict:
        pass

    @staticmethod
    def get_name():
        return 'parent'


class PythonSignature(Signature):
    """
    Allowing to check if a DRB Node match a custom signature.

    Parameters:
        script (str): custom Python (3.8+) script signature, this script must
                    return a boolean, otherwise ``False`` will be always
                    returned
    """

    _logger = logging.getLogger('PythonSignature')
    _ident = '  '

    def __init__(self, script: str):
        self.__code = self._ident + script.replace('\n', f'\n{self._ident}')
        self._script = f'def match():\n{self.__code}\nmatch()'

    # code from https://stackoverflow.com/questions/33409207
    @staticmethod
    def _convert_expr2expression(expr) -> ast.Expression:
        expr.lineno = 0
        expr.col_offset = 0
        result = ast.Expression(expr.value, lineno=0, col_offset=0)
        return result

    # code from https://stackoverflow.com/questions/33409207
    # updated to include the current node in the execution context
    @staticmethod
    def _exec_with_return(code: str, node: DrbNode):
        code_ast = ast.parse(code)

        init_ast = copy.deepcopy(code_ast)
        init_ast.body = code_ast.body[:-1]

        last_ast = copy.deepcopy(code_ast)
        last_ast.body = code_ast.body[-1:]

        my_globals = globals()
        my_globals['node'] = node

        exec(compile(init_ast, "<ast>", "exec"), my_globals)
        if type(last_ast.body[0]) == ast.Expr:
            return eval(compile(
                PythonSignature._convert_expr2expression(last_ast.body[0]),
                "<ast>", "eval"), my_globals)
        else:
            exec(compile(last_ast, "<ast>", "exec"), my_globals)

    def matches(self, node: DrbNode) -> bool:
        try:
            result = PythonSignature._exec_with_return(self._script, node)
            if isinstance(result, bool):
                return result
            return False
        except Exception as ex:
            self._logger.debug('An error occurred during a Python signature'
                               f' check: {ex}')
            return False

    def to_dict(self) -> dict:
        return {self.get_name(): self.__code}

    @staticmethod
    def get_name():
        return 'python'


class Signatures:
    list_signatures = None

    @staticmethod
    def get_signatures(signature_name: str):
        _logger = logging.getLogger('Signatures')

        if Signatures.list_signatures is None:

            Signatures.list_signatures = {}

            eps = entry_points()

            try:
                for ep in eps['drb.signature']:
                    # load module
                    try:
                        importlib.import_module(ep.value)
                    except ModuleNotFoundError as ex:
                        _logger.warning(f'Invalid entry point {ep.name}: '
                                        f'{ex.msg}')
                        continue
            except Exception:
                # No drb.signature defined, not an error
                pass

            subclasses = Signature.__subclasses__()
            subclasses.extend(SignatureAggregator.__subclasses__())
            for subclass in subclasses:
                try:
                    name_signature = subclass.get_name()
                except Exception:
                    name_signature = None

                if name_signature is None or name_signature == '':
                    _logger.warning(f'Signature {subclass.__name__} '
                                    'have no signature name')
                    continue

                if name_signature in Signatures.list_signatures.keys():
                    _logger.warning(
                        f'Signature {name_signature} '
                        f'have more than one definition '
                        f'{Signatures.list_signatures[name_signature]} and '
                        f'{subclass}')

                else:
                    Signatures.list_signatures[name_signature] = subclass

        if signature_name in Signatures.list_signatures.keys():
            return Signatures.list_signatures[signature_name]

        error_msg = f'Signature {signature_name} is unknown ' \
                    f'in the current environment'
        _logger.error(error_msg)
        raise DrbException(error_msg)


def parse_signature(data: dict) -> Signature:
    signatures = []
    for key in data.keys():
        signature = Signatures.get_signatures(key)(data[key])
        if signature is not None:
            signatures.append(signature)
    return SignatureAggregator(signatures)
