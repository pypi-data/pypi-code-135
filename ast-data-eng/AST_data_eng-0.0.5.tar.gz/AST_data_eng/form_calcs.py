# -*- coding: utf-8 -*-

"""
Functions to process, format, and conduct calculations on the annotated or verified dataset
"""
# Standard packages
#from __future__ import print_function
import warnings
import urllib
import shutil
import os
import math 
import json
import tqdm
from glob import glob

import xml.dom.minidom
from xml.dom.minidom import parseString
import xml.etree.ElementTree as et
from xml.dom import minidom

#install standard
import numpy as np
import pandas as pd
import cv2
import matplotlib 
import matplotlib.pyplot as plt
import fiona #must be import before geopandas
import geopandas as gpd
import rasterio
import rioxarray
import re #pip install regex
import rtree
import pyproj
import shapely
from shapely.ops import transform
from shapely.geometry import Polygon, Point, MultiPoint, MultiPolygon, MultiLineString

from skimage.metrics import structural_similarity as compare_ssim
#import imutils
#import psutil
#Parsing/Modifying XML
from lxml.etree import Element,SubElement,tostring

import data_eng.az_proc as ap


## Write files
def write_list(list_, file_path):
    """ 
    Write data from a list
    Args:
        list_ (str): data stored in a list
        file_path (str): a file path to store the list
    """
    print("Started writing list data into a json file")
    with open(file_path, "w") as fp:
        json.dump(list_, fp)
        print("Done writing JSON data into .json file")

# Read list to memory
def read_list(file_path):
    """ 
    Read data writen to a list
    Args:
        file_path (str): a file path to store the list
    Returns:
        list_ (str): data stored in a list
    """
    # for reading also binary mode is important
    with open(file_path, 'rb') as fp:
        list_ = json.load(fp)
        return list_

######################################################################################################################################################
######################################                      Write Tile Level Annotations  (shift to write gdf)          ##################################################
######################################################################################################################################################

def write_gdf(gdf, output_filepath, output_filename = 'tile_level_annotations'):
    gdf.crs = "EPSG:4326" #assign projection

    #save geodatabase as json
    with open(os.path.join(output_filepath, output_filename+".json"), 'w') as file:
        file.write(gdf.to_json()) 

    ##save geodatabase as geojson 
    with open(os.path.join(output_filepath, output_filename+".geojson"), "w") as file:
        file.write(gdf.to_json()) 

    ##save geodatabase as shapefile (specify columns to drop as a arg
    gdf_shapefile = gdf.drop(columns=["chip_name","polygon_vertices_pixels","polygon_vertices_lon_lat"])
    gdf_shapefile.to_file(os.path.join(output_filepath,output_filename+".shp"))
    
####################################################### get png images ###################################################
########################################################################################
def png4jpg(image_dir, new_image_dir, tiles_dir, item_dim = int(512)):
    """ Get the png for labeled images 
    Load tile of interest; Identify labeled images, and save labeled images as png
    Args:
    new_image_dir(str): path to folder that will contain the png images
    image_dir(str): path to folder contain labeled images 
    tiles_dir(str): path to folder containing tiles
    """
    #get list of images 
    remove_thumbs(image_dir) #remove thumbs db first
    images = os.listdir(image_dir) 
    
    #get list of tile names and list of image names (without extensions
    image_names = []
    tile_names = []
    for image in images: #iterate over annotated images 
        image_names.append(os.path.splitext(image)[0]) #remove extension
        tile_names.append(image.rsplit("_",2)[0]) #remove tile
    tile_names = np.unique(tile_names)

    for tile_name in tile_names: #iterate over and load tiles        
        images_in_tile = [string for string in image_names if tile_name in string]  

        tile = cv2.imread(os.path.join(tiles_dir, tile_name + ".tif"), cv2.IMREAD_UNCHANGED) #read in tile
        tile_height,  tile_width,  tile_channels = tile.shape #the size of the tile 
        row_index = math.ceil(tile_height/item_dim) 
        col_index = math.ceil(tile_width/item_dim)
    
        for image_name in images_in_tile: #iterate over images associated with each tile
            y, x = image_name.split("_")[-2:] #y=row;x=col
            y = int(y)
            x = int(x)
            
            #save image
            img = tile_to_chip_array(tile, x, y, item_dim) #subset the chip from the tile
            image_name_ext = image_name + '.png' # row_cols #specify the chip names
            image_path = os.path.join(new_image_dir, image_name_ext)
            if not os.path.exists(image_path):
                cv2.imwrite(image_path, img) #save images
                