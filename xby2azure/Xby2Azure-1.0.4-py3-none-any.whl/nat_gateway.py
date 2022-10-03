import pulumi
import pulumi_azure as azure
import json


class BaseNatGateway:

    params = {
        "resource_name": "test-nat-gateway"
    }

    def __init__(self, resource_group_name, **kwargs):
        self.params["resource_group_name"] = resource_group_name 
        self.variable_reassignment(**kwargs)
        self.create_nat_gateway()

    def variable_reassignment(self, **kwargs):
        for key in kwargs:
            if key in self.params:
                self.params[key] = kwargs[key]
            else:
                print("hey this is probably an issue you should address")

    def create_nat_gateway(self):
        # Create an azure resource (lb)
        main = azure.network.NatGateway(**self.params)