import pulumi
import pulumi_azure as azure
import json


class BaseVirtualNetworkPeering:

    params = {
        "resource_name": "test-ssis-ir",
        "remote_virtual_network_id": "test",
        "virtual_network_name": "test"

    }

    def __init__(self, resource_group_name, **kwargs):
        self.params["resource_group_name"] = resource_group_name 
        self.variable_reassignment(**kwargs)
        self.create_vnp()

    def variable_reassignment(self, **kwargs):
        for key in kwargs:
            if key in self.params:
                self.params[key] = kwargs[key]
            else:
                print("hey this is probably an issue you should address")

    def create_vnp(self):
        # Create an azure resource (vnp)
        main = azure.network.VirtualNetworkPeering(**self.params)