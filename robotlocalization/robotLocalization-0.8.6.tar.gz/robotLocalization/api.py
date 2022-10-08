#!/usr/bin/env python3
import sys
import os
import re
import codecs

from robotLocalization import util
from robotLocalization import loader

def traverse_tree(rootdir,locale="en",filetype="properties",verbose=False):
    basefiles = util.get_basefiles(rootdir,filetype=filetype,verbose=verbose)

    properties = {}

    for file in basefiles:
        p = loader.load_files(basefiles[file]["en"],verbose=verbose)
        if locale != "en":
            lfile = util.locale_lookup(basefiles[file]["en"],locale)
            if lfile and lfile != basefiles[file]["en"]:
                l = loader.load_files(lfile)
                p.update(l)
            else:
                if lfile:
                    relpath = os.path.relpath(lfile)
                    if verbose:
                        print (f'Warning: properties file "{relpath}" is not localized for the target locale "{locale}".')
                else:
                    if verbose:
                        print (f'Warning: file "{file}" is not recognized for the locale "{locale}".')

        properties.update(p)

    return properties

text_pat = re.compile(r'''(text\(\)\s*|@aria-label\s*|@placeholder\s*|@title\s*|\.\s*?)([=,]\s*)(['"])(?P<T>.*?)\3''')
value_pat = re.compile(r'(?<=\s\s)(?P<value>\S.*)(?=\s\s)')
value2_pat = re.compile(r'(?<=\s\s)(?P<value>\S.*)')
I18NOK_pat = re.compile(r"#\s*i18n:OK")
placeholder_pat = re.compile(r'\(_+\w+_+\)')
def extract(path,variables=None,verbose=False):
    propfile = ""
    robotfile = ""
    syspropfile = ""
    sysprop = []

    if not os.path.exists(path):
        print (f"{path} does not exist.")
        return None, None, None

    with codecs.open(path,'r',encoding='utf-8') as fp:
        lines = fp.readlines()

    keys = {}
    for line in lines:
        newline = line
        m = I18NOK_pat.search(line)
        if m:
            robotfile += line
            continue
        m = value_pat.search(line)
        if not m:
            m = value2_pat.search(line)
        if m:
            value = m.group('value')
            if not value.startswith('xpath'):
            # process variables
                var = varname(value)
                if variables:
                    sysprop.extend(bundle_reference(value,variables)) # call before var_reference
                value , nhit = var_reference(value,variables,hint="label",verbose=verbose)
                if nhit:
                    print (f"var={var} value={value} {m.start()} {m.end()}")
                    line = line[:m.start()] + "${" + value + "}" + line[m.end():]
                else:
                    line = line[:m.start()] + "${" + var + "}" + line[m.end():]
                    if var not in keys:
                        propfile += f"{var} = {value}\n"
                        keys[var] = 0
                    keys[var] += 1
                robotfile += line
                continue

        seg = text_pat.finditer(newline)
        if seg:
            count = 0
            lastchar = 0
            edlist = []
            for m in iter(seg):
                strcls = m.group(1)
                #print (f"strcls={strcls}")
                value = m.group(4)
                var = varname(value)
                n = placeholder_pat.match(value)
                if n:
                    #print(f"placeholder={value}")
                    continue
                if value[0:2] == '${' or value == '(_____placeholder_____)': # var reference
                    continue
                #newline = newline[:m.start()] + m.group(1) + m.group(2) + "'" + var + "'" + newline[m.end():]
                if variables:
                    sysprop.extend(bundle_reference(value,variables)) # call before var_reference

                value , nhit = var_reference(value,variables,hint=strcls,verbose=verbose)
                if nhit:
                    # print (f"Indirect reference: {var} = {value}")
                    var = value
                    keys[var] = 0

                edlist.append({"begin":m.start(), "end":m.end(),"var":var , "g1":m.group(1), "g2":m.group(2)})
                if var not in keys:
                    propfile += f"{var} = {value}\n"
                    keys[var] = 0
                keys[var] += 1
                count += 1
            #print (f"keys={keys}")
            if count == 0:
                robotfile += line
            else:
                edlist.reverse()
                for ix in edlist:
                    newline = newline[:ix["begin"]] + ix["g1"] + ix["g2"] + '"${' + ix["var"] + '}"' + newline[ix["end"]:]
                #print (f"edlist={edlist}")
                robotfile += newline
            #print (f"   line={line}\nnewline={newline}")
        else:
            print (f"Return from finditer is None: {line}")
            robotfile += line

    return robotfile, propfile, sysprop

def varname(label):
    label = label.lower().replace(' ','_')
    label = label.replace(':','C')
    label = label.replace('?','Q')
    label = label.replace('.','P')
    label = label.replace(',','M')
    label = label.replace('"','D')
    label = label.replace('{','L')
    label = label.replace('}','R')
    label = label.replace('(','S')
    label = label.replace(')','T')
    label = label.replace('$','V')
    label = label.replace("'",'A')
    #label = "${" + label +  "}"
    return label

def var_reference(label,variables=None,hint=None,verbose=False):
    # hint: text(), ., @placeholder, @aria-label, @title
    chrclass = { "placeholder":[], "label":[], "title":[], "tooltip":[], "icon":[] }
    nhit = 0
    candidates = []

    if not variables:
        return label, 0

    for key in variables:
        if variables[key] == label:
            nhit += 1
            candidates.append(key)

    if len(candidates)==0:
        return label, 0
    if len(candidates)==1:  # only one found
        label = candidates[0]
        return label, 1
    # clasify keys
    for key in candidates:
        lkey = key.lower()
        if lkey.find("icon.label")>=0:
            chrclass["icon"].append(key)
        elif lkey.find("title")>=0:
            chrclass["title"].append(key)
        elif lkey.find("placeholder")>=0:
            chrclass["placeholder"].append(key)
        elif lkey.find("label")>=0:
            chrclass["label"].append(key)
        elif lkey.find("tooltip")>=0:
            chrclass["tooltip"].append(key)
        else:
            chrclass["label"].append(key)

    def select(key,list):
        ncount = len(chrclass[key])
        if ncount >=1:
            if ncount >1 and verbose:
                print (f'Warning: {ncount} keys found for {key}:')
                for st in chrclass[key]:
                    print (f"\t{st}")
            return chrclass[key][0], ncount
        return None, ncount

    if hint == "@title":
        label0, count0 = select("title",candidates)
        if count0 > 0:
            return label0, count0
    elif hint == "@placeholder":
        label0, count0 = select("placeholder",candidates)
        if count0 > 0:
            return label0, count0
    elif hint == "@aria-label":
        label0, count0 = select("label",candidates)
        if count0 > 0:
            return label0, count0

    label0, count0 = select("label",candidates)
    if count0 > 0:
        return label0, count0

    # text() or .
    label0 , count0 = select("title",candidates)
    if count0 >0:
        return label0, count0

    label = candidates[0]
    nhit = len(candidates)
    if verbose:
        print (f'Warning: {nhit} keys found for text():')
        for st in candidates:
            print (f"\t{st}")

    return candidates[0], nhit

def bundle_reference(label,variables):
    candidates = []
    for key in variables:
        if variables[key] == label:
            candidates.append(key)
    return candidates

def generate_bundle(keys,variables=None):
    propfile = ""
    added_keys = {}
    if not variables:
        return propfile
    for key in keys:
        if key in added_keys:
            # print(f"duplicated entries {key}")
            added_keys[key] += 1
            continue
        added_keys[key] = 1
        propfile += f"{key} = {variables[key]}\n"
    return propfile

def write_file(path,buffer,destname):
    dir = os.path.dirname(path)
    if dir and not os.path.exists(dir):
        sys.stderr.write(f"Error: directory {dir} does not exist\n")
        return 0
    with codecs.open(path,'w','utf-8') as outp:
        outp.write(buffer)
    nlines = buffer.count('\n')
    #print (f"{destname} written to \"{path}. {nlines}")
    print (f"{nlines} lines written to \"{path}\".")
    return 1

if __name__ == "__main__":

    text ='''${Obj_DE_ZeroState_Svg}    xpath://*[text()= "No data is selected."] '''
    m = text_pat.search(text)
    if m:
        print (f'{m.group("T")}')
    else:
        print ("not found.")
