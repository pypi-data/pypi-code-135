from sklearn.decomposition import PCA
from AtomicAI.data.descriptor_cutoff import descriptor_cutoff
from AtomicAI.io.write_data_in_py import write_data_in_py
import sys, os
import ase.io
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def pca():
    '''
    The features that are read from 'descriptors' directoy will be classify using PCA from sklearn.
    The classified data will be written as a python file called 'pca_projected_data.py' in 'pca' direcroy. 
    '''
    in_dir = './descriptors/'
    des_files = sorted([f for f in os.listdir(in_dir) if '.dat' in f])
    if len(des_files) > 0:
        print(f"Availabel files are \n {', '.join(des_files)}")
    else:
        print("No des_file.dat file is availabel HERE!!!")
        exit()
    out_directory = './pca/'
    py_out_file = 'pca_projected_data.py'
    if not os.path.isdir(out_directory):
        os.makedirs(out_directory)
    if os.path.isfile(out_directory+py_out_file):
        os.remove(out_directory+py_out_file)
    # Initializing output python file
    data_names = ['pca_projected']
    for data_name in data_names:
        initialize_variables = {}
        initialize_variables['data_name'] = data_name
        initialize_variables['data'] = '{}'
        write_data_in_py(out_directory+py_out_file, initialize_variables)
    for des_file in des_files:
        features = pd.read_csv(in_dir+des_file, header=None).values
        loc_pca = PCA(n_components = 2)
        py_output_data = {}
        py_output_data['data_name'] = f"pca_projected['{des_file[:-4]}']"
        data = loc_pca.fit_transform(features).transpose()
        py_output_data['data'] = [list(data[0]), list(data[1])]
        write_data_in_py(out_directory+py_out_file, py_output_data)
    return
