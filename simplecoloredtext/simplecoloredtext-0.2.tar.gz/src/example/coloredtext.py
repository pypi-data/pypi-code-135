from colorama import Fore, Style, init
import re
init()

def colored(texto):
    # Find all color tags in the string
    color_store = []
    pat1 = r'<([\w]+)>'
    tags = re.findall(pat1, texto)
    for tag in tags:
        if tag not in color_store:
            color_store.append(tag)

    # Use the tag to replace
    for tag in tags:
        pat2 = f'<{tag}>(.*?)</{tag}>'
        if 'green' in tag:
            texto = re.sub(pat2, r'{Fore.GREEN}\1{Style.RESET_ALL}', texto)
        elif 'blue' in tag:
            texto = re.sub(pat2, r'{Fore.BLUE}\1{Style.RESET_ALL}', texto)
        elif 'red' in tag:
            texto = re.sub(pat2, r'{Fore.RED}\1{Style.RESET_ALL}', texto)
        elif 'yellow' in tag:
            texto = re.sub(pat2, r'{Fore.YELLOW}\1{Style.RESET_ALL}', texto)
        elif 'cyan' in tag:
            texto = re.sub(pat2, r'{Fore.CYAN}\1{Style.RESET_ALL}', texto)
        elif 'magenta' in tag:
            texto = re.sub(pat2, r'{Fore.MAGENTA}\1{Style.RESET_ALL}', texto)
        elif 'black' in tag:
            texto = re.sub(pat2, r'{Fore.BLACK}\1{Style.RESET_ALL}', texto)
        elif 'lightblack' in tag:
            texto = re.sub(pat2, r'{Fore.LIGHTBLACK_EX}\1{Style.RESET_ALL}', texto)
        elif 'lightgreen' in tag:
            texto = re.sub(pat2, r'{Fore.LIGHTGREEN_EX}\1{Style.RESET_ALL}', texto)
        elif 'lightblue' in tag:
            texto = re.sub(pat2, r'{Fore.LIGHTBLUE_EX}\1{Style.RESET_ALL}', texto)
        elif 'lightred' in tag:
            texto = re.sub(pat2, r'{Fore.LIGHTRED_EX}\1{Style.RESET_ALL}', texto)
        elif 'lightyellow' in tag:
            texto = re.sub(pat2, r'{Fore.LIGHTYELLOW_EX}\1{Style.RESET_ALL}', texto)
        elif 'lightcyan' in tag:
            texto = re.sub(pat2, r'{Fore.LIGHTCYAN_EX}\1{Style.RESET_ALL}', texto)
        elif 'lightmagenta' in tag:
            texto = re.sub(pat2, r'{Fore.LIGHTMAGENTA_EX}\1{Style.RESET_ALL}', texto)

    exec('print(f"' + texto + '")')

colored("Hello everyone, <green>Happy</green> <lightred>New</lightred> <blue>Year</blue>")