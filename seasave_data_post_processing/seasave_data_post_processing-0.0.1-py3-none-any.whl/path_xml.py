from xml.dom import minidom
import os

class Create_path_xml:
    def __init__(self):
        try:
            os.mkdir('processing_modules_cookies')
        except FileExistsError:
            pass

    def ModuleTags(self, tag_name:list, data_processing_modules:list, root_name:str, file_path = 'No_data')->None:
        root = minidom.Document()
        xml  = root.createElement(root_name)
        root.appendChild(xml)
        for i in tag_name:
            FirstChild = root.createElement(i)  
            xml.appendChild(FirstChild)
            if i == 'Raw_data_processing':
                for module in data_processing_modules:
                    child_module = root.createElement(module)
                    if module == 'DatCnvW':
                        FirstChild.appendChild(self.create_path_tag_with_ros(root, child_module))
                    elif module == 'BottleSumW':
                        FirstChild.appendChild(self.create_path_tagsA(root, child_module))
                    elif module == 'MarkScanW':
                        FirstChild.appendChild(self.create_path_tagsB(root, child_module))

            elif i == 'data_processing':               
                for module in data_processing_modules:
                    child_module = root.createElement(module)
                    FirstChild.appendChild(child_module)
                    if module == 'Derive':
                        child_module = self.create_path_tagsA(root, child_module)
                    else:
                        child_module = self.create_path_tagsB(root, child_module)
                    FirstChild.appendChild(child_module)
            elif i == 'FileManipulation':
                pass
            elif i == 'Data Plotting':
                pass
            xml_str = root.toprettyxml(indent='\t')
        with open(file_path, 'w') as file:
            file.write(str(xml_str))

    def create_path_tag_with_ros(self, root, child_module):
        paths = ['sigleOrMultipleFile','setupFilePath', 'instrumentconfigPath', 'inputDirectory', 'inputFIles', 'outPutDir', 'nameAppend', 'outputFileName', 'ros']
        pathtags = [root.createElement(i) for i in paths]
        [pathtag.appendChild(root.createTextNode('Nil'))for pathtag in pathtags]
        [child_module.appendChild(pathtags) for pathtags in pathtags]
        return child_module


    def create_path_tagsA(self, root, child_module):
        paths = ['sigleOrMultipleFile','setupFilePath', 'instrumentconfigPath', 'inputDirectory', 'inputFIles', 'outPutDir', 'nameAppend', 'outputFileName']
        pathtags = [root.createElement(i) for i in paths]
        [pathtag.appendChild(root.createTextNode('Nil'))for pathtag in pathtags]
        [child_module.appendChild(pathtags) for pathtags in pathtags]
        return child_module

    def create_path_tagsB(self, root, child_module):
        paths = ['sigleOrMultipleFile', 'setupFilePath', 'inputDirectory', 'inputFIles', 'outPutDir', 'nameAppend', 'outputFileName']
        pathtags = [root.createElement(i) for i in paths]
        [pathtag.appendChild(root.createTextNode('Nil'))for pathtag in pathtags]
        [child_module.appendChild(pathtags) for pathtags in pathtags]
        return child_module

    def save_path(self, module_name:str, file_path:str, path_tag:str, value:str):            
        try:
            with open(file_path, 'r', encoding="utf-8")as f:
                domObj = minidom.parse(f)
                dataConversion = domObj.getElementsByTagName(module_name)[0]   
                value = 'No_path' if value == ''   else value   
                dataConversion.getElementsByTagName(path_tag)[0].childNodes[0].nodeValue = value
            with open(file_path, 'w', encoding="utf-8")as f:
                domObj.writexml(f)
        except FileNotFoundError:
            print('There are no file named dataPostProcessing.xml is found')