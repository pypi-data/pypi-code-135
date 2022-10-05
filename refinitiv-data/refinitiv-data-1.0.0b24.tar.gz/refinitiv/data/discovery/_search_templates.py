"""Module to create and use templated search presets for the discovery search

Use templated search from the "Equity" template that was defined in the config:
>>> import refinitiv.data as rd
>>> rd.content.discovery.search_templates["Equity"].search()
"""
__all__ = ["templates"]

import operator
import string
import itertools
from functools import reduce
from typing import Iterable, Optional, Dict, Set, List, Any, Tuple

from humps import depascalize

from refinitiv.data import get_config
from refinitiv.data._tools import inspect_parameters_without_self
from refinitiv.data.errors import ConfigurationError
from refinitiv.data.content.search._definition import Definition
from refinitiv.data.content.search._views import Views

CONFIG_PREFIX = "search.templates"


def depascalize_view(value: str) -> str:
    """Convert search View value to upper snakecase

    We need to have separate function for that because some enum View values
    does not follow the rules of pascal case
    """
    if "STIRs" in value:
        value = value.replace("STIRs", "Stirs")

    return depascalize(value).upper()


def join_sets(sets: Iterable[set]) -> set:
    """Join multiple sets into one"""
    iterator = iter(sets)
    try:
        # Can't pass an empty iterator to `reduce`, that's the way to handle it
        default = next(iterator)
    except StopIteration:
        return set()
    else:
        return reduce(operator.or_, iterator, default)


def generate_docstring(description: str, methods: Dict[str, dict]):
    doc = [
        description,
        "",
        "    Methods",
        "    -------",
    ]

    for method_name, method_desc in methods.items():
        doc.append(f"    {method_name}")

        for param, desc in method_desc["args"].items():
            doc.append(f"        {param}")
            if "description" in desc:
                doc.append(f"            {desc['description']}")
            if "default" in desc:
                doc.append(f"            default: {repr(desc['default'])}")
            doc.append("")

    return "\n".join(doc)


def shorten_string_to_include_position(
    line: str, limit: int, pos: int, padding: int = 0
) -> Tuple[str, int]:
    """Shorten string to given limit to include given position

    Can be used when we need to display position in a string when screen width is
    limited.

    Parameters
    ----------
    line : str
        target string
    limit : int
        maximum length of resulting string
    pos : int
        position in string that must be included in shortened string, starting from 0
    padding
        number of symbols left and right of pos that also must be included

    Returns
    -------
    Tuple of shortened string and number of symbols removed from the start
    """
    cur_right = pos + padding
    if padding >= len(line):
        raise ValueError("padding must be less than the length of line")
    if len(line) <= limit:
        return line, 0
    if cur_right < limit:
        return line[:limit], 0
    left = max(cur_right - limit + 1, 0)
    return line[left:cur_right + 1], left


def index_to_line_and_col(index: int, target_string: str) -> Tuple[int, int]:
    """Convert position index in multiline string to line and column

    Parameters
    ----------
    index : int
        index of symbol in target string
    target_string : str
        target string

    Returns
    -------
    Tuple of line index and column index of given symbol, starting from zero
    """
    lines = target_string[:index].splitlines(keepends=True)

    if not lines:
        return 0, 0

    col_index = index - len("".join(lines[:-1]))
    line_index = len(lines) - 1
    return line_index, col_index


class InvalidPlaceholderError(ValueError):
    """Exception to display syntax errors in string templates"""

    def __init__(
        self,
        index: int,
        template_text: str,
        limit: int = 80,
        padding: int = 0,
        prefix: str = "",
    ):
        """
        Parameters
        ----------
        index : int
            index of wrong placeholder start, get it from regex match
        template_text
            original text template
        limit : int
            maximum length of error message
        padding : int
            padding around place where invalid placeholder starts in error message text
        prefix : int
            prefix before error message, for additional information
        """
        self.limit = limit
        self.padding = padding
        self.index = index
        self.template_text = template_text
        self.prefix = prefix

    def __str__(self):
        line_index, col_index = index_to_line_and_col(self.index, self.template_text)
        target_line = self.template_text.splitlines()[line_index]
        target_line, shift = shorten_string_to_include_position(
            target_line, self.limit, col_index, self.padding
        )
        return "\n".join(
            [
                f"{self.prefix}Invalid placeholder in the template string: "
                f"line {line_index + 1}, col {col_index + 1}:",
                target_line,
                "-" * (col_index - shift) + "^",
            ]
        )


class StringTemplate(string.Template):
    """string.Template with extended validation capabilities"""

    delimiter = "#"

    def names(self) -> Set[str]:
        """Get names of substitution variables in pattern"""
        return {
            match_tuple[1] or match_tuple[2]  # named or braced
            for match_tuple in self.pattern.findall(self.template)
            if match_tuple[1] or match_tuple[2]
        }

    def validate(self, prefix: str = ""):
        """Validate sub variables syntax and raise InvalidPlaceholderException"""

        def convert(mo):
            if mo.group("invalid") is None:
                return

            raise InvalidPlaceholderError(
                mo.start("invalid"),
                self.template,
                padding=3,
                prefix=prefix,
            )

        self.pattern.sub(convert, self.template)


class SearchTemplate:
    """Discovery search preset

    Initialized with default values for content.search.Definition.
    Any string value acts as template string. You can use placeholder variables,
    and that variables will be required to prepare search parameters through
    `._search_kwargs()` or to launch search through `.search()`.

    Placeholder variables syntax:
    - Prepend variable name with # symbol: #varname
    - If after variable name must come alphanumeric symbol or _, that can be interpreted
      like a part of variable name - use curly braces: #{varname}
    - Or you can use hash with curly braces all the time, if you want
    - Hash symbol escaped with itself. '##' will be interpreted as '#'.

    Attributes
    ----------

    name: str
        name of the template

    Examples
    --------

    >>> SearchTemplate(filter="ExchangeName xeq '#name'")._search_kwargs(name="<name>")
    {'filter': "ExchangeName xeq '<name>'"}
    >>> SearchTemplate(filter="ExchangeName xeq '#name'")._search_kwargs()
    Traceback (most recent call last):
        ...
    KeyError: 'Those keyword arguments must be defined, but they are not: name'
    >>> SearchTemplate(filter="ExchangeName xeq '#{name}'", placeholders_defaults={"name": "<name>"})._search_kwargs()
    {'filter': "ExchangeName xeq '<name>'"}
    """

    def __init__(
        self,
        name=None,
        placeholders_defaults: Optional[Dict[str, Any]] = None,
        pass_through_defaults: Optional[Dict[str, Any]] = None,
        **search_defaults,
    ):
        """
        Parameters
        ----------
        name : str, optional
            name of the template
        placeholders_defaults: dict, optional
            <placeholder_name> : <placeholder_default_value>
        search_defaults
            default values for discovery search Definition
        """
        self._available_search_kwargs = inspect_parameters_without_self(Definition)
        """ List search keyword arguments we can use in this template """
        self._placeholders_defaults = (
            {} if placeholders_defaults is None else placeholders_defaults
        )
        """ Default template variables values for a templated defaults """
        if pass_through_defaults is None:
            pass_through_defaults = {}

        bad_pass_through_params = (
            set(pass_through_defaults) - self._available_search_kwargs
        )
        if bad_pass_through_params:
            raise ValueError(
                "All the parameters described in 'parameters' section of search "
                "template configuration, must be either placeholders variables or "
                "parameters of the discovery search Definition. Those parameters are "
                "neither of them: " + ", ".join(bad_pass_through_params)
            )

        self.name = name

        unknown_defaults = set(search_defaults) - set(self._available_search_kwargs)
        if unknown_defaults:
            raise ValueError(
                "This arguments are defined in template, but not in search Definition: "
                + ", ".join(unknown_defaults)
            )

        self._placeholders_names: Set[str] = set()
        self._templated_defaults: Dict[str, StringTemplate] = {}
        self._pass_through_defaults: Dict[str, Any] = {}

        for name, value in search_defaults.items():

            if not isinstance(value, str):
                self._pass_through_defaults[name] = value
                continue

            template = StringTemplate(value)
            template.validate(prefix=f'Parameter "{name}": ')
            if template.names():
                self._templated_defaults[name] = template
                self._placeholders_names |= template.names()
            else:
                self._pass_through_defaults[name] = value

        self._pass_through_defaults.update(pass_through_defaults)

        bad_tpl_var_names = self._placeholders_names & self._available_search_kwargs
        if bad_tpl_var_names:
            raise ValueError(
                "You can't use template arguments with the same name"
                " as search arguments. You are used: " + ", ".join(bad_tpl_var_names)
            )

    def _defaults(self):
        return itertools.chain(self._templated_defaults, self._pass_through_defaults)

    def __repr__(self):
        return f"<SearchTemplate '{self.name}'>"

    def _search_kwargs(self, **kwargs) -> dict:
        """Get dictionary of arguments for content.search.Definition"""

        undefined_placeholders = (
            self._placeholders_names - set(kwargs) - set(self._placeholders_defaults)
        )

        if undefined_placeholders:
            raise KeyError(
                "Those keyword arguments must be defined, but they are not: "
                + ", ".join(undefined_placeholders)
            )

        unexpected_arguments = (
            set(kwargs)
            - self._placeholders_names
            # templated defaults can't be redefined
            - (self._available_search_kwargs - self._templated_defaults.keys())
        )

        if unexpected_arguments:
            raise KeyError(f"Unexpected arguments: {', '.join(unexpected_arguments)}")

        kwargs = kwargs.copy()
        # Applying template variables defaults
        for name, value in self._placeholders_defaults.items():
            if name not in kwargs:
                kwargs[name] = value

        result = self._pass_through_defaults.copy()

        # Apply variables to templated defaults
        for name, template in self._templated_defaults.items():
            result[name] = template.substitute(**kwargs)

        # Apply other variables from kwargs
        for name, value in kwargs.items():
            if name not in self._placeholders_names:
                result[name] = value

        return result

    def search(self, **kwargs):
        """Please, use help() on a template object itself to get method documentation"""
        # ^ we need this docstring because we can't easily generate docstring for
        # the method, but can change __doc__ for class instance
        return Definition(**self._search_kwargs(**kwargs)).get_data().data.df


class Templates:
    """Easy access to search templates from the library config

    Check if search template with the name "Equity" is defined in the config:
    >>> templates = Templates()
    >>> "Equity" in templates
    True
    Get "Equity" search template:
    >>> templates["Equity"]
    Get list of available search template names:
    >>> templates.keys()
    ["Equity"]
    """

    def __iter__(self):
        config = get_config()
        return config.get(CONFIG_PREFIX, {}).keys().__iter__()

    def __getitem__(self, name: str) -> SearchTemplate:
        config = get_config()
        key = f"{CONFIG_PREFIX}.{name}"
        if key not in config:
            raise KeyError(f"Template '{name}' is not found in the config")
        data = config[key].as_attrdict() if config[key] is not None else {}

        # <param_name>: {"default": <default>, "description": <doc>}
        tpl_strs_defaults = {
            name: attrs["default"]
            for name, attrs in data.get("parameters", {}).items()
            if "default" in attrs
        }
        params = depascalize(data.get("request_body", {}))

        if "view" in params:
            # Convert string value to enum for the view argument
            view = params["view"]
            try:
                params["view"] = getattr(Views, depascalize_view(view))
            except AttributeError:
                raise ConfigurationError(
                    -1,
                    f"Wrong search template value: View={view}. "
                    "It must be one of the following: "
                    f"{', '.join(Views.possible_values())}",
                )
        tpl = SearchTemplate(name, placeholders_defaults=tpl_strs_defaults, **params)

        method_args = {}
        # Some placeholders may be only in string, but not in "parameters"
        for param in sorted(tpl._placeholders_names):
            method_args[param] = data.get("parameters", {}).get(param, {})

        # That's why we can get them all in one cycle with pass-through parameters
        # that is located in "parameters" config session, but not in template string
        for param, desc in data.get("parameters", {}).items():
            if param not in tpl._placeholders_names:
                method_args[param] = desc

        tpl.__doc__ = generate_docstring(
            description=data.get("description", ""),
            methods={"search": {"description": "", "args": method_args}},
        )

        return tpl

    def keys(self) -> List[str]:
        """Get list of available search template names"""
        return list(self)


templates = Templates()
