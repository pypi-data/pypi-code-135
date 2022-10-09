import datetime
import os

ERROR = 0   # prints only errors
WARNING = 1 # prints errors + warnings
INFO = 2    # prints errors + waringns + info

class jnlog:
    def __init__(self, name=None, loglevel=2, timed=True, whitetext=True, log1name='LOG1', log2name='LOG2'):

        """        
        [non important]
        log fmt : '[hh/mm/ss] {level} [name] {message}'
        """

        self.name = name        
        self.loglevel = loglevel
        self.timed = timed
        self.coloredtext = not whitetext
        
        self.timecolor = '\033[10;37m'        
        self.namecolor = '\033[36;97m' if 0 else ''
        self.textcolor = '\033[31;97m'        
        
        self.errorcolor = '\033[31;31m'
        self.warncolor ='\033[31;93m'
        self.infocolor = '\033[31;96m'
        self.l1color = '\033[31;95m'
        self.l2color = '\033[31;92m'                
        self.l1name = log1name
        self.l2name = log2name

        os.system('color')

    def __log(self, color, type, a):
        """
        internal log backend
        """
        t = datetime.datetime.now().time()

        hour = str(t.hour)
        min = str(t.minute)
        if len(min) == 1:
            min = '0'+min
        sec = str(t.second)
        if len(sec) == 1:
            sec = '0'+sec
        
        
        txt = ''.join(a)        
        out = ''
        out += f'{self.timecolor}[{hour}/{min}/{sec}] ' if self.timed else ''
        out += f'{color}[{type}]'
        out += f' {self.namecolor}[{self.name}]' if self.name else ''
        out += f'{self.textcolor}' if not self.coloredtext else ''
        out += f' {txt}\033[0m'

        print(out)        
    
    
    def info(self, *a):
        if self.loglevel < INFO:
            return
               
        self.__log(self.infocolor, 'INFO', a)
    
    def warn(self, *a):
        if self.loglevel < WARNING:
            return
        
        self.__log(self.warncolor, 'WARN', a)
    
    def error(self, *a):
        if self.loglevel < ERROR:
            return

        self.__log(self.errorcolor, 'ERROR', a)                
    
    def log1(self, *a):
        if self.loglevel < INFO:
            return

        self.__log(self.l1color, self.l1name, a)

    def log2(self, *a):
        if self.loglevel < INFO:
            return

        self.__log(self.l2color, self.l2name, a)
