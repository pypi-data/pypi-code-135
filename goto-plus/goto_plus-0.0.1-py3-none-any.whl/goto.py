###PLACE ME AT THE TOP OF YOUR CODE### (this function can not be imported as it requires the __file__ var of the specific file it is used in)
import sys
import os

sys.trackbacklimit=0

global CONFIG__FILE__VAR, CONFIG_COMPLETE
CONFIG__FILE__VAR = ""
CONFIG_COMPLETE = False

def goto(line):
    global CONFIG__FILE__VAR
    if CONFIG__FILE__VAR == "": raise Exception("Please run `gotoconfig(__file__)` before using goto")
    with open(os.path.abspath(CONFIG__FILE__VAR), "r") as f: content = [i.replace("    ", "\t") for i in f.readlines()]
    #print(content)
    try: exec("".join(content[(line-1):]), globals())
    except SystemExit: raise __import__("sys").exit()       
    except RecursionError: raise __import__("sys").exit("GoTo Exception - GoTo has formed a loop.")
    except IndentationError:
        while any([i.isalpha() for i in content[(line-1)]]) == False: line += 1
        editout = content[(line-1):]
        for j, i in enumerate(list(content[(line-1):][0].replace(content[(line-1):][0].lstrip(), ""))):
            editout.insert(0, "{}if True:\n".format('\t' * (len(list(content[(line-1):][0].replace(content[(line-1):][0].lstrip(), "")))-j-1)))
        exec("".join(editout))
    raise __import__("sys").exit()

def gotoconfig(f):

    global CONFIG__FILE__VAR, CONFIG_COMPLETE
    if CONFIG_COMPLETE:
        return
    CONFIG__FILE__VAR = f
    CONFIG_COMPLETE = True
    newfolder = os.path.dirname(os.path.abspath(CONFIG__FILE__VAR))
    sys.path.insert(1, newfolder)
    #print(CONFIG__FILE__VAR, "correct")
    goto(1) # not this file lol
    raise SystemExit

if __name__ == "__main__":
    raise Exception("Please import goto")