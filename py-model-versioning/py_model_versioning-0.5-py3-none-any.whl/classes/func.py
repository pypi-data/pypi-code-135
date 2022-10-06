import json
import os
import click
from os import walk

from .google_storage import googleStorage


class App:
    __conf = {
        "Chosen_Cloud_Provider": "", "Google_Bucket_Name": "",
        "AWS_Bucket_Name": ""
    }
    __setters = ["Chosen_Cloud_Provider", "Google_Bucket_Name", "AWS_Bucket_Name"]

    @staticmethod
    def config(name):
        return App.__conf[name]

    @staticmethod
    def set(name, value):
        if name in App.__setters:
            App.__conf[name] = value
        else:
            raise NameError("Name not accepted in set() method")


class func:
    config_dir = "config-model-ver"
    full_path_config_file = config_dir + '/config.json'

    def __init__(self, init=True):
        if init:
            self.config_files_exists = func.check_config_files_exists(self)
            self.get_bucket_name()
            self.func_storage = googleStorage(self.bucket_name)

    def delete_entire_directory(self, directory_name):
        if self.bucket_name == "" or not self.config_files_exists:
            return
        self.func_storage.delete_entire_directory(directory_name)

    def delete_file(self, directory_name, file_name):
        if self.bucket_name == "" or not self.config_files_exists:
            return
        self.func_storage.delete_file(directory_name, file_name)

    def download_file_from_storage(self, source_blob_name, destination_file_name):
        if self.bucket_name == "" or not self.config_files_exists:
            return
        self.func_storage.download_file_from_storage(source_blob_name, destination_file_name)

    def download_ver_from_storage(self, project, ver):
        if self.bucket_name == "" or not self.config_files_exists:
            return
        self.func_storage.download_ver_from_storage(project, ver)

    def download_all_ver_from_storage(self, project):
        if self.bucket_name == "" or not self.config_files_exists:
            return
        self.func_storage.download_all_ver_from_storage(project)

    def list_dir(self, full_folder, get_version_files, display_console=True):
        if self.bucket_name == "" or not self.config_files_exists:
            return
        self.func_storage.list_dir(full_folder, get_version_files, display_console)

    def add_directory(self, directory, project, ver):
        if self.bucket_name == "" or not self.config_files_exists:
            return
        full_directory = os.getcwd() + '/' + directory
        filenames = next(walk(full_directory), (None, None, []))[2]
        for file in filenames:
            self.upload_file(project, ver, full_directory + '/' + file, directory)

    def upload_file(self, project, ver_name, file_name, dir_name):
        storage_file_name = os.path.basename(file_name)
        if os.path.exists(file_name):
            if dir_name == '':
                self.func_storage.upload_to_bucket(project + '/' + ver_name + '/' + storage_file_name, file_name)
            else:
                self.func_storage.upload_to_bucket(project + '/' + ver_name + '/' + dir_name + '/' + storage_file_name,
                                                   file_name)
        else:
            click.echo("file " + file_name + " does not exists")

    def add_file(self, project, ver_name, file_name):
        if self.bucket_name == "" or not self.config_files_exists:
            return
        if not file_name.endswith("/."):
            self.upload_file(project, ver_name, file_name, '')
        else:
            prefix_dir = file_name.replace("/.", "")
            if len(prefix_dir) > 0:
                prefix_dir = prefix_dir + "/"
            full_dir_name = os.getcwd() + '/' + prefix_dir
            filenames = next(walk(full_dir_name), (None, None, []))[2]
            for file in filenames:
                self.upload_file(project, ver_name, prefix_dir + file, '')

    def get_bucket_name(self):
        if App.config("Chosen_Cloud_Provider") == "google":
            self.bucket_name = App.config("Google_Bucket_Name")
        elif App.config("Chosen_Cloud_Provider") == "aws":
            self.bucket_name = App.config("Google_Bucket_Name")
        if self.bucket_name == "":
            click.echo("no bucket defined, please configure bucket name")

    def create_config_if_not_exists(self):
        full_path_config_file = self.config_dir + '/config.json'
        if not os.path.exists(self.config_dir):
            os.makedirs(self.config_dir)

        if not os.path.isfile(full_path_config_file):
            json_create_first_time = {"Chosen_Cloud_Provider": "", "Google_Bucket_Name": "",
                                      "AWS_Bucket_Name": ""}
            with open(full_path_config_file, 'w') as config_file:
                json.dump(json_create_first_time, config_file)
            return False
        else:
            return True

    def save_cloud_provider_to_config_file(self, cloud_provider):
        self.create_config_if_not_exists()
        with open(self.full_path_config_file) as config_file:
            json_decoded = json.load(config_file)
        json_decoded['Chosen_Cloud_Provider'] = cloud_provider
        with open(self.full_path_config_file, 'w') as config_file:
            json.dump(json_decoded, config_file)
            click.echo("cloud provider set successfully")

    def save_config_file(self, cloud_provider, bucket_name):
        config_file_exists = self.create_config_if_not_exists()
        with open(self.full_path_config_file) as config_file:
            json_decoded = json.load(config_file)
        if not config_file_exists:
            json_decoded['Chosen_Cloud_Provider'] = cloud_provider
        if cloud_provider.lower() == "google":
            json_decoded['Google_Bucket_Name'] = bucket_name
        elif cloud_provider.lower() == "aws":
            json_decoded['AWS_Bucket_Name'] = bucket_name
        with open(self.full_path_config_file, 'w') as config_file:
            json.dump(json_decoded, config_file)
            click.echo("configuration file saved successfully")

    def display_config_file(self):
        if not self.read_config_file(True):
            click.echo("no configuration file was found, please use configure flag to create one")

    def check_config_files_exists(self):
        if not self.read_config_file():
            return False
        else:
            return True

    def read_config_file(self, print_json=False):
        if os.path.exists(self.config_dir + '/config.json'):
            with open('config-model-ver/config.json', 'r') as config_file:
                json_config = json.load(config_file)
                if "Chosen_Cloud_Provider" in json_config:
                    App.set("Chosen_Cloud_Provider", json_config["Chosen_Cloud_Provider"])
                if "Google_Bucket_Name" in json_config:
                    App.set("Google_Bucket_Name", json_config["Google_Bucket_Name"])
                if "AWS_Bucket_Name" in json_config:
                    App.set("AWS_Bucket_Name", json_config["AWS_Bucket_Name"])
                if print_json:
                    pretty_json = json.dumps(json_config, indent=4)
                    click.echo(pretty_json)
            return True;
        else:
            print("Configuration file not found in config-model-ver directory\n")
            return False
