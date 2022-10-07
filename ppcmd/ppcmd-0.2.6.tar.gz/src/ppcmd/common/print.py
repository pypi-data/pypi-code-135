from colorama import Fore, Style


def echo__(msg):
    print(msg)
    return msg + "\n"


def print_reset():
    print(Style.RESET_ALL, end='')


def print_step__(step, color):
    print(color + f'>> {step}')
    print_reset()


def print_major_cmd_step__(cmd):
    print_step__(cmd, Fore.YELLOW)


def print_cmd_step__(cmd):
    print_step__(cmd, Fore.BLUE)


def print_additional_explanation__(msg):
    print(Fore.CYAN + f"  : {msg}")
    print_reset()
