# -*- coding: utf-8 -*-
import glob,json, os, pathlib, shutil, sys, tarfile,zipfile
import importlib, inspect
from typing import Optional, Union
import yaml


from utilmy.utilmy_base import to_file



#################################################################
from utilmy.utilmy_base import log, log2

def help():
    """function help"""
    from utilmy import help_create
    ss = help_create(__file__)
    print(ss)




#####################################################################
def test_all():
    """.
    Doc::

         cd utilmy
         python utils.py  test_all


     Easy to maintain and re-factors.
    """
    test1()
    # test2()
    # test3()
    # test4





def test1():
    """function test1.
    Doc::

            Args:
            Returns:

    """

    import utilmy as uu
    drepo, dirtmp = uu.dir_testinfo()


    log("####### dataset_download_test() ..")
    test_file_path = dataset_donwload("https://github.com/arita37/mnist_png/raw/master/mnist_png.tar.gz", './testdata/tmp/test/dataset/')
    f = os.path.exists(os.path.abspath(test_file_path))
    assert f == True, "The file made by dataset_download_test doesn't exist"

    # dataset_donwload("https://github.com/arita37/mnist_png/raw/master/mnist_png.tar.gz", './testdata/tmp/test/dataset/')




    log("####### os_extract_archive() ..")
    #Testing os_extract_archive() extracting a zip file
    path1    = dirtmp + "/dirout/"
    path_zip = path1 + "test.zip"

    uu.to_file("Dummy test", path1 + "/zip_test.txt")

    ### https://docs.python.org/3/library/zipfile.html
    ### https://stackoverflow.com/questions/16091904/how-to-eliminate-absolute-path-in-zip-archive-if-absolute-paths-for-files-are-pr
    zf       = zipfile.ZipFile(path_zip, "w")
    zf.write(path1 + "/zip_test.txt", "zip_test.txt")
    zf.close()

    is_extracted  = os_extract_archive(
        file_path = path_zip,
        path      = drepo + "testdata/tmp/zip_test"
        #,archive_format = "auto"
        )
    assert is_extracted == True, "The zip wasn't extracted"

    # os_extract_archive("./testdata/tmp/test/dataset/mnist_png.tar.gz","./testdata/tmp/test/dataset/archive/", archive_format = "auto")





#####################################################################
def load_function(package="mlmodels.util", name="path_norm"):
  """function load_function.
  Get the function of a package.

  Docs::
          
        Args:
            package (string): Package's name. Defaults to "mlmodels.util".
            name (string): Name of the function that belongs to the package.  

        Returns:
            Returns the function of the package.

        Example:
            from utilmy import utils

            function = utils.load_function(
                package="datetime",
                name="timedelta")

            print(function())#0:00:00
    
  """
  import importlib
  return  getattr(importlib.import_module(package), name)



def load_function_uri(uri_name="path_norm"):
    """ Load dynamically function from URI.
    Docs::

        ###### Pandas CSV case : Custom MLMODELS One
        #"dataset"        : "mlmodels.preprocess.generic:pandasDataset"
    
        ###### External File processor :
        #"dataset"        : "MyFolder/preprocess/myfile.py:pandasDataset"

        Args:
            uri_name (string): URI of the function to get.
        
        Returns:
            Returns the function with the given URI.

        Example:
            from utilmy import utils

            function = utils.load_function_uri(uri_name="datetime:timedelta")

            print(function()) #0:00:00


    """
    
    import importlib, sys
    from pathlib import Path
    pkg = uri_name.split(":")

    assert len(pkg) > 1, "  Missing :   in  uri_name module_name:function_or_class "
    package, name = pkg[0], pkg[1]
    
    try:
        #### Import from package mlmodels sub-folder
        return  getattr(importlib.import_module(package), name)

    except Exception as e1:
        try:
            ### Add Folder to Path and Load absoluate path module
            path_parent = str(Path(package).parent.parent.absolute())
            sys.path.append(path_parent)
            #log(path_parent)

            #### import Absolute Path model_tf.1_lstm
            model_name   = Path(package).stem  # remove .py
            package_name = str(Path(package).parts[-2]) + "." + str(model_name)
            #log(package_name, model_name)
            return  getattr(importlib.import_module(package_name), name)

        except Exception as e2:
            raise NameError(f"Module {pkg} notfound, {e1}, {e2}")


def load_callable_from_uri(uri="mypath/myfile.py::myFunction"):
    """ Will return the function Python Object from the string path mypath/myfile.py::myFunction
    Doc::
            
            Args:
                uri:   
            Returns:
                
    """
    import importlib, inspect
    assert(len(uri)>0 and ('::' in uri or '.' in uri))
    if '::' in uri:
        module_path, callable_name = uri.split('::')
    else:
        module_path, callable_name = uri.rsplit('.',1)
    if os.path.isfile(module_path):
        module_name = '.'.join(module_path.split('.')[:-1])
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    else:
        module = importlib.import_module(module_path)
    return dict(inspect.getmembers(module))[callable_name]
        

def load_callable_from_dict(function_dict, return_other_keys=False):
    """function load_callable_from_dict.
    Doc::
            
            Args:
                function_dict:   
                return_other_keys:   
            Returns:
                
    """
    function_dict = function_dict.copy()
    uri = function_dict.pop('uri')
    func = load_callable_from_uri(uri)
    try:
        assert(callable(func))
    except:
        raise TypeError(f'{func} is not callable')
    arg = function_dict.pop('arg', {})
    if not return_other_keys:
        return func, arg
    else:
        return func, arg, function_dict
    







##########################################################################################
################### donwload  ############################################################
def dataset_donwload(url, path_target):
    """Donwload on disk the tar.gz file.
    Docs::
            
        Args:
            url (string): File's URL to download.
            path_target (string): Folder's path to save the file.

        Returns:
            string: Full path of the saved file.

        Example:
            from utilmy import utils

            url = "{url of the file}"
            path_target = "/home/username/Desktop/example"

            full_path = utils.dataset_donwload(
                url=url, 
                path_target=path_target)

            print(full_path)

    """
    import wget
    log(f"Donwloading mnist dataset in {path_target}")
    os.makedirs(path_target, exist_ok=True)
    wget.download(url, path_target)
    tar_name = url.split("/")[-1]
    os_extract_archive(path_target + "/" + tar_name, path_target)
    log2(path_target)
    return path_target + tar_name

  

def os_extract_archive(file_path, path=".", archive_format="auto"):
    """Extracts an archive if it matches tar, tar.gz, tar.bz, or zip formats..
    
    Docs::
                
        Args:
            file_path (string): path to the archive file
            path (string): path to extract the archive file
            archive_format (string): Archive format to try for extracting the file.
                Options are 'auto', 'tar', 'zip', and None.
                'tar' includes tar, tar.gz, and tar.bz files.
                The default 'auto' is ['tar', 'zip'].
                None or an empty list will return no matches found.
        Returns:
            True if a match was found and an archive extraction was completed,
            False otherwise.

        Example:
        from utilmy import utils

        is_extracted = utils.os_extract_archive(
            file_path="/home/necromancer/Desktop/example.zip",
            path="/home/necromancer/Desktop/testingfolder")

        print(is_extracted)#Displays true if the match was found

    """
    if archive_format is None:
        return False
    if archive_format == "auto":
        archive_format = ["tar", "zip"]
    if isinstance(archive_format, str):
        archive_format = [archive_format]

    file_path = os.path.abspath(file_path)
    path = os.path.abspath(path)

    for archive_type in archive_format:
        if archive_type == "tar":
            open_fn = tarfile.open
            is_match_fn = tarfile.is_tarfile
        if archive_type == "zip":
            open_fn = zipfile.ZipFile
            is_match_fn = zipfile.is_zipfile

        if is_match_fn(file_path):
            with open_fn(file_path) as archive:
                try:
                    archive.extractall(path)
                except (tarfile.TarError, RuntimeError, KeyboardInterrupt):
                    if os.path.exists(path):
                        if os.path.isfile(path):
                            os.remove(path)
                        else:
                            shutil.rmtree(path)
                    raise
            return True
    return False





###################################################################################################
if __name__ == "__main__":
    import fire
    fire.Fire()


"""
pip install fire

https://www.google.com/search?q=pip+insall+fire&pws=0&gl=us&gws_rd=cr


cd myutil
cd utilmy

python  utils.py   test_all








"""