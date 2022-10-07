        
#####################################################
def get_img_xml_paths(img_paths_anno_paths):
    img_paths = []
    xml_paths = []
    for directory in tqdm.tqdm(img_paths_anno_paths):
        #get all the image and xml paths in directory of annotated images
        remove_thumbs(directory[0])
        img_paths += sorted(glob(directory[0] + "/*.jpg", recursive = True))
        xml_paths += sorted(glob(directory[1] + "/*.xml", recursive = True))  
    return(img_paths, xml_paths)

def get_unique_tile_names(paths):
    img_names = []
    tile_names = []
    for path in paths:
        img_name = os.path.splitext(os.path.basename(path))[0]
        if img_name.count("_") > 9:
            tile_name = img_name.split("_",4)[-1].rsplit("_",1)[0] #state-year included in image name
        else:
            tile_name = img_name.rsplit("_",2)[0] #tile name formated image name
        img_names.append(img_name)
        tile_names.append(tile_name)
    tile_names = sorted(np.unique(tile_names))
    img_names = sorted(np.unique(img_names))
    return(img_names, tile_names)

def get_tile_names(paths):
    tile_names = []
    img_names = []
    for path in paths:
        img_name = os.path.splitext(os.path.basename(path))[0]
        if img_name.count("_") > 9:
            tile_name = img_name.split("_",4)[-1].rsplit("_",1)[0] #state-year included in image name
        else:
            tile_name = img_name.rsplit("_",2)[0] #tile name formated image name
        img_names.append(img_name)
        tile_names.append(tile_name)
    tile_names = sorted(tile_names)
    img_names = sorted(img_names)
    return(tile_names, img_names)

def make_by_tile_dirs(home_dir, tile_name):
    #create folder to store corrected chips/xmls
    tile_dir = os.path.join(home_dir, tile_name) #sub folder for each tile 
    chips_positive_path = os.path.join(tile_dir,"chips_positive") #images path
    chips_positive_xml_path = os.path.join(tile_dir,"chips_positive_xml") #xmls paths
    os.makedirs(tile_dir, exist_ok=True)
    os.makedirs(chips_positive_path, exist_ok=True)
    os.makedirs(chips_positive_xml_path, exist_ok=True)
    return(tile_dir)

def read_tile(tile_path, item_dim = int(512)):
    tile = cv2.imread(tile_path, cv2.IMREAD_UNCHANGED) 
    tile_height,  tile_width,  tile_channels = tile.shape #the size of the tile 
    row_index = math.ceil(tile_height/item_dim) #y
    col_index = math.ceil(tile_width/item_dim) #x
    return(tile, row_index, col_index)

def copy_and_replace_images_xml(img_name, img_path, xml_path, copy_dir):                  
    ####    
    new_img_path = os.path.join(copy_dir, "chips_positive", img_name + ".jpg")
    shutil.copy(img_path, new_img_path)
        
    new_xml_path = os.path.join(copy_dir, "chips_positive_xml", img_name + ".xml")
    shutil.copy(xml_path, new_xml_path) #destination

def move_and_replace_images_xml(img_name, img_path, xml_path, copy_dir):                  
    ####    
    new_img_path = os.path.join(copy_dir, "chips_positive", img_name + ".jpg")
    shutil.move(img_path, new_img_path)
        
    new_xml_path = os.path.join(copy_dir, "chips_positive_xml", img_name + ".xml")
    shutil.move(xml_path, new_xml_path) #destination
    
def compare_images(t_2_chip, labeled_img):  
    gray_t_2_chip = cv2.cvtColor(t_2_chip.astype(np.uint8), cv2.COLOR_BGR2GRAY) # make gray
    gray_labeled_image = cv2.cvtColor(labeled_img.astype(np.uint8), cv2.COLOR_BGR2GRAY) #image that has been chipped from tile
    score = compare_ssim(gray_t_2_chip, gray_labeled_image, win_size = 3) #set window size so that is works on the edge peices 
    if score >= 0.95: #If the labeled image is correct
        #chip_name_incorrectly_chip_names[index]
        return(True)
    else: #if it is incorrect
        ## move incorrectly named image if it one of the same name has not already been moved
        return(False)
    
def compare_move_imgs_standard(t_2_chip, x, y, tile_name, img_count, img_in_tile_paths, xml_in_tile_paths, img_in_tile_names,
                               compile_tile_dir, incorrect_dir):
    img_name_wo_ext = tile_name + '_' + f"{y:02}"  + '_' + f"{x:02}" # row_col
    standard_img_name_wo_ext = [string for string in img_in_tile_names if img_name_wo_ext in string]
    standard_img_name_wo_ext = list(set(standard_img_name_wo_ext))
    standard_index, = np.where(np.isin(np.array(img_in_tile_names), standard_img_name_wo_ext))    
    if len(standard_index) >= 1: 
        for index in standard_index:
            img_path = img_in_tile_paths[index]
            xml_path = xml_in_tile_paths[index]
            img_name = img_in_tile_names[index]
            if compare_images(t_2_chip, cv2.imread(img_path)):
                img_count += 1
                copy_and_replace_images_xml(img_name, img_path, xml_path, compile_tile_dir) #use standard name and copy to compiled directory
            #else:
            #    print(img_name,"\n",img_path)
            #    copy_and_replace_images_xml(img_name, img_path, xml_path, incorrect_dir) #move to incorrect directory
    return(img_count)
        #counter for image pathway
    
    
def compare_move_imgs_state_year(t_2_chip, x, y, tile_name, count, img_count,
                                 img_in_tile_paths, xml_in_tile_paths, img_in_tile_names, 
                                 compile_tile_dir, incorrect_dir):
    standard_quad_img_name_wo_ext = tile_name + '_' + f"{y:02}"  + '_' + f"{x:02}" # row_col
    img_name_wo_ext = tile_name + '_'+ str(count).zfill(6) #specify the chip names
    
    state_year_img_name_wo_ext = [string for string in img_in_tile_names if img_name_wo_ext in string]
    state_year_img_name_wo_ext = list(set(state_year_img_name_wo_ext))     
    state_year_index, = np.where(np.isin(np.array(img_in_tile_names), state_year_img_name_wo_ext)) 
    if len(state_year_index) >= 1: 
        for index in state_year_index:
            img_path = img_in_tile_paths[index]
            xml_path = xml_in_tile_paths[index]
            img_name = img_in_tile_names[index]
            if compare_images(t_2_chip, cv2.imread(img_path)):
                img_count += 1
                copy_and_replace_images_xml(standard_quad_img_name_wo_ext, img_path, xml_path, compile_tile_dir) #use standard name and copy to compiled directory
            #else:
            #    print(img_name, "\n",standard_quad_img_name_wo_ext, img_path)
            #    copy_and_replace_images_xml(img_name, img_path, xml_path, incorrect_dir) #move to incorrect directory
    return(img_count)
        #counter for image pathway

def iterate_over_tile_compare_move_state_year_by_image_name(tile_name, compiled_by_tile_dir, tile_dir_path, 
                                                            images_do_not_match_names_dir, correctly_chipped_incorrect_dir,
                                                            img_paths, xml_paths, img_names, img_count_state_year, img_count_standard):
    
    compile_tile_dir = make_by_tile_dirs(compiled_by_tile_dir, tile_name)
    tile, row_index, col_index = read_tile(os.path.join(tile_dir_path, tile_name + ".tif")) #read in tile
    
    img_in_tile_paths = [string for string in img_paths if tile_name in string]
    xml_in_tile_paths = [string for string in xml_paths if tile_name in string]
    img_in_tile_names = [string for string in img_names if tile_name in string]
    assert len(img_in_tile_paths) == len(xml_in_tile_paths) == len(img_in_tile_names), "The same number of images and xmls"
                                                            
    count = 1
    for y in range(0, row_index): #rows #use row_index to account for the previous errors in state/year naming conventions
        for x in range(0, row_index): #cols   
            standard_quad_img_name_wo_ext = tile_name + '_' + f"{y:02}"  + '_' + f"{x:02}" # row_col
            state_year_img_name_wo_ext = tile_name + '_'+ str(count).zfill(6) #specify the chip names

            t_2_chip = tile_to_chip_array(tile, x, y, int(512)) #get correct chip from tile
            img_count_state_year = compare_move_imgs_state_year(t_2_chip, x, y, tile_name, count, img_count_state_year,
                                                                   img_in_tile_paths, xml_in_tile_paths, img_in_tile_names, 
                                                                   compile_tile_dir, images_do_not_match_names_dir)
            
            img_count_standard = compare_move_imgs_standard(t_2_chip, x, y, tile_name, img_count_standard,
                                                               img_in_tile_paths, xml_in_tile_paths, img_in_tile_names,
                                                               compile_tile_dir, correctly_chipped_incorrect_dir)
            count += 1  
            
    return(img_count_state_year, img_count_standard)


def get_six_digit_index_from_img_path(state_year_img_paths):
    six_digit_index = []
    for img_path in state_year_img_paths:
        img_name = os.path.splitext(os.path.basename(img_path))[0]
        assert img_name.count("_") > 9, "Not state year format"
        six_digit_index.append(img_name.rsplit("_",1)[-1])
    return(six_digit_index)

def get_x_y_index(standard_img_paths):
    xs = []
    ys = []
    for img_path in standard_img_paths:
        img_name = os.path.splitext(os.path.basename(img_path))[0]
        assert (img_name.count("_") < 9) and (img_name.split("_",1)[0] == "m"), "Not standard format"
        y, x = img_name.split("_")[-2:] #y=row;x=col
        ys.append(y)
        xs.append(x)
    return(ys,xs)

def compare_move_imgs_state_year_by_six_digit_index(x, y, tile_name, count, img_count, idxs, img_paths, xml_paths, 
                                                     compile_tile_dir):
    
    t_2_chip = tile_to_chip_array(tile, x, y, int(512)) #get correct chip from tile
    #get standard and state_year img_names
    standard_quad_img_name_wo_ext = tile_name + '_' + f"{y:02}"  + '_' + f"{x:02}" # row_col
    state_year_img_name_wo_ext = tile_name + '_'+ str(count).zfill(6) #specify the chip names
    
    #identify img/xml that have been moved
    #img_paths_copy = copy.copy(img_paths)
    #xml_paths_copy = copy.copy(xml_paths)
    assert len(img_paths) == len(xml_paths), "The same number of images and xmls"

    #identify imgs/xmls that match the chip position
    for idx in idxs:
        img_path = img_paths[idx]
        xml_path = xml_paths[idx]
        if compare_images(t_2_chip, cv2.imread(img_path)):
            img_count += 1
            copy_and_replace_images_xml(standard_quad_img_name_wo_ext, img_path, xml_path, compile_tile_dir) #use standard name and copy to compiled directory
            #remove img/xmls that have been moved from list
            #img_paths_copy.remove(img_path)
            #xml_paths_copy.remove(xml_path)
        #else:
        #   copy_and_replace_images_xml(state_year_img_name_wo_ext, img_path, xml_path, incorrect_dir) #move to incorrect directory
                    
    return(img_count)#, img_paths_copy, xml_paths_copy)
        #counter for image pathway
    
def iterate_over_tile_compare_move_state_year_by_six_digit_index(all_tile_names, compile_by_tile_state_year_dir, tile_dir_path, 
                                                                 state_year_img_paths, state_year_xml_paths, six_digit_index_list,
                                                                 images_do_not_match_names_dir):
                                                                 
    img_count_state_year = 0
    for tile_name in tqdm.tqdm(all_tile_names):
        compile_tile_dir = make_by_tile_dirs(compile_by_tile_state_year_dir, tile_name)
        tile, row_index, col_index = read_tile(os.path.join(tile_dir_path, tile_name + ".tif")) #read in tile
        count = 1
        for y in range(0, row_index): #rows #use row_index to account for the previous errors in state/year naming conventions
            for x in range(0, row_index): #cols               
                #get imgs/xmls where the count matches a la
                six_digit_index = str(count).zfill(6)

                indicies, = np.where(np.array(six_digit_index_list) == six_digit_index)

                state_year_img_paths, state_year_xml_paths
                if len(state_year_img_paths) > 0:

                    img_count_state_year, state_year_img_paths, state_year_xml_paths = compare_move_imgs_state_year_by_six_digit_index(x, y, tile_name, count, img_count_state_year, indicies, 
                                                                                                                                  state_year_img_paths, state_year_xml_paths, 
                                                                                                                                  compile_tile_dir)
                count += 1  
        print(len(state_year_img_paths), len(state_year_xml_paths))
        print(img_count_state_year)
    
def multi_iterate_over_tile_compare_move_state_year_by_six_digit_index(tile_name, compile_by_tile_state_year_dir, tile_dir_path, 
                                                                 state_year_img_paths, state_year_xml_paths, six_digit_index_list):
    print(tile_name)                                                         
    img_count_state_year = 0
    compile_tile_dir = make_by_tile_dirs(compile_by_tile_state_year_dir, tile_name)
    tile, row_index, col_index = read_tile(os.path.join(tile_dir_path, tile_name + ".tif")) #read in tile
    
    count = 1
    for y in range(0, row_index): #rows #use row_index to account for the previous errors in state/year naming conventions
        for x in range(0, row_index): #cols               
            #get imgs/xmls where the count matches a la
            six_digit_index = str(count).zfill(6)
            indicies, = np.where(np.array(six_digit_index_list) == six_digit_index)
            if len(state_year_img_paths) > 0:
                img_count_state_year, state_year_img_paths, state_year_xml_paths = compare_move_imgs_state_year_by_six_digit_index(x, y, tile_name, count,                                                                                                                                                         img_count_state_year, indicies,
                                                                                                                                  state_year_img_paths, state_year_xml_paths, 
                                                                                                                                  compile_tile_dir)
            count += 1  
    print(len(state_year_img_paths), len(state_year_xml_paths))
    print(img_count_state_year)
    
def make_tile_dir_and_get_correct_imgs(tile_name, compile_dir_path, tile_dir_path, correct_chip_dir_path):
    compile_tile_dir = make_by_tile_dirs(compile_dir_path, tile_name) #make directory to store positive chips and xmls
    tile, row_index, col_index = read_tile(os.path.join(tile_dir_path, tile_name + ".tif")) #read in tile
    
    count = 1
    for y in range(0, row_index): #rows #use row_index to account for the previous errors in state/year naming conventions
        for x in range(0, row_index): #cols   
            t_2_chip = tile_to_chip_array(tile, x, y, int(512)) #get correct chip from tile
            six_digit_idx = str(count).zfill(6)
            cv2.imwrite(os.path.join(correct_chip_dir_path, tile_name + "-" + f"{y:02}"  + "-" + f"{x:02}" + "-" + six_digit_idx+".jpg"), t_2_chip) #save images  
            count += 1  

def make_tile_dir_and_get_correct_imgs_w_and_wo_black_sq(tile_name, compile_dir_path, tile_dir_path,
                                                         correct_chip_w_black_sq_dir_path,correct_chip_wo_black_sq_dir_path):
    compile_tile_dir = make_by_tile_dirs(compile_dir_path, tile_name) #make directory to store positive chips and xmls
    tile, row_index, col_index = read_tile(os.path.join(tile_dir_path, tile_name + ".tif")) #read in tile
    item_dim = (int(512))
    count = 1
    for y in range(0, row_index): #rows #use row_index to account for the previous errors in state/year naming conventions
        for x in range(0, row_index): #cols  
            #define image name
            six_digit_idx = str(count).zfill(6)
            t_2_chip_wo_black_sq_img_name=tile_name + "-" + f"{y:02}"  + "-" + f"{x:02}" + "-" + six_digit_idx + ".jpg" #for compare analysis
            standard_quad_img_name_wo_ext=tile_name + '_' + f"{y:02}"  + '_' + f"{x:02}" + ".jpg" # row_col #for save

            #save images without black pixels added  
            t_2_chip_wo_black_sq = tile[y*item_dim:y*item_dim+item_dim, x*(item_dim):x*(item_dim)+item_dim]
            if t_2_chip_wo_black_sq.size != 0:
                #write image without black pixels added 
                cv2.imwrite(os.path.join(correct_chip_wo_black_sq_dir_path, t_2_chip_wo_black_sq_img_name), t_2_chip_wo_black_sq) 
                #write and save black pixels added  
                t_2_chip_w_black_sq = tile_to_chip_array(tile, x, y, int(512)) #get correct chip from tile
                cv2.imwrite(os.path.join(correct_chip_w_black_sq_dir_path, standard_quad_img_name_wo_ext), t_2_chip_w_black_sq) #write images 
            count += 1 
            
def compare_imgs_xmls_x_y_index_dcc(correct_img_path, state_year_six_digit_idx_list, state_year_img_paths, state_year_xml_paths, compile_dir):
    #change to moving for dcc
    #correct_img_path.rsplit("-",3) # tile name formated image name
    correct_img_name = os.path.splitext(os.path.basename(correct_img_path))[0]
    tile_name, y, x, six_digit_idx = correct_img_name.rsplit("-",3)
    y = int(y)
    x = int(x)
    # all image
    idxs, = np.where(np.array(state_year_six_digit_idx_list) == six_digit_idx)
    tile_dir = os.path.join(compile_dir, tile_name) #sub folder for correct directory 
    if len(state_year_img_paths) > 0: 
        #get standard and state_year img_names
        standard_quad_img_name_wo_ext = tile_name + '_' + f"{y:02}"  + '_' + f"{x:02}" # row_col
        #identify img/xml that have been moved
        #img_paths_copy = copy.copy(img_paths)
        #xml_paths_copy = copy.copy(xml_paths)
        assert len(state_year_img_paths) == len(state_year_xml_paths), "The same number of images and xmls"
        #identify imgs/xmls that match the chip position
        for idx in idxs:
            img_path = state_year_img_paths[idx]
            xml_path = state_year_xml_paths[idx]

            if os.path.exists(img_path) and os.path.exists(xml_path): #confirm image and xml is still there 
                if compare_images(cv2.imread(correct_img_path), cv2.imread(img_path)):
                    #move_and_replace_images_xml(standard_quad_img_name_wo_ext, img_path, xml_path, tile_dir) #use standard name and copy to compiled directory
                    copy_and_replace_images_xml(standard_quad_img_name_wo_ext, img_path, xml_path, tile_dir) #use standard name and copy to compiled directory
                    #remove img/xmls that have been moved from list
                    #img_paths_copy.remove(img_path)
                    #xml_paths_copy.remove(xml_path)
    #return(img_paths_copy, xml_paths_copy)
    
            
def compare_imgs_wo_blk_pxls_state_yr_std_from_6_digit_xy_idxs(correct_img_wo_black_sq, correct_img_wo_black_sq_path, 
                                                                            compile_dir, state_year_six_digit_idx_list, 
                                                                            state_year_img_paths, state_year_xml_paths,
                                                                            yx_list, standard_img_paths, standard_xml_paths):
    #process correct img (wo black sq) info
    correct_img_name = os.path.splitext(os.path.basename(correct_img_wo_black_sq_path))[0] #get correct img name
    row_dim = correct_img_wo_black_sq.shape[0] #get row dim
    col_dim = correct_img_wo_black_sq.shape[1] #get col dim
    
    if min(row_dim, col_dim) >= 3:#compare function has a minimum window set to 3 pixels
        tile_name, y, x, six_digit_idx = correct_img_name.rsplit("-",3) #identify tile name and indicies from correct img name
        by_tile_dir = os.path.join(compile_dir, tile_name) #sub folder for correct directory 

        #get standard and state idxs that match the correct img
        state_idxs, = np.where(np.array(state_year_six_digit_idx_list) == six_digit_idx)
        standard_idxs, = np.where((yx_list == (y, x)).all(axis=1))
        #turn the y/x into integers
        y = int(y)
        x = int(x)
        standard_quad_img_name_wo_ext = tile_name + '_' + f"{y:02}"  + '_' + f"{x:02}" # (row_col) get standard and state_year img_names

        #identify imgs/xmls that match the chip position (state imgs)
        for idx in state_idxs:
            #get verified img/xml path
            img_path = state_year_img_paths[idx]
            xml_path = state_year_xml_paths[idx]
            img = cv2.imread(img_path)
            img = img[0:row_dim, 0:col_dim]
            if (np.sum(img) != 0) & (compare_images(correct_img_wo_black_sq, img)): #only move images if they are not all black and they match the correct image
                copy_and_replace_images_xml(standard_quad_img_name_wo_ext, img_path, xml_path, by_tile_dir) #use standard name and copy to compiled directory       

        #identify imgs/xmls that match the chip position (standard imgs)
        for idx in standard_idxs:
            img_path = standard_img_paths[idx]
            xml_path = standard_xml_paths[idx]
            img = cv2.imread(img_path)
            img = img[0:row_dim, 0:col_dim]
            if (np.sum(img) != 0) & (compare_images(correct_img_wo_black_sq, img)):
                #print("match", correct_img_path, img_path)
                copy_and_replace_images_xml(standard_quad_img_name_wo_ext, img_path, xml_path, by_tile_dir) #use standard name and copy to compiled directory

def rename_x_y_index_named_chips(compile_by_tile_dir, tile_names):
    #change to moving for dcc
    #correct_img_path.rsplit("-",3) # tile name formated image name
    for tile in tqdm.tqdm(tile_names):
        chip_by_tile_path = os.path.join(compile_by_tile_dir, tile, "chips")
        chip_paths = sorted(glob(chip_by_tile_path + "/*.jpg", recursive = True))
        for chip_path in chip_paths:
            chip_name = os.path.splitext(os.path.basename(chip_path))[0]
            
            if chip_name.count("-") > 0:
                tile_name, y, x, six_digit_idx = chip_name.rsplit("-",3)
                y = int(y)
                x = int(x)
                standard_quad_chip_path = os.path.join(chip_by_tile_path,
                                                       tile_name + '_' + f"{y:02}"  + '_' + f"{x:02}"+".jpg") # row_col
                os.rename(chip_path, standard_quad_chip_path)

def rename_x_y_index_named_chips_by_tile(compile_by_tile_dir, tile_name):
    #change to moving for dcc
    #correct_img_path.rsplit("-",3) # tile name formated image name
    chip_by_tile_path = os.path.join(compile_by_tile_dir, tile_name, "chips")
    chip_paths = sorted(glob(chip_by_tile_path + "/*.jpg", recursive = True))
    
    for chip_path in chip_paths:
        chip_name = os.path.splitext(os.path.basename(chip_path))[0]
        
        if chip_name.count("-") > 0:
            tile_name_split, y, x, six_digit_idx = chip_name.rsplit("-",3)
            y = int(y)
            x = int(x)
            standard_quad_chip_path = os.path.join(chip_by_tile_path,
                                                   tile_name_split + '_' + f"{y:02}"  + '_' + f"{x:02}"+".jpg") # row_col
            os.rename(chip_path, standard_quad_chip_path)
####################################################################################################################
########## Identify images where the contents and naming conventions doe not match ##################################
#####################################################################################################################
def standard_name_verified_images_to_img_anno_by_tile_dir(verified_set_paths, img_anno_directory, incorrect_named_correctly_chipped_dir, tile_dir_path):
    """
    After annotations (with standard quad naming convention) have been verified move images to directory organized by tile_name,
    if the image contents are correct (row/col chip in tile). 
    Structure:
    image_anno_dir
        tile_name
            chips_positive
            chips_postiive_xml
    Args: 
    verified_set_paths(str): path to folder containing verified sets
    img_anno_directory(str): path to folder containing img and annotations for each tile by each folder (correct naming convention)
    incorrect_named_correctly_chipped_dir(str): path to folder that will contain all of the incorrectly named images (correctly chipped)
    tiles_dir(str): path to folder containing tiles
    """
    for directory in tqdm.tqdm(verified_set_paths):
        #get all the image and xml paths in directory of annotated images
        remove_thumbs(directory[0])
        #sort so that img/xml paths allign
        labeled_img_paths = sorted(glob(directory[0] + "/*.jpg", recursive = True))
        labeled_xml_paths = sorted(glob(directory[1] + "/*.xml", recursive = True))
        #identify tiles in each folder
        tiles = []
        for img_path in labeled_img_paths:
            img_name = os.path.splitext(os.path.basename(img_path))[0]
            if img_name.count("_") > 9:
                tile_name = img_name.split("_",4)[-1].rsplit("_",1)[0] #state included in image name
            else:
                tile_name = img_name.rsplit("_",2)[0] #tile name formated image name
            tiles.append(tile_name)
        tiles = np.unique(tiles)

        #identify the images/xmls that correspond with each tile in folder
        for tile_name in tiles:  
            labeled_img_paths_by_tile = [string for string in labeled_img_paths if tile_name in string]          
            labeled_xml_paths_by_tile = [string for string in labeled_xml_paths if tile_name in string]  
            assert len(labeled_img_paths_by_tile) == len(labeled_xml_paths_by_tile), "The same number of images and xmls"

            #identify path to correct iamge path
            #create folder to store corrected chips/xmls
            img_anno_for_tile_path = os.path.join(img_anno_directory, tile_name) #sub folder for each tile 
            imgs_positive_dir_path = os.path.join(img_anno_for_tile_path, "chips_positive") #images path
            imgs_positive_dir = os.makedirs(imgs_positive_dir_path, exist_ok = True)
            imgs_positive_xml_dir_path = os.path.join(img_anno_for_tile_path, "chips_positive_xml") #xmls paths
            imgs_positive_xml_dir = os.makedirs(imgs_positive_xml_dir_path, exist_ok=True)
            #create folder to store incorrected chips/xmls
            incorrect_imgs_positive_dir_path = os.path.join(incorrect_named_correctly_chipped_dir, tile_name, "chips_positive")
            incorrect_imgs_positive_dir = os.makedirs(incorrect_imgs_positive_dir_path, exist_ok=True)
            incorrect_imgs_positive_xml_dir_path = os.path.join(incorrect_named_correctly_chipped_dir, tile_name, "chips_positive_xml")
            incorrect_imgs_positive_xml_dir = os.makedirs(incorrect_imgs_positive_xml_dir_path, exist_ok=True)
            #read in tile
            tile_path = os.path.join(tile_dir_path, tile_name + ".tif")
            tile = cv2.imread(tile_path, cv2.IMREAD_UNCHANGED) 

            for i, (labeled_img_path, labeled_xml_path) in enumerate(zip(labeled_img_paths_by_tile, labeled_xml_paths_by_tile)):
                # labeled image
                img_name = os.path.splitext(os.path.basename(labeled_img_path))[0]  #get image name 
                gray_labeled_img = cv2.cvtColor(cv2.imread(labeled_img_path), cv2.COLOR_BGR2GRAY) #load labeled image 
                # image from tile
                y, x = img_name.split("_")[-2:] #name of tif with the extension removed; y=row;x=col
                t_2_chip = tile_to_chip_array(tile, int(x), int(y), int(512)) # load tile to chip
                gray_t_2_chip = cv2.cvtColor(t_2_chip.astype(np.uint8), cv2.COLOR_BGR2GRAY) # make gray
                # check if images are the same
                (score, diff) = compare_ssim(gray_labeled_img, gray_t_2_chip, full=True)

                if score >= 0.95: #If the labeled image is correct; copy from verfied folder to img/anno tile folder
                    img_name_correct.append(img_name)
                    ## move correct postive chip
                    shutil.copy(labeled_img_path, os.path.join(imgs_positive_dir_path, img_name + ".jpg")) #source, destination
                    shutil.copy(labeled_xml_path, os.path.join(imgs_positive_xml_dir_path, img_name + ".xml")) 
                else: #if it is incorrect
                    ## move incorrectly named image if it one of the same name has not already been moved
                    if not os.path.exists(os.path.join(incorrect_imgs_positive_dir_path, img_name + ".jpg")):
                        shutil.copy(labeled_img_path, os.path.join(incorrect_imgs_positive_dir_path, img_name + ".jpg"))
                    else:
                        print("already exists")
                    ## move incorrectly named xml if it one of the same name has not already been moved
                    if not os.path.exists(os.path.join(incorrect_imgs_positive_xml_dir_path, img_name + ".xml")):
                        shutil.copy(labeled_xml_path, os.path.join(incorrect_imgs_positive_xml_dir_path, img_name + ".xml")) #destination
                    else:
                        print("already exists")

def relocate_incorrect_image_content_and_naming(img_anno_directory, incorrect_named_correctly_chipped_dir, tile_dir):
    """ 
    Identify images where the name and content are not correctly alligned (the tile_name and row/col do not match the content);
    then rellocate to a new folder
    Args: 
    img_anno_directory(str): path to folder containing img and annotations for each tile by each folder (correct naming convention)
    tiles_dir(str): path to folder containing tiles
    incorrect_named_correctly_chipped_dir(str): path to folder that will contain all of the incorrectly named images (correctly chippeD)
    """
    tile_names = sorted(os.listdir(img_anno_directory))
    for tile_name in tqdm.tqdm(tile_names):
        # get paths to all positive images/mls
        img_path = os.path.join(img_anno_directory, tile_name, "chips_positive")
        xml_path = os.path.join(img_anno_directory, tile_name, "chips_positive_xml")
        remove_thumbs(img_path)
        # get all the image and xml paths in directory of annotated images
        img_paths = sorted(glob(img_path + "/*.jpg", recursive = True))
        xml_paths = sorted(glob(xml_path + "/*.xml", recursive = True))
        ## get path to directory containing chipped images 
        tile_to_chips_path = os.path.join(img_anno_directory, tile_name, "chips")
        #read in tile
        tile_path = os.path.join(tile_dir, tile_name + ".tif")
        tile = cv2.imread(tile_path, cv2.IMREAD_UNCHANGED) 
        #get the image names 
        img_name_wo_ext = []
        for i, (img_path, xml_path) in enumerate(zip(img_paths, xml_paths)):
            #get image name 
            img_name = os.path.splitext(os.path.basename(img_path))[0]
            img_name_wo_ext.append(img_name)
            ## load labeled image
            gray_labeled_img = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2GRAY) #image that had been labeled
            ## load correct image from tile             
            y, x = img_name.split("_")[-2:] #name of tif with the extension removed; y=row;x=col
            t_2_chip = tile_to_chip_array(tile, int(x), int(y), int(512)) # load tile to chip
            gray_t_2_chip = cv2.cvtColor(t_2_chip.astype(np.uint8), cv2.COLOR_BGR2GRAY) # make gray
            
            ## check if images are the same
            (score, diff) = compare_ssim(gray_labeled_img, gray_t_2_chip, full=True)

            if score < 0.95: #If the labeled image is inccorrect
                # create and specify new directory path for chips
                chips_dir_path = os.path.join(incorrect_named_correctly_chipped_dir, tile_name, "chips")
                chips_dir = os.makedirs(chips_dir_path, exist_ok=True)
                ## move correct chip
                t_2_chip_4_labeled_img_path = os.path.join(tile_to_chips_path,  img_name + ".jpg")
                shutil.copy(t_2_chip_4_labeled_img_path, os.path.join(chips_dir_path, img_name + ".jpg"))
                # create and specify new directory paths for positive chips
                chips_positive_dir_path = os.path.join(incorrect_named_correctly_chipped_dir, tile_name, "chips_positive")
                chips_positive_dir = os.makedirs(chips_positive_dir_path, exist_ok=True)
                ## move incorrectly named image if it one of the same name has not already been moved
                if not os.path.exists(os.path.join(chips_positive_dir_path, img_name + ".jpg")):
                    shutil.move(img_path, os.path.join(chips_positive_dir_path, img_name + ".jpg")) 
                else:
                    print("already exists")
                    
                #create and specify new directory paths for annotations
                chips_positive_xml_dir_path = os.path.join(incorrect_named_correctly_chipped_dir, tile_name, "chips_positive_xml")
                chips_positive_xml_dir = os.makedirs(chips_positive_xml_dir_path, exist_ok=True)
                ## move annotation corresponding to incorrectly named image if it one of the same name has not already been moved
                if not os.path.exists(os.path.join(chips_positive_xml_dir_path, img_name + ".xml")):
                    shutil.move(xml_path, os.path.join(chips_positive_xml_dir_path, img_name + ".xml")) 
                else:
                    print("already exists")
                    
def identify_correct_name_incorrectly_named_chipped_images(img_anno_directory, incorrect_named_correctly_chipped_dir, tile_dir):
    """ 
    Where images are named incorrectly, but have the correct naming convention; 
    identify if the image corresponds with another image within a tile and move the image and annotation
    Args: 
    img_anno_directory(str): path to folder containing img and annotations for each tile by each folder (correct naming convention)
    tiles_dir(str): path to folder containing tiles
    incorrect_named_correctly_chipped_dir(str): path to folder that will contain all of the incorrectly named images (correctly chippeD)
     """
    tile_names = sorted(os.listdir(incorrect_named_correctly_chipped_dir))
    for tile_name in tqdm.tqdm(tile_names):
        #print(tile_name)
        incorrectly_named_img_dir = os.path.join(incorrect_named_correctly_chipped_dir, tile_name, "chips_positive")
        incorrectly_named_xml_dir = os.path.join(incorrect_named_correctly_chipped_dir, tile_name, "chips_positive_xml")
        incorrectly_named_img_paths = sorted(glob(incorrectly_named_img_dir + "/*.jpg", recursive = True))
        if len(incorrectly_named_img_paths) > 0:
            #load tile
            tile_path = os.path.join(tile_dir, tile_name + ".tif")
            tile = cv2.imread(tile_path, cv2.IMREAD_UNCHANGED) 
            #tile characteristics
            tile_height,  tile_width,  tile_channels = tile.shape #the size of the tile #determine tile dimensions
            row_index = math.ceil(tile_height/512) #divide the tile into 512 by 512 chips (rounding up)
            col_index = math.ceil(tile_width/512)
            #specify path with correct images
            img_dir_path = os.path.join(img_anno_directory, tile_name, "chips_positive") ## path positive images
            xml_dir_path = os.path.join(img_anno_directory, tile_name, "chips_positive_xml") ## path annotations 

            for y in range(0, row_index): # rows
                for x in range(0, col_index): # cols
                    t_2_chip = tile_to_chip_array(tile, x, y, int(512)) # load tile to chip
                    gray_t_2_chip = cv2.cvtColor(t_2_chip.astype(np.uint8), cv2.COLOR_BGR2GRAY) # make gray

                    for incorrectly_named_img_path in incorrectly_named_img_paths:
                        gray_incorrectly_named_img = cv2.cvtColor(cv2.imread(incorrectly_named_img_path), cv2.COLOR_BGR2GRAY) #read incorrect image
                        (score, diff) = compare_ssim(gray_t_2_chip, gray_incorrectly_named_img, full = True)

                        if score >= 0.95: #Save the same images
                            correct_img_name = tile_name + '_' + f"{y:02}"  + '_' + f"{x:02}" + '.jpg' # The index is a six-digit number like '000023'.
                            correct_xml_name = tile_name + '_' + f"{y:02}"  + '_' + f"{x:02}" + '.xml' # The index is a six-digit number like '000023'.

                            incorrect_img_name = os.path.splitext(os.path.basename(incorrectly_named_img_path))[0]
                            incorrectly_named_img_paths.remove(incorrectly_named_img_path)

                            #move image and rename
                            shutil.move(os.path.join(incorrectly_named_img_dir,  incorrect_img_name + ".jpg"), #source
                                        os.path.join(img_dir_path, correct_img_name)) #destination                                  

                            #move anno and rename
                            shutil.move(os.path.join(incorrectly_named_xml_dir, incorrect_img_name + ".xml"), #source
                                        os.path.join(xml_dir_path, correct_xml_name)) #destination
                        
###########################################################################################################
############################# Identify incorrect/correct images ###########################################
def identify_correct_images(tile_dir, tiles_in_directory, 
                            images_in_directory, images_in_directory_array,
                            image_directories):
    """
    Find images that do not align with the tiles chipped ####flipped rows and columns####
    Confirm that the standard tile name in the chip and the contents of the chip match
    """
    #index over the tiles with corresponding images in the given directory
    tile_names = []
    correct_chip_names = []
    correct_chip_paths = []
    ys = []
    xs = []
    #correct_0_incorrect_1_images = []

    #same_image_counter = 0
    for tile_name in tiles_in_directory: 
        file_name, ext = os.path.splitext(tile_name) # File name
        
        #get tile shape
        item_dim = int(512)          
        tile = cv2.imread(os.path.join(tile_dir, tile_name),cv2.IMREAD_UNCHANGED) 
        tile_height,  tile_width,  tile_channels = tile.shape #the size of the tile #determine tile dimensions
        row_index = math.ceil(tile_height/512) #divide the tile into 512 by 512 chips (rounding up)
        col_index = math.ceil(tile_width/512)

        count = 1  
        for y in range(0, col_index): #rows
            for x in range(0, row_index): #cols
                chip_name_temp = file_name+ '_' + str(count).zfill(6) + '.jpg'
                #create a numpy array of each correctly chipped images 
                correct_image = tile_to_chip_array(tile, x, y, item_dim)
                count += 1  

                #Identify if images that are contained in the directory of interest
                confirmed_chips = [string for string in images_in_directory if chip_name_temp in string]
                if len(confirmed_chips) > 0:
                    for confirmed_chip in confirmed_chips: #there may be duplicate images corresponding to the same standard tile name (nj and ny overlap)
                    #obtain a numpy array of the image in the directory of interest
                        index, = np.where(images_in_directory == confirmed_chip)
                        image_in_directory_array = images_in_directory_array[index[0]] #use the actual value of index (saved as an array)
                        image_directory = image_directories[index[0]]
                        ##https://pyimagesearch.com/2017/06/19/image-difference-with-opencv-and-python/
                        #https://pyimagesearch.com/2014/09/15/python-compare-two-images/
                        gray_image_in_directory_array = cv2.cvtColor(image_in_directory_array, cv2.COLOR_BGR2GRAY)
                        gray_correct_image = cv2.cvtColor(correct_image, cv2.COLOR_BGR2GRAY)
                        (score, diff) = compare_ssim(gray_image_in_directory_array, gray_correct_image, full=True)
                        diff = (diff * 255).astype("uint8")
                        if score >= 0.90:
                            tile_names.append(tile_name)
                            xs.append(x)
                            ys.append(y)
                            correct_chip_names.append(confirmed_chip)
                            correct_chip_paths.append(os.path.join(image_directory,confirmed_chip))
                        if (score < 0.90) and (score >= 0.80):                           
                            fig, (ax1, ax2) = plt.subplots(1, 2)
                            ax1.set_title('correct_image')
                            ax1.imshow(correct_image)
                            ax2.set_title('labeled_chip_array')
                            ax2.imshow(image_in_directory_array)
                            plt.show() 

    return(tile_names, xs, ys, correct_chip_names, correct_chip_paths)


def identify_incorrect_images(tile_dir, tiles_in_directory, 
                          images_in_directory, images_in_directory_array,
                             image_directories):
    """
    Find images that do not align with the tile chip
    Confirm that the standard tile name in the chip and the contents of the chip match
    """
    #index over the tiles with corresponding images in the given directory
    tile_names = []
    incorrect_chip_names = []
    incorrect_chip_paths = []
    ys = []
    xs = []
    #correct_0_incorrect_1_images = []

    #same_image_counter = 0
    for tile_name in tiles_in_directory: 
        file_name, ext = os.path.splitext(tile_name) # File name
        
        #get tile shape
        item_dim = int(512)          
        tile = cv2.imread(os.path.join(tile_dir, tile_name),cv2.IMREAD_UNCHANGED) 
        tile_height,  tile_width,  tile_channels = tile.shape #the size of the tile #determine tile dimensions
        row_index = math.ceil(tile_height/512) #divide the tile into 512 by 512 chips (rounding up)
        col_index = math.ceil(tile_width/512)

        count = 1  
        for y in range(0, col_index):
            for x in range(0, row_index):
                chip_name_temp = file_name+ '_' + str(count).zfill(6) + '.jpg'
                #create a numpy array of each correctly chipped images 
                correct_image = tile_to_chip_array(tile, x, y, item_dim)
                count += 1  

                #Identify if images that are contained in the directory of interest
                confirmed_chips = [string for string in images_in_directory if chip_name_temp in string]
                if len(confirmed_chips) > 0:
                    for confirmed_chip in confirmed_chips: #there may be duplicate images corresponding to the same standard tile name (nj and ny overlap)
                    #obtain a numpy array of the image in the directory of interest
                        index, = np.where(images_in_directory == confirmed_chip)
                        image_in_directory_array = images_in_directory_array[index[0]] #use the actual value of index (saved as an array)
                        image_directory = image_directories[index[0]]
                        ##https://pyimagesearch.com/2017/06/19/image-difference-with-opencv-and-python/
                        #https://pyimagesearch.com/2014/09/15/python-compare-two-images/
                        gray_image_in_directory_array = cv2.cvtColor(image_in_directory_array, cv2.COLOR_BGR2GRAY)
                        gray_correct_image = cv2.cvtColor(correct_image, cv2.COLOR_BGR2GRAY)
                        (score, diff) = compare_ssim(gray_image_in_directory_array, gray_correct_image, full=True)
                        diff = (diff * 255).astype("uint8")
                        #if score >= 0.90:
                        #    correct_0_incorrect_1_images.append(0)

                        if score < 0.90: 
                            #print("different image")
                            tile_names.append(tile_name)
                            xs.append(x)
                            ys.append(y)
                            incorrect_chip_names.append(confirmed_chip)
                            incorrect_chip_paths.append(os.path.join(image_directory,confirmed_chip))
                            #print("SSIM: {}".format(score))
                            #correct_0_incorrect_1_images.append(1)

    return(tile_names, xs, ys, incorrect_chip_names, incorrect_chip_paths)

def identify_incorrect_images_simultaneous(tile_dir, tiles_in_directory, images_path):
    """
    Find images that do not align with the tile chip
    Confirm that the standard tile name in the chip and the contents of the chip match
    """
    #index over the tiles with corresponding images in the given directory
    tile_names = []
    incorrect_chip_names = []
    incorrect_chip_paths = []
    ys = []
    xs = []
    #correct_0_incorrect_1_images = []

    #same_image_counter = 0
    for tile_name in tqdm.tqdm(tiles_in_directory): 
        file_name, ext = os.path.splitext(tile_name) # File name
        
        #get tile shape
        item_dim = int(512)          
        tile = cv2.imread(os.path.join(tile_dir, tile_name),cv2.IMREAD_UNCHANGED) 
        tile_height,  tile_width,  tile_channels = tile.shape #the size of the tile #determine tile dimensions
        row_index = math.ceil(tile_height/512) #divide the tile into 512 by 512 chips (rounding up)
        col_index = math.ceil(tile_width/512)

        count = 1  
        for y in range(0, col_index):
            for x in range(0, row_index):
                chip_name_temp = file_name+ '_' + str(count).zfill(6) + '.jpg'
                #create a numpy array of each correctly chipped images 
                correct_image = tile_to_chip_array(tile, x, y, item_dim)
                count += 1  

                #Identify if images that are contained in the directory of interest
                labeled_chip_paths = [string for string in images_path if chip_name_temp in string]
                if len(labeled_chip_paths) > 0:
                    for labeled_chip_path in labeled_chip_paths: #there may be duplicate images corresponding to the same standard tile name (nj and ny overlap)
                    #obtain a numpy array of the image in the directory of interest
                        index, = np.where(images_path == labeled_chip_path)
                        labeled_chip_array = cv2.imread(os.path.join(images_path[index[0]]),cv2.IMREAD_UNCHANGED) #open image

                        ##https://pyimagesearch.com/2017/06/19/image-difference-with-opencv-and-python/
                        #https://pyimagesearch.com/2014/09/15/python-compare-two-images/
                        gray_labeled_chip_array = cv2.cvtColor(labeled_chip_array, cv2.COLOR_BGR2GRAY)
                        gray_correct_image = cv2.cvtColor(correct_image, cv2.COLOR_BGR2GRAY)
                        (score, diff) = compare_ssim(gray_labeled_chip_array, gray_correct_image, full=True)
                        diff = (diff * 255).astype("uint8")
                        #if score >= 0.90:
                        #    correct_0_incorrect_1_images.append(0)

                        if score < 0.90: 
                            #print("different image")
                            tile_names.append(tile_name)
                            xs.append(x)
                            ys.append(y)
                            incorrect_chip_paths.append(labeled_chip_path)
                            #print("SSIM: {}".format(score))
                            #correct_0_incorrect_1_images.append(1)
    return(tile_names, xs, ys, incorrect_chip_paths)