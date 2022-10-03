import pulumi
import pulumi_azure as azure
import json


class BaseSecurityGroup:

    params = {
        "resource_name": "test-security-group"
    }

    def __init__(self, resource_group_name, **kwargs):
        self.params["resource_group_name"] = resource_group_name 
        self.variable_reassignment(**kwargs)
        self.create_security_group()

    def variable_reassignment(self, **kwargs):
        for key in kwargs:
            if key in self.params:
                self.params[key] = kwargs[key]
            else:
                print("hey this is probably an issue you should address")

    def create_security_group(self):
        # Create an azure resource (lb)
        main = azure.network.NetworkSecurityGroup(**self.params)