""" ctd data post processing """

import os
import subprocess
from xml.dom import minidom

class Data_post_processing:
    def __init__(self, batch_executable:str = 'No_data', setup_file_name:str = 'No_data', instrument_config_file_name:str = 'No_data', input_directory:str = 'No_data', \
        input_file_name:str = 'No_data', output_directory:str = 'No_data', name_append:str = 'No_data', output_file_name:str = 'No_data') -> None:
        self.__batch_execuable = batch_executable
        self.__input_file_name = input_file_name
        self.__setup_file_name = setup_file_name
        self.__instrument_config_file_name = instrument_config_file_name
        self.__input_directory = input_directory
        self.__output_directory= output_directory
        self.__name_append = name_append
        self.__output_file_name = output_file_name
        
    @property
    def batch_executable(self):
        return self.__batch_execuable

    @batch_executable.setter
    def batch_executable(self, value):
        self.__batch_execuable = value
    @property
    def input_file_name(self):
        return self.__input_file_name
    @input_file_name.setter
    def input_file_name(self, input_file_name):
        self.__input_file_name= input_file_name
    
    @property
    def setup_file_name(self):
        return self.__setup_file_name
    
    @setup_file_name.setter
    def setup_file_name(self, setup_file_name):
        self.__setup_file_name = setup_file_name
    
    @property
    def instrument_config_file_name(self):
        return self.__instrument_config_file_name
    
    @instrument_config_file_name.setter
    def instrument_config_file_name(self, instrument_config_file_name):
        self.__instrument_config_file_name = instrument_config_file_name
    
    @property
    def input_directory(self):
        return self.__input_directory
    @input_directory.setter
    def input_directory(self, input_directory):
        self.__input_directory= input_directory
    
    @property
    def output_directory(self):
        return self.__output_directory
    @output_directory.setter
    def output_directory(self, output_directory):
        self.__output_directory=output_directory
    
    @property
    def name_append(self):
        return self.__name_append

    @name_append.setter
    def name_append(self, name_append):
        self.__name_append= name_append

    @property
    def output_file_name(self):
        return self.__output_file_name
        
    @output_file_name.setter
    def output_file_name(self, output_file_name):
        self.__output_file_name = output_file_name


    def set_file_path(self, arg_file_name, module_list:list):
        for moduleItem, mdName in zip(arg_file_name, module_list):  
            print('processing_modules_cookies'+'/'+moduleItem) 
            with open('processing_modules_cookies'+'/'+moduleItem, 'r', encoding="utf-8") as f:                
                domObj = minidom.parse(f)
                rootTag = domObj.getElementsByTagName(mdName)[0].childNodes                              
                for tag in rootTag:
                    if tag.nodeType == minidom.Node.ELEMENT_NODE:            
                        if tag.nodeType == minidom.Node.ELEMENT_NODE:                        
                            tgName = tag.tagName                       
                            if tgName == 'setupFilePath':
                                self.setup_file_name = tag.firstChild.nodeValue
                                
                            elif tgName in 'instrumentconfigPath':
                                self.instrument_config_file_name = tag.firstChild.nodeValue  
                                                                    
                            elif tgName in 'inputFIles':
                                self.input_file_name = tag.firstChild.nodeValue

                            elif tgName in 'outPutDir':
                                self.output_directory = tag.firstChild.nodeValue
            
                            elif tgName in 'nameAppend':
                                self.name_append = tag.firstChild.nodeValue

                            elif tgName in 'inputDirectory':
                                self.input_directory = tag.firstChild.nodeValue
                            elif tgName in 'outputFileName':
                                self.output_file_name = tag.firstChild.nodeValue
                               
            self.save_setup_file(mdName, self.setup_file_name)

    def check_input_file_or_dir(self, module_name):

        if os.path.isfile(self.__input_directory+'\\'+self.__input_file_name) :
            if (module_name == 'DatCnvW') or (module_name == 'Bottlesum'):
                return '  '+'/i'+self.__input_directory+'\\'+ self.__input_file_name
            #return '  '+'/i'+self.__input_directory+'\\'+ self.__input_file_name

        elif (os.path.isdir(self.__input_directory)) and (self.input_file_name == 'Nil'):
            if (module_name == 'DatCnvW'):
                return ' '+'/i'+self.__input_directory+'/*.hex'
            elif (module_name == 'Bottlesum'):
                return ' '+'/i'+self.__input_directory+'/*.ros'
            elif (module_name == 'Markscan'):
                return  ' '+'/i'+self.__input_directory+'/*.mrk'
            else:
                return '  '+'/i'+self.__input_directory+'/*.cnv'
        else:
             return ' /i'+self.__input_directory+ '\\' +self.__input_file_name
            
    


    def process_data(self, module_list:list, batch_executable):
        with open('files\\'+'arg_file.txt', 'r') as file: 
            for module, lines in zip(module_list, file):
                lines = lines.strip('\n')
                secargs = [batch_executable+'//'+module+'.exe', lines]    
                p =subprocess.Popen(secargs)              
                p.wait()
       


    def create_batch_argument_file(self, model, file_name:str = 'files\\arg_file.txt'):
        ipArg = list()
        ipArg.append('  '+'/p'+self.__setup_file_name)
        ipArg.append(self.add_config_file(module_name=model))
        ipArg.append('  '+'/o'+self.__output_directory)
        ipArg.append('  '+'/a'+self.__name_append)
        ipArg.append('  ' + '/s')
        ipArg.append(self.check_input_file_or_dir(module_name=model))  

        with open(file_name, 'a') as f:
                [f.write(ipa) for ipa in ipArg if (ipa != None)]  
                f.write('\n')


    def batch_argument_file_with_config(self, module_list:list, file_name:str = 'files\\arg_file.txt'):
            ipArg = list()
            for model in module_list:
                ipArg.append('  '+'/p'+self.__setup_file_name)
                ipArg.append(self.add_config_file(module_name=model))
                ipArg.append('  '+'/o'+self.__output_directory)
                ipArg.append('  '+'/a'+self.__name_append)
                ipArg.append('  ' + '/s')
                ipArg.append(self.check_input_file_or_dir(module_name=model))  

            with open(file_name, 'a') as f:
                    [f.write(ipa) for ipa in ipArg if (ipa != None)]  
                    f.write('\n')

    def add_config_file(self, module_name):
        if (module_name == 'DatCnvW') or (module_name == 'Bottlesum'):
            if os.path.isfile(self.__instrument_config_file_name):
                return '  '+'/c'+self.__instrument_config_file_name if self.__instrument_config_file_name != None else '    '
            else:
                return self.__instrument_config_file_name
        else:
            return ''


    def save_setup_file(self, model_name, file_name):
        print(model_name)
        try:
            with open(file_name, 'r') as sf:
                domObj = minidom.parse(sf)
                if (model_name == 'DatCnvW') or (model_name == 'Bottlesum') or (model_name == 'Markscan'):
                    domObj.getElementsByTagName('OutputDir')[0].attributes['value'] = self.output_directory
                    domObj.getElementsByTagName('InputDir')[0].attributes['value'] = self.input_directory
                    domObj.getElementsByTagName('InstrumentPath')[0].attributes['value'] = self.instrument_config_file_name 
                    domObj.getElementsByTagName('ArrayItem')[0].attributes['value'] = self.input_file_name 
                    domObj.getElementsByTagName('NameAppend')[0].attributes['value'] = self.name_append
                    domObj.getElementsByTagName('OutputFile')[0].attributes['value'] = self.input_file_name

                else:
                    domObj.getElementsByTagName('OutputDir')[0].attributes['value'] = self.output_directory
                    domObj.getElementsByTagName('InputDir')[0].attributes['value'] = self.input_directory
                    domObj.getElementsByTagName('ArrayItem')[0].attributes['value'] = self.input_file_name 
                    domObj.getElementsByTagName('NameAppend')[0].attributes['value'] = self.name_append
                    domObj.getElementsByTagName('OutputFile')[0].attributes['value'] = self.input_file_name

                with open(self.__setup_file_name, 'w') as nsf:
                    domObj.writexml(nsf)
            self.create_batch_argument_file(model_name)
        except TypeError:
            pass
       