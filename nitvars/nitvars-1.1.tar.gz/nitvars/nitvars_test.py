from .nitvars import *



def gotestlocals():
    print(f'simple locals=> {locals()}(is empty!) locals2=> {locals2(-1).dict} + ^up level=globals. you can get/set/del, create vars in locals()dict')
    locals2(-1).x=700
    locals2('testlocals2').y=70
    locals2(2).z=7 
z=1
def testlocals2(x=2):
    '''run this for test locals2'''
    y=3
    print(f'locals = {x,y,z}')
    gotestlocals()
    print(f'locals set in other nested function! locals = {locals()} + global z=7.  result= {x+y+z}) #=777')
    



def exec2test(x=50,y=100):
    '''
    print('this code run in exec2');print('and return result of x=x+50 , x+y');
x=x+50
x+y
'''
    result=e2(exec2test.__doc__)
    print(result)

def lambdatestgo(multiline_lambda): 
    return multiline_lambda(10,20) 
def lambda2test():
    '''test multiline lambdas!
    This code run multiline lambda => x,y:e2('x=x+5;x+y') '''
    print(lambda2test.__doc__)
    print(lambdatestgo(lambda x,y:e2('x=x+5;x+y')))


#test comm
def testscaner(x=1,y=2):
    '''tesc doc'''
    print('Test scan other objects andframes. Scan this frame:')
    z=3
    includescaner()

def includescaner():
    s=scaner()
    print(f'''Scan results:
    name: {s.name}
    all: {s.all('frame,globals,stack')}''')



def tracertest():
    t=tracer()
    print('TEST TRACE DECORATOR')
    @t.trace
    def decfunc(xx,x=120):
        return xx+x
    decfunc(80)
    print(f'Trace results=>>calls=>{t.calls} returns=>{t.returns}')
    def testfunc(xx,x=170):
        return xx+x
    print('TEST TRACE DECORATOR 2')     
    t.trace(testfunc)(80) 
    print(f'Trace results=>>calls=>{t.calls} returns=>{t.returns}')
    print('TEST TRACE WITH')
    with tracer() as tt:
        testfunc(270)
        testfunc(370)
    print(f'Trace results=>>calls=>{tt.calls} returns=>{tt.returns}')
    print('TEST TRACE GLOBAL TRACE ON')
    t.on
    testfunc(470)
    testfunc(570)
    t.off
    print(f'Trace results=>>calls=>{tt.calls} returns=>{tt.returns}')
    print('TEST TRACE str combo returns Demo version of use tracer')
    link=lambda href,title: f'<a href="{href}">{title}</a>\n'
    with tracer(maxlevel=1).silent as html:
        link('http://link1.com','Link1')
        link('http://google.com','Google') 
    print(f'<div id="linksblock">\n{"".join(html.returns)}</div>')


def callhelptest():
    '''test callhelp decorator run myfunc(x,y,z=7) as myfunc() . x and y not defined'''
    print(callhelptest.__doc__)
    print(callhelp.__doc__)
    @callhelp
    def myfunc(x,y,z=7):
        return int(x)+int(y)+z
    print(myfunc())
    
testvar='TESTVAR Finded.' 
tests=[testglobals2,testlocals2,exec2test,lambda2test,testscaner,tracertest,callhelptest]


 
@sysargsrun
def main(test=None):
    test=test or input(f'Select test {[f"{i}={t.__name__}" for i,t in enumerate(tests)]+["all=all tests",]}:')
    xtests=tests if test in ['','all'] else [tests[int(test)],]
    
    for t in xtests:
        print(f'\n######## {t.__name__}')
        t()
        if input('Press Enter to continue..q=exit')=='q':break