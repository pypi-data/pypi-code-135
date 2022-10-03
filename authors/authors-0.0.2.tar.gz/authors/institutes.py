import numpy as np
from collections import OrderedDict
import io
import copy

from yaml import load
import pyperclip


def substr_in_list(sub, lst):
    return next((s for s in lst if sub in s), None)


# def substr_where_in_list(sub, lst):
#     return next(((i, s) for i, s in enumerate(lst) if sub in s), (None,None))


def print_and2str(*args, **kwargs):
    output = io.StringIO()
    print(*args, file=output, **kwargs)
    print(*args, **kwargs)
    contents = output.getvalue()
    output.close()
    return contents


def print2str(*args, **kwargs):
    output = io.StringIO()
    print(*args, file=output, **kwargs)
    contents = output.getvalue()
    output.close()
    return contents


i = load(open('/home/jfaria/Work/institutes.txt'))
known_authors = [s.lower() for s in i.keys()]


def authors_AandA_list(authors, alphabetical=False, skip_first=True,
                       add_author_command=True, verbose=False, getstr=False):
    if isinstance(authors, str):
        authors = (authors, )

    for author in authors:
        if not substr_in_list(author, i.keys()):
            print('Cannot find author "%s" in known list of authors!' % author)
            return

    if alphabetical:
        if skip_first:
            # sort alphabetically by last name
            coauthors = [a.split('~')[-1] for a in authors[1:]]
            ind = np.argsort(coauthors)
            authors = [
                authors[0],
            ] + list(np.array(authors[1:])[ind])
        else:
            authors = sorted(authors)

    institutes_in_list = dict()
    out = ''

    if verbose:
        print = print_and2str
    else:
        print = print2str

    if add_author_command:
        out += print('\\author{')

    for j, author in enumerate(authors):
        if j > 0:
            out += print('\\and')

        found = substr_in_list(author, i.keys())
        if found:
            out += print('%-30s' % found, end=' ')

            numbers = []
            for institute in i[found]:
                institutes_in_list[institute] = None
                numbers.append(
                    list(institutes_in_list.keys()).index(institute) + 1)

            inst_list = ','.join(map(str, numbers))
            inst_list = '\\inst{%s}' % inst_list
            out += print(inst_list)

    if add_author_command:
        out += print('}')

    pyperclip.copy(out)
    if not verbose:
        _ = print_and2str(
            'Author list copied to clipboard, paste it (Ctrl+V) somewhere')

    if getstr:
        return institutes_in_list, out


def institutes_AandA_list(institutes, add_institute_command=True,
                          verbose=False, getstr=False):
    out = ''
        
    if verbose:
        print = print_and2str
    else:
        print = print2str

    if add_institute_command:
        out += print('\\institute{')

    out += print('\n\\and\n'.join(institutes.keys()))

    if add_institute_command:
        out += print('}')

    pyperclip.copy(out)
    if not verbose:
        _ = print_and2str(
            'Institute list copied to clipboard, paste it (Ctrl+V) somewhere')
    
    if getstr:
        return out