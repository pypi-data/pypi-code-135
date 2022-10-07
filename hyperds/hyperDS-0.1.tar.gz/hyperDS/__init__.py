import pickle
import os
import pprint
import re
import zipfile
from ast import literal_eval
from abc import ABC
class TargetClass(ABC):
    """
This a abstract class used just for reading the variables, any changes made to this class will be ignored
    """    
    pass
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
#        
#        
def data_type_parser(line):
    new_line = line
    for idx,i in enumerate(line):
        if i.strip() == "":
            new_line = new_line[idx+1:]
        else:
            break 
    return literal_eval(new_line)
class HyperDataStorage():
    def __init__(self,filename=None):
        """

        """
        if filename:
            with open(filename,"rb") as f:
                self.data = f.read().decode("utf-8").split("\n")
        else:
            self.data = []
        self.variables = {}
        self.python_objs = {}
        self.logs = True
    
    def read(self,target_class=None):
        self.custom_parse(self.data,target_class=target_class)
    def read_archive(self,archive_path,target_class=None):
        with zipfile.ZipFile(archive_path) as zipf:
            self.data = zipf.read("main.hds").decode("utf-8").split("\n")
            self.custom_parse(self.data,archive_path,target_class)
    def whole_str(self):
        str_ = ""
        for line in self.data:
            str_ += line
        return str_
    def add_python_obj(self,name,obj):
        self.python_objs[name] = obj
    def new_variable(self,var,value):
        if isinstance(value,str):format = "string"
        elif isinstance(value,int):format = "integer"
        elif isinstance(value,dict):format = "dict"
        elif isinstance(value,list):format = "list"
        elif isinstance(value,tuple):format = "tuple"
        self.variables[var] = [value,format]
    def custom_parse(self, data, archive_path=None, target_class=None):
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
                    else:
                        with zipfile.ZipFile(archive_path) as zipf:
                            obj = pickle.loads(zipf.read(filename))
                    setattr(target_class, name,obj)

    def save(self,filename="test.hds",archive=True,devlogs=True):
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
            f.write("devlogs "+str(devlogs))
            for variable,values in self.variables.items():
                value, format = values
                new_value = ""
                if format == "string":new_value = '"'+value+'"'
                else:new_value = str(value)
                f.write("\n"+variable+" = "+str(new_value))
            for name,obj in self.python_objs.items():
                f.write(f"\n<[{name}]python.object[*]>"+name+".py.obj"+f"</[{name}]python.object[*]>")
                files.append(name+".py.obj")
                with open(name+".py.obj","wb") as objf:
                    objf.write(pickle.dumps(obj)) 

        if archive:          
            with zipfile.ZipFile(filename,"w") as zipf:
                for file in files:
                    zipf.write(file,file)
                zipf.write(filename+".temp","main.hds")
            os.remove(filename+".temp")
            for file in files:
                os.remove(file)