import sys
import time
import termios


def getch():
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

def pop_print(string, speed=0.03, lback='普通', lcolor='白', ltype='高亮', ltype2='', pop_space_number=5):
    color_dict = {'黑': 30, '红': 31, '绿': 32, '黄': 33, '蓝': 34, '紫': 35, '青': 36, '白': 37}
    backgroud_dict = {'黑': 40, '红': 41, '绿': 42, '黄': 43, '蓝': 44, '紫': 45, '青': 46, '白': 47, '': 48}
    type_dict = {'': 6, '高亮': 1, '低亮': 2, '斜体': 3, '下划线': 4, '闪烁': 5, '普通': 6}
    if speed < 0.005:
        speed = 0.005
    elif speed > 0.2:
        speed = 0.2
    # 限制speed的数值
    count = len(string) - 1
    fore_space_number = pop_space_number
    orig_string = string
    string = ' '*fore_space_number + orig_string
    print('\033[?25l\033[s', end='')
    count = len(string) - 1
    row = 1
    print('\033[?25l', end='')
    while count >= 0:
        print(f'\033[{color_dict[lcolor]};{backgroud_dict[lback]};{type_dict[ltype]};{type_dict[ltype2]}m' + string[count:] + '\033[0m')
        if count != 0:
            time.sleep(speed)
            print(f'\033[{row}A', end='')
        count -= 1

def choice(
    item_list,
    item_color='白',
    cur_item_color='绿',
    i_background='',
    ci_background='',
    i_type1='',
    i_type2='',
    ci_type1='高亮',
    ci_type2='',
    is_pop=True,
    pop_speed=0.0,
    pop_space_num=5
    ):
    color_dict = {'黑': 30, '红': 31, '绿': 32, '黄': 33, '蓝': 34, '紫': 35, '青': 36, '白': 37}
    backgroud_dict = {'黑': 40, '红': 41, '绿': 42, '黄': 43, '蓝': 44, '紫': 45, '青': 46, '白': 47, '': 48}
    type_dict = {'': 6, '高亮': 1, '低亮': 2, '斜体': 3, '下划线': 4, '闪烁': 5, '普通': 6}
    tot_lines = len(item_list)
    if tot_lines == 0:
        print('\033[33;1m选项个数为0\033[0m')
        return None
    cur_index = 0
    if is_pop:
        for index, item in enumerate(item_list):
            pop_print(string=item, lcolor=item_color, speed=pop_speed, lback=i_background, ltype=i_type1, ltype2=i_type2, pop_space_number=pop_space_num)
        print(f'\033[{tot_lines}A', end='')
    else:
        pop_space_num = 0
    while True:
        for index, item in enumerate(item_list):
            if cur_index % tot_lines == index:
                print(f'\033[{pop_space_num}C\033[{color_dict[cur_item_color]};{backgroud_dict[ci_background]};{type_dict[ci_type1]};{type_dict[ci_type2]}m' + item + '\033[0m')
            else:
                print(f'\033[{pop_space_num}C\033[{color_dict[item_color]};{backgroud_dict[i_background]};{type_dict[i_type1]};{type_dict[i_type2]}m' + item + '\033[0m')
        ch = getch()
        if ch.lower() == 'w':
            cur_index -= 1
        if ch.lower() == 's':
            cur_index += 1
        if ch == '\n':
            return cur_index % tot_lines
        print(f'\033[{tot_lines}A', end='')

def lprint(string='', lsep='', lend='\n', speed=0.03, lcolor='green', ltype='normal', ltype2 = '', is_wate=True, width=24, is_endl=True):
    # lsep 同print的sep
    # lend 同print的end
    # speed 控制单个字符显示的速度
    # lcolor 字符串显示颜色
    # ltype  字符串显示样式
    # is_wait 是否等待确认
    # 以上参数都有默认值
    len_str = len(string)
    lines = len_str // width
    ls_string = list(string)
    for i in range(lines):
        ls_string.insert(i + width - 1 + i * width, '\n')
    string_copy = ''.join(ls_string)
    row = 1
    color_dict = {'black': 30, 'red': 31, 'green': 32, 'yellow': 33, 'blue': 34, 'purple': 35, 'cyan': 36, 'white': 37}
    type_dict = {'': 6, 'highlight': 1, 'lowlight': 2, 'italic': 3, 'underline': 4, 'blink': 5, 'normal': 6}
    count = 0
    if speed < 0.005:
        speed = 0.005
    elif speed > 0.2:
        speed = 0.2
    # 限制speed的数值
    print('\033[?25l', end='')
    while count < len(string_copy):
        if string_copy[count] == '\n':
            row += 1
        print(f'\033[{color_dict[lcolor]};{type_dict[ltype]};{type_dict[ltype2]}m' + string_copy[:count + 1] + '\033[0m', sep=lsep, end='\n')
        if count != len(string_copy) - 1:
            print(f'\033[{row}A', end='')
            time.sleep(speed)
        count += 1
    if not is_endl:
        pr_str = string_copy[-(len(string_copy) % width):]
        print(f'\033[{color_dict[lcolor]};{type_dict[ltype]};{type_dict[ltype2]}m\033[1A' + pr_str + '\033[0m', end='')
    # 打印字符串
    if is_wate:
        while True:
            resp = input()
            if resp != '':
                continue
            else:
                break
    else:
        return

def choice2(
    item_list,
    item_color='白',
    cur_item_color='绿',
    i_background='',
    ci_background='',
    i_type1='',
    i_type2='',
    ci_type1='高亮',
    ci_type2='',
    is_pop=True,
    pop_speed=0.0,
    pop_space_num=5
    ):
    color_dict = {'黑': 30, '红': 31, '绿': 32, '黄': 33, '蓝': 34, '紫': 35, '青': 36, '白': 37}
    backgroud_dict = {'黑': 40, '红': 41, '绿': 42, '黄': 43, '蓝': 44, '紫': 45, '青': 46, '白': 47, '': 48}
    type_dict = {'': 6, '高亮': 1, '低亮': 2, '斜体': 3, '下划线': 4, '闪烁': 5, '普通': 6}
    tot_lines = len(item_list)
    if tot_lines == 0:
        print('\033[33;1m选项个数为0\033[0m')
        return None
    cur_index = 0
    if is_pop:
        for index, item in enumerate(item_list):
            pop_print(string=item, lcolor=item_color, speed=pop_speed, lback=i_background, ltype=i_type1, ltype2=i_type2, pop_space_number=pop_space_num)
        print(f'\033[{tot_lines}A', end='')
    else:
        pop_space_num = 0
    while True:
        for index, item in enumerate(item_list):
            print(f'\033[{pop_space_num}C\033[{color_dict[item_color]};{backgroud_dict[i_background]};{type_dict[i_type1]};{type_dict[i_type2]}m' + item + '\033[0m')
        print(f'\033[{tot_lines - (cur_index % tot_lines)}A', end='')
        print(f'\033[{pop_space_num}C\033[{color_dict[cur_item_color]};{backgroud_dict[ci_background]};{type_dict[ci_type1]};{type_dict[ci_type2]}m' + item + '\033[0m')
        print(f'\033[{tot_lines - (cur_index % tot_lines) - 1}A', end='')
        ch = getch()
        if ch.lower() == 'w':
            cur_index -= 1
        if ch.lower() == 's':
            cur_index += 1
        if ch == '\n':
            return cur_index % tot_lines
        print(f'\033[{tot_lines + 1}A', end='')