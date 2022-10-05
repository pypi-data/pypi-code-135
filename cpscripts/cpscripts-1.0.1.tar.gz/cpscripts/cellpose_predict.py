# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:14:00 2022

@author: akhan
"""
from cellpose import models
import tifffile
import os
import numpy as np
from pathlib import Path
from skimage.transform import downscale_local_mean
from termcolor import colored
import argparse


parser = argparse.ArgumentParser(description='run cellpose model for prediction on 3D data')
parser.add_argument("--img_path", type=str)
parser.add_argument("--save_dir", type=str)
parser.add_argument("--x_scale", type=int, default=1)
parser.add_argument("--y_scale", type=int, default=1)
parser.add_argument("--z_scale", type=int, default=1)
parser.add_argument("--dia", type=int, default=40)
parser.add_argument("--model", default='cyto', type=str)
parser.add_argument("--cellprob_threshold", default=0.0, type=float)
parser.add_argument("--flow_threshold", default=0.4, type=float)
parser.add_argument("--anisotropy", default=None, type=float)
parser.add_argument('--headless', action='store_true')
parser.add_argument('--no-headless', dest='headless', action='store_false')
parser.set_defaults(headless=True)

args = parser.parse_args()

## Parameters
cell_diameter = args.dia
cp_thresh = args.cellprob_threshold
f_thres = args.flow_threshold
anis_factor = args.anisotropy
downscale_factor_x = args.x_scale
downscale_factor_y = args.y_scale
downscale_factor_z = args.z_scale
headless = args.headless

save_path = args.save_dir
file_path = args.img_path


# Read image
img = tifffile.imread(file_path)
# Downscale image 
img = downscale_local_mean(img, (downscale_factor_z,
                                 downscale_factor_x,
                                 downscale_factor_y)) 

# Get Cellpose model
model_cp = models.CellposeModel(gpu=True, 
                                model_type=args.model)
# Do segmentation using Cellpose model
masks, flows, styles = model_cp.eval(img, 
                                     channels=[0,0], 
                                     diameter=cell_diameter, 
                                     do_3D=True,
                                     cellprob_threshold=cp_thresh,
                                     flow_threshold=f_thres,
                                     anisotropy=anis_factor)

if headless:
    savename = Path(file_path.split('\\')[-1]).name.replace(".tif","")+'_labels.tif'
else:
    savename = save_path+os.sep+Path(
        file_path.split('\\')[-1]).name.replace(".tif","")+'_labels.tif'

# Save label mask
tifffile.imwrite(savename, masks.astype(np.uint16))
print(colored('File saved as : ', 'cyan'), colored(savename, 'green'))