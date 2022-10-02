# std
from typing import List

# internal
from laz.model.path import Path
from laz.model.matcher import Matcher
from laz.model.target import Target
from laz.model.node import Node
from laz.utils.node import get_node_configuration, get_target_configuration, get_path


class Resolver:
    def __init__(self, node: Node, path: Path):
        self.node = node
        self.path = path

    def resolve(self) -> List[Target]:
        nodes = self.resolve_nodes()
        return self.resolve_targets(nodes)

    def resolve_nodes(self) -> List[Node]:
        matcher = Matcher(self.path.base_pattern)
        nodes: List[Node] = []
        for node in self.node.nodes():
            name_path = get_path(node)
            if matcher.match(name_path):
                nodes.append(node)
        return nodes

    def resolve_targets(self, nodes: List[Node]) -> List[Target]:
        matcher = Matcher(self.path.target)
        configurations = []
        for node in nodes:
            node_configuration = get_node_configuration(node)
            for target_name in node_configuration.data.get("targets", {}).keys():
                if matcher.match(target_name):
                    target_configuration = get_target_configuration(node, target_name)
                    configurations.append(target_configuration)
        return configurations
