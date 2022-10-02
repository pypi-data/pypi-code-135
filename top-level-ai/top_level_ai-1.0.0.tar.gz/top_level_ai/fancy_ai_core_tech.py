# Fancy AI core tech
# Welcome to Zetaspace :)
# 2202/10/03 03:1B

# The core secret of our ai...
# Just pretend you didn't see it.
coreen = 'hey you me to go and also what is this'.split()
modeen = lambda x:x.capitalize()+'.'
corezhs = '你好我听不懂在说啥吗'
modezhs = lambda x:x.replace(' ','')+'。'
corezht = '你好我聽不懂在説啥嗎'
modezht = lambda x:x.replace(' ','')+'。'
lang = ['en', 'zhs', 'zht']

class SUPER_DUPER_AI_BLUEPRINT:
 '''AI.'''
 lang = lang
 def __call__(*args1, **args2):
  # Guess what? the machine it-SELF is also here.
  if len(args1) > 1:
   input = args1[1]  # Oh you wont need this, right?
   if isinstance(input, int):
    input = input  # Yes it is.
   else:
    input = int(__import__('hashlib').md5(str(input).encode()).hexdigest(), 16)
  else:
   try:
    input = __import__('random').randint(0,9999)
   except:
    input = 42  # Eternal truth
  seed = map(int, ('0000' + str(input))[-4:])
  lagn = str(args2.get('lang', 'en'))
  lagn = lagn if lagn in lang else 'en'
  core = lagn == 'en'  and coreen or\
         lagn == 'zhs'  and corezhs or\
         lagn == 'zht'   and corezht
  mode = lagn == 'en'     and modeen or\
         lagn == 'zhs'     and modezhs or\
         lagn == 'zht'      and modezht
  return mode(' '.join(core[_]for _ in seed))

 def __str__(*args1, **args2):
  return '<<<AAAArtificial Intelligenceeee>>>'
 def __repr__(*args1, **args2):
  print('[beep]')
  return '__import__(\'top-level-ai\').AI'
  # Always gets a lifetime warranty
  
AI = SUPER_DUPER_AI_BLUEPRINT()
del SUPER_DUPER_AI_BLUEPRINT
# It's so powerful that u'll lose ctrl of it!!
# So we only left u a prototype machine.
# It's enough for <<normal>> purposes.
# And our blueprint will be destroyed immediately!
# That'sssit meow.
