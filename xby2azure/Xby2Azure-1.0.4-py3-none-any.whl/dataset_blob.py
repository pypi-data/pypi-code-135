import pulumi
import pulumi_azure as azure
import json

class BaseDatasetBlob:

    params = {
        "resource_name": "dataset-blob"
    }

    def __init__(self, created, **kwargs):
        self.params["data_factory_id"] = created["data_factory"].id
        self.params["linked_service_name"] = created["linked_service_blob"].name
        self.variable_reassignment(**kwargs)
        self.instance = self.create_dataset_blob()

    def variable_reassignment(self, **kwargs):
        for key in kwargs:
            if key in self.params:
                self.params[key] = kwargs[key]
            else:
                print("hey this is probably an issue you should address")

    def create_dataset_blob(self):
        # Create an azure resource (data factory)
        main = azure.datafactory.DatasetAzureBlob(**self.params)
        return main