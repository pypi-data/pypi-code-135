import pulumi
import pulumi_azure as azure
import json


class BaseBlob:

    params = {
        "resource_name": "testblob",
        "storage_account_name": "testaccount", # this is where you get the resource group from
        "storage_container_name": "testcontainer",
        "type": "Page", # i know i need object storage...can't tell if this is how
        "size": 512
    }

    def __init__(self, resource_group_name, **kwargs):
        # self.params["resource_group_name"] = resource_group_name 
        self.variable_reassignment(**kwargs)
        self.create_blob()

    def variable_reassignment(self, **kwargs):
        for key in kwargs:
            if key in self.params:
                self.params[key] = kwargs[key]
            else:
                print("hey this is probably an issue you should address")

    def create_blob(self):
        # Create an azure resource (Blob)
        main = azure.storage.Blob(**self.params)