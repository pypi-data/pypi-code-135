#!/usr/bin/env python3

import os
import docker
import sys
import signal
from tabulate import tabulate
import requests

client = docker.from_env()


AUTERION_DEVICE_ADDRESS=os.getenv('AUTERION_DEVICE_ADDRESS', "10.41.1.1")

SYSINFO_API_ENDPOINT=f"http://{AUTERION_DEVICE_ADDRESS}/api/sysinfo/v1.0"
APPS_API_ENDPOINT=f"http://{AUTERION_DEVICE_ADDRESS}/api/apps/v1.0"

def signal_handler(sig, frame):
    sys.exit(0)

def usage(error_message=None):
    if error_message:
        print(error_message)
    print("""auterion-cli.py <command> <action>

    commands:
        info
        report
        app
        container
        help

    actions:
        info: Print general information about device and system
        report: Generate diagnostic report
        app:
            (list | ls) [app_name] - List all installed applications
            (remove | rm) <app_name> - Remove given application
            start <app_name> - Start given application
            stop <app_name> - Stop given application
            restart <app_name> - Restart given application
            enable <app_name> - Enable given application (starting next boot)
            disable <app_name> - Disable given application (starting next boot)
            status <app_name> - Get enable/disable state given application
            logs <app_name> - Get logs of given application

        container:
            (list | ls) - List all installed containers
            (remove | rm) <container_name> - Remove given container
            start <container_name> - Start given container
            stop <container_name> - Stop given container
            restart <container_name> - Restart given container
            enable <container_name> - Enable given container (starting next boot)
            disable <container_name> - Disable given container (starting next boot)
            status <container_name> - Get enable/disable state given container
            logs <container_name> - Get logs of given container
    """)

def error(msg, code=1):
    print(msg)
    exit(code)

def get_information(target):
    try:
        response = requests.get(f"{SYSINFO_API_ENDPOINT}/{target}",  timeout=5)
        if response:
            return response.json()
        else:
            return None
    except Exception as e:
        print(f"Failed to get {target} information:")
        print(e)
        return None

def info(args):
    print("===== Device Information =====")
    device = get_information("device")
    if device:
        print("UUID: {}".format(device['uuid']))
        print("FCID: {}".format(device['fcid']))
        print("Release: {}".format(device['release']))
        print("AuterionOS: {}".format(device['auterion_os']))
        if "px4" in device:
            print("PX4: {}".format(device['px4']))
        print("AOS hash: {}".format(device['hash']))
        if "px4_hash" in device:
            print("PX4 hash: {}".format(device['px4_hash']))
    else:
        print("No device information available")

    print("\n===== FC Information =====")
    fc = get_information("fc")
    if fc:
        print("Target: {}".format(fc['target']))
        if "px4" in device:
            print("PX4: {}".format(fc['px4']))
        if "px4_hash" in device:
            print("PX4: {}".format(fc['px4_hash']))
        print("Expected PX4: {}".format(fc['expected_px4_version']))
        print("Expected hash: {}".format(fc['expected_px4_hash']))
        print("Found FMU binary: {}".format(fc['fmu_binary']))
        print("Found FMU package: {}".format(fc['fmu_package']))
        print("Found FMU dev binary: {}".format(fc['fmu_dev_package']))

    else:
        print("No FC information available")

    print("\n===== Connectivity Information =====")
    connectivity = get_information("connectivity")
    if connectivity:
        print(f"Connectivity: {connectivity['status']}")
    else:
        print("No connectivity information available")

    print("\n===== Hardware Information =====")
    hardware = get_information("hardware")
    if hardware:
        for name, state in hardware.items():
            state_str = "[\033[32mGOOD\033[39m]" if state else "[\033[31mERROR\033[39m]"
            print("{}: {}".format(name.replace("_", " "), state_str))
    else:
        print("No hardware information available")

    print("\n===== Network Information =====")
    network = get_information("network")
    if network:
        for interface, data in network.items():
            print("{}:".format(interface))
            for k, v in data.items():
                print("\t{}:{}".format(k,v))
    else:
        print("No network information available")

    print("\n===== Software Information =====")
    software = get_information("software")
    if software:
        for name, data in software.items():
            print("{}:".format(name))
            if data['status'] == "running":
                status_str = "[\033[32mRUNNING\033[39m]"
            elif data['status'] == "succeed":
                status_str = "[\033[32mSUCCEED\033[39m]"
            else:
                status_str = "[\033[31mERROR\033[39m]"
            print("\thash: {}".format(data['hash']))
            print("\tstatus: {}".format(status_str))
    else:
        print("No software information available")

    print("\n===== System services Information =====")
    services = get_information("services")
    if services:
        for software, data in services.items():
            print("{}:".format(software))
            if data['status'] == "running":
                status_str = "[\033[32mRUNNING\033[39m]"
            elif data['status'] == "succeed":
                status_str = "[\033[32mSUCCEED\033[39m]"
            else:
                status_str = "[\033[31mERROR\033[39m]"
            print("\tstatus: {}".format(status_str))
    else:
        print("No services information available")

    print("\n===== USB devices Information =====")
    devices = get_information("usb_devices")
    if devices:
        for data in devices["usb_devices"]:
            if "product" in data:
                print(f"Product: {data['product']}")
            if "serial_number" in data:
                print(f"Serial number: {data['serial_number']}")
            if "manufacturer" in data:
                print(f"Manufacturer: {data['manufacturer']}")
            print("")
    else:
        print("No USB devices information available")

    print("\n===== Partitions Information =====")
    partitions = get_information("partitions")
    if partitions:
        for data in partitions["partitions"]:
            if "partition" in data:
                print(f"Partition: {data['partition']}")
            if "mount" in data:
                print(f"Mount point: {data['mount']}")
            if "size" in data:
                print(f"Size: {data['size']}")
            if "used" in data:
                print(f"Used: {data['used']}")
            if "available" in data:
                print(f"Available: {data['available']}")
            if "use" in data:
                print(f"Use: {data['use']}")
            print("")
    else:
        print("No partitions information available")

def report(args):
    report_name = "/tmp/report.zip"
    if len(args) > 2:
        if args[2] in ["-o", "--output"]:
            report_name = args[3]
    if not report_name.endswith(".zip"):
        report_name += ".zip"
    print(f"Downloading report: {report_name}")
    r = requests.get(f"{SYSINFO_API_ENDPOINT}/report")
    open(report_name, 'wb').write(r.content)

def get_app(app):
    data = requests.get(f'{APPS_API_ENDPOINT}/apps/{app}')
    try:
        body = data.json()
    except:
        body = {}
    if data:
        return body
    else:
        if "message" in body:
            error(body["message"])
        else:
            error(f"App {app} is not installed")

def get_apps():
    apps = requests.get(f'{APPS_API_ENDPOINT}/apps')
    if apps:
        return apps.json()
    else:
        error(f"Failed to get apps")

def print_apps(apps):
    headers=["Name", "Version", "Status", "Enable", "Services", "Status", "Enable"]
    matrix = []
    for app in apps:
        row = [app['name'], app['version'], app['status'], app['enable']]
        if len(app['services']) > 0:
            row.append(app['services'][0]["name"])
            row.append(app['services'][0]["status"])
            row.append(app['services'][0]["enable"])
        else:
            row.append("")
            row.append("")
        matrix.append(row)
        for s in app['services'][1:]:
            matrix.append(["", "", "", "", s["name"], s["status"], s["enable"]])
    print(tabulate(matrix, headers=headers))

def print_app_result(data, app, success_message):
    try:
        body = data.json()
    except:
        body = {}

    if data:
        if "message" in body:
            print(body["message"])
        else:
            print(f'App {app} {success_message}')
    else:
        if "message" in body:
            error(body["message"])
        else:
            error(f"App {app} is not installed")

def print_container_result(data, container, success_message):
    try:
        body = data.json()
    except:
        body = {}

    if data:
        if "message" in body:
            print(body["message"])
        else:
            print(f'Container {container} {success_message}')
    else:
        if "message" in body:
            error(body["message"])
        else:
            error(f"Container {container} not found")

def remove_app(app):
    data = requests.post(f'{APPS_API_ENDPOINT}/apps/{app}/remove')
    print_app_result(data, app, "removed")

def log_app(app, follow=False):
    data = requests.get(f'{APPS_API_ENDPOINT}/apps/{app}/logs')
    print(data)
    if data:
        print(data.text)
    else:
        error(f"App {app} is not installed")

def start_app(app):
    data = requests.post(f'{APPS_API_ENDPOINT}/apps/{app}/start')
    print_app_result(data, app, "started")

def stop_app(app):
    data = requests.post(f'{APPS_API_ENDPOINT}/apps/{app}/stop')
    print_app_result(data, app, "stopped")

def restart_app(app):
    data = requests.post(f'{APPS_API_ENDPOINT}/apps/{app}/restart')
    print_app_result(data, app, "restarted")

def enable_app(app):
    data = requests.post(f'{APPS_API_ENDPOINT}/apps/{app}/enable')
    print_app_result(data, app, "enabled")

def disable_app(app):
    data = requests.post(f'{APPS_API_ENDPOINT}/apps/{app}/disable')
    print_app_result(data, app, "disabled")

def status_app(app):
    data = requests.get(f'{APPS_API_ENDPOINT}/apps/{app}/status')
    print_app_result(data, app, "status")

def handle_app(args):
    if len(args) < 3:
        usage("Action is missing")
    action = args[2]

    if action in ["list", "ls"]:
        if len(args) > 3:
           print_apps([get_app(args[3])])
        else:
            print_apps(get_apps())
    elif action in ["remove", "rm"]:
        if len(args) < 4:
            usage("app name is missing")
        remove_app(args[3])
    elif action == "logs":
        follow = False
        if len(args) < 4:
            usage("app name is missing")
        if len(args) > 4:
            if args[4] in ["-f", "--follow"]:
                follow = True
        log_app(args[3], follow)
    elif action == "start":
        if len(args) < 4:
            usage("app name is missing")
        start_app(args[3])
    elif action == "stop":
        if len(args) < 4:
            usage("app name is missing")
        stop_app(args[3])
    elif action == "restart":
        if len(args) < 4:
            usage("app name is missing")
        restart_app(args[3])
    elif action == "enable":
        if len(args) < 4:
            usage("app name is missing")
        enable_app(args[3])
    elif action == "disable":
        if len(args) < 4:
            usage("app name is missing")
        disable_app(args[3])
    elif action == "status":
        if len(args) < 4:
            usage("app name is missing")
        status_app(args[3])
    elif action == "help":
        usage()
    else:
        usage(f'Unknown action {action}')

def get_containers():
    containers = requests.get(f'{APPS_API_ENDPOINT}/containers')
    if containers:
        return containers.json()
    else:
        error(f"Failed to get containers")

def print_containers(containers):
    headers=["Name","ID", "Image", "Status"]
    matrix = []
    for container in containers:
        matrix.append([container["name"],
            container["id"],
            container["image"],
            container["status"]])
    print(tabulate(matrix, headers=headers))

def remove_container(container):
    data = requests.post(f'{APPS_API_ENDPOINT}/containers/{container}/remove')
    print_container_result(data, container, "removed")

def log_container(container, follow=False):
    data = requests.get(f'{APPS_API_ENDPOINT}/containers/{container}/logs')
    if data:
        print(data.text)
    else:
        error(f"No container {container} found")

def start_container(container):
    data = requests.post(f'{APPS_API_ENDPOINT}/containers/{container}/start')
    print_container_result(data, container, "started")

def stop_container(container):
    data = requests.post(f'{APPS_API_ENDPOINT}/containers/{container}/stop')
    print_container_result(data, container, "stopped")

def restart_container(container):
    data = requests.post(f'{APPS_API_ENDPOINT}/containers/{container}/restart')
    print_container_result(data, container, "restarted")

def enable_container(container):
    data = requests.post(f'{APPS_API_ENDPOINT}/containers/{container}/enable')
    print_container_result(data, container, "enabled")

def disable_container(container):
    data = requests.post(f'{APPS_API_ENDPOINT}/containers/{container}/disable')
    print_container_result(data, container, "disabled")

def status_container(container):
    data = requests.get(f'{APPS_API_ENDPOINT}/containers/{container}/status')
    print_container_result(data, container, "status")

def handle_container(args):
    if len(args) < 3:
        usage("Action is missing")
    action = args[2]

    if action in ["list", "ls"]:
        print_containers(get_containers())
    elif action in ["remove", "rm"]:
        if len(args) < 4:
            usage("container name is missing")
        remove_container(args[3])
    elif action == "logs":
        follow = False
        if len(args) < 4:
            usage("container name is missing")
        if len(args) > 4:
            if args[4] in ["-f", "--follow"]:
                follow = True
        log_container(args[3], follow)
    elif action == "start":
        if len(args) < 4:
            usage("container name is missing")
        start_container(args[3])
    elif action == "stop":
        if len(args) < 4:
            usage("container name is missing")
        stop_container(args[3])
    elif action == "restart":
        if len(args) < 4:
            usage("container name is missing")
        restart_container(args[3])
    elif action == "enable":
        if len(args) < 4:
            usage("container name is missing")
        enable_container(args[3])
    elif action == "disable":
        if len(args) < 4:
            usage("container name is missing")
        disable_container(args[3])
    elif action == "status":
        if len(args) < 4:
            usage("container name is missing")
        status_container(args[3])
    elif action == "help":
        usage()
    else:
        usage(f'Unknown action {action}')

def main():
    args = sys.argv
    signal.signal(signal.SIGINT, signal_handler)
    if len(args) < 2:
        usage()
        return
    command = args[1]
    if command == "app":
        handle_app(args)
    elif command == "container":
        handle_container(args)
    elif command == "report":
        report(args)
    elif command == "info":
        info(args)
    elif command == "help":
        usage()
    else:
        usage(f'Unknown command {command}')

if __name__ == "__main__":
    main()
