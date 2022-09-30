#!/usr/bin/env python
'''
A script to transform CASA Guide webpages and casapy scripts to casapy
scripts suited for interactive or non-interactive use.  This script can be
run from the command line.  Use the '-h' option to obtain a help message
explaining the command line parameters and options.
The script runs in one of three modes:
1) interactive (default): Generates a casapy script that requests user input
   when interactive GUIs are invoked.
2) non-interactive: Generates a casapy script that sleeps for 60s when an
   interactive GUI is invoked.  (Note: 60s may not be enough time for some
   plots.)
3) benchmark: Generates a casapy script that makes all tasks noninteractive or
   removes their invocation all together.  The output script imports and makes
   extensive use of module *casa_call.py* to keep track of the start and stop
   time of tasks.  *casa_call.py* must be in the casapy Python path when 
   the casapy script is run.  To work properly, the list of casapy tasks hard
   coded below must be consistent with the tasks available in the version of
   casa being tests.  To check for consistency or update the hardcoded list,
   use the function listCASATasks() below (see the function's docstring for
   instructions).
   The intended functionality of the benchmarking mode is (1) to allow easy
   assessment of whether the scripts are working and (2) to produce useful
   benchmarks of performance, e.g., as a function of machine.
'''

#from __future__ import print_function

# =====================
# IMPORTS
# =====================

import urllib
import sys
import codecs
import re
import string
import os, os.path
from optparse import OptionParser, SUPPRESS_HELP

# =====================
# PY3 compatiable
# =====================
py3 = False
if sys.version_info[0] > 2:
    py3 = True
    import urllib.request
else:
    import urllib2

# =====================
# DEFINITIONS
# =====================

# Expression that define the beginning and end of CASA code blocks in the HTML
#beginBlock = "class=\"python source-python\""
#endBlock = "</pre></div></div>"


beginBlocks = ["class=\"p\"","class=\"n\"","class=\"k\"","class=\"s1\"","class=\"s2\""]

endBlock = "</span>"


# interactives
interactive=re.compile("[\s;]*(plotxy|plotcal|plotms|viewer|plotants|imview)")

# CASA task list (used for benchmarking markup, else ignored)
# Check and update this list using function listCASATasks(), below.
# for CASA 4.5...

casa_tasks = [
    'accor','accum', 'applycal', 'asdmsummary', 'bandpass',
    'blcal', 'boxit', 'browsetable', 'calstat', 'caltabconvert', 'clean',
    'clearcal', 'clearplot', 'clearstat', 'concat', 'conjugatevis', 'csvclean',
    'cvel', 'deconvolve', 'delmod', 'exportasdm', 'exportfits', 'exportuvfits',
    'feather', 'find', 'fixplanets', 'fixvis', 'flagcmd', 'flagdata', 'flagmanager',
    'fluxscale', 'ft', 'gaincal', 'gencal', 'hanningsmooth',
    'help par.parametername', 'help taskname', 'imcollapse', 'imcontsub', 'imfit',
    'imhead', 'immath', 'immoments', 'impbcor', 'importasdm', 'importevla',
    'importfits', 'importfitsidi', 'importgmrt', 'importuvfits', 'importvla',
    'impv', 'imreframe', 'imregrid', 'imsmooth', 'imstat', 'imsubimage', 'imtrans',
    'imval', 'imview', 'listcal', 'listfits', 'listhistory', 'listobs',
    'listpartition', 'listsdm', 'listvis', 'makemask', 'mosaic', 'msmoments',
    'mstransform', 'msview', 'partition', 'plotants', 'plotbandpass', 'plotcal',
    'plotms', 'plotuv', 'plotweather', 'plotxy', 'polcal', 'predictcomp', 'rmfit',
    'rmtables', 'sdbaseline', 'sdcal', 'sdfit', 'sdfixscan', 'sdgaincal', 
    'sdimaging', 'sdsmooth', 'setjy', 'simalma', 'simanalyze', 'simobserve', 
    'slsearch', 'smoothcal', 'specfit', 'splattotable', 'split', 'spxfit', 
    'startup', 'oldstatwt', 'taskhelp', 'tasklist', 'taskname', 'tclean', 'testconcat', 'toolhelp', 
    'uvcontsub', 'uvcontsub3', 'uvmodelfit', 'uvsub', 'viewer', 'virtualconcat', 
    'vishead', 'visstat', 'widebandpbcor', 'widefield', 'wvrgcal'
    ]

casa6_tools = [ 
    'agentflagger','atcafiller','atmosphere','calanalysis','calibrater',
    'componentlist','coordsys','functional','image','imagemetadata',
    'imagepol','imager','iterbotsink','logsink','measures',
    'miriadfiller','ms','msmetadata','mstransformer','quanta',
    'regionmanager','sakura','sdm','simulator','singledishms',
    'spectralline','synthesisdeconvolver','synthesisimager','synthesisimstore',
    'synthesisnormalizer','synthesisutils','table','vlafiller','vpmanager'
    ]

# define formatting junk that needs to be filtered
# JFG comments that regular expressions might clean this up
# JBM - cleaned up declaration of the junkStr list

junkStr = [ 
    '<div dir="ltr" class="mw-geshi mw-code mw-content-ltr">',
    '<div class="mw-highlight mw-content-ltr" dir="ltr">',
    "<div dir=\"ltr\" class=\"mw-geshi\" style=\"text-align: left;\">",
    "<div class=\"python source-python\"><pre class=\"de1\">",
    "<pre>",
    "</span>",
    "</pre></div></div>",
    "</pre></div>",
    "&nbsp;",
];


paren1 = "&#40;"
paren2 = "&#41;"
brack2 = "&#93;"
brack1 = "&#91;"
sqirl1 = "&#123;"
sqirl2 = "&#125;"
quote1 = "&quot;"
quote2 = "&#39;"
lessthan = "&lt;"
greaterthan = "&gt;"
ampersand = "&amp;"
substr1 = r"<span class=[^>]*>"
nbsp = "&#160;"

# tasks to suppress in benchmarking run
# plotms -- produces table locks; must be run synchronously
# plotants -- produces a table lock that causes wvrgcal to fail
tasks_to_suppress = ["plotms", "plotants"]

# =====================
# FUNCTIONS
# =====================
def convert_execfile(line):
    if "execfile" in line:
        line = line.replace("execfile",'exec(open')
        line = line + ".read())"
    return line

def comment_out_casa_builtins(line):
    patterns = [ r''' *(inp)''',r''' *(go)''',r''' *(help)''']
    for pattern in patterns:
        if extract_task(line) in casa_tasks:
            return line
        if re.search( pattern, line ):
            new_line = ' ' * indentation(line) + line
            line = "#" + new_line
    return line

def countParen(line):
    """
    Returns the net open and closed parentheses.
    """
    pcount = 0
    for char in line:
        if char == '(': pcount += 1
        if char == ')': pcount -= 1
    return pcount

def isInput(line):
    """
    Tests if a line is waiting for user input.
    """
    temp = line.find("raw_input")
    return  temp > -1

def extract_task(line):
    """
    Tries to return the task name being called in the line.
    """
    # Fix for a taskcall with plotms in VLA_high_frequency_Spectral_Line_tutorial_-_IRC%2B10216 Guide
    if "plotweather" in line:
        stripped = line.lstrip()
        temp = stripped.find("(")
        if "=" in stripped[0:temp]:
            return stripped[0:temp].split("=")[-1].strip()

    stripped = line.lstrip()
    temp = stripped.find("(")
    if temp == -1:
        return None
    return stripped[0:temp]

# Uncomment if we swtich from import casatasks; casatasks.<taskname> to from casatasks import <taskname>
def is_task_call_casa6(line,array):
    """
    Tests if the line is a task call and adds to list.
    """
    if extract_task(line) in casa_tasks:
        array.append(extract_task(line))
    return array

def is_task_call(line):
    """
    Tests if the line is a task call.
    """
    if extract_task(line) in casa_tasks:
        return True
    return False

def indentation(line):
    spaces = 0
    active = True
    for char in line:
        if active == False:
            continue
        if char == " ":
            spaces += 1
        else:
            active=False
    return spaces

def add_benchmarking(line,tasknum=0):
    this_task = extract_task(line)
    indents = indentation(line)
    pre_string = ""
    for i in range(indents):
        pre_string+=" "
    before = pre_string+"this_call = casa_call.Call('"+this_task+"','"+str(tasknum)+"')\n"
    after = "\n"+pre_string+"this_call.end(out_file)"
    return before+line+after

def suppress_for_benchmark(line):
    if is_task_call(line) == False:
        return False
    if extract_task(line) in tasks_to_suppress:
        return True
    return False

def make_func_noninteractive(line):
    """
    Make calls to specific tasks/functions non interactive.
    Set argument interactive to false for specific tasks and functions.
    """
    # First, check to see if clean is called with function arguments.
    funcName = extract_task(line)
    if funcName == "clean" or funcName == "au.plotbandpass" or funcName == "tclean" or funcName == "plotbandpass" :
        # Set argument interactive to false
        pattern = r'''interactive\ *=\ *(True)'''
        new_line = re.sub( pattern, 'interactive = False', line )
        # Leave the mask parameter for testing          
        #if funcName == "clean":
        #    # Remove clean mask parameter if it exists
        #    pattern = r'''mask\ *=\ *['"].*['"].*?,?'''
        #    new_line = re.sub( pattern, '', new_line )
        return new_line
    # Second, check for variables in local namespace
    else:
        pattern = r'''^[ \t]*interactive\ *=\ *(True)'''
        # If variable interactive is being set, make sure it is set to false.
        if re.match( pattern, line ):
            pattern2 = r'''\ *(True)'''
            new_line = re.sub( pattern2, ' False', line )
            return new_line
    return line

def suppress_gui( line ):
    """
    Suppress GUIs. Return modified line.
    * line = a python statement
    """
    if is_task_call(line): 
        # Plotcal
        if extract_task(line) == "plotcal":
            # if showgui is specified, make sure it is false
            pattern = r'''showgui\ *=\ *(True|False)'''
            new_line = re.sub( pattern, 'showgui = False', line )
            if new_line == line: # no substituion made
                # add showgui=False to parameter list
                pattern = r'''\('''
                new_line = re.sub( pattern, '( showgui=False, ', line, count=1 )
            return new_line

        if extract_task(line) == "plotms":
            # if showgui is specified, make sure it is false
            pattern = r'''showgui\ *=\ *(True|False)'''
            new_line = re.sub( pattern, 'showgui = False', line )
            if new_line == line: # no substituion made
                # add showgui=False to parameter list
                pattern = r'''\('''
                new_line = re.sub( pattern, '( showgui=False, ', line, count=1 )
            return new_line

        # Flagdata

        if extract_task(line) == "flagdata":
            pattern = r"""display\ *=\ *['"].*['"]"""
            if re.search( pattern, line ):
            # if showgui is specified, make sure it is false
                new_line = re.sub( pattern, "display=''", line )
                return new_line

        # Suppress GUIs for other tasks here...
    return line


def turnTaskOff( taskname, line ):
    """ Turn off task calls. """
    if is_task_call(line):
        if extract_task(line) == taskname:
            line = ' '*indentation(line) + "print('Turned " + taskname + " off')"
    return(line)

def turnPlotmsOff( line ):
    """ Turn off plotms calls. """
    line = turnTaskOff("plotms", line)
    #line = include_raw_input( "plotcal",line )
    return(line)


def turnDiagPlotsOff( line ):
    """ Turn diagnostic plots off (plotms, plotcal, aU.plotbandpass, plotants, plotxy, plotbandpass, plotweather) """
    line = turnTaskOff("plotms", line)
    line = turnTaskOff("plotcal", line)
    line = turnTaskOff("plotants", line)
    line = turnTaskOff("plotxy", line)
    line = turnTaskOff("plotbandpass", line)
    line = turnTaskOff("plotweather", line)
    line = turnTaskOff("viewer", line)
    line = turnTaskOff("imview", line)
    line = turnTaskOff("au.plotWVRSolutions",line)
    line = suppress_gui(line)
    line = exclude_raw_input(line)

    return line

# function to clean up html strings (convert html markup to executable python)
def loseTheJunk(line):
    """
    Strip garbage from line.
    """
    outline = line # this should be function'd -- need to replace tgets etc as in first version of script
    outline = re.sub(substr1, r'', outline)
    for junk in junkStr:
        outline = outline.replace(junk, "")
    outline = outline.replace(quote1, "\"")
    outline = outline.replace(quote2, "\'")
    outline = outline.replace(paren1, "(")
    outline = outline.replace(paren2, ")")
    outline = outline.replace(brack1, "[")
    outline = outline.replace(brack2, "]")
    outline = outline.replace(sqirl1, "{")
    outline = outline.replace(sqirl2, "}")
    outline = outline.replace(lessthan, "<")
    outline = outline.replace(greaterthan, ">")
    outline = outline.replace(ampersand, "&")
    outline = outline.replace(nbsp, " ")
    outline = outline.replace("<br />", " ")
    outline = outline.replace("<snip>", " ")

    #some additional parsing -- scripting has slightly different
    #syntax than interactive session for tget, default, and go
    #(presumably among others). 

    newline = outline
    newline = newline.replace(r'tget ', r'tget(')
    newline = newline.replace(r'default ', r'default(')
    if newline == 'go':
        newline = 'go('
    if newline != outline: newline = newline + ')'
    outline = newline
    return outline

def addInteractivePause(outline):
    newoutline = outline
    indent = " "*indentation(outline)
    # Use a raw string for the print statement because outline could contain
    # single and/or double quotes.
    newoutline += "\n" + indent + "print r'''Command: " + outline.lstrip().replace('\n','\\n') + "'''"
    newoutline += "\n" + indent + "user_check=raw_input('When you are done with the window, close it and press enter to continue:')"
    return newoutline

def addNonInteractivePause(outline):
    newoutline = outline
    newoutline += "\ninp()\nprint('Pausing for 30 seconds...')\n"
    newoutline += "time.sleep(30)\n"
    #newoutline = string.replace(newoutline, '\n', '\n'+' '*indentation(outline))

    newoutline = ' '*indentation(outline) + newoutline
    return newoutline

# Return the pre-material needed to set up benchmarking
def benchmark_header( scriptName='script' ):
    """
    Write the header of the benchmarking script.
    * scriptName = Name of the benchmarking script
    """
    out_file = scriptName.replace('.py','.benchmark.txt')
    lines = []
    lines.append("### Begin Benchmarking Material")
    lines.append("import casa_call")
    lines.append("try:")
    lines.append("    out_file")
    lines.append("except NameError:")
    lines.append("    out_file = '" + out_file + "'")
    lines.append("if os.path.exists(out_file):")
    lines.append("    counter = 1")
    lines.append("    while os.path.exists(out_file+'.'+str(counter)):")
    lines.append("        counter += 1")
    lines.append("    os.system('mv '+out_file+' '+out_file+'.'+str(counter))")
    lines.append("os.system('rm -rf '+out_file)")
    lines.append("### End Benchmarking Material")
    return lines

def pythonize_shell_commands( line ):
    """
    Make casapy-friendly shell commands Python compatible.
    Unix shell commands included below in the 'commands' list can be called
    directly from the casapy prompt. These commands cannot be called from inside
    a Python script. To run these commands in a script, place them in an 
    os.system call.

    * line = a python statement
    """
    commands = [ 'ls', 'pwd', 'less', 'pwd', 'cd', 'cat' ]
    firstWord = line.split(' ')[0]
    if firstWord in commands:
        line = 'os.system("' + line + '")'
    if 'wget' in line:
        line = '\n'
    return line

def make_system_call_noninteractive( line ):
    """
    Make calls to os.system non-interactive. Return non-interacive line.
    Some shell commands called via os.system require user interaction, such as
    more.  Make these shell calls noninteractive.
    Replacements:
    1) Replace more with cat,
    2) [Add other replacements here...]
    * line = a python statement
    """
    command = ''
    newCommand = ''
    # Extract the system command from the os.system statement
    pattern = r'''os.system\ *\(\ *(['"])(.*)\1\ *\)'''
    matchObj = re.match( pattern, line )
    if matchObj:
        command = matchObj.group(2)
        command = command.strip()
        # Replace more with cat
        pattern2 = r'''^more\ '''
        newCommand = re.sub( pattern2, 'cat ', command )
        # Add additional substutions here...
    newLine = line.replace( command, newCommand, 1 )
    return newLine

def include_raw_input( task,line ):
    """
    * line = a python statement
    """
    if is_task_call(line):
        if extract_task(line) == task:
            line = ''*indentation(line) + line + '\n'
        line += ' '*indentation(line) + 'user_check=raw_input("press enter to continue script")\n'
    return line

def exclude_raw_input( line ):
    """
    Exclude raw_input calls from non-interactive scripts.
    * line = a python statement
    """
    pattern = r'''raw_input\ *\('''
    if re.search( pattern, line ):
        #newline = ' ' * indentation(line) + 'print("script will continue")\n'
        newline = ' ' * indentation(line) + '#' + line
        newline += '\n' + ' '*indentation(line) + 'pass\n'
        line = newline
    return line

def correct_casa_builtins_go( line ):  
    """
    Correct inp built-in from non-interactive scripts.
    * line = a python statement
    """
    pattern = r''' *(go )'''
    if re.search( pattern, line ):
        new_line = re.sub( pattern, 'go', line )
        new_line = ' ' * indentation(line) + new_line + ')'
        line = new_line
    return line

def correct_casa_builtins_inp( line ):  
    """
    Correct inp built-in from non-interactive scripts.
    * line = a python statement
    """
    pattern = r''' *(inp )'''
    if re.search( pattern, line ):
        new_line = re.sub( pattern, 'inp(', line )
        new_line = ' ' * indentation(line) + new_line + ')'
        line = new_line
    return line

def correct_casa_builtins_help( line ):  
    """
    Correct help built-in from non-interactive scripts.
    * line = a python statement
    """
    pattern = r''' *(help )'''
    if re.search( pattern, line ):
        new_line = re.sub( pattern, 'help(', line )
        new_line = ' ' * indentation(line) + new_line + ')'
        new_line = "#" + new_line
        line = new_line
    return line

def correct_execfile( line ):  
    """
    Correct execfile
    * line = a python statement
    """
    pattern = r''' *(execfile)'''

    if re.search( pattern, line ):
        new_line = re.sub( pattern, 'exec(open', line )
        new_line = ' ' * indentation(line) + new_line + '.read())'
        line = new_line
    return line

def make_noninteractive( line ):
    """
    Make *line* non-interactive.
    * line = a python statement
    """
    line = make_func_noninteractive(line)
    line = make_system_call_noninteractive(line)
    line = exclude_raw_input(line)
    line = correct_casa_builtins_inp( line )
    line = correct_casa_builtins_help( line )
    line = suppress_gui(line)
    return line

def listCASATasks():
    """
    Return a list of all the CASA tasks.
    Also report the difference between the task list in this module and the
    task list obtained from CASA. Note that the appropriate list will vary
    with the version of CASA.
    This function requires casapy module *tasks*.
    In casapy:
    >>> import extractCASAscript
    >>> taskList = extractCASAscript.listCASATasks()
    
    Review the difference between the task lists here...
    To update the task list in this module, 
    >>> print taskList
    Then, copy-paste the output list into this module.
    THIS COULD BE AUTOMATED IF THE SCRIPT EXTRACTOR WAS RUN WITHIN CASAPY!  THE
    CURRENT DESIGN ASSUMES THIS IS NOT THE CASE.
    """
    from tasks import allcat
    all_tasks=[]
    for key in allcat.keys():
        for taskname in allcat[key]:
            if (taskname[0] == '(') or (taskname[0]=='{'):
                taskname = taskname[1:-1]
            if (taskname in all_tasks) == False:
                all_tasks.append(taskname)
    all_tasks.sort()
    all_tasks_set = set(all_tasks)
    casa_tasks_set = set(casa_tasks)
    print("Tasks in casapy but not in this module: " + \
          str(all_tasks_set.difference(casa_tasks_set)))
    print("Tasks in this module but not in casapy: " + \
          str(casa_tasks_set.difference(all_tasks_set)))
    return all_tasks

def checkModules():
    """ Check that modules required for the benchmarking script are in the
    Python path. """
    try:
        import casa_call
    except ImportError:
        print("casa_call.py must exist in the casapy module search path!")
        raise


def casa6_line(line):
    if extract_task(line) in casa_tasks:
        line = "casatasks.{}".format(line)
    return line

# =====================
# MAIN PROGRAM
# =====================

def main(URL, benchmark=False , diagplotoff=False , plotmsoff=False, noninteractive=False, casa6=False, py2to3=False):

    """ Create a Python script from a CASA Guide or existing Python script.
    
    * URL = URL to a CASA Guide web page (HTML) or a Python script.  
    * benchmark: produce a benchmark test from the CASA Guide or existing Python script
        If URL to a CASA Guide, extract the Python from the guide and create
        an executable Python script. If options.benchmark is true, . 
        If URL to a Python script, convert the script to a benchmarking script.
    * diagplotoff: Turn off diagnostic plots
    * plotmsoff: Turn off task plotms
    * noninteractive: Turn off interactive features
    * (BETA) casa6: set extracted script to CASA6 format
    * (BETA) py2to3: Add python 3 print and execfile features

    """
    # Determine if the input file is a Python script

    pyInput = False
    if ( URL[-3:].upper() == '.PY' ):
        pyInput = True

    # Pull the input file across the web or get it from local network
    responseLines = []
    outFile = ''
    if ( URL[:4].upper() == 'HTTP' ):
        print("Acquiring " + URL)
        if os.uname()[0] == 'Darwin': #http://stackoverflow.com/questions/27835619/ssl-certificate-verify-failed-error
            import ssl
            if py3:
                req = urllib.request.Request(URL)
                gcontext = ssl.SSLContext(ssl.PROTOCOL_TLS) # Fix for python versions > 3.0
                response = urllib.request.urlopen(req,context=gcontext)
                responseLines = response.read().decode('utf-8').split("\n")
            else:
                req = urllib2.Request(URL)
                gcontext = ssl.SSLContext(ssl.PROTOCOL_TLS) # Fix for python versions > 2.7.13 to match new certificates 
                response = urllib2.urlopen(req,context=gcontext)
                responseLines = response.read().split("\n")
        else:
            if py3:
                req = urllib.request.Request(URL)
                response = urllib.request.urlopen(req)
                responseLines = response.read().decode('utf-8').split("\n")

            else:
                req = urllib2.Request(URL)
                response = urllib2.urlopen(req)
                responseLines = response.read().split("\n")
        # Clean up the output file name
        outFile = URL.split('/')[-1]
        if not pyInput: 
            outFile += '.py'
        outFile = outFile.replace("index.php?title=","")
        outFile = outFile.replace(":","")
        outFile = outFile.replace("_","") 
        outFile = outFile.replace("%","_") 
    else:
        print("Copying " + URL + " to CWD.")
        os.system('cp '+URL+' ./')
        outFile = os.path.basename(URL)
        localFile = open( outFile , 'r' )
        responseLines = localFile.read().split("\n")

    # Initialize the parser and output line list
    readingCode = False
    lineList = []

    if pyInput:
        lineList = responseLines



    else:
        # Loop over the lines read from the web page
        for line in responseLines:
            # If we are not currently reading code, see if this line
            # begins a python code block.
            if (readingCode == False):
                if any([beginBlocks[0] in line, beginBlocks[1] in line, beginBlocks[2] in line, beginBlocks[3] in line, beginBlocks[4] in line]):
                    readingCode = True
                    outline = loseTheJunk(line)
                    lineList += [outline]
                    if endBlock in line:
                        readingCode = False

    # The python code is now loaded into a list of lines.  Now compress the
    # lines into individual commands, allowing for commands to span multiple
    # lines.  Lines are grouped by closed parentheses.
    compressedList = []
    iline = 0
    while iline < len(lineList):
        line = lineList[iline]
        pcount = countParen(line)
        while(pcount > 0):
            line += '\n'
            iline += 1
            line += lineList[iline]
            pcount = countParen(line)
        if py3:
            line = line.expandtabs()
        else:
            line = string.expandtabs(line)
        compressedList += [line]
        iline += 1

    print(str(len(lineList))+" total lines become")
    print(str(len(compressedList))+" compressed lines")

    # All modes
    for i,line in enumerate(compressedList):
        compressedList[i] = pythonize_shell_commands(compressedList[i])

    # Prepare for benchmark and noninteractive modes
    if noninteractive:
        for i,line in enumerate(compressedList):
            compressedList[i] = make_noninteractive(compressedList[i])

    # Write script for benchmark mode
    if benchmark:
        task_list = []
        task_nums = []
        print("Writing file for execution in benchmarking mode.")
        tasknum = 0
        f = codecs.open(outFile, 'w','utf-8')
        checkModules()
        header = benchmark_header(scriptName=outFile)
        for line in header:
            if py3:
                print(line, file=f)
            else:
                print >>f, line
        for line in compressedList:
            if suppress_for_benchmark(line):
                if py3:
                    print(' ' * indentation(line) + 'pass #' + \
                        line.replace('\n', ''), file=f)
                else:
                    print >>f, ' ' * indentation(line) + 'pass #' + \
                        line.replace('\n','')
            else:
                line = suppress_gui(line)
                if is_task_call(line):
                    this_task = extract_task(line)
                    print("I found a task call for ", this_task)
                    tasknum += 1
                    line = add_benchmarking(line,tasknum)
                    task_list.append(this_task)
                    task_nums.append(tasknum)
                if py3:
                    print(line.decode('utf-8'), file=f)
                else:
                    print >>f, line.decode('utf-8')
        if py3:
            print('casa_call.summarize_bench( out_file, out_file+".summary" )', file=f)
        else:
            print >>f, 'casa_call.summarize_bench( out_file, out_file+".summary" )'
        f.close()

        # Write task list to expectation file
        exp_file = outFile+'.expected'
        print("I am writing the expected flow to a file called "+exp_file)
        f = codecs.open(exp_file, 'w', 'utf-8')
        for i in range(len(task_list)):
            if py3:
                print(task_list[i], task_nums[i], file=f)
            else:
                print >>f, task_list[i], task_nums[i]
        f.close()
    else:
        # Write script for interactive and noninteractive modes
        f = codecs.open(outFile, 'w','utf-8')
        #if not py2to3:
        #    print("from __future__ import print_function", file=f)
        if casa6:
            # Uncomment if we swtich from import casatasks; casatasks.<taskname> to from casatasks import <taskname>
            task_list = []
            for line in compressedList:
                task_list = is_task_call_casa6(line,task_list)
            task_list = sorted(set(task_list))

            # Fix to remove plotms from casatasks and use casaplotms
            use_casaplotms = False
            if "plotms" in task_list:
                use_casaplotms = True
                task_list.remove("plotms")


            use_casaviewer = False
            if "viewer" in task_list:
                use_casaviewer = True
                task_list.remove("viewer")

            tasks = ', '.join(map(str, task_list))

            print("import os, sys, numpy", file=f)
            print("import casatools", file=f)
            print("import casatasks", file=f)

            if not plotmsoff:
                if use_casaplotms:
                    print("import casaplotms", file=f)
                    print("from casaplotms import plotms" ,file=f)

            if not diagplotoff:
                if use_casaviewer:
                    print("import casaviewer", file=f)
                    print("from casaviewer import viewer" ,file=f)

            print("from casatasks import ", tasks ,file=f)

        for line in compressedList:

            if line == 'viewer':
                line = 'viewer()\n'

            if line.startswith("!") or line.startswith("%"):
                line = "#" + line

            line = turnTaskOff('taskname', line)
            if diagplotoff:
                #print("Turning off diagnostic plots...")
                line = turnDiagPlotsOff(line)

            if plotmsoff:
                #print "Turning off plotms..."
                line = turnPlotmsOff(line)

            if noninteractive:
                #print "Turning on Non Interactive features..."
                line = exclude_raw_input(line)
                line = suppress_gui(line)
                # NOTE compressedList iterates through make_noninteractive
                if extract_task(line) == 'plotms':
                    line = addNonInteractivePause(line)

            else: #interactive

                line = line
                line = correct_casa_builtins_inp(line)
                line = correct_casa_builtins_help(line)

            if py2to3:
                line = correct_execfile(line)


            if casa6:
                line = correct_casa_builtins_go(line)
                line = comment_out_casa_builtins(line)
                line = convert_execfile(line)
                #line = casa6_line(line)

            if py3:
                line = convert_execfile(line)
                print(line, file=f)
            else:
                print(line.decode('utf-8'), file=f)

        f.close()

    print("New file " + outFile + " written to current directory.")
    print("In casapy, run the file using ")

    if sys.version_info[0] > 2 or py2to3:
        print('exec(open("' + outFile + '").read())')
    else:
        print('execfile("' + outFile + '")')
    #sys.exit(0)
    return


if __name__ == "__main__":
    usage = \
""" %prog [options] URL
*URL* should point to a CASA Guide webpage or to a Python script. *URL* can also be
a local file system path."""
    parser = OptionParser(usage=usage)
    parser.add_option('-a', '--casa6', action="store_true", default=False, help=SUPPRESS_HELP ) #help="produce CASA6 compatiable script"
    parser.add_option('-t', '--py2to3', action="store_true", default=False, help=SUPPRESS_HELP ) #help="produce python 3 compatiable script"
    parser.add_option('-b', '--benchmark', action="store_true", default=False, help="produce benchmark test script")
    parser.add_option('-n', '--noninteractive', action="store_true", default=False, help="make script non-interactive (non-benchmark mode only)")
    parser.add_option('-p', '--plotmsoff', action="store_true", help="turn off all plotms commands")
    parser.add_option('-d', '--diagplotoff', action="store_true", help="turn off diagnostic plots (imview, plotms, plotcal, aU.plotbandpass, plotants, plotxy)")
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.print_help()
        #raise ValueError("")
        sys.exit(1)
    main(args[0], benchmark=options.benchmark, diagplotoff=options.diagplotoff, plotmsoff=options.plotmsoff, noninteractive=options.noninteractive, casa6=options.casa6, py2to3=options.py2to3)
    sys.exit(0)
    #main(args[0], options)


