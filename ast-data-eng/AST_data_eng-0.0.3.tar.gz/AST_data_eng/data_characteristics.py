###################################################################################################################
##########################   Create dataframe of Image and Tile Characteristics  ##################################
###################################################################################################################   
def image_tile_characteristics(images_and_xmls_by_tile_path, tiles_dir):#, tile_name_tile_url, verified_positive_jpgs):
    tile_names_by_tile = []
    tile_paths_by_tile = []
    #tile_urls_by_tile = []

    tile_heights = []
    tile_widths = []
    tile_depths = []
    min_utmx_tile = [] #NW_coordinates
    min_utmy_tile = []  #NW_coordinates
    max_utmx_tile = [] #SE_coordinates
    max_utmy_tile = [] #SE_coordinates
    utm_projection_tile = [] 

    min_lon_tile = [] #NW_coordinates
    min_lat_tile = []  #NW_coordinates
    max_lon_tile = [] #SE_coordinates
    max_lat_tile = [] #SE_coordinates

    chip_names = []
    tile_names_by_chip = []
    tile_paths_by_chip = []
    #tile_urls_by_chip = []

    minx_pixel = []
    miny_pixel = []
    maxx_pixel = []
    maxy_pixel = []
    min_lon_chip = [] #NW_coordinates
    min_lat_chip = [] #NW_coordinates
    max_lon_chip = [] #SE_coordinates
    max_lat_chip = [] #SE_coordinates
    min_utmx_chip = [] #NW_coordinates
    min_utmy_chip = [] #NW_coordinates
    max_utmx_chip = [] #SE_coordinates
    max_utmy_chip = [] #SE_coordinates
    utm_projection_chip = [] 

    row_indicies = []
    col_indicies = []
    image_paths  = []
    xml_paths = []
    item_dim = int(512)
    folders_of_images_xmls_by_tile = os.listdir(images_and_xmls_by_tile_path)
    for tile_name in tqdm.tqdm(folders_of_images_xmls_by_tile):
        #specify image/xml paths for each tile
        positive_image_dir = os.path.join(images_and_xmls_by_tile_path, tile_name, "chips_positive")
        remove_thumbs(positive_image_dir)
        positive_xml_dir = os.path.join(images_and_xmls_by_tile_path, tile_name, "chips_positive_xml")
        #load a list of images/xmls for each tile
        positive_images = os.listdir(positive_image_dir)
        positive_xmls = os.listdir(positive_xml_dir)
        #read in tile
        tile_path = os.path.join(tiles_dir, tile_name + ".tif")
        #obtain tile url
        #tile name/path/urls by tile
        tile_names_by_tile.append(tile_name)
        tile_paths_by_tile.append(tile_path)
        #tile_url = [string for string in tile_name_tile_url[:,1] if tile_name in string][0]
        #tile_urls_by_tile.append(tile_url)
        #determine the utm coords for each tile 
        utmx, utmy, tile_band, tile_height, tile_width = tile_dimensions_and_utm_coords(tile_path)
        tile_heights.append(tile_height)
        tile_widths.append(tile_width)
        tile_depths.append(tile_band)
        min_utmx_tile.append(utmx[0]) #NW_coordinates
        min_utmy_tile.append(utmy[0])  #NW_coordinates
        max_utmx_tile.append(utmx[-1]) #SE_coordinates
        max_utmy_tile.append(utmy[-1]) #SE_coordinates
        utm_proj = get_utm_proj(tile_path)
        utm_projection_tile.append(utm_proj)
        minlon, minlat = transform_point_utm_to_wgs84(utm_proj, utmx[0], utmy[0])
        maxlon, maxlat = transform_point_utm_to_wgs84(utm_proj, utmx[-1], utmy[-1]) 
        min_lon_tile.append(minlon) #NW_coordinates
        min_lat_tile.append(minlat) #NW_coordinates
        max_lon_tile.append(maxlon) #SE_coordinates
        max_lat_tile.append(maxlat) #SE_coordinates
        

        for positive_image in positive_images: #iterate over each image affiliated with a given tile
            #tile and chip names
            chip_name = os.path.splitext(positive_image)[0]
            chip_names.append(chip_name) # The index is a six-digit number like '000023'.
            tile_names_by_chip.append(tile_name)
            #path
            tile_paths_by_chip.append(tile_path)
            #tile_urls_by_chip.append(tile_url)

            image_paths.append(os.path.join(positive_image_dir, positive_image))
            xml_paths.append(os.path.join(positive_xml_dir, chip_name +".xml"))
            #row/col indicies 
            y, x = chip_name.split("_")[-2:] #name of tif with the extension removed; y=row;x=col
            y = int(y)
            x = int(x)
            row_indicies.append(y)
            col_indicies.append(x)
            #get the pixel coordinates (indexing starting at 0)
            minx = x*item_dim 
            miny = y*item_dim 
            maxx = (x+1)*item_dim - 1
            maxy = (y+1)*item_dim - 1
            if maxx > tile_width:
                maxx = tile_width - 1
            if maxy > tile_height:
                maxy = tile_height - 1
            minx_pixel.append(minx) #NW (max: Top Left) # used for numpy crop
            miny_pixel.append(miny) #NW (max: Top Left) # used for numpy crop
            maxx_pixel.append(maxx) #SE (min: Bottom right) 
            maxy_pixel.append(maxy) #SE (min: Bottom right) 
            #determine the lat/lon
            min_lon, min_lat = transform_point_utm_to_wgs84(utm_proj, utmx[minx], utmy[miny])
            max_lon, max_lat = transform_point_utm_to_wgs84(utm_proj, utmx[maxx], utmy[maxy]) 
            min_utmx_chip.append(utmx[minx]) #NW_coordinates
            min_utmy_chip.append(utmy[miny]) #NW_coordinates
            max_utmx_chip.append(utmx[maxx]) #SE_coordinates
            max_utmy_chip.append(utmy[maxy]) #SE_coordinates
            utm_projection_chip.append(utm_proj)
            min_lon_chip.append(min_lon) #NW (max: Top Left) # used for numpy crop
            min_lat_chip.append(min_lat) #NW (max: Top Left) # used for numpy crop
            max_lon_chip.append(max_lon) #SE (min: Bottom right) 
            max_lat_chip.append(max_lat) #SE (min: Bottom right)
    tile_characteristics = pd.DataFrame(data={'tile_name': tile_names_by_tile, 'tile_path': tile_paths_by_tile, #'tile_url': tile_urls_by_tile, 
                        'tile_heights': tile_heights, 'tile_widths': tile_widths, 'tile_bands': tile_depths, 'min_utmx': min_utmx_tile, 'min_utmy': min_utmy_tile, 
                        'max_utmx': max_utmx_tile, 'max_utmy': max_utmy_tile, 'utm_projection': utm_projection_tile,
                        'min_lon_tile': min_lon_tile,'min_lat_tile': min_lat_tile,'max_lon_tile': max_lon_tile,'max_lat_tile': max_lat_tile})

    image_characteristics = pd.DataFrame(data={'chip_name': chip_names, 'image_path': image_paths, 'xml_path': xml_paths,'tile_name': tile_names_by_chip, 
                            'row_indicies': row_indicies, 'col_indicies': col_indicies,'tile_path': tile_paths_by_chip, #'tile_url': tile_urls_by_chip, 
                            'minx_pixel': minx_pixel, 'miny_pixel': miny_pixel, 'maxx_pixel': maxx_pixel,'maxy_pixel': maxy_pixel, 'utm_projection': utm_projection_chip,
                            'min_utmx': min_utmx_chip, 'min_utmy': min_utmy_chip, 'max_utmx': max_utmx_chip, 'max_utmy': max_utmy_chip, 
                            'min_lon_chip': min_lon_chip,'min_lat_chip': min_lat_chip,'max_lon_chip': max_lon_chip, 'max_lat_chip': max_lat_chip})
    tile_characteristics.to_csv("tile_characteristics.csv")
    image_characteristics.to_csv("image_characteristics.csv")
    return(tile_characteristics, image_characteristics)