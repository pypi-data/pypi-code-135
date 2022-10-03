import pulumi
import pulumi_azure as azure
import json

class BaseDB:

    params = {
        "resource_name": "test-db",
        "server_name": "erase-me"
    }

    def __init__(self, resource_group, **kwargs): 
        self.params["resource_group_name"] = resource_group.name
        self.variable_reassignment(**kwargs)
        self.create_db()

    def variable_reassignment(self, **kwargs):
        for key in kwargs:
            if key in self.params:
                self.params[key] = kwargs[key]
            else:
                print("hey this is probably an issue you should address")

    def create_db(self):
        # Create an azure resource (db)
        main = azure.sql.Database(**self.params)