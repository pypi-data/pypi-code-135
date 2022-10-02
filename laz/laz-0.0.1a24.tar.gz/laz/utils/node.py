# internal
from laz.model.configuration import Configuration
from laz.model.node import Node
from laz.model.target import Target


def get_target_configuration(node: Node, target_name: str) -> Target:
    target = Target(target_name)
    target_path = f"{get_path(node)}{target_name}"
    node_configuration = get_node_configuration(node)
    target.push({"target": {"name": target_name, "path": target_path}})
    target.push(node_configuration.data)
    target.push(node_configuration.get_target(target_name).data)
    return target


def get_node_configuration(node: Node) -> Configuration:
    nodes = node.root_path()
    conf = Configuration(node.configuration.id)
    for node in nodes:
        conf.push(node.configuration.data)
    return conf


def get_path(node: Node) -> str:
    nodes = node.root_path()
    names = [node.configuration.name for node in nodes]
    return "/".join(names + [""])
