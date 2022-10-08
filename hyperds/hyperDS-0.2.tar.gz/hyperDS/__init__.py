import io
import pickle
import os
import pprint
import re
import zipfile
from ast import literal_eval
from abc import ABC

class TargetClass(ABC):   
    def __init__(self,cls):
        self.cls = cls

def get_var_format(line):

    if re.match(r'\w*\s*?=\s*?".*"\s*?',line):
        return "string"
    elif re.match(r'\w*\s*?=\s*?\{\s*?',line):
        return "dict"    
    elif re.match(r'\w*\s*?=\s*?\[\s*?',line):
        return "list"      
    elif re.match(r'\w*\s*?=\s*?[0-9]*[\+\-\*\/\/][0-9]*\s*?',line):
        return "mathematical_expression"
    elif re.match(r'\w*\s*=\s*\d*\s*',line):
        return "integer"    
    elif re.match(r'\w*\s*?=\s*?\(\s*?',line):
        return "tuple"            
    elif re.match(r'\w*\s*?=\s*?\w*\s*?',line):
        return "variable"
    
def log(variable,format,value,expression=None):
    log = f"""
Parsing variable: {variable}          
type: {format}
value: {value}"""
    if expression:log+=f'\nexpression: {expression}'    
    print(log)
    
def parse_variable(parser,line,lines,format,target_class):
    variable = line.split("=")[0].strip()
    if format == "string":
        value = line.split("=")[1].split('"')[1].replace('"',"")
        if parser.logs:log(variable,format,value)
    elif format == "mathematical_expression":
        value = eval(line.split("=")[1])
        if parser.logs:log(variable,format,value,line.split("=")[1])      
    elif format == "dict":
        lines_dict_present = line.split("=")[1]
        value = data_type_parser(lines_dict_present)
        if parser.logs:log(variable,format,value)       
    elif format == 'list':
        value = data_type_parser(line.split("=")[1])   
        if parser.logs:log(variable,format,value)     
    elif format == "tuple":
        value = data_type_parser(line.split("=")[1])   
        if parser.logs:log(variable,format,value)   
    elif format == "integer":
        value = int(line.split("=")[1])
        if parser.logs:log(variable,format,value)  
    elif format == "variable":
        value = parser.variables[line.split("=")[1].strip()]
        if parser.logs:log(variable,format,value)   
    parser.variables[variable] = [value,format]
    if target_class:setattr(target_class,variable,value)         

def data_type_parser(line):
    new_line = line
    for idx,i in enumerate(line):
        if i.strip() == "":
            new_line = new_line[idx+1:]
        else:
            break 
    return literal_eval(new_line)


class HyperDataStorage():
    def __init__(self,filename=None,file_read_errors="ignore"):
        """
*file_read_errors* = ignore/ True
        """
        if filename:
            try:
                with open(filename,"rb") as f:
                    self.data = f.read().decode("utf-8").split("\n")
            except Exception as e:
                if file_read_errors == True:raise Exception(e)
                else:self.data = []
        else:
            self.data = []
        self.variables = {}
        self.python_objs = {}
        self.read_python_objs = {}
        self.logs = True
        self.file_read_errors = file_read_errors
    def read(self,target_class=None):
        self.custom_parse(self.data,target_class=target_class)
    def new_target_class(self):
        return _new_target_class()
    def read_archive(self,archive_path,target_class=None):
            with zipfile.ZipFile(archive_path) as zipf:
                self.data = zipf.read("main.hds").decode("utf-8").split("\n")

                self.custom_parse(self.data,archive_path,target_class)

    def whole_str(self):
        str_ = ""
        for line in self.data:
            str_ += line
        return str_
    def add_python_obj(self,name,obj,mode="w"):
        """
name -> the name which object should be saves\n
value -> object to be saves\n
mode -> mode is a optional string, "w" means create/overwrite python object where "x" means create python object, does nothing if exists
        """    
        if mode=="x":    
            if name not in self.python_objs.keys():
                self.python_objs[name] = obj
        else:
            self.python_objs[name] = obj            
    def get_python_obj(self,name):
        if name in self.read_python_objs.keys():
            return self.read_python_objs[name]
    def delete_variables(self):
        self.variables = {}
    def set_variable(self,var,value,mode="w",target_class=None):
        """
var -> variable name\n
value -> variable value\n
mode -> mode is a optional string, "w" means create/overwrite variable where "x" means create variable and does nothing if exists
        """
        if isinstance(value,str):format = "string"
        elif isinstance(value,int):format = "integer"
        elif isinstance(value,dict):format = "dict"
        elif isinstance(value,list):format = "list"
        elif isinstance(value,tuple):format = "tuple"
        if mode=="x":
            if var not in list(self.variables.keys()):
                self.variables[var] = [value,format]
        else:
            self.variables[var] = [value,format]
        return self.get_variable(var)
    def update_target_class(self,target_class):
        """
Overwrites the variables and python_objects in HyperDataStorage to the target_class
        """
        for var,value in self.variables.items():
            value, format = value
            setattr(target_class,var,value)
        for name,obj in self.read_python_objs.items():
            setattr(target_class,name,obj)
    def get_variable(self,var):
        var = self.variables.get(var)
        if var:return var[0]
        else:return None
    def remove_variable(self,var):
        try:
            self.variables.remove(var)
        except:pass        
    def custom_parse(self, data, archive_path=None,target_class=None):
        self.outputs = []  
        for line in data:
            if line.strip() != "" and not line.startswith("#"):
                if line.strip().startswith("devlogs"):
                    if line.split("devlogs ")[1].strip().lower() == "true":self.logs = True
                    else:self.logs = False
                elif re.match(r"[a-z]+\s*\=\s*[\{\[\(]?[a-z]*[0-9]*\s*",line):
                    self.outputs.append(parse_variable(self,line,data,get_var_format(line),target_class))                    
                elif re.match(r'\s*?\<\[\w*\]python.object\[\*\]\>\s*?\w*?.*?\w*?.*\s*?',line):
                    span = re.search(r'\<\[\w*\]',line).span()
                    name = line[span[0]+2:span[1]-1]
                    filename = line.split(f"<[{name}]python.object[*]>")[1].split(f"</[{name}]python.object[*]>")[0]
                    if not archive_path:
                        with open(filename,"rb") as f:
                            obj = pickle.loads(f.read())
                            self.read_python_objs[name] = obj
                            if target_class:setattr(target_class,name,obj)                            
                    else:
                        zipf = zipfile.ZipFile(archive_path)
                        data = zipf.read(filename)
                        obj = pickle.loads(data)
                        self.read_python_objs[name] = obj
                        if target_class:setattr(target_class,name,obj)
                        zipf.close()
    def save(self,filename="test.hds",archive=True,target_class=None,devlogs=True):
        files = []
        try:
            if not archive:
                if os.path.dirname(filename):os.makedirs(os.path.dirname(filename))
        except:pass
        if not archive:
            if os.path.dirname(filename) and os.path.dirname(filename).strip()!="":folder = os.path.dirname(filename)
            else:folder = ""
        else:folder = ""
        with open(filename+".temp" if archive else os.path.join(folder,filename),"w+") as f:
            f.write("""# File created by HyperDataStorage\n# Editing files manually can create errors!\n# Formating the file can also create errors!\n# Edit files manually at your own risk!""")
            f.write("\n\ndevlogs "+str(devlogs))
            for variable,values in self.variables.items():
                value, format = values
                if target_class:
                    if hasattr(target_class,variable):
                        value = getattr(target_class,variable)
                new_value = ""
                if format == "string":new_value = '"'+value+'"'
                else:new_value = str(value)
                f.write("\n"+variable+" = "+str(new_value))
            for name,obj in self.python_objs.items():
                f.write(f"\n<[{name}]python.object[*]>"+name+".py.obj"+f"</[{name}]python.object[*]>")
                files.append(name+".py.obj")
                with open(name+".py.obj","wb") as objf:
                    pickle.dump(obj,objf,-1)

        if archive:          
            with zipfile.ZipFile(filename,"w") as zipf:
                for file in files:
                    zipf.write(file,file)
                zipf.write(filename+".temp","main.hds")
            os.remove(filename+".temp")
            for file in files:
                os.remove(file)

def _new_target_class() -> object:
    class Data(TargetClass):
        def __init__(self):
            pass    
    return Data()

if __name__ == "__main__":
    # Creating HyperDS instance
    hds = HyperDataStorage("test.hds")
    # Trying to read archive 
    # ignores every errors while reading the file eg. file does not exists because of parameter file_read_errors: str = "ignore" while creating instance     
    hds.read_archive("test.hds")
    # creating a target class which could be used to read variables and python objects
    data = hds.new_target_class()
    # creating empty dict variable if variable "persons" does not exists  
    persons = hds.set_variable("persons",{},"x")
    # getting user input
    cmd = input(">> ")
    try:
        if cmd == "add":
            while True:
                name = input("Name: ")
                age = input("Age: ")
                # updating "persons" dict
                persons.update({name:age})
                # updating "persons" variable in target_class (variable data)
                hds.update_target_class(data)
        elif cmd == "get":
            # iterating through "persons" dict and printing their values
            for person,age in hds.get_variable("persons").items():
                print(person+" >> "+str(age))
    except KeyboardInterrupt:
        # Save all data as archive test.hds which may contain py.obj files if any python objects are added
        hds.save(devlogs=False)    