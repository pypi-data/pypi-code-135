from ctypes import Union
from dataclasses import dataclass
from typing import List, Tuple, Dict, Any


@dataclass
class ColorMeta:
    curseIndex: int
    printPrefix: str
    printSubfix: str


COLOR_DICT: Dict[str, ColorMeta] = {
    'k': ColorMeta(2, "\033[0;30m", "\033[0m"),
    'r': ColorMeta(3, "\033[0;31m", "\033[0m"),
    'g': ColorMeta(4, "\033[0;32m", "\033[0m"),
    'y': ColorMeta(5, "\033[0;33m", "\033[0m"),
    'b': ColorMeta(6, "\033[0;34m", "\033[0m"),
    'm': ColorMeta(7, "\033[0;35m", "\033[0m"),
    'c': ColorMeta(8, "\033[0;36m", "\033[0m"),
    'w': ColorMeta(9, "\033[0;37m", "\033[0m"),
}


def change_str(s: str, idx, c):
    temp = list(s)
    temp[idx] = c
    return ''.join(temp)


class OvTable:
    def __init__(self, width: int = 150, height: int = 38, print_to_terminal: bool = True) -> None:
        """ self.table[行][列] = (内容, color) """
        self.table: List[List[List[Tuple[Union[str, Any], Union[str, Any]]]]] = []

        self.width = width
        self.height = height

        self.print_to_terminal = print_to_terminal
        self.c = None
        if not print_to_terminal:
            # on windows pip install windows-curses
            import curses
            self.c = curses
        self.stdscr = None

    def add_row(self, cols: int = 1):
        assert len(self.table) * 2 + 1 <= self.height, f'too many rows {len(self.table) + 1} for height {self.height}!'
        assert cols * 30 <= self.width, f'too many cols {cols} for width {self.width}!'
        self.table.append([[] for _ in range(cols)])

    def __getitem__(self, index: Tuple[int, int]):
        assert len(index) == 2, 'x and y must be decleared!'
        x, y = index
        assert x < len(self.table) and y < len(self.table[x]), 'index out of bound'
        if self.table[x][y] is None:
            self.table[x][y] = []
        return self.table[x][y]

    def __setitem__(self, index: Tuple[int, int], v):
        assert len(index) == 2, 'x and y must be decleared!'
        x, y = index
        assert x < len(self.table) and y < len(self.table[x]), 'index out of bound'

        if (not isinstance(v, type((1, 1))) and not isinstance(v, type([1, 1]))) or len(v) == 1:
            if not isinstance(v, type((1, 1))) and not isinstance(v, type([1, 1])):
                self.table[x][y] = [(v, None)]
            else:
                self.table[x][y] = [(v[0], None)]
        elif len(v) > 1:
            if not isinstance(v[0], type((1, 1))) and not isinstance(v[0], type([1, 1])):  # v is [s, c]
                self.table[x][y] = [v]
            else:  # v is [[s, c], ...]
                self.table[x][y] = list(v)
        else:
            raise KeyError('v should only be like string or (string, color) or [(s, c), (s, c), ...]!')

    def _init_stdscr(self):
        self.stdscr = self.c.initscr()
        self.c.start_color()
        self.c.use_default_colors()
        self.c.init_pair(2, self.c.COLOR_BLACK, -1)
        self.c.init_pair(3, self.c.COLOR_RED, -1)
        self.c.init_pair(4, self.c.COLOR_GREEN, -1)
        self.c.init_pair(5, self.c.COLOR_YELLOW, -1)
        self.c.init_pair(6, self.c.COLOR_BLUE, -1)
        self.c.init_pair(7, self.c.COLOR_MAGENTA, -1)
        self.c.init_pair(8, self.c.COLOR_CYAN, -1)
        self.c.init_pair(9, self.c.COLOR_WHITE, -1)
        self.c.noecho()
        self.c.cbreak()

    def _print_with_color(self, s: str, colorName: str = None, end: str = '') -> None:
        if colorName is not None:
            assert colorName in COLOR_DICT.keys(), f"illegal color: '{colorName}'!"
            colorMeta = COLOR_DICT[colorName]
            print(colorMeta.printPrefix + str(s) + colorMeta.printSubfix, end=end)
        else:
            print(str(s), end=end)

    def _printf(self, s: str, colorName: str = None, end: str = '', only_str: bool = False) -> str:
        """
        format string: https://www.python.org/dev/peps/pep-3101/
        [[fill]align][sign][#][0][minimumwidth][.precision][type]
        """
        if only_str:
            return str(s) + end
        if self.print_to_terminal:
            self._print_with_color(s, colorName, end)
        else:
            if self.stdscr is None:
                self._init_stdscr()
            if colorName is not None:
                assert colorName in COLOR_DICT.keys(), f"illegal color: '{colorName}'!"
                color = COLOR_DICT[colorName].curseIndex
            else:
                color = 0
            self.stdscr.addstr(str(s) + end, self.c.color_pair(color))
        return str(s) + end

    @property
    def _first_line(self):
        res = '┌' \
                + '─' * (self.width - 2) \
                + '┐'
        if len(self.table) == 0:
            return res
        first_row = self.table[0]
        segs = len(first_row)
        seg_width = (self.width - (segs + 1)) // segs
        for i in range(1, segs):
            res = change_str(res, (1 + seg_width) * i, '┬')
        return res

    @property
    def _last_line(self):
        res = '└' \
                + '─' * (self.width - 2) \
                + '┘'
        if len(self.table) == 0:
            return res
        first_row = self.table[-1]
        segs = len(first_row)
        seg_width = (self.width - (segs + 1)) // segs
        for i in range(1, segs):
            res = change_str(res, (1 + seg_width) * i, '┴')
        return res

    def below_line(self, x: int):
        assert x < len(self.table), f'index {x} out of bound {len(self.table)}'
        if x == len(self.table) - 1:
            return self._last_line
        b = x + 1
        """
        x │ abc │ bcd │
          ├──┬──┼─────┤  <-- we gonna draw
        b │aa│cc│     │
        """
        segs = len(self.table[x])
        seg_width = (self.width - (segs + 1)) // segs
        xs = [(1 + seg_width) * i for i in range(1, segs)]
        segs = len(self.table[b])
        seg_width = (self.width - (segs + 1)) // segs
        bs = [(1 + seg_width) * i for i in range(1, segs)]

        res = '├' + '─' * (self.width - 2) + '┤'
        for i in set(xs + bs):
            if i in xs and i in bs:
                res = change_str(res, i, '┼')
            elif i in xs:
                res = change_str(res, i, '┴')
            else:
                res = change_str(res, i, '┬')

        return res

    def print_table_line(self, x: int, only_str: bool = False) -> str:
        res = ""

        assert x < len(self.table), f'index {x} out of bound {len(self.table)}'
        res += self._printf('│', only_str=only_str)

        segs = len(self.table[x])
        seg_width = (self.width - (segs + 1)) // segs

        for i, v in enumerate(self.table[x]):
            currLen = seg_width
            if v is not None:
                currLen = seg_width
                for pair in v:
                    if pair is None:
                        continue
                    string, c = pair
                    if (len(str(string)) > currLen):
                        currLen = 0
                        break
                    currLen -= len(str(string))
            prefix = currLen // 2
            if (currLen % 2 != 0):
                res += self._printf(' ' * (prefix + 1), only_str=only_str)
            else:
                res += self._printf(' ' * prefix, only_str=only_str)
            if v is not None:
                currLen = seg_width
                for pair in v:
                    if pair is None:
                        continue
                    string, c = pair
                    if (len(str(string)) > currLen):
                        res += self._printf(string[:currLen], colorName=c, only_str=only_str)
                        break
                    res += self._printf(string, colorName=c, only_str=only_str)
                    currLen -= len(str(string))
            res += self._printf(' ' * prefix, only_str=only_str)
            if i < len(self.table[x]) - 1:
                res += self._printf('│', only_str=only_str)

        slen = seg_width * segs + segs + 1
        while slen < self.width:
            slen += 1
            res += self._printf(' ', only_str=only_str)

        res += self._printf('│', end='\n', only_str=only_str)

        return res

    def render(self):
        self._printf(s=self._first_line, end='\n')

        for i in range(len(self.table)):
            self.print_table_line(i)
            self._printf(s=self.below_line(i), end='\n')

        if not self.print_to_terminal:
            self.stdscr.move(0, 0)
            self.stdscr.refresh()

    def __str__(self) -> str:
        res = ""

        res += self._printf(s=self._first_line, end='\n', only_str=True)

        for i in range(len(self.table)):
            res += self.print_table_line(i, only_str=True)
            res += self._printf(s=self.below_line(i), end='\n', only_str=True)

        return res
