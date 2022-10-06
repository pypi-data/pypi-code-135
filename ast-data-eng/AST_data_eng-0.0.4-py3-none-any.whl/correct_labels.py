#################################################################################################################
####################################     Correct object names in xmls      ######################################
#################################################################################################################
def reclassify_narrow_closed_roof_and_closed_roof_tanks(xml_path):
    """ Reclassify Narrow Closed Roof and Closed Roof Tanks
    """
    #load each xml
    class_ob = []
    tree = et.parse(xml_path)
    root = tree.getroot()
    for obj in root.iter('object'):
        name = obj.find("name").text 
        xmlbox = obj.find('bndbox') #get the bboxes
        obj_xmin = xmlbox.find('xmin').text
        obj_ymin = xmlbox.find('ymin').text
        obj_xmax = xmlbox.find('xmax').text
        obj_ymax = xmlbox.find('ymax').text
        width = int(obj_xmax) - int(obj_xmin)
        height = int(obj_ymax) - int(obj_ymin)
        if (int(obj.find('difficult').text) == 0) and (int(obj.find('truncated').text) == 0): 
            #if a closed roof tank is less than or equal to the narrow closed roof tank threshold than reclassify as  narrow closed roof tank
            if (name == "closed_roof_tank") and (width <= 15) and (height <= 15): 
                name = "narrow_closed_roof_tank"
            #if a narrow closed roof tank is greater than the closed roof tank threshold than reclassify as closed roof tank
            if (name == "narrow_closed_roof_tank") and (width > 15) and (height > 15):
                name = "closed_roof_tank"
    
    tree.write(os.path.join(xml_path))
    
def correct_inconsistent_labels_xml(xml_dir):
    #Create a list of the possible names that each category may take 
    correctly_formatted_object = ["closed_roof_tank","narrow_closed_roof_tank",
                                  "external_floating_roof_tank","sedimentation_tank",
                                  "water_tower","undefined_object","spherical_tank"] 
    object_dict = {"closed_roof_tank": "closed_roof_tank",
                   "closed_roof_tank ": "closed_roof_tank",
                   "closed roof tank": "closed_roof_tank",
                   "narrow_closed_roof_tank": "narrow_closed_roof_tank",
                   "external_floating_roof_tank": "external_floating_roof_tank",
                   "external floating roof tank": "external_floating_roof_tank",
                   'external_floating_roof_tank ': "external_floating_roof_tank",
                   'external_closed_roof_tank': "external_floating_roof_tank",
                   "water_treatment_tank": "sedimentation_tank",
                   'water_treatment_tank ': "sedimentation_tank",
                   "water_treatment_plant": "sedimentation_tank",
                   "water_treatment_facility": "sedimentation_tank",
                   "water_tower": "water_tower",
                   "water_tower ": "water_tower",
                   'water_towe': "water_tower",
                   "spherical_tank":"spherical_tank",
                   'sphere':"spherical_tank",
                   'spherical tank':"spherical_tank",
                   "undefined_object": "undefined_object",
                   "silo": "undefined_object" }

    #"enumerate each image" This chunk is actually just getting the paths for the images and annotations
    for xml_file in os.listdir(xml_dir):
        # use the parse() function to load and parse an XML file
        tree = et.parse(os.path.join(xml_dir, xml_file))
        root = tree.getroot()         
        
        for obj in root.iter('object'):
            for name in obj.findall('name'):
                if name.text not in correctly_formatted_object:
                    name.text = object_dict[name.text]

            if int(obj.find('difficult').text) == 1:
                obj.find('truncated').text = '1'
                obj.find('difficult').text = '1'
            if int(obj.find('truncated').text) == 1:
                obj.find('truncated').text = '1'
                obj.find('difficult').text = '1'

        tree.write(os.path.join(xml_dir, xml_file))       
