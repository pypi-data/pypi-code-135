

import sys
import time


if sys.platform == 'win32':
    import msvcrt
else:
    import termios
    import select
    import tty


class TxtColor:
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    PURPLE = 35
    CYAN = 36
    WHITE = 37
    RESET = 39

    # 高色
    LIGHTBLACK = 90
    LIGHTRED = 91
    LIGHTGREEN = 92
    LIGHTYELLOW = 93
    LIGHTBLUE = 94
    LIGHTPURPLE = 95
    LIGHTCYAN = 96
    LIGHTWHITE = 97

    黑色 = BLACK
    红色 = RED
    绿色 = GREEN
    黄色 = YELLOW
    蓝色 = BLUE
    紫色 = PURPLE
    青色 = CYAN
    白色 = WHITE
    黑灰色 = LIGHTBLACK
    亮红色 = LIGHTRED
    亮绿色 = LIGHTGREEN
    亮黄色 = LIGHTYELLOW
    亮蓝色 = LIGHTBLUE
    亮紫色 = LIGHTPURPLE
    亮青色 = LIGHTCYAN
    亮白色 = LIGHTWHITE
    重置 = RESET


class BgColor:
    BLACK = 40
    RED = 41
    GREEN = 42
    YELLOW = 43
    BLUE = 44
    PURPLE = 45
    CYAN = 46
    WHITE = 47
    RESET = 49

    # 亮色
    LIGHTBLACK = 100
    LIGHTRED = 101
    LIGHTGREEN = 102
    LIGHTYELLOW = 103
    LIGHTBLUE = 104
    LIGHTPURPLE = 105
    LIGHTCYAN = 106
    LIGHTWHITE = 107

    黑色 = BLACK
    红色 = RED
    绿色 = GREEN
    黄色 = YELLOW
    蓝色 = BLUE
    紫色 = PURPLE
    青色 = CYAN
    白色 = WHITE
    黑灰色 = LIGHTBLACK
    亮红色 = LIGHTRED
    亮绿色 = LIGHTGREEN
    亮黄色 = LIGHTYELLOW
    亮蓝色 = LIGHTBLUE
    亮紫色 = LIGHTPURPLE
    亮青色 = LIGHTCYAN
    亮白色 = LIGHTWHITE
    重置 = RESET


class Style:
    BRIGHT = 1
    DIM = 2
    ITALIC = 3
    UNDERLINE = 4
    NORMAL = 6
    INVERSION = 7
    HIDE = 8
    CROSSLINE = 9
    RESET_ALL = 0
    高亮 = BRIGHT
    黯淡 = DIM
    斜体 = ITALIC
    下划线 = UNDERLINE
    正常 = NORMAL
    反显 = INVERSION
    重置 = RESET_ALL
    隐藏 = HIDE
    中划线 = CROSSLINE



class Conio:
    ASC = '\033['
    asc = '\033['
    ENDL = '\033[0m'
    endl = '\033[0m'

    def __init__(self):
        if sys.platform == 'win32':
            self.platform = 'win32'
        elif sys.platform == 'linux':
            self.platform = 'linux'
        else:
            self.platform = 'unknow'
        self.TxtColor = TxtColor
        self.BgColor = BgColor
        self.Style = Style
        self.tc = self.TxtColor
        self.bgc = self.BgColor
        self.s = self.Style
    # - - 控制台光标控制代码的封装 - - #

    # 带s_前缀的返回\033字符串
    # 不带的直接执行
    
    # 隐藏光标
    def hideCursor_s(self):
        return '\033[?25l'
    
    # 显示光标
    def showCursor_s(self):
        return '\033[?25h'
    
    # 光标上移n行
    def upCursor_s(self, n):
        return f'\033[{n}A'
    
    # 光标左移n列
    def moveCursorLeft_s(self, n):
        return f'\033[{n}D'

    # 光标右移n列
    def moveCursorRight_s(self, n):
        return f'\033[{n}C'

    # 光标下移n行
    def s_downCursor_s(self, n):
        return f'\033[{n}B'

    # 移动光标到该行行首
    def moveToLineStart_s(self):
        return '\033[\n\033[A'

    # 清除光标到该行首间的字符
    def clrLine_s(self):
        return '\033[2K'

    # 清除光标到该行首间的字符 并 移动光标到该行行首
    def resetLine_s(self):
        return '\033[2K\n\033[A'

    # 清除光标到该行首间的字符 并 移动光标到上一行行首
    def resetLineAndUp_s(self, n):
        return f'\033[2K\n\033[{n}A'

    # 移动光标到指定行列
    def posCurson_s(self, x=0, y=0):
        return f'\033[{y};{x}H'

    # 清除光标到行首之间所有字符 并 移动光标到行首
    # 解释一下
    # 光标0 和 1 在输出的时候都是同一个位置
    # 除这两个之外，坐标在哪就说明光标在哪
    # 光标会在其所在位置打印新字符
    def clrscr_s(self):
        return '\033[2J\033[1;1H'

    # 以下作用同上，但不反回字符串直接执行

    def hideCursor(self):
        print('\033[?25l', end='')

    def showCursor(self):
        print('\033[?25h', end='')

    def upCursor(self, n):
        if n <= 0:
            return
        print(f'\033[{n}A', end='')

    def moveCursorLeft(self, n):
        if n <= 0:
            return
        print(f'\033[{n}D', end='')

    def moveCursorRight(self, n):
        if n <= 0:
            return
        print(f'\033[{n}C', end='')

    def downCursor(self, n):
        if n <= 0:
            return
        print(f'\033[{n}B', end='')

    def moveToLineStart(self):
        print('\033[\n\033[A', end='')

    def clrLine(self):
        print('\033[2K', end='')

    def resetLine(self):
        print('\033[2K\n\033[A', end='')

    def resetLineAndUp(self, n):
        print(f'\033[2K\n\033[{n}A', end='')

    def clrscr(self):
        # print('\033[2J\033[1;1H', end='')
        print('\033c', end='')

    def posCurson(self, x=0, y=0):
        print(f'\033[{y};{x}H', end='')

    # 同c语言的getch()
    def getch(self):
        if self.platform == 'win32':
            return self.__getch_msvcrt()
        elif self.platform == 'linux':
            return self.__getch_termios()
        elif self.platform == 'unknow':
            return self.__getch_termios()

    # 同c语言的kbhit()
    def kbhit(self):
        if self.platform == 'win32':
            return self.__kbhit_msvcrt()
        elif self.platform == 'linux':
            return self.__kbhit_termios()
        elif self.platform == 'unknow':
            return self.__kbhit_termios()

    def getFormatStr(self, *kwargs):
        format_str = '\033['
        for arg in kwargs:
            if not 0 <= arg <= 9:
                pass
            elif not 30 <= arg <= 49:
                pass
            elif not 90 <= arg <= 107:
                raise ValueError('所给参数不格式控制代码范围内')
            format_str += str(arg) + ';'
        return format_str[:-1] + 'm'

    def formattingStr(self, text, *kwargs):
        return self.getFormatStr(*kwargs) + text + '\033[0m'

    # 可中断的sleep | break_char_list 为触发打断按键字符列表
    def interruptibleSleep(self, delay, break_char_list=None):
        start = time.time()
        while (time.time() - start) < delay:
            ch = self.kbhit()
            if break_char_list is None:
                if ch is None:
                    return ch
            else:
                if ch in break_char_list:
                    return ch

    def __getch_msvcrt(self):
        return msvcrt.getch().decode('utf-8')
    
    def __getch_termios(self):
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        new[3] = new[3] & ~termios.ECHO & ~termios.ICANON
        try:
            termios.tcsetattr(fd, termios.TCSADRAIN, new)
            char = sys.stdin.read(1)
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
            return char
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

    def __kbhit_msvcrt(self):
        if msvcrt.kbhit():
            return self.__getch_msvcrt()

    def __kbhit_termios(self):
        old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())
        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
            c = sys.stdin.read(1)
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
            return c
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
