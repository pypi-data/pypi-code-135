import unicodedata
from bs4 import BeautifulSoup


def default_parser(string):
    return string


def remove_spaces(string):
    return string.replace(' ', '')


def handle_html(string):
    return unicodedata.normalize('NFKC', BeautifulSoup(string, features='html.parser').get_text())


def remove_spaces_and_tabs(string):
    return remove_spaces(string).replace('\t', '')


default = remove_spaces_and_tabs