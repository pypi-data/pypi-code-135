# GeoGraph: Graph theory with geometric functions as well
#
# Adam Birchfield, Texas A&M University
# 
# Log:
# 8/8/22 Created initial version
#
from ..containers import Bus, Sub
import networkx as nx
from scipy.spatial import Delaunay
import numpy as np

class GeoGraph:

    def __init__(self, nodes):
        self.g = nx.Graph()
        nodes = list(nodes)
        if len(nodes) > 1 and type(nodes[0]) == Bus:
            self.g.add_nodes_from([(b, dict(x=b.sub.longitude, y=b.sub.latitude)) for b in nodes])
        elif len(nodes) > 1 and type(nodes[0]) == Sub:
            self.g.add_nodes_from([(s, dict(x=s.longitude, y=s.latitude)) for s in nodes])
        else:
            self.g.add_nodes_from(nodes)

    def add_edges(self, edges):
        self.g.add_edges_from(edges)

    def Delaunay(self, del_dist=1):
        nodes = list(self.g.nodes)
        points = [(self.g.nodes[n]["x"], self.g.nodes[n]["y"]) for n in nodes]
        tri = Delaunay(points)
        pairs = set()
        for simp in tri.simplices:
            pairs.add(tuple(sorted([simp[0], simp[1]])))
            pairs.add(tuple(sorted([simp[0], simp[2]])))
            pairs.add(tuple(sorted([simp[2], simp[1]])))
        edges = [(nodes[p[0]], nodes[p[1]], dict(dist=self.great_circle_dist(
            self.g.nodes[nodes[p[0]]]["x"], self.g.nodes[nodes[p[0]]]["y"], 
            self.g.nodes[nodes[p[1]]]["x"], self.g.nodes[nodes[p[1]]]["y"], 
            True), dela_dist=1)) for p in pairs]
            
        # MST Algorithm (Kruskals from http://algs4.cs.princeton.edu/43mst/)
        edges.sort(key=lambda e:e[2]["dist"])
        node_index = {nodes[i]:i for i in range(len(nodes))}
        parent = list(range(len(nodes)))
        rank = [0 for _ in range(len(nodes))]
        edges_mst = []
        for e in edges:
            g1 = node_index[e[0]]
            g2 = node_index[e[1]]
            while g1 != parent[g1]:
                g1 = parent[g1] = parent[parent[g1]]
            while g2 != parent[g2]:
                g2 = parent[g2] = parent[parent[g2]]
            if g1 == g2:
                continue
            if rank[g1] < rank[g2]:
                parent[g1] = g2 
            elif rank[g2] < rank[g1]:
                parent[g2] = g1
            else:
                parent[g2] = g1
                rank[g1] += 1
            e[2]["dela_dist"] = 0
            edges_mst.append(e)

        if del_dist == 0:
            self.g.add_edges_from(edges_mst)
            return

        self.g.add_edges_from(edges)

        if del_dist == 1:
            return

        # BFS to find second and third neighbors
        d23edges = []
        edge_lookup = {(e[0], e[1]):e for e in edges}
        for n in self.g.nodes:
            for n1 in self.g.adj[n]:
                for n2 in self.g.adj[n1]:
                    if n2 == n:
                        continue
                    if (n, n2) in edge_lookup:
                        if edge_lookup[(n, n2)][2]["dela_dist"] == 3:
                            edge_lookup[(n, n2)][2]["dela_dist"] = 2
                    elif (n2, n) in edge_lookup:
                        if edge_lookup[(n2, n)][2]["dela_dist"] == 3:
                            edge_lookup[(n2, n)][2]["dela_dist"] = 2
                    else:
                        e = (n, n2, dict(dist=self.great_circle_dist(
                            self.g.nodes[n]["x"], self.g.nodes[n]["y"], 
                            self.g.nodes[n2]["x"], self.g.nodes[n2]["y"], 
                            True), dela_dist=2))
                        edge_lookup[(n, n2)] = e
                        d23edges.append(e)
                    if del_dist == 3:
                        for n3 in self.g.adj[n2]:
                            if n3 == n1 or n3 == n:
                                continue
                            if (n, n3) in edge_lookup:
                                continue
                            if (n3, n) in edge_lookup:
                                continue
                            e = (n, n3, dict(dist=self.great_circle_dist(
                                self.g.nodes[n]["x"], self.g.nodes[n]["y"], 
                                self.g.nodes[n3]["x"], self.g.nodes[n3]["y"], 
                                True), dela_dist=3))
                            edge_lookup[(n, n3)] = e
                            d23edges.append(e)
        self.g.add_edges_from(d23edges)


    def great_circle_dist(self, el1, p1, el2, p2, deg=False, km=False):
        if deg:
            el1 = el1*np.pi/180
            p1 = p1*np.pi/180
            el2 = el2*np.pi/180
            p2 = p2*np.pi/180
        part1 = np.power(np.sin((p2 - p1) / 2), 2)
        part2 = np.cos(p1) * np.cos(p2) * np.power(np.sin((el2 - el1) / 2), 2)
        rearth = 3959
        if km:
            rearth *= 1.60934
        return rearth * 2 * np.arcsin(np.sqrt(part1 + part2))