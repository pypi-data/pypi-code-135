import pulumi
import pulumi_azure as azure
import json


class BaseAppService:

    params = {
        "resource_name": "test-app-service"
    }

    def __init__(self, resource_group, **kwargs): 
        self.params["resource_group_name"] = resource_group.name
        self.variable_reassignment(**kwargs)
        self.create_app_service()

    def variable_reassignment(self, **kwargs):
        for key in kwargs:
            if key in self.params:
                self.params[key] = kwargs[key]
            else:
                print("hey this is probably an issue you should address")

    def create_app_service(self):
        # Create an azure resource (app service)
        self.params["app_service_plan_id"] = self.create_plan()
        main = azure.appservice.AppService(**self.params)

    def create_plan(self):
        plan_params = {
            "resource_name": "test-plan",
            "resource_group_name": self.params["resource_group_name"],
            "sku": azure.appservice.PlanSkuArgs(tier="Standard", size="S1")
        }
        return azure.appservice.Plan(**plan_params).id