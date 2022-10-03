import pulumi
import pulumi_azure as azure
import json


class BaseVM:

    params = {
        "resource_name": "test-vm",

        "network_interface_name": "network_interface",
        "private_ip_address_allocation": "Dynamic",

        "subnet_id": "test-subnet-0",

        "vm_size": "Standard_DS1_v2",

        "sod_name": "test_storage_os_disk",
        "sod_caching": "ReadWrite",
        "sod_create_option": "FromImage",
        "sod_managed_disk_type": "Standard_LRS"

    }

    def __init__(self, resource_group, current_vn, **kwargs): 
        self.params["resource_group_name"] = resource_group.name
        self.variable_reassignment(**kwargs)
        #self.params["subnet_id"] = vpc.instance.private_subnet_ids.apply(lambda id: id[0])
        self.create_vm()

    def variable_reassignment(self, **kwargs):
        for key in kwargs:
            if key in self.params:
                self.params[key] = kwargs[key]
            else:
                print("hey this is probably an issue you should address")

    def network_interface(self):
        main_network_interface = azure.network.NetworkInterface("mainNetworkInterface",
            resource_group_name=self.params["resource_group_name"],
            ip_configurations=[azure.network.NetworkInterfaceIpConfigurationArgs(
                name=self.params["network_interface_name"],
                private_ip_address_allocation=self.params["private_ip_address_allocation"],
            )])
        return main_network_interface

    def storage_os_disk(self):
        return azure.compute.VirtualMachineStorageOsDiskArgs(
            name=self.params["sod_name"],
            caching=self.params["sod_caching"],
            create_option=self.params["sod_create_option"],
            managed_disk_type=self.params["sod_managed_disk_type"]
        )

    def create_vm(self):
        # Create an azure resource (vm)

        network_interface = self.network_interface()
        storage_os_disk = self.storage_os_disk()

        finalized_params = {
            "resource_group_name": self.params["resource_group_name"],
            "resource_name": self.params["resource_name"],
            "network_interface_ids": [network_interface.id],
            "storage_os_disk": storage_os_disk,
            "vm_size": self.params["vm_size"]
        }
        main = azure.compute.VirtualMachine(**finalized_params)