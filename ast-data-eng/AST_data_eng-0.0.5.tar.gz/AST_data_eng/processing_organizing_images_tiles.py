############################################################################################################
###########################################   Remove Thumbs    #############################################
############################################################################################################
def remove_thumbs(path_to_folder_containing_images):
    """ Remove Thumbs.db file from a given folder
    Args: 
        path_to_folder_containing_images(str): path to folder containing images
    """
    if len(glob(path_to_folder_containing_images + "/*.db", recursive = True)) > 0:
        os.remove(glob(path_to_folder_containing_images + "/*.db", recursive = True)[0])
    
def remove_thumbs_all_positive_chips(parent_directory):
    """ Remove Thumbs.db file from all chips_positive folders in parent directory
    Args: 
        parent_directory (str): path to parent directory
    """
    for r, d, f in os.walk(parent_directory):
        folder_name = os.path.basename(r) #identify folder name
        if 'chips_positive' == folder_name: #Specify folders that contain positive chips
            remove_thumbs(r)

########### Extract information from tile_names_tile urls numpy arrays ##########
def add_formatted_and_standard_tile_names_to_tile_names_time_urls(tile_names_tile_urls):
    #get a list of the formated tile names
    tile_names = []
    for tile_url in tile_names_tile_urls:
        tile_url = tile_url[1].rsplit("/",3)
        #get the quad standard tile name 
        tile_name = tile_url[3]
        tile_name = os.path.splitext(tile_name)[0] 
        #format tile_names to only include inital capture date 1/20
        if tile_name.count("_") > 5:
            tile_name = tile_name.rsplit("_",1)[0]
        #get the tile name formated (1/14/2022)
        tile_name_formatted = tile_url[1] + "_" + tile_url[2] + "_" + tile_url[3]
        tile_name_formatted = os.path.splitext(tile_name_formatted)[0] 
        tile_names.append([tile_name, tile_name_formatted])
    
    #create array that contains the formated tile_names and tile_names
    tile_names_tile_urls_formatted_tile_names = np.hstack((tile_names_tile_urls, np.array(tile_names)))
    
    return(tile_names_tile_urls_formatted_tile_names)

def unique_formatted_standard_tile_names(tile_names_tile_urls_complete_array):
    unique_tile_name_formatted, indicies = np.unique(tile_names_tile_urls_complete_array[:,3], return_index = True)
    tile_names_tile_urls_complete_array_unique_formatted_tile_names = tile_names_tile_urls_complete_array[indicies,:]
    print("unique formatted tile names", tile_names_tile_urls_complete_array_unique_formatted_tile_names.shape) 

    unique_tile_name_standard, indicies = np.unique(tile_names_tile_urls_complete_array[:,2], return_index = True)
    tile_names_tile_urls_complete_array_unique_standard_tile_names = tile_names_tile_urls_complete_array[indicies,:]
    print("unique standard tile names", tile_names_tile_urls_complete_array_unique_standard_tile_names.shape) 
    
    return(tile_names_tile_urls_complete_array_unique_standard_tile_names, tile_names_tile_urls_complete_array_unique_formatted_tile_names)

################## Get tiles names or jpg names from jpg paths ####################
def jpg_path_to_tile_name_formatted(jpg_paths):
    tile_names = []
    for jpg_path in jpg_paths:
        base = os.path.basename(jpg_path)
        jpg = os.path.splitext(base)[0] #name of tif with the extension removed
        tile_name_formated_name = jpg.rsplit("_",1)[0] #name of tif with the extension removed
        tile_names.append(tile_name_formated_name)
    return(tile_names)

def jpg_path_to_jpg_name_formatted(jpg_paths):
    jpgs_ext = []
    jpgs_without_ext = []
    for jpg_path in jpg_paths:
        jpg_ext = os.path.basename(jpg_path)
        jpg_without_ext = os.path.splitext(jpg_ext)[0] #name of tif with the extension removed
        jpgs_ext.append(jpg_ext)
        jpgs_without_ext.append(jpg_without_ext)
    return(jpgs_ext, jpgs_without_ext)

def unique_positive_jpgs_from_parent_directory(parent_directory):
    files = []
    paths = []
    counter = 0
    # r=root, d=directories, f = files
    # https://mkyong.com/python/python-how-to-list-all-files-in-a-directory/
    for r, d, f in tqdm.tqdm(os.walk(parent_directory)):
        folder_name = os.path.basename(r) #identify folder name
        if 'chips_positive' == folder_name: #Specify folders that contain positive chips
            for file in f:
                if '.jpg' in file:
                    paths.append(os.path.join(r, file))
                    files.append(file)
                    counter += 1
    positive_jpgs = np.array((files,paths)).T
    unique_tile_name_formatted_positive_jpgs, indicies = np.unique(positive_jpgs[:,0], return_index = True)
    unique_positive_jpgs = positive_jpgs[indicies]
    print(unique_positive_jpgs.shape)

    return(unique_positive_jpgs)


## Processing Tiles
def move_tiles_of_verified_images_to_complete_dataset(tile_img_annotation, tiles_complete_dataset_path, path_to_verified_sets):
    """Move already downloaded tiles to completed dataset
    """
    #obtain the paths of tifs in the verified sets
    path_to_tifs_in_verified_sets = glob(path_to_verified_sets + "/**/*.tif", recursive = True)
    print("Number of tifs to be moved", len(path_to_tifs_in_verified_sets))

    #move verified tifs 
    for path in path_to_tifs_in_verified_sets:
        base = os.path.basename(path)
        tif = os.path.splitext(base)[0] #name of tif with the extension removed
        if tif in tile_img_annotation[:,0]:
            shutil.move(path, os.path.join(tiles_complete_dataset_path,base)) # copy images with matching .xml files in the "chips_tank" folder
            
def tiles_in_complete_dataset(tiles_complete_dataset_path):
    #Make a list of the tiles in the completed dataset
    os.makedirs(tiles_complete_dataset_path, exist_ok=True)
    
    tiles_downloaded = os.listdir(tiles_complete_dataset_path)
    tiles_downloaded_with_ext_list = []
    tiles_downloaded_without_ext_list = []
    
    for tile in tiles_downloaded:
        tiles_downloaded_with_ext_list.append(tile)
        tiles_downloaded_without_ext_list.append(os.path.splitext(tile)[0]) #name of tif with the extension removed
    return(np.array(tiles_downloaded_with_ext_list), np.array(tiles_downloaded_without_ext_list))

def jpg_paths_to_tiles_without_ext(jpg_paths):
    """
    Determine which tiles corresponding to jpg that have been annotated #jpg_tiles
    Get a numpy array of the unique standard tile names corresponding to a list of jpg paths
    Args:
    jpgs_paths(list): list of jpg paths
    Returns:
    tiles(numpy): 
    """
    tiles = []
    for path in jpg_paths:
        base = os.path.basename(path)
        img = os.path.splitext(base)[0] #name of tif with the extension removed
        tile = img.rsplit("_",1)[0]
        tile = tile.split("_",4)[4] #get the tile names to remove duplicates from being downloaded
        tiles.append(tile)
    return(np.unique(tiles))
##############################################################################################################################
###################################                  Chip Tiles              #################################################
##############################################################################################################################
def tile_to_chip_array(tile, x, y, item_dim):
    """
    ##
    x: col index
    y: row index
    """
    dimensions = tile.shape[2]
    chip_img = tile[y*item_dim:y*item_dim+item_dim, x*(item_dim):x*(item_dim)+item_dim]
    #add in back space if it is the edge of an image
    if (chip_img.shape[0] != 512) & (chip_img.shape[1] != 512): #width
        #print("Incorrect Width")
        chip = np.zeros((512,512,dimensions), np.uint8)
        chip[0:chip_img.shape[0], 0:chip_img.shape[1]] = chip_img
        chip_img = chip
    if chip_img.shape[0] != 512:  #Height
        black_height = 512  - chip_img.shape[0] #Height
        black_width = 512 #- chip_img.shape[1] #width
        black_img = np.zeros((black_height,black_width,  dimensions), np.uint8)
        chip_img = np.concatenate([chip_img, black_img])
    if chip_img.shape[1] != 512: #width
        black_height = 512 #- chip_img.shape[0] #Height
        black_width = 512 - chip_img.shape[1] #width
        black_img = np.zeros((black_height,black_width, dimensions), np.uint8)
        chip_img = np.concatenate([chip_img, black_img],1)
    return(chip_img)


############## Download Tiles ##########################################################################################
def download_tiles_of_verified_images(positive_images_complete_dataset_path, tiles_complete_dataset_path, tiles_downloaded, tile_names_tile_urls_complete_array):
    """
    # Download remaining tiles that correspond to ONLY to verified images
    #Gather the locations of tiles that have already been downlaoded and verified 
    """
    # Make a list of the tiles moved to completed dataset
    tiles_downloaded_with_ext, tiles_downloaded = tiles_in_complete_dataset(tiles_complete_dataset_path)
    
    positive_jpg_paths = glob(positive_images_complete_dataset_path + "/*.jpg", recursive = True)
    print("number of positive and verified images:", len(positive_jpg_paths))
    
    #  Determine which tiles corresponding to jpg that have been annotated #jpg_tiles
    positive_jpg_tiles = jpg_paths_to_tiles_without_ext(positive_jpg_paths)
    print("the number of tiles corresponding to verified images:", len(positive_jpg_tiles))

    # Identify tiles that have not already been downloaded
    tiles_to_download = []
    for tile in positive_jpg_tiles: #index over the downloaded tiled
        if tile not in tiles_downloaded: #index over the tiles that should be downloded
            tiles_to_download.append(tile)
    print("the number of tiles that need to be downloaded:", len(tiles_to_download))
    
    # Download Tiles  
    tile_names = []
    tile_urls = []
    file_names = []
    tile_names_without_year = []
    for tile in tiles_to_download:   
        ### download the tiles if they are not in the tiles folder 
        #check if the tile name is contained in the string of complete arrays
        tile_name = [string for string in tile_names_tile_urls_complete_array[:,0] if tile in string]          
        if len(tile_name) == 1: #A single tile name # get tile url from the first (only) entry
            tile_url = tile_names_tile_urls_complete_array[tile_names_tile_urls_complete_array[:,0]==tile_name[0]][0][1] 
            tile_names.append(tile_name[0])
            tile_urls.append(tile_url)
        elif len(np.unique(tile_name)) > 1: # Multiple (different tiles) possibly the same tiles in different states, possible different years
            tile_url = tile_names_tile_urls_complete_array[tile_names_tile_urls_complete_array[:,0]==tile_name[0]][0][1]# get tile url
            tile_names.append(tile_name[0])
            tile_urls.append(tile_url)
        elif (len(tile_name) > 1): #Multiple different tile names that are the same, probably different naip storage locations
            # get tile url from the second entry 
            tile_url = tile_names_tile_urls_complete_array[tile_names_tile_urls_complete_array[:,0]==tile_name[1]][1][1] 
            tile_names.append(tile_name[1])
            tile_urls.append(tile_url)
            
        #get file name
        file_name = tile_name[0]
        if tile_name[0].count("_") > 5:
            tile_name = tile_name[0].rsplit("_",1)[0]
            file_name = tile_name + ".tif"
        print(file_name)
        ### Download tile
        file_names.append(ap.download_url(tile_url, tiles_complete_dataset_path,
                                                     destination_filename = file_name,       
                                                             progress_updater=ap.DownloadProgressBar()))
    #get the tile_names without the year
    for file_name in file_names:
        tile_names_without_year.append(file_name.rsplit("_",1)[0])
        
    return(np.array((tile_names, tile_urls, file_names, tile_names_without_year)).T)


def downloaded_tifs_tile_names_tile_urls_file_names_tile_names_without_year(tile_path, tile_names_tile_urls_complete_array):
    #remove thumbs
    remove_thumbs(tile_path)
    tif_paths = glob(tile_path + "/**/*.tif", recursive = True)
    
    tile_names = []
    tile_urls = []
    file_names = [] 
    tile_names_without_year = []  
    
    for path in tif_paths:
        base = os.path.basename(path)
        tile_name = os.path.splitext(base)[0] #name of tif with the extension removed
        #check if the tile name is contained in the string of complete arrays
        tile_name = [string for string in tile_names_tile_urls_complete_array[:,0] if tile_name in string]      
        
        if len(tile_name) == 1: #A single tile name # get tile url from the first (only) entry
            tile_url = tile_names_tile_urls_complete_array[tile_names_tile_urls_complete_array[:,0]==tile_name[0]][0][1] 
            tile_names.append(tile_name[0])
            tile_urls.append(tile_url)
        elif len(np.unique(tile_name)) > 1: # Multiple (different tiles) possibly the same tiles in different states, possible different years
            tile_url = tile_names_tile_urls_complete_array[tile_names_tile_urls_complete_array[:,0]==tile_name[0]][0][1]# get tile url
            tile_names.append(tile_name[0])
            tile_urls.append(tile_url)
        elif (len(tile_name) > 1): #Multiple different tile names that are the same, probably different naip storage locations
            # get tile url from the second entry 
            tile_url = tile_names_tile_urls_complete_array[tile_names_tile_urls_complete_array[:,0]==tile_name[1]][1][1] 
            tile_names.append(tile_name[1])
            tile_urls.append(tile_url)

        #get file name
        file_name = tile_name[0]
        if tile_name[0].count("_") > 5:
            tile_name = tile_name[0].rsplit("_",1)[0]
            file_name = tile_name + ".tif"
        file_names.append(file_name)
        ### Download tile
        
    #get the tile_names without the year
    for file_name in file_names:
        tile_names_without_year.append(file_name.rsplit("_",1)[0])
    
    return(np.array((tile_names, tile_urls, file_names, tile_names_without_year)).T)

####### add chips to rechip folder ############################################################
def add_chips_to_chip_folders(rechipped_image_path, tile_name):
    """ 
    Args:
        remaining_chips_path (str): path to folder that will contain all of the remaining images
            that have not been labeled and correspond to tiles that have labeled images
        tile_name (str): name of tile without of extension
    """
    chips_path = os.path.join(rechipped_image_path, tile_name, "chips")
    os.makedirs(chips_path, exist_ok=True)
    
    item_dim = int(512)
    tile = cv2.imread(os.path.join(tiles_complete_dataset_path, tile_name + ".tif"),cv2.IMREAD_UNCHANGED)
    tile_height,  tile_width,  tile_channels = tile.shape #the size of the tile 
    row_index = math.ceil(tile_height/512) 
    col_index = math.ceil(tile_width/512)
    #print(row_index, col_index)

    count = 1            
    for y in range(0, row_index): #rows
        for x in range(0, col_index): #cols
            chip_img = tile_to_chip_array(tile, x, y, item_dim)
            #specify the chip names
            chip_name_correct_chip_name = tile_name + '_' + f"{y:02}"  + '_' + f"{x:02}" + '.jpg' # The index is a six-digit number like '000023'.
            if not os.path.exists(os.path.join(chips_path, chip_name_correct_chip_name)):
                cv2.imwrite(os.path.join(chips_path, chip_name_correct_chip_name), chip_img) #save images  