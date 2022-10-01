import sys,inspect



class frame_info:
    '''frame info class'''
    def __init__(self,frame) -> None: 
        if not frame: return
        self.frame=frame
        self.filename = frame.f_code.co_filename
        if self.filename=='<stdin>':
            self.name='<stdinput_frame>'
            return
        
        self.line= frame.f_lineno
        self.name=frame.f_code.co_name
        self.locals=frame.f_locals
        self.globals=frame.f_globals 
        self.module=self.globals['__name__']
        try:
            self.code=inspect.getsource(frame.f_code)
            #self.doc=inspect.getdoc(frame.f_code)#err
            self.comment=inspect.getcomments(frame.f_code)
            self.args_str=self.code[self.code.find(self.name)+len(self.name):self.code.find(':')]
        except:self.args_str=''
        self.path=[self.module,*self.parent]
        self.object=self.locals.get('self',None)
        if self.object:
            self.objectname=self.object.__class__.__qualname__
            self.path.append(self.objectname)
        self.path.append(self.name)
        self.path='.'.join(self.path)
        self.signature=f'line {self.line}[level:{self.level}]: {self.path}{self.args_str} {self.locals}'
            
    @property
    def caller(self):
        return frame_info(self.frame.f_back)#self.__class__
    @property
    def level(self):
        def get_level(frame,level=0):
            try: return get_level(frame.f_back,level+1)
            except: return level-1
        return get_level(self.frame.f_back)
    @property
    def parent(self):
        def get_parent(frame,parent=None):
            if not parent:parent=[]
            if hasattr(frame,'name'):parent.append(frame.name) 
            try: return get_parent(frame.caller,parent)
            except: return parent
        return get_parent(self.caller)[:-1][::-1]

    def all(self,dellines='frame,globals'):
        return '\n'.join([f'{k}: {v}' for k,v in self.__dict__.items() if k   not in dellines.split(',')]) # str(self.__dict__)
    def __repr__(self):
        #print(self.locals)
        return getattr(self,'signature','No Signature')


class notfound: 
    '''reaction if var not found'''
    __slots__='notfound_result,on_notfound,defaultmsg'.split(',')
    @property
    def raiseexception(s): 
        s.on_notfound='raise' 
        return s
    @property
    def printmsg(s): 
        s.on_notfound,s.notfound_result='print',None
        return s
    @property
    def ignore(s): 
        s.on_notfound,s.notfound_result=None,None
        return s
    @classmethod
    def strinit(cls,mode='raise'):
        modes={'raise':('not_found','raise'),'print':(None,'print'),None:(None,None)}
        return cls(*modes[mode])
    def __init__(s,notfound_result='not_found',on_notfound='raise',defaultmsg='Not Found.') -> None:
        s.on_notfound,s.notfound_result,s.defaultmsg=on_notfound,notfound_result,defaultmsg
    def __call__(self,notfound_msg=None):
        msg=notfound_msg or self.defaultmsg
        if self.on_notfound=='raise': raise AttributeError(msg)
        elif self.on_notfound=='print': print(msg) 
        return self.notfound_result
    def __repr__(self) -> str:
        return f'{super().__repr__()} on-notfound={self.on_notfound} result={self.notfound_result}'
        

testvar2='TESTVAR2 finded!'
def testglobals2(): 
    '''import this to you script and run or run nitvars_test.py'''
    def checkvar():
        print(f'var "testvar" in simple globals()={globals().get("testvar","NOT FOUND!")}')
        print(f'var "testvar" in globals2()={globals2().silent.testvar}')
        print(f'var "testvar" in realglobals()={realglobals().silent.testvar}')
        print(f'testvar in [level:id]: {g2("*",notfound=None).stat("testvar")}')
    print('Now get testvar. testvar in globals!')
    checkvar()
    print('Why?  globals() find globals only in this script(in nitvars.py..)')
    #g2().testvar='NOT SET!'
    print('\nNow set testvar with "global testvar"')
    global testvar
    testvar='SET OK!'
    checkvar()
    print('Why?  global x set globals only in this script(in nitvars.py..)')
    #g2().testvar='NOT SET!'
    print('\nNow set testvar2 with "globals()[testvar]"')
    globals()["testvar"]='SET OK!2'
    checkvar()
    print('Why?  globals() set globals only in this script(in nitvars.py..)')
    g2().testvar='NOT SET!'
    print('\nNow set testvar2 with nitvars "globals2()[testvar]"')
    globals2()["testvar"]='SET OK!3'
    checkvar()
    print('Why?  globals2() is real globals, globals() is ...')

   

class globals2:
    '''unit2.py import unit1.py with call globals() => globals()==globals in unit1.py /allglobals=globals()+sys.modules['main']
    get globals2().x or globals2()['x'] 
    set globals2().x=y or globals2()['x']=y 
    run test_globalvars2.py'''
    #__slots__='getters,levels,notfound,set_on'.split(',')
    #levels=None
    #__slots__=['notfound']
    @property
    def silent(self):
        return self.settings(notfound='print')
    @property
    def ignore(self):
        return self.settings(notfound=None)
    @property
    def notset(self):
        return self.settings(set_on=False)
    #def __new__(cls ,set_on=True,getlevels='main>thisscript',setlevels='main+finded+thisscript',notfound='raise') :
    #    self=super().__new__(cls) 

    def setself(f):#decorator
        def go(self,*a,**ka):
            self.__class__.__setattr__=self.__class__.__setitem__=super().__class__.__setattr__#set in self object
            r=f(self,*a,**ka)
            self.__class__.__setattr__=self.__class__.__setitem__=self.__class__.set#set in levels global/local/module..
            self.__class__.__getattr__=self.__class__.__getitem__=self.__class__.get
            return r
        return go
    
    @setself
    def __init__(self,set_on=True,getlevels='main>thisscript',setlevels='main+finded+thisscript',notfound='raise') -> None:
        self.thisscript=self.__module__
        self.settings(getlevels=getlevels,setlevels=setlevels, notfound=notfound,set_on=set_on)
  
    
    def getter(self,name,level): return getattr(sys.modules[level],name,self.notfound) 
    def setter(self,name,value,level):setattr(sys.modules[level],name,value)
    def getall(self,level):return vars(sys.modules[level])
    @property
    def all_levels(self):return list(sys.modules.keys())


    def make_levels(self,levels,sep):
        if levels=='*': r=self.all_levels
        else:r=levels.replace('main','__main__').replace('thisscript',self.thisscript).split(sep) if type(levels)==str else levels
        return set(r)
 

    def settings(self,**new_settings): 
        correct_settings={'notfound': lambda v:notfound.strinit(v) if not type(v)==notfound else v,
                            'getlevels':lambda v:self.make_levels(v,'>'),
                            'setlevels':lambda v:self.make_levels(v,'+'), }
        for k,v in new_settings.items():
            if k in correct_settings: new_settings[k]=correct_settings[k](v)
        self.__dict__.update(new_settings)
        return self

    

    def __contains__(self,name):#'x' in self
        return self.check(name)
    def check(self,name):
        nf=self.notfound
        self.settings(notfound=notfound('not_found!',None))#(nf[0],None))
        r=self.get(name)
        rz=not r==self.notfound.notfound_result
        self.settings(notfound=nf)
        return rz
    def stat(self,name):
        r=self.get(name,True)
        if not r==self.notfound.notfound_result:
            r,modules=r
            m={k:id(v) for k,v in modules.items()}
            return m

    @property
    def dict(self):
        r={}
        for level in self.getlevels: r.update(self.getall(level))
        return r
    
    @property
    def setdict(self):
        r=type('setdict',(dict,),{})
        r.__setattr__=r.__setitem__=self.set
        return r()
    def get(self,n,getlevels=False):  
        levels={}
        for level in self.getlevels: 
            r=self.getter(n,level) 
            if r is not self.notfound:levels[level]=r
            if r is not self.notfound and not getlevels: break
         
        if r is self.notfound and len(levels)==0:  
            nf=f'Not found "{n}" in levels {self.getlevels}'
            r=r(nf)
        elif getlevels: r=(list(levels.values())[0],levels)
        return r

    def gettry(self,name,getlevels=False): 
        nf=self.notfound
        self.settings(notfound=notfound(nf.notfound_result,None))#(nf[0],None))
        r=self.get(name,getlevels)
        self.settings(notfound=nf)
        return r
 
    def set(self,n,v,modules='fromself'):
        if self.set_on:
            if modules=='fromself': modules=self.setlevels 
            else: modules=self.make_levels(modules,'+')
            for level in modules:
                if level=='finded':
                    if not n in self: continue
                    else:
                        _,levels=self.get(n,True)
                        for finded in levels.keys(): self.setter(n,v,finded)
                else:self.setter(n,v,level) 
        else: raise Exception(f'{type(self)} SET disabled. You can not set {n}')




class locals2(globals2):
    '''locals2 for set locals in back frames
    run gotestlocals()'''
    @globals2.setself
    def __init__(self,getlevels=0,set_on=True,setlevels='0+finded',notfound='raise'): 
        '''levels  2=2 -2=[0,-1,-2] 0>-1 = [0,-1] globals=globals'''
        self.frame=sys._getframe(2)
        super().__init__(set_on,getlevels,setlevels,notfound) 
        
          
    def make_levels(self, levels, sep):
        if type(levels)==int: 
            if levels<0: levels=[z for z in range(abs(levels))]+[abs(levels),]
            else: levels=str(levels)
        elif type(levels)==str: levels=levels.replace('globals','module')
        return super().make_levels(levels, sep)
        
    def getall(self,level,getframe=False):  
        import re
        f=self.frame
        if type(level)==int or ( type(level)==str and re.fullmatch('[0-9-]+',level)):
            for l in range(abs(int(level))):  f=f.f_back
        else: #find frame names
            for l in range(99999):  
                if f.f_code.co_name in [level,f'<{level}>']:break
                f=f.f_back 
                
        r=f.f_locals
        if getframe:r=(f,r)
        return r
    def getter(self,name,level): return self.getall(level).get(name,self.notfound)
    def setter(self,name,value,level):
        f,loc=self.getall(level,True)
        loc[name]=value
        import ctypes
        ctypes.pythonapi.PyFrame_LocalsToFast(ctypes.py_object(f), ctypes.c_int(0))

    @property
    def all_levels(self):
        r=[]
        for i in range(99999):
            try: 
                f,_=self.getall(i,True)
                #print(i,f.f_code.co_name)
                r.append(-i)
            except: break
        return r
    def levelnames(self,levels_or_level):
        levels=self.make_levels(levels_or_level,'>')
        return [self.getall(level,True)[0].f_code.co_name for level in levels]


 

def exec2(code,in_global=False): 
    ''' exec and return func
    last line = return
    exec2('globals()["z"]=7;5+5') =10
    lambda x,y:e2('print(12345);x+y')
    '''
    code=code.strip().replace(';','\n').split('\n')
    
    def go(code,met):
        loc=l2('0>-1>-2')
        setvars=g2().setdict  if in_global else loc.setdict 
        glvars=g2().dict
        glvars.update(loc.dict)
        return met(code,glvars,setvars)
 
    for c in code[:-1]:
        go(c,exec) 
    r= go(code[-1],eval) if not '=' in code[-1] else go(code[-1],exec)
    return r 




from types import MethodType,FunctionType,BuiltinFunctionType,BuiltinMethodType
func_types=(MethodType,FunctionType,property,BuiltinFunctionType,BuiltinMethodType,type(str.encode))


class scaner:
    def __new__(cls,target=3): 
        #self=super().__new__(cls)
        if type(target)==str:
            if target.isdigit(): target=int(target)
            if type(target)==str:
                o=globals()[target]
                return cls.function(o)
        if type(target)==int: return cls.code(target)
        elif type(target) in func_types: return cls.function(target)
        else: return cls.object(target)
        #return self

    class code(frame_info): 
        def __init__(self,target=3) -> None:
            self.stack=inspect.stack() 
            target=self.stack[target]
            super().__init__(target[0])
            '''self.name=target[3]
            self.file=target.filename
            target=target[0]
            self.code=inspect.getsource(target.f_code)
            self.locals=target.f_locals
            self.globals=target.f_globals 
            self.module=self.globals['__name__']'''
            
    class function:
        def __init__(self,target) -> None: 
            def scanarg(arg): 
                r=jd()
                r.name=arg.name
                if not arg.annotation==inspect._empty: r.annotation=arg.annotation
                if not arg.default==inspect._empty: r.default=arg.default
                return +r
            self.name=target.__name__ 
            self.args=jd({k:scanarg(v) for k,v in dict(inspect.signature(target).parameters).items()})# if not str(v).startswith('*')}
            self.args_str=str(inspect.signature(target))
            self.code=inspect.getsource(target)
            self.signature=self.name+self.args_str
            self.doc=inspect.getdoc(target)
            self.comment=inspect.getcomments(target)
    class object:
            def __init__(self,target) -> None: 
                if hasattr(target,'__qualname__'):name=target.__qualname__ 
                elif hasattr(target,'__name__'):name=target.__name__ 
                else: name=str(target)[:100] 
                self.name=name 
                d=vars(target) if isinstance(target,type) else vars(type(target))#if tagret=obj() vars(target) = huinya
                #d={k:getattr(target,k) for k in dir(target) }
                not_priv={k:v for k,v in d.items() if not k.startswith('__')}
                self.not_private=not_priv
                self.vars={k:v for k,v in not_priv.items() if type(v) not in func_types} 
                self.functions={k:v for k,v in not_priv.items() if type(v) in func_types}  

         

class tracer:
    '''
    >>> nitweb.parse('dfg[34]','[^]')
    >>>CALL: line 124: nitweb.parse(data,search,getend=False) {'data': 'dfg[34]', 'search': '[^]', 'getend': False}
    ### RETURN: line 138: nitweb.parse(data,search,getend=False) {'data': '34]', 'search': ['[', ']'], 'getend': False, 's': 2, 'x': 4, 'r': '34'} ==> 34 [<class 'str'>]
    # '''

    def __init__(self,on_call=...,on_return=...,maxlevel=999) -> None:
        if on_call is not ...:self.on_call=on_call
        if on_return is not ...:self.on_return=on_return
        self.maxlevel=maxlevel
        self.calls=[]
        self.returns=[]
    @property
    def silent(self):
        self.on_call,self.on_return=None,None
        return self
    @property
    def clean(self):
        self.calls=[]
        self.returns=[]

    def frame_info(self,frame): 
        return frame_info(frame)
        
    def on_call(self,frame): 
        print("\t"*frame.level+f">>>CALL: {frame}")
        #import inspect
        #print(inspect.getsource(frame.f_code)) 
    def on_return(self,frame,value):
        print("\t"*frame.level+f'### RETURN: {frame} ==> {value} [{type(value)}]')
    def tracer(self,frame, event, arg):
        #tracer.level=0 if not hasattr(tracer,'level') else tracer.level+1
        #frame.f_trace_opcodes= True
        if event in ['call','return']:
            frame_info=self.frame_info(frame)
            if frame_info.filename=='<stdin>': return #no  input frames
            if getattr(frame_info,'object',None).__class__==self.__class__: return# no trace me
            if frame_info.level>self.maxlevel: return #no level out
            if event == 'call':
                self.calls.append(frame_info)
                if self.on_call:self.on_call(frame_info)
                frame.f_trace_lines = False
                return self.tracer 
            elif event == 'return':
                if arg is None: return # no None returns
                if arg.__class__==self.__class__: return# no trace me 
                self.returns.append(arg) 
                if self.on_return:self.on_return(frame_info,arg) 
            #elif event == 'c_call':  print(f"Entering2: {arg.__name__}") 
            #elif event == 'c_return':  print(f"Returning from: {arg.__name__}")
            #else: print (frame,event,arg)
    @property
    def on(self): 
        self.old_tracer=sys.gettrace() 
        sys.tracebacklimit=1
        sys.settrace(self.tracer)
    @property
    def off(self):sys.settrace(self.old_tracer)
    #@classmethod
    @property
    def active(self): return sys.gettrace()==self.tracer
    def trace(self,func):#decorator or run tracerobj.trace(func)(funcargs)
        def trace_func(*a,**ka):
            #self=cls()
            self.clean
            self.on
            func(*a,**ka)
            self.off
        return trace_func
    def __call__(self, func, *a,**ka):
        return self.trace(func)
    def __rshift__(self, other,*a):#x>>other  traceobj>>func= 
        return self.trace(other)
    def __enter__(self): #with trace():
        self.clean
        self.on
        return self
    def __exit__(self,*a):   self.off


 
def dec(func,newfunc):
    def aka(*a,**ka):
        return newfunc(func,*a,**ka)
    return aka

def dec2(newfunc):
    def dec(func):
        def aka(*a,**ka):
            return newfunc(func,*a,**ka)
        return aka
    return dec


def callhelp(func):#decorator
    '''help call func if args not defined'''
    def callhelper(*a,**ka):
        import inspect,re
        try: r=func(*a,**ka)# inspect.getcallargs(x,*a,**ka)  
        except TypeError as e: 
            if 'missing' in str(e) and 'argument' in str(e):
                help=' help: '+func.__doc__ if func.__doc__ else ''
                print(f'Запуск функции {func.__name__}{inspect.signature(func)} {help}')
                notset=re.findall('\'([A-z0-9_]+)\'',str(e)) #x() missing 2 required positional arguments: 'q' and 'w'
                #nowset={}
                for n in notset: 
                    ka[n]=input(f'Введите параметр "{n}"("#q" для отмены запуска)')
                    if ka[n]=='#q': return None
                r=func(*a,**ka)
            else: raise e
        return r
    return callhelper


def sysargsrun(func): 
    #import inspect 
    #realname2=inspect.stack()[1][0].f_globals['__name__'] #real __name__ .if script run(no import) realname=__main__ (fix: __name__==superclass)  
    in_module=realname()
    import json
    '''Decorator: auto run func if main with func(*sys.argv)
        @sysargsrun  
        def main(lp,proxy):
        ''' 
    if in_module=='__main__':
        print('CMD Command run:',sys.argv)
        sa=sys.argv[1:]
        sa2=[]
        for s in sa:
            if s.startswith('@'): #list from file
                with open(s[1:],'r') as f:
                    s=f.read().strip().split('\n') 
            elif s.startswith('#'): #json load
                s=json.loads(s[1:])
            sa2.append(s)
        spec_commands(*sa2)
        callhelp(func)(*sa2)
    else: return func


#@sysargsrun
def spec_commands(speccomm=False,*a):
    if speccomm=='pyc': make_pyc()

def make_pyc(script=sys.argv[0],filename=None): 
    import py_compile
    filename= filename or script.split('.',1)[0]+'_bin.py'
    py_compile.compile(script,filename)
    print(f'Maked pyc: {filename}')



def input_hook(hookname='$>'): 
    i=input(hookname) 
    if i=='^': return#exit hook
    r=None
    r=e2(i)
    if r:print(r)
    return input_hook(hookname)

e2=exec2
g2=globals2#class g(globals2):...
l2=locals2
realglobals=lambda:l2('globals')
realname=lambda:inspect.stack()[2][0].f_globals['__name__'] 
