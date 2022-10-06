import tkinter as tk
from tkinter import filedialog
import io,os,sys
sys.path.append(os.path.dirname(__file__))
from load_save_helpers import create_default_params, save_parameters, load_parameters
from BBHP_function import param_types, BBHP
from PIL import Image
import requests 

base_param_name = 'base_parameters'

def runBB():
    
    
    file_path = get_filepath()
    param = load_parameters(file_path+base_param_name,param_types)

    BBHP(file_path,param)#, train_img_count = train_img_count)#,dt_string='22_06_06_20_44_28');#,train_img_count=train_img_count,test_img_count=test_img_count,dt_string=dt_string)


# returns images of a list of filenames for a given folder
def createdir(example=0):
    
    # request filepath from user
    file_path = get_filepath()

    # if pre-loaded example, images, masks, etc will be added
    if example == 1:
        folder_name = 'PhotoelasticDisks'
        
    elif not example == 0:
        print('[BB] Bad input, no such example #'+example+'.')
        return
    
    else: # example == 0
        folder_name = input('[INPUT] Enter folder name for new project: ')
        
        
    full_filename = file_path+folder_name
    if os.path.isdir(full_filename):
        print('[BB] Desired new folder already exists! Nohting has been changed.')
        return
   
    
    
    # Create file structure
    os.mkdir(full_filename)
    os.mkdir(full_filename+'/train_images')
    os.mkdir(full_filename+'/test_images')
    os.mkdir(full_filename+'/predict_images')
    os.mkdir(full_filename+'/masks')
    os.mkdir(full_filename+'/areas_of_interest')

    param = create_default_params();


        
    
    # given example must moves images, masks, aois into structure
    if example ==1:
        download_image("https://raw.githubusercontent.com/sdillavou/BellybuttonExampleData/blob/main/PhotoelasticDisks/areas_of_interest/test.png", \
            full_filename+'/areas_of_interest/test_early.png')

        

    save_parameters(full_filename+'/'+base_param_name,list(param.keys()),list(param.values()))
   
    print('Created and populated '+full_filename)

    
def get_filepath():
    # request filepath from user
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory()
    return file_path + '/'

def download_image(url,image_file_path):
    PIL.Image.open(io.BytesIO(request.urlopen(url).read())).save(image_file_path)
    