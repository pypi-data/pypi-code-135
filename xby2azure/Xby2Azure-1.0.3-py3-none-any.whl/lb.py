import pulumi
import pulumi_azure as azure
import json


class BaseLB:

    params = {
        "resource_name": "test-lb"
    }

    def __init__(self, resource_group, **kwargs): 
        self.variable_reassignment(**kwargs)
        self.params["resource_group_name"] = resource_group.name
        self.create_lb()

    def variable_reassignment(self, **kwargs):
        for key in kwargs:
            if key in self.params:
                self.params[key] = kwargs[key]
            else:
                print("hey this is probably an issue you should address")

    def create_lb(self):
        # Create an azure resource (lb)
        main = azure.lb.LoadBalancer(**self.params)