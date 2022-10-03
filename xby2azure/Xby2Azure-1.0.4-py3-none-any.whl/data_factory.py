import pulumi
import pulumi_azure as azure
import json

class BaseDataFactory:

    params = {
        "resource_name": "test-data-factory"
    }

    def __init__(self, created, **kwargs): 
        self.params["resource_group_name"] = created["resource_group"].name
        self.variable_reassignment(**kwargs)
        self.instance = self.create_data_factory()

    def variable_reassignment(self, **kwargs):
        for key in kwargs:
            if key in self.params:
                self.params[key] = kwargs[key]
            else:
                print("hey this is probably an issue you should address")

    def create_data_factory(self):
        # Create an azure resource (data factory)
        main = azure.datafactory.Factory(**self.params)
        return main