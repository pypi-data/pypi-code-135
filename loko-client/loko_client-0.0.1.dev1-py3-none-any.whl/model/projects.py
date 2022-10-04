from loko_client.utils.gobjects_utils import GObject


class Nodes:
    def __init__(self, nodes):
        self.nodes = {node['id']: GObject('Node', **node) for node in nodes}

    def all(self):
        return list(self.nodes.keys())

    def search(self, key, value):
        for _id,node in self.nodes.items():
            val = node
            for k in key.split('.'):
                val = val.get(k)
                if not val:
                    break
            if val==value:
                yield _id

    def __getitem__(self, item):
        return self.nodes[item]


class Edges:
    def __init__(self, edges):
        self.edges = {edge['id']: GObject('Edge', **edge) for edge in edges}

    def all(self):
        return list(self.edges.keys())


class Project:
    def __init__(self, name, id, description, created_on, last_modify, graphs, open, active, version, deployed):
        self.name = name
        self.id = id
        self.description = description
        self.created_on = created_on
        self.last_modify = last_modify
        self.open = open
        self.active = active
        self.version = version
        self.deployed = deployed

        self.graphs = graphs

        self.tabs = GObject('Tabs', **{name: GObject('Tab', nodes=Nodes(tab['nodes']), edges=Edges(tab['edges']))
                                       for name,tab in self.graphs.items()})




