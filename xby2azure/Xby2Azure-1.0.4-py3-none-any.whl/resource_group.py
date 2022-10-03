import pulumi
import pulumi_azure as azure
import json

class BaseResourceGroup:
    
    params = {}

    def __init__(self, **kwargs):
        self.variable_reassignment(**kwargs)
        self.instance = self.create_resource_group()

    def variable_reassignment(self, **kwargs):
        for key in kwargs:
            if key in self.params:
                self.params[key] = kwargs[key]
            else:
                print("hey this is probably and issue you should address")

    def create_resource_group(self):
        main = azure.core.VirtualNetwork(**finalized_params)
        