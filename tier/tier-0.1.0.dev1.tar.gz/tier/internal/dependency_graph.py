# std
from __future__ import annotations
import os
from typing import List, Optional as Opt

# internal
from tier.internal.graph import Graph, Vertex
from tier.internal.pyproject import PyProject


class DependencyGraph(Graph[PyProject]):

    def __init__(self, *vertices: Vertex[PyProject]):
        super().__init__(*vertices)
        self.vertices_by_package_name = {
            v.data.build_system().get_package_name(): v for v in vertices
        }

    def get_project(self, package_name: str) -> PyProject:
        return self.vertices_by_package_name[package_name].data

    def get_internal_dependencies(self, package_name: str) -> List[str]:
        project: PyProject = self.vertices_by_package_name[package_name].data
        dependency_names = project.build_system().get_dependencies().keys()
        internal_dependencies = [d for d in dependency_names if d in self.vertices_by_package_name]
        return internal_dependencies

    @classmethod
    def create(cls, dirpath: Opt[str] = None) -> DependencyGraph:
        dirpath = dirpath or os.getcwd()
        vertices = {
            p.build_system().get_package_name(): Vertex(p)
            for p in PyProject.find_recursively(dirpath)
        }
        graph = DependencyGraph(*vertices.values())
        for package_name, package_vertex in vertices.items():
            for dependency_name in graph.get_internal_dependencies(package_name):
                if dependency_name in vertices:
                    dependency_vertex = vertices[dependency_name]
                    graph.add_edge(package_vertex, dependency_vertex)
        return graph
