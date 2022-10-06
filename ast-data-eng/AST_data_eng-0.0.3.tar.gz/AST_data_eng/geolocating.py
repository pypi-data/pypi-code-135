###################################################################################################################
#################################   Obtain Location Data (UTM to WGS84)  ##########################################
###################################################################################################################   
def tile_dimensions_and_utm_coords(tile_path):
    """ Obtain tile band, height and width and utm coordinates
    Args: tile_path(str): the path of the tile 
    Returns: 
    utmx(np array): the x utm coordinates
    utmy(np array): the y utm coordinates
    tile_band(int): the number of bands
    tile_height(int): the height of the tile (in pixels)
    tile_width(int): the width of the tile (in pixels)
    """
    ## Get tile locations
    da = rioxarray.open_rasterio(tile_path) ## Read the data
    # Compute the lon/lat coordinates with rasterio.warp.transform
    # lons, lats = np.meshgrid(da['x'], da['y'])
    tile_band, tile_height, tile_width = da.shape[0], da.shape[1], da.shape[2]
    utmx = np.array(da['x'])
    utmy = np.array(da['y'])
    return(utmx, utmy, tile_band, tile_height, tile_width)
def get_utm_proj(tile_path):
    """ Obtain utm projection as a string 
    Args: tile_path(str): the path of the tile 
    Returns: 
    utm_proj(str): the UTM string as the in term of EPSG code
    """
    da = rasterio.open(tile_path)
    utm_proj = da.crs.to_string()
    return(utm_proj)
def transform_point_utm_to_wgs84(utm_proj, utm_xcoord, utm_ycoord):
    """ Convert a utm pair into a lat lon pair 
    Args: 
    utm_proj(str): the UTM string as the in term of EPSG code
    utmx(int): the x utm coordinate of a point
    utmy(int): the y utm coordinates of a point
    Returns: 
    (wgs84_pt.x, wgs84_pt.y): the 'EPSG:4326' x and y coordinates 
    """
    #https://gis.stackexchange.com/questions/127427/transforming-shapely-polygon-and-multipolygon-objects
    #get utm projection
    utm = pyproj.CRS(utm_proj)
    #get wgs84 proj
    wgs84 = pyproj.CRS('EPSG:4326')
    #specify utm point
    utm_pt = Point(utm_xcoord, utm_ycoord)
    #transform utm into wgs84 point
    project = pyproj.Transformer.from_crs(utm, wgs84, always_xy=True).transform
    wgs84_pt = transform(project, utm_pt)
    return(wgs84_pt.x, wgs84_pt.y)