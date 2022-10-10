# This file is part of PyGeBR library.
#
# PyGeBR is a library to create, merge, edit, inspect and run
# processing flows. It was originally designed for seismic
# data processing, but it extends to other data as well.
#
# PyGeBR is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyGeBR is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyGeBR.  If not, see <https://www.gnu.org/licenses/>
#
# Copyright 2021-2022 Ricardo Biloti <biloti@unicamp.br>
#                     Eduardo Filpo <efilpo@gmail.com>
#

import os, re, datetime

from .flow    import Flow
from .setup   import Setup

def LoadFlow(filename, menulist, title, description="", par=None):
    """
    Convenience function to load a flow or built it from menus

    If the file indicated by filename exists, it is load and
    returned, with no further process. Otherwise, a new
    flow is created by merging the menus in `menulist`. In
    that case, a title for the menu must be provided.

    Parameters
    ----------

    filename: str
        Filename to load the new flow (if it exists)

    menulist: List of str
        List of menus to merge to compose the flow
        When the flow doesn't exist, a new flow is
        built from those menus.

    title: str
        Title for new flow

    description: str (optional)
        One-line sentence describing the new flow

    par: dict (optional)
        Dictionary of variables to defined in local scope to
        evalute programs' parameters
    """

    if os.path.exists(filename):
        return Flow(filename = filename, par=par)

    setup = Setup()

    flow = None
    first = True
    tags = []
    for menu in menulist:
        found = False

        # Where to look for the menu
        if menu[0] == '/':
            paths = ['']
        else:
            paths = setup.menudirs()

        # Append .json to menu's name, if needed
        if menu[-5:] == ".json":
            menufn = menu
        else:
            menufn = menu + '.json'

        for path in paths:
            fname = os.path.join(path,menufn)

            if os.path.isfile(fname):
                found = True
                if first:
                    flow = Flow(filename = fname,
                                authors = setup.authors(),
                                title = title,
                                description = description,
                                par = par)
                    flow.filename(filename)
                    tags.extend(flow.tags())
                    first = False
                else:
                    new = Flow(filename=fname)
                    tags.extend(new.tags())
                    flow.merge(new)
                break

        if not found:
            raise Exception("Menu %s not found"%menu)

    if (flow):
        flow.tags(list(set(tags)))

    return flow

#-----------------------------------------------------------------------
def Catalog(htmlfn="catalog.html"):
    """
    Save, as HTML, a catalog of locally installed menus

    The catalog is save in the filename informed in `htmlfn`.

    Parameter
    ---------

    htmlfn: str (optional)
        Filename were the catalog will be written.
    """

    def _dump_dir(base):

        files = os.listdir(base)

        if re.search("lib/.*site-packages.*/pygebr/menus/", base):
            path = "&lt;SYSTEM&gt;/"+os.path.basename(base)
        else:
            path = re.sub(home, "&lt;HOME&gt;", base)

        menus = list(filter(lambda menu: re.search(".json$",menu), files))
        menus.sort()

        if len(menus) == 0:
            return ""

        lst = '<li class="list-group-item d-flex justify-content-between ' + \
              'align-items-center head"><span><a href="file://' + base + '">' + \
              '<i class="fas fa-folder-open"></i></a>' + \
              '<span class="font-weight-bold">' + \
              path + '</span></span><span class="badge badge-light badge-pill">' + \
              str(len(menus)) + '</span></li>\n'

        for menu in menus:
            fname = os.path.join(base, menu)
            flow = Flow(filename = fname)
            tags = flow.tags()
            lst += '<li class="list-group-item">'
            lst += f'<span class="title">{flow.title()}</span> '
            lst += f'(<span class="menu">{menu[:-5]}</span>). '
            lst += f'<span class="description">{flow.description()}.</span> '
            tags.sort()
            for tag in tags:
                lst += f'<span class="badge badge-light">{tag}</span> '
            for prog in flow.programs():
                lst += '<span class="link">'
                lst += f'<a href="{prog.url()}" target="_blank"><i class="fas fa-external-link-alt"></i></a>'
                lst += '</span> <span class="author">'
                lst += '<a href="#" data-toggle="tooltip" title="Program %s by\n\n'%prog.executable()
                authortxt = ""
                for author in prog.authors():
                    authortxt = "\n\n".join([authortxt, str(author)])
                lst += f'{authortxt.strip()}"><i class="fas fa-user"></i>'
                lst += '</a></span> '

            lst += '<span class="author">'
            lst += '<a href="#" data-toggle="tooltip" title="Menu by\n\n'
            authortxt = ""
            for author in flow.authors():
                authortxt = "\n\n".join([authortxt, str(author)])
            lst += f'{str(authortxt.strip())}">'
            lst += '<i class="fas fa-user"></i></a></span></li>\n'

        return lst

    home = os.getenv('HOME')
    template = os.path.join(os.path.dirname(__file__),
                            "docs",
                            "catalog.html.in")

    with open(template,"r") as gtmlfp:
        gtml = gtmlfp.read()

    # Scan for menus
    setup = Setup()
    dirs = setup.menudirs()
    dirs.sort()
    menuslst = ""
    for path in dirs:
        menuslst += _dump_dir(path)

    # Output a static HTML catalog page
    now = datetime.datetime.now()
    gtml = re.sub("##TODAY##", str(now.strftime('%Y-%m-%d %H:%M:%S')), gtml)
    gtml = re.sub("#include .menulist.html.", menuslst, gtml)

    with open(htmlfn,"w") as hfp:
        hfp.write(gtml)
