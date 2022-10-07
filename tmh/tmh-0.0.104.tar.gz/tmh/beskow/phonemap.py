
import csv
import os
class phonemap:

    def __init__(self,frombet,tobet,mapfile=None,stripchars='',accept_empty=False,verbose=False):
        self.m = {}
        self.charmap = {}
        self.accept_empty = accept_empty
        self.stripchars = stripchars
        self.verbose = verbose
        dir = os.path.dirname(os.path.abspath(__file__))
        if mapfile:
            self.mapfile = mapfile
        else:
            self.mapfile = os.path.join(dir,'phonemap_lexikon.py')
        with open(self.mapfile) as csvf:
            dictreader = csv.DictReader(csvf,delimiter='\t')
            if not frombet in dictreader.fieldnames:
                raise Exception('frombet {} not in mapfile'.format(frombet))
            if not tobet in dictreader.fieldnames:
                raise Exception('tobet {} not in mapfile'.format(tobet))

            for item in dictreader:
                if tobet.startswith('is'):
                    self.m[item[frombet]] = bool(eval(item[tobet]))  #interpret numbers and 'True'/'False' as boolean
                else:
                    self.m[item[frombet]] = item[tobet]
    def normalize(self,sym):
        sym = sym.replace('ː',':').replace('ɡ','g')
        if self.stripchars:
            sym = sym.strip(self.stripchars)
        return sym

    def map(self,item):

        if type(item)==list: # list of symbols
            return [self.map(p) for p in item]
        else: # single symbol
            sym = self.normalize(item)
            ret = self.m[sym]
            if sym in self.m:
                if self.verbose:
                    print(sym,'->',ret)
                return ret
            else:
                print('no match for',sym)
                if self.accept_empty:
                    return ''
                else:
                    raise Exception('no mapping for {}'.format(sym))
    
    def splitphonestring(self,string):
        allphones = sorted(list(self.m),key=len,reverse=True) # all phones sorted by length
        allphones = [p for p in allphones if p!='']
        maxlen = len(allphones[0])
        res = []
        string = string.strip()
        smatch = False
        for ph in allphones:
            if string.startswith(ph):
                #print(ph)
                smatch = True
                res.append(ph)
                rest = string[len(ph):]
                #print(res,'-',rest)
                if rest in allphones:
                    res.append(rest)
                elif len(rest)>1:
                    res += self.splitphonestring(rest)
                else:
                    raise Exception('?:'+rest)
                break
        if not smatch:
            raise Exception('no match for:'+string)
        return res

    def exists(self,sym):
        sym = self.normalize(sym)
        return sym in self.m

if __name__ == '__main__':

    #    pm = phonemap('MTM','IPA','swmap.tsv')
    pm = phonemap('STA','IPA')
    s = 'A:'
    print('map():\n',s,'->',pm.map(s))
    a = 'SJÖ:SJU:KA'
    b = pm.splitphonestring(a)
    print('splitphonestring():\n',a,'\n',b)
    print('map():\n',b,'\n',pm.map(b))
