import speeddb
from code import InteractiveConsole
from os.path import abspath, dirname, join, isdir
from os import listdir

def read(rel_path):
   here = abspath(dirname(__file__))
   with open(join(here, rel_path), 'r') as fp:
      return fp.read()

def get_version(rel_path):
   for line in read(rel_path).splitlines():
      if line.startswith('__version__'):
         delim = '"' if '"' in line else "'"
         return line.split(delim)[1]

def load_databases(path:str="db"):
   if not isdir(path):
      return []

   clean_files = lambda e: e.endswith(".sdb")
   files = list(filter(clean_files, listdir(path)))

   result = {}
   for db in files:
      db_path = join(path, db)
      result[db.replace(".sdb", "")] = speeddb.connect(db_path)

   return result

def run_shell(dbs_path:dict):
   version = get_version("__init__.py")
   dbs = load_databases(dbs_path)
   variables = globals()

   del variables["get_version"]
   del variables["read"]
   variables["dbs"] = dbs
   variables.update(dbs)

   banner = f'''SpeedDB Shell {version}
Type "dbs" to list your databases'''

   console = InteractiveConsole(variables)
   console.interact(banner, "")