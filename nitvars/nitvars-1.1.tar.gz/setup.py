# -*- coding: utf-8 -*-
from setuptools import setup


desc=r'''
# nitvars
Python variables v2 package
Python version 3 or later


add new version of globals, locals
globals fix
add tracer, scaner frame info
add exec v2 = multiline exec and return result
add multiline  lambda  lambda x,y:e2('x=x+1;print(x);x+y')

for see and test all functions run nitvars_test.py  or "py -m nitvars" or
from nitvars.nitvars_test import * 
main()



Select test ['0=testglobals2', '1=testlocals2', '2=exec2test', '3=lambda2test', '4=testscaner', '5=tracertest', '6=callhelptest', 'all=all tests']:

######## testglobals2
Now get testvar. testvar in globals!
var "testvar" in simple globals()=NOT FOUND!
Not found "testvar" in levels {'nitvars.nitvars', '__main__'}
var "testvar" in globals2()=None
Not found "testvar" in levels {'module'}
var "testvar" in realglobals()=None
testvar in [level:id]: None
Why?  globals() find globals only in this script(in nitvars.py..)

Now set testvar with "global testvar"
var "testvar" in simple globals()=SET OK!
var "testvar" in globals2()=SET OK!
Not found "testvar" in levels {'module'}
var "testvar" in realglobals()=None
testvar in [level:id]: {'nitvars.nitvars': 2538507971952}
Why?  global x set globals only in this script(in nitvars.py..)

Now set testvar2 with "globals()[testvar]"
var "testvar" in simple globals()=SET OK!2
var "testvar" in globals2()=SET OK!2
Not found "testvar" in levels {'module'}
var "testvar" in realglobals()=None
testvar in [level:id]: {'nitvars.nitvars': 2538507972016}
Why?  globals() set globals only in this script(in nitvars.py..)

Now set testvar2 with nitvars "globals2()[testvar]"
var "testvar" in simple globals()=SET OK!3
var "testvar" in globals2()=SET OK!3
var "testvar" in realglobals()=SET OK!3
testvar in [level:id]: {'nitvars.nitvars': 2538507972144, '__main__': 2538507972144}
Why?  globals2() is real globals, globals() is ...
Press Enter to continue..q=exit

######## testlocals2
locals = (2, 3, 1)
simple locals=> {}(is empty!) locals2=> {'x': 2, 'y': 3} + ^up level=globals. you can get/set/del, create vars in locals()dict       
locals set in other nested function! locals = {'x': 700, 'y': 70} + global z=7.  result= 771) #=777
Press Enter to continue..q=exit

######## exec2test
this code run in exec2
and return result of x=x+50 , x+y
200
Press Enter to continue..q=exit

######## lambda2test
test multiline lambdas!
    This code run multiline lambda => x,y:e2('x=x+5;x+y')
35
Press Enter to continue..q=exit

######## testscaner
Test scan other objects andframes. Scan this frame:
Scan results:
    name: testscaner
    all: filename: C:\Users\nikos\Desktop\py\nitvars\nitvars_test.py
line: 44
name: testscaner
locals: {'x': 1, 'y': 2, 'z': 3}
module: nitvars.nitvars_test
code: def testscaner(x=1,y=2):
     
    print('Test scan other objects andframes. Scan this frame:')
    z=3
    includescaner()

comment: #test comm

args_str: (x=1,y=2)
path: nitvars.nitvars_test._run_code.<module>.main.testscaner
object: None
signature: line 44[level:3]: nitvars.nitvars_test._run_code.<module>.main.testscaner(x=1,y=2) {'x': 1, 'y': 2, 'z': 3}
Press Enter to continue..q=exit

######## tracertest
TEST TRACE DECORATOR
                                        >>>CALL: line 57[level:5]: nitvars.nitvars_test._run_code.<module>.main.tracertest.trace_func.decfunc(xx,x=120) {'xx': 80, 'x': 120}
                                        ### RETURN: line 59[level:5]: nitvars.nitvars_test._run_code.<module>.main.tracertest.trace_func.decfunc(xx,x=120) {'xx': 80, 'x': 120} ==> 200 [<class 'int'>]
Trace results=>>calls=>[line 57[level:5]: nitvars.nitvars_test._run_code.<module>.main.tracertest.trace_func.decfunc(xx,x=120) {'xx': 80, 'x': 120}] returns=>[200]
TEST TRACE DECORATOR 2
                                        >>>CALL: line 62[level:5]: nitvars.nitvars_test._run_code.<module>.main.tracertest.trace_func.testfunc(xx,x=170) {'xx': 80, 'x': 170}
                                        ### RETURN: line 63[level:5]: nitvars.nitvars_test._run_code.<module>.main.tracertest.trace_func.testfunc(xx,x=170) {'xx': 80, 'x': 170} ==> 250 [<class 'int'>]
Trace results=>>calls=>[line 62[level:5]: nitvars.nitvars_test._run_code.<module>.main.tracertest.trace_func.testfunc(xx,x=170) {'xx': 80, 'x': 170}] returns=>[250]
TEST TRACE WITH
                                >>>CALL: line 62[level:4]: nitvars.nitvars_test._run_code.<module>.main.tracertest.testfunc(xx,x=170) {'xx': 270, 'x': 170}
                                ### RETURN: line 63[level:4]: nitvars.nitvars_test._run_code.<module>.main.tracertest.testfunc(xx,x=170) {'xx': 270, 'x': 170} ==> 440 [<class 'int'>]
                                >>>CALL: line 62[level:4]: nitvars.nitvars_test._run_code.<module>.main.tracertest.testfunc(xx,x=170) {'xx': 370, 'x': 170}
                                ### RETURN: line 63[level:4]: nitvars.nitvars_test._run_code.<module>.main.tracertest.testfunc(xx,x=170) {'xx': 370, 'x': 170} ==> 540 [<class 'int'>]
Trace results=>>calls=>[line 62[level:4]: nitvars.nitvars_test._run_code.<module>.main.tracertest.testfunc(xx,x=170) {'xx': 270, 'x': 170}, line 62[level:4]: nitvars.nitvars_test._run_code.<module>.main.tracertest.testfunc(xx,x=170) {'xx': 370, 'x': 170}] returns=>[440, 540]
TEST TRACE GLOBAL TRACE ON
                                >>>CALL: line 62[level:4]: nitvars.nitvars_test._run_code.<module>.main.tracertest.testfunc(xx,x=170) {'xx': 470, 'x': 170}
                                ### RETURN: line 63[level:4]: nitvars.nitvars_test._run_code.<module>.main.tracertest.testfunc(xx,x=170) {'xx': 470, 'x': 170} ==> 640 [<class 'int'>]
                                >>>CALL: line 62[level:4]: nitvars.nitvars_test._run_code.<module>.main.tracertest.testfunc(xx,x=170) {'xx': 570, 'x': 170}
                                ### RETURN: line 63[level:4]: nitvars.nitvars_test._run_code.<module>.main.tracertest.testfunc(xx,x=170) {'xx': 570, 'x': 170} ==> 740 [<class 'int'>]
Trace results=>>calls=>[line 62[level:4]: nitvars.nitvars_test._run_code.<module>.main.tracertest.testfunc(xx,x=170) {'xx': 270, 'x': 170}, line 62[level:4]: nitvars.nitvars_test._run_code.<module>.main.tracertest.testfunc(xx,x=170) {'xx': 370, 'x': 170}] returns=>[440, 540]
TEST TRACE str combo returns Demo version of use tracer
<div id="linksblock">
</div>
Press Enter to continue..q=exit

######## callhelptest
test callhelp decorator run myfunc(x,y,z=7) as myfunc() . x and y not defined
help call func if args not defined
Запуск функции myfunc(x, y, z=7)
Введите параметр "x"("#q" для отмены запуска)111
Введите параметр "y"("#q" для отмены запуска)222
340
Press Enter to continue..q=exit

'''
 
setup(name='nitvars',#long_description=desc,
      version='1.1',
      description='new versions of globals,locals,tracer and other functions..',
      packages=['nitvars'],
      author_email='createsoft@mail.ru',
      zip_safe=False ,#new
      long_description=desc,
    long_description_content_type="text/plain",
    url="https://github.com/NITSoftware/nitvars", 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5')
