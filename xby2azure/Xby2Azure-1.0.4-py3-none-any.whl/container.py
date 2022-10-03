import pulumi
import pulumi_azure as azure
import json


class BaseContainer:

    params = {
        "resource_name": "testcontainer",
        "container_access_type": "blob"
    }

    def __init__(self, created, **kwargs):
        self.params["storage_account_name"] = created["account"].name 
        self.variable_reassignment(**kwargs)
        self.instance = self.create_container()

    def variable_reassignment(self, **kwargs):
        for key in kwargs:
            if key in self.params:
                self.params[key] = kwargs[key]
            else:
                print("hey this is probably an issue you should address")

    def create_container(self):
        # Create an azure resource (storage container)
        main = azure.storage.Container(**self.params)
        return main