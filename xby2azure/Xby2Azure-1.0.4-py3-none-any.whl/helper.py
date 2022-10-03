import json
import os

def help():
    print('''Xby2 Azure Cloud Practice Library
Steps for getting started:
* Install this package
* Run xby2-init
* Activate virtual environment (.\venv\Scripts\activate)
* Install requirements (pip install -r requirements.txt)
* Add resources to resources.json file
* Run pulumi up (using active Azure profile)
* Push to BitBucket repo (Coming Soon)

VN:
Here are the fields you can customize in KWARGS and the (defaults):  
* "address_spaces": "full",
* "resource_name": "test-vn",
* "dns_servers": ["10.0.0.4", "10.0.0.5"],
* "subnet_address_prefixes":["10.0.1.0/24", "10.0.2.0/24"],
* "subnet_names":["test-subnet-0", "test-subnet-1"]

Security Group:
Here are the fields you can customize in KWARGS and the (defaults):  
* "resource_name": "test-security-group"

LB:
Here are the fields you can customize in KWARGS and the (defaults):  
* resource_name (test-lb)

VM:
Here are the fields you can customize in KWARGS and the (defaults):  
* "resource_name": "test-vm",
* "network_interface_name": "network_interface",
* "private_ip_address_allocation": "Dynamic",

* "subnet_id": "test-subnet-0",

* "vm_size": "Standard_DS1_v2",

* "sod_name": "test_storage_os_disk",
* "sod_caching": "ReadWrite",
* "sod_create_option": "FromImage",
* "sod_managed_disk_type": "Standard_LRS"

DB:
Here are the fields you can customize in KWARGS and the (defaults):  
* "resource_name": "test-db",
* "server_name": "erase-me"

Blob:
Here are the fields you can customize in KWARGS and the (defaults):    
* "resource_name": "testblob",
* "storage_account_name": "testaccount",
* "storage_container_name": "testcontainer",
* "type": "Page",
* "size": 512

App Service
* "resource_name": "test-app-service"

Nat Gateway
* "resource_name": "test-nat-gateway"

Resource Group
Resource groups are presently the only resource where an existing instance can be retrieved from Azure as a part of our default library. This can be accomplished using an additional boolean in the resource group entry of the config file. When this variable (called "does_exist") is set to true, the program will attempt to retrieve the resource group that corresponds to the parameters provided in the overrides dictionary. The only required parameters are "resource_name" and "id" but you can feel free to include the others described in the documentation.

SSIS IR
* "resource_name": "test-ssis-ir",
* "data_factory_id": "test-data-factory",
* "node_size": "Standard_D1_v2",
* "location": "eastus2"

Virtual Network Peering
* "resource_name": "test-ssis-ir",
* "remote_virtual_network_id": "test",
* "virtual_network_name": "test"

Adding Resources:
Keep the order of declaration in mind. For example, the resource group, followed by the VN should likely be the first things declared. When using the options above, the resource will use require a "module", which will refer to a file within the BaseAzure folder, a "resource_name", which will be the name of one of our custom classes, "overrides", which will be a list of any parameters that we want changed from the default values, and a boolean: "req_vn". This will indicate whether a particular resource will need us to pass in a vn. Additionally, we can create resources that we haven't customized. This will require a "module", which will probably begin with "pulumi_azure.", the "resource_name", which will be a class within said module, "overrides", which will consist of **all** of the parameters needed for this resource, and the aforementioned booleans. Below is an example of an item in the resources list:  
```json
{
    "module": "BaseAzure.vm",
    "resource_name": "BaseVM",
    "overrides": {},
    "req_vn": true
}
```

Resource Booleans
| Resource | req_vn |
| --- | ----------- |
| BaseBlob | false | 
| BaseDB | false |
| BaseSecurityGroup | true |
| BaseVM | true |
| BaseVN | false | 
| BaseLB | false | 
| BaseResourceGroup | false |
| BaseSSIS | false |
| BaseVirtualNetworkPeering | false | 
| BaseNatGateway | false | 
| BaseAppService | false |  ''')

def init():

    os.system('pulumi new python')
    os.system('git init')
    json_string = "{\"resources\": [{}]}"
    with open('resources.json', 'w') as outfile:
        outfile.write(json_string)

    main = '''import pulumi
import pulumi_azure
import BaseAzure
import json
import traceback
import importlib

with open ("resources.json", "r") as deployfile:
    res = json.load(deployfile)

current_vn = None

for resource in res["resources"]:
    assert resource["module"].startswith("BaseAzure") or resource["module"].startswith("azure")
    try:
        if resource["module"] is "BaseAzure.resource_group" and resource["does_exist"]:
            resource_group = pulumi_azure.core.get(resource["overrides"]["resource_name"], resource["overrides"]["id"])
        else:
            module = importlib.import_module(resource["module"])
            resource_class = getattr(module, resource["resource_name"])

            if resource["req_vn"]:
                instance = resource_class(resource_group, current_vn, **resource["overrides"])
            else:
                instance = resource_class(resource_group, **resource["overrides"])

            # set current vn
            if resource["resource_name"] == "BaseVN":
                current_vn = instance

            # set current resource group
            if resource["resource_name"] == "BaseResourceGroup":
                resource_group = instance

            # add roles to a list of roles
            roles = {}
            if resource["resource_name"] == "RoleDefinition":
                roles[resource["overrides"]["resource_name"]] = instance.id

            pulumi.export(resource["resource_name"], instance)

    except:
        traceback.print_exc()
        print(resource["module"])'''

    with open('__main__.py', 'w') as outfile:
        outfile.write(main)

    req = '''pulumi>=3.0.0,<4.0.0
pulumi-azure-native>=1.0.0,<2.0.0
pulumi-azure
Xby2Azure>=1.0.0'''

    with open('requirements.txt', 'w') as outfile:
        outfile.write(req)

    pipeline = '''image: python:3.10
# this is a look at what a CI/CD pipeline for this package might look like
# feel free to make changes but this should work out of the box, assuming you find a way to connect to AWS
# check out this link if you'd like to see how I went about doing that
# https://support.atlassian.com/bitbucket-cloud/docs/deploy-on-aws-using-bitbucket-pipelines-openid-connect/
pipelines:
  default:
    - step:
        oidc: true
        caches:
          - pip
        script:
          # TO DO: Add Azure CLI login
          # pulumi
          - curl -fsSL https://get.pulumi.com/ | sh
          - export PATH=$PATH:$HOME/.pulumi/bin
          - pulumi plugin install resource aws v5.4.0
          - pulumi stack select dev
          - pulumi up -y
          - pulumi destroy -y
          - pulumi stack export --file manifest.json'''

    with open('bitbucket-pipelines.yml', 'w') as outfile:
        outfile.write(pipeline)
