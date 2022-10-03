import pulumi
import pulumi_azure as azure
import json

class BaseLinkedServiceBlob:

    params = {
        "resource_name": "ls-blob",
    }

    def __init__(self, created, **kwargs): 
        self.params["data_factory_id"] = created["data_factory"].id
        self.params["connection_string"] = created["account"].primary_connection_string
        self.variable_reassignment(**kwargs)
        self.instance = self.create_ldb()

    def variable_reassignment(self, **kwargs):
        for key in kwargs:
            if key in self.params:
                self.params[key] = kwargs[key]
            else:
                print("hey this is probably an issue you should address")

    def create_ldb(self):
        # Create an azure resource (data factory)
        main = azure.datafactory.LinkedServiceAzureBlobStorage(**self.params)
        return main