import pulumi
import pulumi_azure as azure
import json


class BaseSSIS:

    params = {
        "resource_name": "test-ssis-ir",
        "data_factory_id": "test-data-factory", # this is where you get the resource group from
        "node_size": "Standard_D1_v2",
        "location": "eastus2"
    }

    def __init__(self, resource_group_name, **kwargs):
        # self.params["resource_group_name"] = resource_group_name 
        self.variable_reassignment(**kwargs)
        self.create_ssis_ir()

    def variable_reassignment(self, **kwargs):
        for key in kwargs:
            if key in self.params:
                self.params[key] = kwargs[key]
            # else:
            #     print("hey this is probably an issue you should address")

    def create_ssis_ir(self):
        # Create an azure resource (ssis-ir)
        main = azure.datafactory.IntegrationRuntimeSsis(**self.params)