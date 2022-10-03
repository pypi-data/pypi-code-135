""" trial"""
from ctypes import Union
import json
import re
import os
import csv
from abc import ABC, abstractmethod
from typing import Callable, Generator


class SourceFileInfo(ABC):
    """abstarct class"""
    @abstractmethod
    def check_Isfile(self):
        """check weather the path is folder or file """
        return bool

    def get_file_names(self):
        """read the file and return textio"""

class MetaData(ABC):
    """abstarct class"""
    @abstractmethod
    def get_index_from_file(cls):
        """parse the idex from the file"""
    @abstractmethod
    def add_flags():
        """to add quality flags"""

class DataWriter(ABC):
    """abstarct class"""
    @abstractmethod
    def attribute_write(self):
        """write index to the output file"""
    
    def data_writer(self):
        """write data to the output file"""

class CsvWriter(DataWriter):
    """csv writer class"""
    def __init__(self, converted_data_folder:str):
        self.converted_data_folder = converted_data_folder

    def attribute_write(self, index:list, f:str):
        try:
            if os.path.isfile(self.converted_data_folder+r'/'+f.split(r'/')[-1].split('.')[0]+'.csv'):
                os.remove(self.converted_data_folder+r'/'+f.split(r'/')[-1].split('.')[0]+'.csv')
            with open(self.converted_data_folder+r'/'+f.split(r'/')[-1].split('.')[0]+'.csv', 'a',  encoding="utf-8" , newline="") as inx:
                write = csv.writer(inx, delimiter=',')
                write.writerow(index)
            return True
        except FileNotFoundError:
            return False
        except PermissionError:
            return False
           
    def data_writer(self, string_check, f, Qflag = None, addQflag = None):
           
            with open(f, 'r',  encoding="utf-8") as source_file:
                if os.path.exists(self.converted_data_folder+'/'+f.split('/')[-1].split('.')[0]+'.csv'):
                    with open(self.converted_data_folder+'/'+f.split('/')[-1].split('.')[0]+'.csv', 'a' , newline="") as target_file:
                        write = csv.writer(target_file)
                        for line in source_file:
                            if( string_check.search(line) == None): 
                                data_line = line.split(r"\t")[0].strip()
                                data_line = data_line.split()
                                if addQflag:
                                    write.writerow(data_line+Qflag)
                                else:
                                    write.writerow(data_line)
                                
                            #yield progress_bar_value       
                   
                    return True
                else:
                    pass

class TextWriter(DataWriter):
    """Text writer class"""
    def __init__(self, converted_data_folder:str):
        self.converted_data_folder = converted_data_folder

    def attribute_write(self, index:list, f:str)->None:
        try:
            if os.path.isfile(self.converted_data_folder+r'/'+f.split(r'/')[-1].split('.')[0]+'.txt'):
                os.remove(self.converted_data_folder+r'/'+f.split(r'/')[-1].split('.')[0]+'.txt')
            with open(self.converted_data_folder+r'/'+f.split(r'/')[-1].split('.')[0]+'.txt', 'a') as inx:
                [inx.write(ele +'\t') for ele in index]
                inx.write('\n')
            return True
        except FileNotFoundError:
           
            return False
    def data_writer(self, string_check, f, Qflag = None, addQflag = None):
           
            with open(f, 'r',  encoding="utf-8", newline="") as source_file:
                if os.path.exists(self.converted_data_folder+'/'+f.split('/')[-1].split('.')[0]+'.txt'):
                    with open(self.converted_data_folder+'/'+f.split('/')[-1].split('.')[0]+'.txt', 'a') as target_file:
                        for line in source_file:
                            if( string_check.search(line) == None): 
                                data_line = line.split(r"\t")[0].strip()
                                data_line = data_line.split()
                                if addQflag:
                                    [data_line.append(q) for q in Qflag]
                                    [target_file.write(data+'\t') for data in data_line]
                                    target_file.write('\n')
                                else:
                                    [target_file.write(data+'\t') for data in data_line]
                                    target_file.write('\n')
                                
                            #yield progress_bar_value       
                   
                    return True
                else:
                    pass

class DataBaseType(ABC):
    """abstarct class"""
    @abstractmethod
    def get_database_type():
        """returns the database name"""

class PangaeaTypeDataBase(DataBaseType):
    """abstarct class"""
    @staticmethod
    def get_database_type():
        return 'pangaea'

class DefaultDataBaseType(DataBaseType):
    """abstarct class"""
    @staticmethod
    def get_database_type():
        return 'default'

class DatabaseFormat(ABC):
    """abstarct class"""
    @abstractmethod
    def get_attribute(self):
        """return a dict with pangaea style attribute"""
    
class PangaeaColumnAttribute(DatabaseFormat):
    """pangae"""
    def __init__(self):
        self.pangaea_attribute_dict = {"t190C":[{"pangaea" : "Temperature, water [°C]//*Sensor 2"}],\
            "prDM":[{"pangaea": "Pressure, water [dbar]"}],\
                "c0mS/cm":[{"pangaea": "Conductivity [mS/cm]//*Sensor 1"}],\
                    "c1mS/cm":[{"pangaea": "Conductivity [mS/cm]//*Sensor 2"}],\
                        "t090C":[{"pangaea":"Temperature, water [°C]//*Sensor 1"}],\
                            "sal00":[{"pangaea":"Salinity [PSU]//*Sensor 1"}],\
                                "sal11":[{"pangaea":"Salinity [PSU]//*Sensor 2"}],\
                                    "sbeox1ML/L":[{"pangaea":"Oxygen [ml/l]//*Sensor 2"}],\
                                        "sbeox0Mm/Kg":[{"pangaea":"Oxygen [umol/kg]//*Sensor 1"}],\
                                            "oxsatML/L":[{"pangaea":"Oxygen saturation, Weiss [ml/l]"}],\
                                                "par":[{"pangaea":"Radiation, photosynthetically active []"}],\
                                                    "spar":[{"pangaea":"Radiation, photosynthetically active, surface [µE/m**2/s]"}],\
                                                        "potemp090C":[{"pangaea":"Temperature, water, potential [°C]"}],\
                                                            "sigma-é00":[{"pangaea":"Density, water [kg/m**3]"}],\
                                                                "altM":[{"pangaea":"Altimeter [m]"}],\
                                                                    "svCM":[{"pangaea":"Sound velocity in water [m/s]//*Chen-Millero"}],\
                                                                        "flECO-AFL":[{"pangaea":"Fluorescence [mg/m**3]"}], \
                                                                            "turbWETntu0":[{"pangaea":"Turbidity [NTU]"}], \
                                                                                "depSM":[{"pangaea":"Depth, water [m]"}],"nbf":[{"pangaea":"Bottle Fired"}]}
        try:
            with open ('seasave_data_conversion\\index.json', 'r', encoding="utf-8") as index:
                self.pangaea_attribute_dict =  json.load(index)
        except:
            pass
    def get_attribute(self):
        return self.pangaea_attribute_dict


class DefaultColumnAttribute(DatabaseFormat):
    """abstarct class"""
    @staticmethod
    def get_attribute():
        return 'default'

class SingleOrBatch(SourceFileInfo):
    """To check fiels or dir"""
    def __init__(self, path:str):
        self.path = path
        
    def check_Isfile(self):
        if type(self.path) == list:
            return True
        elif  os.path.isdir(self.path):
            return  False
           
    def get_file_names(self, isfile:bool)->list:

        # """method to get pointer of the file, file name and the absolute file path
        # argument:
        #         isfile:bool
        # return: tuple """
        if isfile:
            return self.path
        elif not isfile:
            file_names = [self.path+"/"+ x for x in os.listdir(self.path) if x.endswith('.cnv')]
            return file_names



class ExtractMetaData(MetaData):
    """ To extrac metat data"""
    string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    @classmethod
    def get_index_from_file(cls, column_attributes:Callable[[], dict], file_names:str, data_base_type:str)->list:
        new_attribute = list()
        column_attributes = column_attributes()
        with open(file_names, 'r') as file:
            for line in file:
                if cls.string_check.search(line):
                    if 'name' in line:               
                        if data_base_type == 'default':
                            line =line.split('=')[1].split(':')[1].strip()
                            new_attribute.append(line)
                        else:
                            line =line.split('=')[1].split(':')[0].strip()
                            if line in column_attributes:
                                new_attribute.append(column_attributes[line][0][data_base_type])
                            else:
                                new_attribute.append(line)                    
        return new_attribute
                 
            

    @staticmethod
    def add_flags(column_attributes:list, quality_flags:list):
        return [column_attributes.append(flag) for flag in quality_flags][0]