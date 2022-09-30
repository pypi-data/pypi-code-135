import pulumi
import pulumi_azure as azure
import json

class BaseAccount:

    params = {
        "resource_name": "storageaccount",
        "account_replication_type": "LRS",
        "account_tier": "Standard", #there's a chance that only premium is valid but i can't tell
        "account_kind": "BlobStorage"
    }

    def __init__(self, created, **kwargs): 
        self.params["resource_group_name"] = created["resource_group"].name
        self.variable_reassignment(**kwargs)
        self.instance = self.create_account()

    def variable_reassignment(self, **kwargs):
        for key in kwargs:
            if key in self.params:
                self.params[key] = kwargs[key]
            else:
                print("hey this is probably an issue you should address")

    def create_account(self):
        # Create an azure resource (storage account)
        main = azure.storage.Account(**self.params)
        return main