###################################################################################################################
######################################   Create Tile level  XMLs  #################################################
###################################################################################################################                
def create_tile_xml(tile_name, xml_directory, tile_resolution, tile_year, 
                tile_width, tile_height, tile_band):
    tile_name_ext = tile_name + ".tif"
    root = et.Element("annotation")
    folder = et.Element("folder") #add folder to xml
    folder.text = "tiles" #folder
    root.insert(0, folder)
    filename = et.Element("filename") #add filename to xml
    filename.text = tile_name_ext #filename
    root.insert(1, filename)
    path = et.Element("path") #add path to xml
    path.text = os.path.join(xml_directory, tile_name_ext) #path
    root.insert(2, path)
    resolution = et.Element("resolution") #add resolution to xml
    resolution.text = tile_resolution #resolution
    root.insert(3, resolution)
    year = et.Element("year") #add year to xml
    year.text = tile_year #year
    root.insert(4,year)
    source = et.Element("source") #add database to xml
    database = et.Element("database")
    database.text = "Tile Level Annotation" #
    source.insert(0, database)
    root.insert(5,source)
    size = et.Element("size") #add size to xml
    width = et.Element("width")
    width.text = str(tile_width) #width
    size.insert(0, width)
    height = et.Element("height")
    height.text = str(tile_height) #height
    size.insert(1, height)
    depth = et.Element("depth")
    depth.text = str(tile_band) #depth
    size.insert(2, depth)
    root.insert(6,size)
    tree = et.ElementTree(root)
    et.indent(tree, space="\t", level=0)
    #tree.write("filename.xml")
    tree.write(os.path.join(xml_directory, tile_name +".xml"))     
    
def add_objects(xml_directory, tile_name, obj_class, 
                obj_truncated, obj_difficult, obj_chip_name,
                obj_xmin, obj_ymin, obj_xmax, obj_ymax):
    tree = et.parse(os.path.join(xml_directory, tile_name + ".xml"))
    root = tree.getroot() 
    obj = et.Element("object") #add size to xml
    
    name = et.Element("name") #class
    name.text = str(obj_class) 
    obj.insert(0, name)
    
    pose = et.Element("pose") #pose
    pose.text = "Unspecified" 
    obj.insert(1, pose)
    
    truncated = et.Element("truncated")
    truncated.text = str(obj_truncated) #
    obj.insert(2, truncated)

    difficult = et.Element("difficult")
    difficult.text = str(obj_difficult)
    obj.insert(3, difficult)
 
    chip_name = et.Element("chip_name")
    chip_name.text = str(obj_chip_name)
    obj.insert(4, chip_name)

    bndbox = et.Element("bndbox") #bounding box
    xmin = et.Element("xmin") #xmin
    xmin.text = str(obj_xmin) 
    bndbox.insert(0, xmin)
    ymin = et.Element("ymin") #ymin
    ymin.text = str(obj_ymin) 
    bndbox.insert(1, ymin)
    xmax = et.Element("xmax") #xmax
    xmax.text = str(obj_xmax) 
    bndbox.insert(2, xmax)
    ymax = et.Element("ymax") #ymax
    ymax.text = str(obj_ymax) 
    bndbox.insert(3, ymax)
    obj.insert(5, bndbox)
    
    root.append(obj)
    tree = et.ElementTree(root)
    et.indent(tree, space="\t", level=0)
    tree.write(os.path.join(xml_directory, tile_name +".xml"))   
    
def generate_tile_xmls(images_and_xmls_by_tile_path, tiles_dir, tiles_xml_path, item_dim):
    folders_of_images_xmls_by_tile = os.listdir(images_and_xmls_by_tile_path)
    for tile_name in tqdm.tqdm(folders_of_images_xmls_by_tile):
        tile_name_ext = tile_name + ".tif"
        #get tile dimensions ##replace with information from tile characteristics
        da = rioxarray.open_rasterio(os.path.join(tiles_dir, tile_name_ext))
        tile_band, tile_height, tile_width = da.shape[0], da.shape[1], da.shape[2]
        #specify image/xml paths for each tile
        positive_image_dir = os.path.join(images_and_xmls_by_tile_path, tile_name, "chips_positive")
        positive_xml_dir = os.path.join(images_and_xmls_by_tile_path, tile_name, "chips_positive_xml")
        #load a list of images/xmls for each tile
        positive_images = os.listdir(positive_image_dir)
        positive_xmls = os.listdir(positive_xml_dir)
                       
        for index, chip_xml in enumerate(positive_xmls):
            #identify rows and columns
            chip_name = os.path.splitext(chip_xml)[0]
            y, x = chip_name.split("_")[-2:] #name of tif with the extension removed; y=row;x=col
            y = int(y)
            x = int(x)
            minx = x*item_dim
            miny = y*item_dim
            #load each xml
            tree = et.parse(os.path.join(positive_xml_dir, chip_xml))
            root = tree.getroot()
            #create the tile xml
            if index == 0:
                resolution = root.find('resolution').text
                year = root.find('year').text
                create_tile_xml(tile_name, tiles_xml_path, resolution, year, 
                                tile_width, tile_height, tile_band)
            #add the bounding boxes
            for obj in root.iter('object'):
                xmlbox = obj.find('bndbox')
                obj_xmin = str(int(xmlbox.find('xmin').text) + minx)
                obj_xmax = str(int(xmlbox.find('xmax').text) + minx)
                obj_ymin = str(int(xmlbox.find('ymin').text) + miny)
                obj_ymax = str(int(xmlbox.find('ymax').text) + miny)
                add_objects(tiles_xml_path, tile_name, obj.find('name').text, obj.find('truncated').text, 
                            obj.find('difficult').text, chip_name, obj_xmin, obj_ymin, obj_xmax, obj_ymax)
###################################################################################################################
####################################     Merge tile level XMLs to GDF   ###########################################
###################################################################################################################               
#Generate two text boxes a larger one that covers them
def merge_boxes(bbox1, bbox2):
    """ Generate a bounding box that covers two bounding boxes
    Arg:
    bbox1(list): a list of the (ymin, xmin, ymax, xmax) coordinates for box 1 
    bbox2(list): a list of the (ymin, xmin, ymax, xmax) coordinates for box 2
    Returns:
    merged_bbox(list): a list of the (ymin, xmin, ymax, xmax) coordinates for the merged bbox

    """
    return [min(bbox1[0], bbox2[0]), 
         min(bbox1[1], bbox2[1]), 
         max(bbox1[2], bbox2[2]),
         max(bbox1[3], bbox2[3])]

#Computer a Matrix similarity of distances of the text and object
def calc_sim(bbox1, bbox2, dist_limit):
    """Determine the similarity of distances between bboxes to determine whether bboxes should be merged 
    Arg:
    bbox1(list): a list of the (xmin, ymin, xmax, ymax) coordinates for box 1 
    bbox2(list): a list of the (xmin, ymin, xmax, ymax) coordinates for box 2
    dist_list(int): the maximum threshold (pixel distance) to merge bounding boxes
    Returns:
    (bool): to indicate whether the bboxes should be merged 
    """

    # text: ymin, xmin, ymax, xmax
    # obj: ymin, xmin, ymax, xmax
    bbox1_xmin, bbox1_ymin, bbox1_xmax, bbox1_ymax = bbox1
    bbox2_xmin, bbox2_ymin, bbox2_xmax, bbox2_ymax = bbox2
    x_dist = min(abs(bbox2_xmin-bbox1_xmax), abs(bbox2_xmax-bbox1_xmin))
    y_dist = min(abs(bbox2_ymin-bbox1_ymax), abs(bbox2_ymax-bbox1_ymin))
        
    #define distance if one object is inside the other
    if (bbox2_xmin <= bbox1_xmin) and (bbox2_ymin <= bbox1_ymin) and (bbox2_xmax >= bbox1_xmax) and (bbox2_ymax >= bbox1_ymax):
        return(True)
    elif (bbox1_xmin <= bbox2_xmin) and (bbox1_ymin <= bbox2_ymin) and (bbox1_xmax >= bbox2_xmax) and (bbox1_ymax >= bbox2_ymax):
        return(True)
    #determine if the bboxes are suffucuently close to each other 
    elif (x_dist <= dist_limit) and (abs(bbox2_ymin-bbox1_ymin) <= dist_limit*3) and (abs(bbox2_ymax-bbox1_ymax) <= dist_limit*3):
        return(True)
    elif (y_dist <= dist_limit) and (abs(bbox2_xmin-bbox1_xmin) <= dist_limit*3) and (abs(bbox2_xmax-bbox1_xmax) <= dist_limit*3):
        return(True)
    else: 
        return(False)

def merge_algo(characteristics, bboxes, dist_limit):
    merge_bools = [False] * len(characteristics)
    for i, (char1, bbox1) in enumerate(zip(characteristics, bboxes)):
        for j, (char2, bbox2) in enumerate(zip(characteristics, bboxes)):
            if j <= i:
                continue
            # Create a new box if a distances is less than disctance limit defined 
            merge_bool = calc_sim(bbox1, bbox2, dist_limit) 
            if merge_bool == True:
            # Create a new box  
                new_box = merge_boxes(bbox1, bbox2)   
                bboxes[i] = new_box
                #delete previous text boxes
                del bboxes[j]
                
                # Create a new text string
                ##chip_name list
                if char1[0] != char2[0]: #if the chip_names are not the same
                    #make chip_names into an array
                    if type(char1[0]) == str: 
                        chip_names_1 = np.array([char1[0]])
                    if type(char2[0]) == str:
                        chip_names_2 = np.array([char2[0]])
                    chip_names = np.concatenate((chip_names_1, chip_names_2),axis=0)
                    chip_names = np.unique(chip_names).tolist()
                else:
                    chip_names = np.unique(char1[0]).tolist()  #if the chip_names are not the same
                
                #get object type 
                if char1[1] != char2[1]:
                    object_type = 'undefined_object'
                object_type = char1[1]
                
                characteristics[i] = [chip_names, object_type, 'Unspecified', '1', '1']
                #delete previous text 
                del characteristics[j]
                
                #return a new boxes and new text string that are close
                merge_bools[i] = True
    return merge_bools, characteristics, bboxes

def calculate_diameter(bbox, resolution = 0.6):
    """ Calculate the diameter of a given bounding bbox for imagery of a given resolution
    Arg:
    bbox(list): a list of the (xmin, ymin, xmax, ymax) coordinates for box 
    resolution(float): the (gsd) resolution of the imagery
    Returns:
    (diameter): the diameter of the bbox of interest
    """
    obj_xmin, obj_ymin, obj_xmax, obj_ymax = bbox
    obj_width = obj_xmax - obj_xmin
    obj_height = obj_ymax - obj_ymin
    diameter = min(obj_width, obj_height) * resolution #meter
    return(diameter)

def merge_tile_annotations(tile_characteristics, tiles_xml_dir, tiles_xml_list = None, 
                           distance_limit = 5):
    # https://stackoverflow.com/questions/55593506/merge-the-bounding-boxes-near-by-into-one
    #specify tiles_xml_list
    if tiles_xml_list is None: #if tiles_xml_list not provided, specify the tiles xml list
        tiles_xml_list = os.listdir(tiles_xml_dir)
    #lists for geosons/geodatabase
    tile_names = []
    chip_names = []
    object_class = []
    merged_bbox = []
    geometry = []  
    minx_polygon_pixels = []
    miny_polygon_pixels = []
    maxx_polygon_pixels = []
    maxy_polygon_pixels = []
    polygon_vertices_pixels = []
    nw_corner_polygon_lat = []
    nw_corner_polygon_lon = []
    se_corner_polygon_lat = []
    se_corner_polygon_lon = []
    polygon_vertices_lon_lat = []
    utm_projection = []
    diameter = []
    for tile_xml in tqdm.tqdm(tiles_xml_list): #iterate over tiles
        #save bboxes and characteristics
        trunc_diff_objs_bboxes = []
        trunc_diff_objs_characteristics = []
        remaining_objs_bboxes = []
        remaining_objs_characteristics = []
        #get tilename/tile xml path
        tile_name = os.path.splitext(tile_xml)[0]
        tile_xml_path = os.path.join(tiles_xml_dir, tile_xml)
        #load tile characteristics 
        tile_characteristics_subset = tile_characteristics[tile_characteristics.loc[:,"tile_name"] == tile_name]
        tile_width = tile_characteristics_subset["tile_widths"].values[0]
        tile_height = tile_characteristics_subset["tile_heights"].values[0]
        tile_utmx_array = np.linspace(tile_characteristics_subset["min_utmx"].values[0], 
                                      tile_characteristics_subset["max_utmx"].values[0],
                                      tile_width)
        
        tile_utmy_array = np.linspace(tile_characteristics_subset["min_utmy"].values[0], 
                                      tile_characteristics_subset["max_utmy"].values[0],
                                      tile_height)
        utm_proj = tile_characteristics_subset["utm_projection"].values[0]
        #load each xml
        tree = et.parse(tile_xml_path)
        root = tree.getroot()
        for obj in root.iter('object'):
            xmlbox = obj.find('bndbox') #get the bboxes
            obj_xmin = xmlbox.find('xmin').text
            obj_ymin = xmlbox.find('ymin').text
            obj_xmax = xmlbox.find('xmax').text
            obj_ymax = xmlbox.find('ymax').text
            if int(obj_xmax) > tile_width:
                obj_xmax = tile_width
            if int(obj_ymax) > tile_height:
                obj_ymax = tile_height
            if (int(obj.find('difficult').text) == 1) or (int(obj.find('truncated').text) == 1): #get truncated bboxes/characteristics
                trunc_diff_objs_bboxes.append([obj_xmin, obj_ymin, obj_xmax, obj_ymax])
                trunc_diff_objs_characteristics.append([obj.find('chip_name').text, obj.find('name').text, obj.find('pose').text, 
                                                        obj.find('truncated').text, obj.find('difficult').text])
            else: #get remaining bboxes/characteristics
                remaining_objs_bboxes.append([obj_xmin, obj_ymin, obj_xmax, obj_ymax])
                remaining_objs_characteristics.append([obj.find('chip_name').text, obj.find('name').text, obj.find('pose').text, 
                                                        obj.find('truncated').text, obj.find('difficult').text])
        
        # Add merge bboxes
        trunc_diff_objs_bboxes = np.array(trunc_diff_objs_bboxes).astype(np.int32)
        trunc_diff_objs_bboxes = trunc_diff_objs_bboxes.tolist()
        merged_bools, merged_characteristics, merged_bboxes =  merge_algo(trunc_diff_objs_characteristics,
                                                                      trunc_diff_objs_bboxes, distance_limit) #merge
        for j, (merged_bool, char, bbox) in enumerate(zip(merged_bools, merged_characteristics, merged_bboxes)):
            tile_names.append(tile_name)
            chip_names.append(char[0])
            object_class.append(char[1])
            #state whether bbox were merged
            merged_bbox.append(merged_bool)
            #pixel coordiantes, 0 indexed
            minx = bbox[0] - 1
            miny = bbox[1] - 1
            maxx = bbox[2] - 1
            maxy = bbox[3] - 1 
            minx_polygon_pixels.append(minx)
            miny_polygon_pixels.append(miny)
            maxx_polygon_pixels.append(maxx)
            maxy_polygon_pixels.append(maxy)
            polygon_vertices_pixels.append([(minx,miny), (minx,maxy), (maxx,maxy), (maxx,miny)])
            #geospatial data          
            utm_projection.append(utm_proj)
            min_lon, min_lat = transform_point_utm_to_wgs84(utm_proj, tile_utmx_array[minx], tile_utmy_array[miny])
            max_lon, max_lat = transform_point_utm_to_wgs84(utm_proj, tile_utmx_array[maxx], tile_utmy_array[maxy])
            nw_corner_polygon_lon.append(min_lon)
            nw_corner_polygon_lat.append(min_lat)
            se_corner_polygon_lon.append(max_lon)
            se_corner_polygon_lat.append(max_lat)
            polygon_vertices_lon_lat.append([(min_lon,min_lat),(min_lon,max_lat),(max_lon,max_lat),(max_lon,min_lat)])
            geometry.append(Polygon([(min_lon,min_lat),(min_lon,max_lat),(max_lon,max_lat),(max_lon,min_lat)]))
            #calculate diameter
            diameter.append(calculate_diameter(bbox))
            
        #Add remaining bboxes
        remaining_objs_bboxes = np.array(remaining_objs_bboxes).astype(np.int32)
        remaining_objs_bboxes = remaining_objs_bboxes.tolist()
        for j, (char, bbox) in enumerate(zip(remaining_objs_characteristics,remaining_objs_bboxes)):
            tile_names.append(tile_name)
            chip_names.append(char[0])
            object_class.append(char[1])
            #state whether bbox were merged
            merged_bbox.append(merged_bool)
            #pixel coordiantes 
            minx_polygon_pixels.append(bbox[0])
            miny_polygon_pixels.append(bbox[1])
            maxx_polygon_pixels.append(bbox[2])
            maxy_polygon_pixels.append(bbox[3])
            polygon_vertices_pixels.append([(bbox[0],bbox[1]), (bbox[0],bbox[3]), (bbox[2],bbox[3]), (bbox[2],bbox[1])])
            #geospatial data
            utm_projection.append(utm_proj)
            min_lon, min_lat = transform_point_utm_to_wgs84(utm_proj, tile_utmx_array[bbox[0]-1], tile_utmy_array[bbox[1]-1])
            max_lon, max_lat = transform_point_utm_to_wgs84(utm_proj, tile_utmx_array[bbox[2]-1], tile_utmy_array[bbox[3]-1])
            nw_corner_polygon_lon.append(min_lon)
            nw_corner_polygon_lat.append(min_lat)
            se_corner_polygon_lon.append(max_lon)
            se_corner_polygon_lat.append(max_lat)
            polygon_vertices_lon_lat.append([(min_lon,min_lat), (min_lon,max_lat), (max_lon,max_lat), (max_lon,min_lat)])
            geometry.append(Polygon([(min_lon,min_lat), (min_lon,max_lat), (max_lon,max_lat), (max_lon,min_lat)]))
            #calculate diameter
            diameter.append(calculate_diameter(bbox))
            
    #create geodatabase
    gdf = gpd.GeoDataFrame({'tile_name': tile_names,'chip_name': chip_names, 
            "minx_polygon_pixels": minx_polygon_pixels, "miny_polygon_pixels": miny_polygon_pixels, #min lon/lat
            "maxx_polygon_pixels": maxx_polygon_pixels, "maxy_polygon_pixels": maxy_polygon_pixels, #max lat
            "polygon_vertices_pixels": polygon_vertices_pixels, "utm_projection": utm_projection,
            "nw_corner_polygon_lat": nw_corner_polygon_lat, "nw_corner_polygon_lon": nw_corner_polygon_lon,#min lon/lat
            "se_corner_polygon_lat": se_corner_polygon_lat, "se_corner_polygon_lon": se_corner_polygon_lon, #min lon/lat
            "polygon_vertices_lon_lat": polygon_vertices_lon_lat,'geometry': geometry, 
            "object_class": object_class, 'diameter (m)': diameter, 'merged_bbox': merged_bbox})
    return(gdf) 
######################################################################################################################################################
######################################               Inundation Values for Tile Database            ##################################################
######################################################################################################################################################
      
def getFeatures(gdf):
    """Function to parse features from GeoDataFrame in such a manner that rasterio wants them"""
    return [json.loads(gdf.to_json())['features'][0]['geometry']]

def identify_inundation_for_tanks(gdf, sc_slosh_inundation_map_path):                       
    #identify inundation bounds                               
    category = []
    geometry = []
    for i in range(1,6): #get the bounding box polygons
        sc_slosh_inundation_map_name = "SC_Category" + str(i) + "_MOM_Inundation_HighTide_EPSG4326.tif"
        sc_slosh_inundation_map = rasterio.open(os.path.join(sc_slosh_inundation_map_path, sc_slosh_inundation_map_name))
        min_lon, min_lat, max_lon, max_lat = sc_slosh_inundation_map.bounds
        category.append("SC_Category" + str(i))
        geometry.append(Polygon([(min_lon,min_lat),(min_lon,max_lat),(max_lon,max_lat),(max_lon,min_lat)]))

    #make dataframe of inundation map bounds
    d = {'category': category,'geometry': geometry}
    sc_slosh = gpd.GeoDataFrame(d)

    #idntify useful bounding box
    if sc_slosh["geometry"].nunique() == 1: #all of the bounding boxes for the inundation maps are the same
        sc_inundation_poly = sc_slosh["geometry"].unique()[0] 

    #create dictionary for inundation values for each tank
    inundation_level_for_tank = {}
    for i in range(1,6): 
        inundation_level_for_tank["Category" + str(i)] = np.zeros((len(gdf)))

    #make a list to record whether the inundation level has been recorded
    bbox_within_inundation_bounds = [False] * len(gdf)

    #get inundation values
    for index, poly in enumerate(gdf["geometry"]): #iterate over the polygons
        if sc_inundation_poly.contains(poly): #identify whether the bbox is inside of the inundation map
            bbox_within_inundation_bounds[index] = True #record that the bbox is within the inundation map
            #make a geodatabaframe for each polygon that is 
            geo = gpd.GeoDataFrame({'geometry': poly}, index=[0], crs="EPSG:4326")
            coords = getFeatures(geo)
            for i in range(1,6): #get the bounding box polygons
                sc_slosh_inundation_map_name = "SC_Category" + str(i) + "_MOM_Inundation_HighTide_EPSG4326.tif"
                sc_slosh_inundation_map = rasterio.open(os.path.join(sc_slosh_inundation_map_path, sc_slosh_inundation_map_name))
                out_img, out_transform = rasterio.mask.mask(dataset=sc_slosh_inundation_map, shapes=coords, crop=True)
                if np.all(out_img == 255): #check if all inundation values are equal the no value entry (255)
                    inundation_level_for_tank["Category" + str(i)][index] = 0
                else: 
                    out_img = np.where(out_img >= 255, 0, out_img)
                    inundation_level_for_tank["Category" + str(i)][index] = np.average(out_img)

    #add inundation values to tank database 
    gdf["bbox_within_inundation_bounds"] = bbox_within_inundation_bounds
    for i in range(1,6): 
        gdf["Category" + str(i)] = inundation_level_for_tank["Category" + str(i)]
    return(gdf)

######################################################################################################################################################
######################################                   State Names for Tile Database              ##################################################
######################################################################################################################################################
def identify_state_name_for_each_state(states_gpds_path, gdf):
    #https://gis.stackexchange.com/questions/251812/returning-percentage-of-area-of-polygon-intersecting-another-polygon-using-shape
    states_gpds = gpd.read_file(states_gpds_path)
    states_gds_epsg4326 = states_gpds.to_crs(epsg=4326) #reproject to lat lon

    #get state for each polygon 
    state_list = [None] * len(gdf)
    for tank_index, tank_poly in tqdm.tqdm(enumerate(gdf["geometry"])): #iterate over the tank polygons
        for state_index, state_poly in enumerate(states_gds_epsg4326["geometry"]): #iterate over the state polygons
            if state_poly.intersects(tank_poly) or state_poly.contains(tank_poly): #identify whether the tank bbox is inside of the state polygon
                if state_list[tank_index] == None: 
                    state_list[tank_index] = states_gds_epsg4326.iloc[state_index]["NAME"] #add state name for each tank to list 
                else:
                    index, = np.where(states_gds_epsg4326["NAME"] == state_list[tank_index]) #check percent of tank that intersects with current state 
                    prev_state_poly = states_gds_epsg4326["geometry"][index[0]]
                    prev_state_poly_intersection_area = tank_poly.intersection(prev_state_poly).area/tank_poly.area #check percent of tank that intersects with prev_state_poly
                    
                    proposed_state_poly_intersection_area = tank_poly.intersection(state_poly).area/tank_poly.area #check percent of tank that intersects with proposed state 
                    if proposed_state_poly_intersection_area > prev_state_poly_intersection_area: #change the state if the polygon mainly resides in a different state
                        state_list[tank_index] = states_gds_epsg4326.iloc[state_index]["NAME"]

    #add states to dataframe 
    state_list = np.array(state_list)
    gdf["state"] = state_list
    return(gdf)