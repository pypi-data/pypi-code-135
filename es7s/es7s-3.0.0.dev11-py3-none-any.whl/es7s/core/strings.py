# ------------------------------------------------------------------------------
#  es7s [setup/configuration/commons]
#  (c) 2021-2022 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
import re
from re import Match

from pytermor import Style, Colors, NOOP_STYLE
from pytermor.common import Registry

SANITIZE_REGEX = re.compile(b"[^\x0a\x20-\x7e]", flags=re.ASCII)


class PrefixedNumericsFormatter:
    PREFIX_UNIT_REGEX = re.compile(
        r"(?:(?<!\x1b\[)(?<=[]()\s[-])\b|^)"
        r"(\d+)([.,]\d+)?(\s?)"
        r"([kmgtpuμµn%])?"
        r"("
        r"i?b[/ip]?t?s?|v|a|s(?:econd|ec|)s?|m(?:inute|in|onth|on|o|)s?|"
        r"h(?:our|r|)s?|d(?:ay|)s?|w(?:eek|k|)s?|y(?:ear|r|)s?|hz"
        r")?"
        r"(?=[]\s\b()[]|$)",
        flags=re.IGNORECASE,
    )

    PERCENT_REGEX = re.compile(r'')
                                                                      #/************************************#/
    STYLE_DEFAULT = NOOP_STYLE                                        #| misc.   e0 |-------------| second  #|
    STYLE_NUL = Style(STYLE_DEFAULT, fg=Colors.GREY)                  #| zero    e0 |-------------|---------#|
    STYLE_PRC = Style(STYLE_DEFAULT, fg=Colors.MAGENTA, bold=True)    #|------------| percent e-2 |---------#|
    STYLE_KIL = Style(STYLE_DEFAULT, fg=Colors.BLUE, bold=True)       #| Kilo-   e3 | milli-  e-3 | minute  #|
    STYLE_MEG = Style(STYLE_DEFAULT, fg=Colors.CYAN, bold=True)       #| Mega-   e6 | micro-  e-6 | hour    #|
    STYLE_GIG = Style(STYLE_DEFAULT, fg=Colors.GREEN, bold=True)      #| Giga-   e9 | nano-   e-9 | day     #|
    STYLE_TER = Style(STYLE_DEFAULT, fg=Colors.YELLOW, bold=True)     #| Tera-  e12 | pico-  e-12 | week    #|
    STYLE_MON = Style(STYLE_DEFAULT, fg=Colors.HI_YELLOW, bold=True)  #|------------|-------------| month   #|
    STYLE_PET = Style(STYLE_DEFAULT, fg=Colors.RED, bold=True)        #| Peta-  e15 |-------------| year    #|
                                                                      #/************************************#/
    PREFIX_MAP = {
        '%': STYLE_PRC,
        'K': STYLE_KIL, 'k': STYLE_KIL, 'm': STYLE_KIL,
        'M': STYLE_MEG, 'μ': STYLE_MEG, 'µ': STYLE_MEG,
        'G': STYLE_GIG, 'g': STYLE_GIG, 'n': STYLE_GIG,
        'T': STYLE_TER, 'p': STYLE_TER,
        'P': STYLE_PET,
    }
    UNIT_MAP = {
        's': STYLE_PRC, 'sec': STYLE_PRC, 'second': STYLE_PRC,
        'm': STYLE_KIL, 'min': STYLE_KIL, 'minute': STYLE_KIL,
        'h': STYLE_MEG, 'hr': STYLE_MEG, 'hour': STYLE_MEG,
        'd': STYLE_GIG, 'day': STYLE_GIG,
        'w': STYLE_TER, 'wk': STYLE_TER, 'week': STYLE_TER,
        'M': STYLE_MON, 'mo': STYLE_MON, 'mon': STYLE_MON, 'month': STYLE_MON,
        'y': STYLE_PET, 'yr': STYLE_PET, 'year': STYLE_PET,
    }

    @classmethod
    def format(cls, string: str) -> str:
        return cls.PREFIX_UNIT_REGEX.sub(cls._colorize_match, string)

    @classmethod
    def _colorize_match(cls, m: Match) -> str:
        intp, floatp, sep, pref, unit = m.groups('')
        unitn = unit.rstrip('s').strip()

        style_i = cls.STYLE_DEFAULT
        if pref:
            style_i = cls.PREFIX_MAP.get(pref, cls.STYLE_DEFAULT)
        elif unitn:
            style_i = cls.UNIT_MAP.get(unitn, cls.STYLE_DEFAULT)

        digits = intp + floatp[1:]
        if digits.count('0') == len(digits):
            style_i = cls.STYLE_NUL

        style_f = Style(style_i, dim=True)
        style_un = Style(style_i, dim=True, bold=False)
        return style_i.render(intp) + style_f.render(floatp) + sep + style_un.render(f'{pref}{unit}')


class StyleRegistry(Registry[Style]):
    DISABLED = Style(fg=Colors.GREY_23)
    LABEL = Style(fg=Colors.GREY_35)
