from passql.exceptions import SqlException
from typing_extensions import TypeAlias
from typing import Dict, Type, Any, Callable, Optional, List
import re

__all__ = (
    'Sql',
    'SqlMaker',
    'SqlConverter',
)

ValueToSqlConverter: TypeAlias = Callable[[Any, 'SqlConverter'], str]


class Sql:
    __slots__ = ('_formatter', '_strings', '_params')

    def __init__(self, formatter: 'SqlFormatter', string: str):
        self._formatter = formatter
        self._strings, self._params = formatter.split(string.strip())
        if not self._params:
            self._params = None

    def __repr__(self):
        if self._strings:
            short_preview = self._strings[0][:10] + \
                            ('..., ' if len(self._strings) > 1 or len(self._strings[0]) > 10 else ', ')
        else:
            short_preview = ''
        params = f"{len(self._params)} param" + ('' if self._params == 1 else 's')
        return f"<Sql: {short_preview}{params}>"

    def __str__(self):
        if self._params is not None:
            raise SqlException(f"Cannot convert {self.__class__.__name__} to string, parameters required!")

        return self._strings[0]

    def format(self, obj: Optional) -> str:
        """
        Parse parameters from obj to sql template.

        :param obj: Any object or dictionary with required fields/keys.
        """
        if self._params is None:
            return self._strings[0]

        result = []
        prm_length = len(self._params)

        if type(obj) is dict:
            for i in range(len(self._strings)):
                result.append(self._strings[i])
                if i < prm_length:
                    value = obj[self._params[i]]
                    result.append(value.format(obj) if type(value) is Sql else self._formatter.value(value))
        else:
            for i in range(len(self._strings)):
                result.append(self._strings[i])
                if i < prm_length:
                    value = getattr(obj, self._params[i])
                    result.append(value.format(obj) if type(value) is Sql else self._formatter.value(value))

        return ''.join(result)


class SqlFormatter:
    __slots__ = ('_prm_pattern', '_escape_char', '_converter')

    def __init__(self, prm_pattern: 're.Pattern', escape_char: str, converter: 'SqlConverter'):
        self._prm_pattern = prm_pattern
        self._escape_char = escape_char
        self._converter = converter

    def split(self, string: str) -> (List[str], List[str]):
        fragments = []
        params = []

        if string:
            last = 0
            for m in re.finditer(self._prm_pattern, string):
                start = m.start(0)

                if start - 2 > 0:
                    if string[start - 1] == self._escape_char:
                        if string[start - 2] != self._escape_char:
                            continue
                elif start - 1 > 0:
                    if string[start - 1] == self._escape_char:
                        continue

                s = string[last:start]
                if s:
                    fragments.append(s)

                last = m.end(0)
                params.append(string[start + 1:last])

            s = string[last:]
            if s or not fragments:
                fragments.append(s)
        else:
            fragments.append(string)

        return fragments, params

    def value(self, value: Any) -> str:
        return self._converter(value)


class SqlConverter:
    __slots__ = ('_type_to_converter', )

    def __init__(self, type_to_converter_map: Dict[Type, ValueToSqlConverter]):
        self._type_to_converter = {}
        for t in type_to_converter_map:
            self._type_to_converter[t] = type_to_converter_map[t]

    def __call__(self, value: Any) -> str:
        converter = self._type_to_converter.get(type(value))
        if converter is None:
            raise SqlException(f"Type of mapping object '{value}' has no any convertor!")

        return converter(value, self)

    def __add__(self, other: 'SqlConverter') -> 'SqlConverter':
        type_to_converters = {}

        for t, converter in self._type_to_converter.items():
            type_to_converters[t] = converter
        for t, converter in other._type_to_converter.items():
            type_to_converters[t] = converter

        return SqlConverter(type_to_converters)


# noinspection PyTypeChecker
NoneSqlFormatter = SqlFormatter(None, None, None)
EmptySql = Sql(NoneSqlFormatter, "")


class SqlMaker:
    __slots__ = ('_formatter', )

    def __init__(self, prm_pattern: 're.Pattern', converter: 'SqlConverter', escape_char: str = '\\'):
        """
        :param prm_pattern: regex pattern to detect parameters.
        :param converter: parameter values converter.
        :param escape_char: char to escape prm_pattern.
        """
        self._formatter = SqlFormatter(prm_pattern, escape_char, converter)

    def __call__(self, string: str) -> Sql:
        return Sql(self._formatter, string)

    @staticmethod
    def empty() -> 'Sql':
        return EmptySql
