import pulumi
import pulumi_azure as azure
#import pulumi_azure_native as azure
import json

class BaseVN:
    
    params = {
        "address_spaces": "full",
        "resource_name": "test-vn",
        "dns_servers": ["10.0.0.4", "10.0.0.5"],
        "subnet_address_prefixes":["10.0.1.0/24", "10.0.2.0/24"],
        "subnet_names":["test-subnet-0", "test-subnet-1"]
    }

    def __init__(self, resource_group, **kwargs):
        self.params["location"] = resource_group.location
        self.variable_reassignment(**kwargs)
        self.instance = self.create_vn(resource_group, [])

    def variable_reassignment(self, **kwargs):
        for key in kwargs:
            if key in self.params:
                self.params[key] = kwargs[key]
            else:
                print("hey this is probably and issue you should address")

    def address_space(self):
        # i think this is for address space
        if self.params["address_spaces"] == "partial":
            space = "172.31.0.0/16"
        elif self.params["address_spaces"] == "full":
            space = "10.0.0.0/16"
        else:
            space = "192.168.0.0/16"
        return space

    def create_vn(self, resource_group, security_groups):

        subnets = self.create_subnets()
        address_space = self.address_space()

        finalized_params = {
            "resource_group_name": resource_group,
            "resource_name": self.params["resource_name"],
            "address_spaces": [address_space],
            "subnets": subnets,
            "dns_servers": self.params["dns_servers"],
            "location": self.params["location"]
            
        }
        main = azure.network.VirtualNetwork(**finalized_params)

    def create_subnets(self):
        subnets= []
        while len(self.params["subnet_address_prefixes"]) > 0:
            subnets.append(azure.network.VirtualNetworkSubnetArgs(name=self.params["subnet_names"][0], address_prefix=self.params["subnet_address_prefixes"][0]))
            self.params["subnet_address_prefixes"].pop(0)
            self.params["subnet_names"].pop(0)

        return subnets
        