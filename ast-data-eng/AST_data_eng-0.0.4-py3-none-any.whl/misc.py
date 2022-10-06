######################################################################################################################################################
###################### Identify unlabeled images (cut off by previous chipping code ##################################################
######################################################################################################################################################
    
def incorrectly_chipped_image_and_correctly_chipped_names(incorrectly_chipped_images_path, remaining_chips_path, tiles_complete_dataset_path, tile_name):
    """ Load tile of interest; chip the tile using the mxm, chip dimensions where m > n; Gather the previous chip name format, and the new chip name format;
    save all images, record labeled images that contain relevant data (not black images); save images that were not labeled images; 
    Args:
    incorrectly_chipped_images_path(str): path to folder that will contain all of the incorrect named, images chipped from times
    remaining_chips_path(str): path to folder that will contain all of the remaining images that have not been labeled and correspond to tiles that have labeled images
    tiles_complete_dataset_path(str): path to folder containing tiles
    tile_name(str): name of tile without of extension
    Returns:
    ys(list): list of row indices 
    xs(list): list of column indicies
    chip_name_incorrectly_chip_names(np array): the name of the images following the previous format for images that contain relevant data
    chip_name_correct_chip_names(np array): the name of the images following the previous format for images that contain relevant data
    """
    item_dim = int(512)
    tile = cv2.imread(os.path.join(tiles_complete_dataset_path, tile_name + ".tif"), cv2.IMREAD_UNCHANGED) 
    tile_height,  tile_width,  tile_channels = tile.shape #the size of the tile 
    row_index = math.ceil(tile_height/512) 
    col_index = math.ceil(tile_width/512)
    #print(row_index, col_index)

    chip_name_incorrectly_chip_names = []
    chip_name_correct_chip_names = []
    ys = []
    xs = []

    count = 1            
    for y in range(0, row_index): #rows
        for x in range(0, col_index): #cols
            chip_img = tile_to_chip_array(tile, x, y, item_dim)

            #specify the chip names
            chip_name_incorrect_chip_name = tile_name + '_'+ str(count).zfill(6) + '.jpg'
            chip_name_correct_chip_name = tile_name + '_' + f"{y:02}"  + '_' + f"{x:02}" + '.jpg' # row_cols
            if not os.path.exists(os.path.join(incorrectly_chipped_images_path, chip_name_incorrect_chip_name)):
                cv2.imwrite(os.path.join(incorrectly_chipped_images_path, chip_name_incorrect_chip_name), chip_img) #save images       

            #save names of labeled images  
            if (y < col_index) and (x < col_index): #y:rows already annotated #x:(cols) images that contain relevant data (excludes extraneous annotations of black images)
                ys.append(y)#row index
                xs.append(x)#col index
                chip_name_incorrectly_chip_names.append(chip_name_incorrect_chip_name)
                chip_name_correct_chip_names.append(chip_name_correct_chip_name) # The index is a six-digit number like '000023'. 

            #save remaining images 
            if (y >= col_index): #y: we started at 0 here and 1 before? (save the remaining rows) #x:do not include extraneous black images
                if not os.path.exists(os.path.join(remaining_chips_path, chip_name_correct_chip_name)):
                    cv2.imwrite(os.path.join(remaining_chips_path, chip_name_correct_chip_name), chip_img)   

            #counter for image pathway
            count += 1  
    
    chip_name_incorrectly_chip_names = np.array(chip_name_incorrectly_chip_names)
    chip_name_correct_chip_names = np.array(chip_name_correct_chip_names)
    return(ys,xs,chip_name_incorrectly_chip_names, chip_name_correct_chip_names)

def reformat_xmls_for_rechipped_images(xml_directory, image_in_tile, correct_xml_name, correct_jpg_name, chips_positive_xml_dir_path):
    """ reformat xml files for rechipped images to include resolution, year, updated filename, and updated path. 
    Args:
    xml_directory(str): directory holding xmls
    image_in_tile(str): path to image
    correct_xml_name: correct name for xml
    correct_jpg_name: correct name for jpgs
    chips_positive_xml_dir_path(str): new path for xml
    
    https://docs.python.org/3/library/xml.etree.elementtree.html
    https://stackoverflow.com/questions/28813876/how-do-i-get-pythons-elementtree-to-pretty-print-to-an-xml-file
    https://stackoverflow.com/questions/28813876/how-do-i-get-pythons-elementtree-to-pretty-print-to-an-xml-file
    """
    #load xml
    formatted_chip_name_wo_ext = os.path.splitext(os.path.basename(image_in_tile))[0]
    tree = et.parse(os.path.join(xml_directory, formatted_chip_name_wo_ext +".xml"))
    root = tree.getroot() 
    
    #add resolution to xml
    resolution = et.Element("resolution")
    resolution.text = formatted_chip_name_wo_ext.split("_")[1] #resolution
    et.indent(tree, space="\t", level=0)
    root.insert(3, resolution)
    
    #add year to xml
    year = et.Element("year")
    year.text = formatted_chip_name_wo_ext.split("_")[2]#year
    et.indent(tree, space="\t", level=0)
    root.insert(4,year)
    
    #correct spacing for source (dataset name)
    et.indent(tree, space="\t", level=0)
    
    #correct filename and path to formatting with row/col coordinates
    for filename in root.iter('filename'):
        filename.text = correct_xml_name
    for path in root.iter('path'):
        path.text = os.path.join(xml_directory, correct_jpg_name)

    tree.write(os.path.join(chips_positive_xml_dir_path, correct_xml_name))       

def copy_rename_labeled_images_xmls(xml_directory, images_in_tile, incorrectly_chipped_images_path, chips_positive_dir_path,
                                    chips_positive_xml_dir_path, chip_name_incorrectly_chip_names, chip_name_correct_chip_names, 
                                    multiple_annotations_images, black_images_with_annotations):
    """ reformat xml files for rechipped images to include resolution, year, updated filename, and updated path. 
    Args:
    xml_directory(str): directory holding xmls
    image_in_tile(str): path to image
    incorrectly_chipped_images_path(str): path to folder that will contain all of the incorrect named, images chipped from times
    chips_positive_dir_path(str): new path for jpg
    chips_positive_xml_dir_path(str): new path for xml
    chip_name_incorrectly_chip_names(np array): the name of the images following the previous format for images that contain relevant data
    chip_name_correct_chip_names(np array): the name of the images following the previous format for images that contain relevant data
    multiple_annotations_images: list of images with multiple annotations in a given folder
    black_images_with_annotations: list of black images with annotations
    Return:
    ultiple_annotations_images, black_images_with_annotations
    """
    for image_in_tile in images_in_tile:
        #get the standard image name
        formatted_image_name = os.path.basename(image_in_tile)
        standard_image_name = formatted_image_name.split("_",4)[-1]
        #get the index of the image array of image names #print(standard_image_name)
        index, = np.where(chip_name_incorrectly_chip_names == standard_image_name)

        if len(index) == 0: #If there there is no matching annotation (black image)
            black_images_with_annotations.append(image_in_tile)
            
        elif len(index) >= 1: #If there is a match
            #make sure the image in the folder is correct   
            gray_labeled_image = cv2.cvtColor(cv2.imread(image_in_tile), cv2.COLOR_BGR2GRAY) #image that had been labeled
            incorrectly_chipped_image_path = os.path.join(incorrectly_chipped_images_path, chip_name_incorrectly_chip_names[index[0]])
            gray_known_image = cv2.cvtColor(cv2.imread(incorrectly_chipped_image_path), cv2.COLOR_BGR2GRAY) #image that has been chipped from tile
            (score, diff) = compare_ssim(gray_labeled_image, gray_known_image, full=True)

            if score >= 0.90: #If the labeled image is correct
                #chip_name_incorrectly_chip_names[index]
                correct_xml_name = os.path.splitext(chip_name_correct_chip_names[index[0]])[0] + ".xml"
                correct_jpg_name = os.path.splitext(chip_name_correct_chip_names[index[0]])[0] + ".jpg"
                #copy image
                shutil.copyfile(incorrectly_chipped_image_path, os.path.join(chips_positive_dir_path, correct_jpg_name))
                #create renamed xml
                reformat_xmls_for_rechipped_images(xml_directory, image_in_tile, correct_xml_name, correct_jpg_name, chips_positive_xml_dir_path)
                
        if len(index) > 1: #record images with multiple annotations
            multiple_annotations_images.append(image_in_tile)
    return(multiple_annotations_images, black_images_with_annotations)
    
    
def img_anno_paths_to_corrected_names_for_labeled_images_and_remaining_images(img_paths_anno_paths, correct_directory, incorrectly_chipped_images_path, 
                                                                              remaining_chips_path, tiles_complete_dataset_path):
    """ iterate over all the image and xml paths in directory of annotated images; identify tiles and the corresonding images/xmls in each folder;
    match name of previous naming convention and row/col naming convention;for labeled images and xmls, create folder to store, 
    identify correct images, copy, and rename; identify and save remaining images; 
    Args: 
    img_paths_anno_paths(np array): n x 2 array of jpg and xml paths
    correct_directory(str): path to directory containing xmls and images with correct names
    incorrectly_chipped_images_path(str): path to folder that will contain all of the incorrect named, images chipped from times
    remaining_chips_path(str): path to folder that will contain all of the remaining images that have not been labeled and correspond to tiles that have labeled images
    tiles_complete_dataset_path(str): path to folder containing tiles
    
    Returns:
    multiple_annotations_images: list of images with multiple annotations in a given folder
    black_images_with_annotations: list of black images with annotations
    """
    multiple_annotations_images = []
    black_images_with_annotations = []
    for directory in tqdm.tqdm(img_paths_anno_paths):
        #get all the image and xml paths in directory of annotated images
        print(directory)
        remove_thumbs(directory[0])
        image_paths = sorted(glob(directory[0] + "/*.jpg", recursive = True))
        xml_paths = sorted(glob(directory[1] + "/*.xml", recursive = True))
        #print(len(image_paths),len(xml_paths))

        #identify tiles in each folder
        tiles = []
        for image in image_paths:
            image_name = os.path.splitext(os.path.basename(image))[0]
            if image_name.count("_") > 9:
                tile_name = image_name.split("_",4)[-1].rsplit("_",1)[0] #state included in image name
            else:
                tile_name = image_name.rsplit("_",2)[0] #tile name formated image name
            
            tiles.append(tile_name)
        tiles = sorted(np.unique(tiles))

        #identify the images/xmls that correspond with each tile in folder
        for tile_name in tiles:        
            images_in_tile = [string for string in image_paths if tile_name in string]          
            xmls_in_tile = [string for string in xml_paths if tile_name in string]  
            assert len(images_in_tile) == len(xmls_in_tile), "The same number of images and xmls"
            #print(tile_name, len(images_in_tile))

            #create folder to store corrected chips/xmls
            tile_dir_path = os.path.join(correct_directory, tile_name) #sub folder for each tile 
            chips_positive_dir_path = os.path.join(tile_dir_path,"chips_positive") #images path
            chips_positive_xml_dir_path = os.path.join(tile_dir_path,"chips_positive_xml") #xmls paths

            tile_dir = os.makedirs(tile_dir_path, exist_ok=True)
            chips_positive_dir = os.makedirs(chips_positive_dir_path, exist_ok=True)
            chips_positive_xml_dir = os.makedirs(chips_positive_xml_dir_path, exist_ok=True)

            #identify and save remaining images; match name of previous naming convention and row/col naming convention
            ys, xs, chip_name_incorrectly_chip_names, chip_name_correct_chip_names =  incorrectly_chipped_image_and_correctly_chipped_names(incorrectly_chipped_images_path, remaining_chips_path,                                                                                        tiles_complete_dataset_path, tile_name)

            #identify labeled images that are correct; copy and rename correct images and xmls
            multiple_annotations_images, black_images_with_annotations = copy_rename_labeled_images_xmls(directory[1], images_in_tile, incorrectly_chipped_images_path,
                                                                                                            chips_positive_dir_path, chips_positive_xml_dir_path,
                                                                                                            chip_name_incorrectly_chip_names, chip_name_correct_chip_names,
                                                                                                            multiple_annotations_images, black_images_with_annotations)
        #remaining images
        print("remaining images", len(os.listdir(remaining_chips_path)))
        
        


    
        
        
        
################################################################
#############  Format tiles in tiles folder  ###################
def formatted_tile_name_to_standard_tile_name(tile_name):
    #format tile_names to only include inital capture date 1/20
    tile_name = os.path.splitext(tile_name.split("_",4)[4])[0]
    if tile_name.count("_") > 5:
        tile_name = tile_name.rsplit("_",1)[0]
    tile_name_with_ext = tile_name + ".tif"
    return(tile_name_with_ext)

def rename_formatted_tiles(tiles_complete_dataset_path):
    """
    """
    for tile in os.listdir(tiles_complete_dataset_path):
        #format tile_names to only include inital capture date 1/20
        if tile.count("_") > 5:
            old_tile_path = os.path.join(tiles_complete_dataset_path, tile)
            
            new_tile_name = formatted_tile_name_to_standard_tile_name(tile)
            new_tile_path = os.path.join(tiles_complete_dataset_path, new_tile_name)
            
            if not os.path.exists(new_tile_path): #If the new tile path does not exist, convert the tile to standard format
                os.rename(old_tile_path, new_tile_path)
            if os.path.exists(new_tile_path) and os.path.exists(old_tile_path): #If the new tile path already exists, delete the old tile path (if it still exists)
                os.remove(old_tile_path)
                
#remove_thumbs(os.path.join(parent_directory, complete_dataset_path,"tiles"))
#rename_formatted_tiles(os.path.join(parent_directory, complete_dataset_path, "tiles"))

def formatted_chip_names_to_standard_names(chip):
    """
    """
    chip = os.path.splitext(chip)[0]#remove ext
    chip_name, chip_number = chip.rsplit("_",1)
    tile_name = chip_name.split("_",4)[4]
    if tile_name.count("_") > 5:
        tile_name = tile_name.rsplit("_",1)[0]
    standard_chip_name = tile_name + "_"+ chip_number 
    return(standard_chip_name)

def rename_formatted_chips_images_xmls(complete_dataset_path):
    """
    Rename chips (jps/xmls)
    """
    positive_images_path = os.path.join(complete_dataset_path,"chips_positive")
    for chip in os.listdir(positive_images_path):
        #format tile_names to only include inital capture date 1/20
        if chip.count("_") > 6:
            #old path
            old_chip_path = os.path.join(positive_images_path, chip)
            
            #new name
            new_chip_name = formatted_chip_names_to_standard_names(chip)
            
            #copy images
            if not os.path.exists(os.path.join(complete_dataset_path,"standard_chips_positive", new_chip_name+".jpg")): #If the new tile path does not exist, convert the tile to standard format
                shutil.copyfile(old_chip_path, os.path.join(complete_dataset_path,"standard_chips_positive", new_chip_name+".jpg"))                
            elif not os.path.exists(os.path.join(complete_dataset_path,"dups_chips_positive", new_chip_name+".jpg")): #If the new tile path does not exist, convert the tile to standard format
                shutil.copyfile(old_chip_path, os.path.join(complete_dataset_path,"dups_chips_positive", new_chip_name+".jpg"))                
            else:
                print("so many dups")
                
            #copy annotations
            if not os.path.exists(os.path.join(complete_dataset_path,"standard_chips_positive_xml", new_chip_name+".xml")): #If the new tile path does not exist, convert the tile to standard format
                shutil.copyfile(old_chip_path, os.path.join(complete_dataset_path,"standard_chips_positive_xml", new_chip_name+".xml"))
            elif not os.path.exists(os.path.join(complete_dataset_path,"dups_chips_positive_xml", new_chip_name+".xml")): #If the new tile path does not exist, convert the tile to standard format
                shutil.copyfile(old_chip_path, os.path.join(complete_dataset_path,"dups_chips_positive_xml", new_chip_name+".xml"))                
            else:
                print("so many dups")
            
            #if os.path.exists(new_tile_path) and os.path.exists(old_tile_path): #If the new tile path already exists, delete the old tile path (if it still exists)
            #    os.remove(old_tile_path)
                    
###
def identify_verified_jpgs_missing_annotations(verified_sets_parent_dir, verified_set_dir):
    """
    Args:
    verified_sets_parent_dir(str): Name of the parent folder holding verified images; Ex:"verified/verified_sets"
    verified_set_dir(str): Name of verified set folder containing images without corresponding annotations; Ex:"verify_jaewon_poonacha_cleave_1"
    
    Return: 
    jpgs_missing_xmls(list): list of jpgs without corresponding annotations in the verified folder of interest
    jpgs_missing_xmls_path(list): list of paths containing xmls matching the jpgs missing annotations
    """
    #get the xml ids w/o the ext
    xmls = os.listdir(os.path.join(parent_directory,verified_sets_parent_dir, verified_set_dir, "chips_positive_xml"))
    xmls_without_ext = []
    for xml in xmls:
        xmls_without_ext.append(os.path.splitext(xml)[0])
        
    #get the jpg ids w/o the ext
    jpgs = os.listdir(os.path.join(parent_directory, verified_sets_parent_dir, verified_set_dir,"chips_positive"))
    jpgs_without_ext = []
    for jpg in jpgs:
        jpgs_without_ext.append(os.path.splitext(jpg)[0])

    #identify jpgs tht are missing xmls
    jpgs_missing_xmls = []
    for xml in xmls_without_ext:
        if xml not in jpgs_without_ext:
            jpgs_missing_xmls.append(xml)

    #identify possible xml path 
    all_xmls = glob(parent_directory + "/**/*.xml", recursive = True)
    jpgs_missing_xmls_path =[]
    for jpg in jpgs_missing_xmls:
        jpg_path = [string for string in all_xmls if jpg in string]   
        if len(jpg_path) > 0:
            jpgs_missing_xmls_path.append(jpg_path)
    
    return(jpgs_missing_xmls, jpgs_missing_xmls_path)

####################### Identify Duplicates#####################################################################
def unique_by_first_dimension(a, images):
    #https://stackoverflow.com/questions/41071116/how-to-remove-duplicates-from-a-3d-array-in-python
    tmp = a.reshape(a.shape[0], -1)
    b = np.ascontiguousarray(tmp).view(np.dtype((np.void, tmp.dtype.itemsize * tmp.shape[1])))
    
    _, idx = np.unique(b, return_index=True)
    unique_images = images[idx]
    
    u, c = np.unique(b, return_counts=True)
    dup = u[c > 1]
    duplicate_images = images[np.where(np.isin(b,dup))[0]]
    return(unique_images, duplicate_images)

de(arr1, arr2, arr3):
    # Converting the arrays into sets
    s1 = set(arr1)
    s2 = set(arr2)
    s3 = set(arr3)
      
    # Calculates intersection of sets on s1 and s2
    set1 = s1.intersection(s2)         #[80, 20, 100]
      
    # Calculates intersection of sets on set1 and s3
    result_set = set1.intersection(s3)
      
    # Converts resulting set to list
    final_list = list(result_set)
    print(len(final_list))
    return(final_list)

def move_images(old_image_dir, new_image_dir, image_names):
    #Ensure directory exists
    os.makedirs(new_image_dir, exist_ok = True)
    #move images
    for image in image_names:
        shutil.copyfile(os.path.join(old_image_dir,image), 
                        os.path.join(new_image_dir,image))                

def sorted_list_of_files(dups_chips_positive_path):
    #https://thispointer.com/python-get-list-of-files-in-directory-sorted-by-size/#:~:text=order%20by%20size%3F-,Get%20list%20of%20files%20in%20directory%20sorted%20by%20size%20using,%2C%20using%20lambda%20x%3A%20os.
    #Get list of files in directory sorted by size using os.listdir()

    #list_of_files = filter( lambda x: os.path.isfile(os.path.join(dir_name, x)), os.listdir(dir_name) )
    # Sort list of file names by size 
    #list_of_files = sorted( list_of_files,key =  lambda x: os.stat(os.path.join(dir_name, x)).st_size)
    
    sizes = []
    dup_images = np.array(os.listdir(dups_chips_positive_path))
    for image in dup_images:
        sizes.append(os.stat(os.path.join(dups_chips_positive_path,image)).st_size)
    sizes = np.array(sizes)
    
    df = pd.DataFrame({'dups': dup_images,
                       'sizes': sizes})
    df = df.sort_values(by=['sizes'])
    df.to_csv('dup tile names.csv') 

    return(df)

def list_of_lists_positive_chips(chips_positive_path):
    positive_chips = os.listdir(chips_positive_path)
    positive_chips_lists = [positive_chips[x:x+1000] for x in range(0, len(positive_chips), 1000)]
    return(positive_chips_lists)

def directory_tile_names(directory, output_file_name): 
    tiles = []
    for image in os.listdir(directory):
            img = os.path.splitext(image)[0] #name of tif with the extension removed
            tile = img.rsplit("_",1)[0]
            #print(tile.split("_",4)[4])
            #tile = tile.split("_",4)[4] #get the tile names to remove duplicates from being downloaded
            tiles.append(tile)
    tiles = np.unique(tiles)
    pd.DataFrame(tiles, columns = [output_file_name]).to_csv(output_file_name+'.csv') 

def identify_all_paths_to_duplicate_images(parent_directory, duplicate_images):
    entire_jpg = glob(parent_directory + "/**/*.jpg", recursive = True)
    full_path = []
    jpg_name = []
    for jpg in entire_jpg:
        if jpg.rsplit("\\")[-1] in duplicate_images:
            full_path.append(jpg)
            jpg_name.append(jpg.rsplit("\\")[-1])

    df = pd.DataFrame({'jpg name': jpg_name,
                       'full path': full_path})
    df.to_csv("duplicate_jpgs_full_path.csv")


def get_tile_names_from_chip_names(directory):
    remove_thumbs(directory)
    tile_names = []
    for chip_name in os.listdir(directory):
        chip_name = os.path.splitext(chip_name)[0]#remove ext
        chip_name, _ = chip_name.rsplit("_",1)
        tile_names.append(chip_name.split("_",4)[4] + ".tif")
    return(np.unique(tile_names))

def positive_images_to_array(images_dir_path):
    images = np.array(os.listdir(os.path.join(images_dir_path)))
    image_array = np.zeros((len(images),512,512, 3), dtype='uint8')
    image_directory = np.array([images_dir_path] *len(images))
    for num in range(len(images)):    
        image = cv2.imread(os.path.join(images_dir_path, images[num]),cv2.IMREAD_UNCHANGED) #open image
        image_array[num,:,:,:] = image
        
    return(images, image_array, image_directory)

def positive_images_to_array_rgb(images_dir_path):
    images = np.array(os.listdir(os.path.join(images_dir_path)))
    imgsr = np.zeros((len(images),512,512), dtype='uint8')
    imgsg = np.zeros((len(images),512,512), dtype='uint8')
    imgsb = np.zeros((len(images),512,512), dtype='uint8')
    
    for num in range(len(images)):    
        image = cv2.imread(os.path.join(images_dir_path, images[num]),cv2.IMREAD_UNCHANGED) #open image
        imgsr[num,:,:] = image[:,:,0]
        imgsg[num,:,:] = image[:,:,1]
        imgsb[num,:,:] = image[:,:2]
    return(images, imgsr, imgsg, imgsb)

def positive_images_to_array_correctly_labeled(images_dir_path, incorrect_labeled_chip_names_by_subfolder):
    """
    For every image in the given subdirectory, the name and image contents have been verified and incorrect images have been identified
    This function identifies the images that are correctly labeled 
    get image array for correctly labeled images
    
    Args:
    images_dir_path(str)
    incorrect_labeled_chip_names_by_subfolder(list)
    """
    subfolders_files = os.listdir(images_dir_path)
    for chip in incorrect_labeled_chip_names_by_subfolder["incorrect_chip_names"].tolist():
        if chip in subfolders_files:
            subfolders_files.remove(chip)
        
    correctly_labeled_images = np.array(subfolders_files) #image names 
    correctly_labeled_image_array = np.zeros((len(correctly_labeled_images),512,512, 3), dtype='uint8') #image contents 
    correctly_labeled_image_directory = np.array([images_dir_path] * len(correctly_labeled_images)) #image directory 
    for num in range(len(correctly_labeled_images)):    
        correctly_labeled_image = cv2.imread(os.path.join(images_dir_path, correctly_labeled_images[num]),cv2.IMREAD_UNCHANGED) #open image
        correctly_labeled_image_array[num,:,:,:] = correctly_labeled_image
        
    return(correctly_labeled_images, correctly_labeled_image_array, correctly_labeled_image_directory)      
        
        
  