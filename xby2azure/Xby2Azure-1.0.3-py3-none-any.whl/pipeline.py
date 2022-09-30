import pulumi
import pulumi_azure as azure
import json

class BasePipeline:

    params = {
        "resource_name": "test-pipeline"
    }

    def __init__(self, created, **kwargs): 
        self.params["data_factory_id"] = created["data_factory"].id
        self.params["activities_json"]="""[]"""
        self.variable_reassignment(**kwargs)
        self.instance = self.create_pipeline()

    def variable_reassignment(self, **kwargs):
        for key in kwargs:
            if key in self.params:
                self.params[key] = kwargs[key]
            else:
                print("hey this is probably an issue you should address")

    def create_pipeline(self):
        # Create an azure resource (data factory)
        main = azure.datafactory.Pipeline(**self.params)
        return main