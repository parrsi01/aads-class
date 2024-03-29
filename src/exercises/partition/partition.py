#!/usr/bin/env python3
"""Implementation of the Partition data structure"""

from xml.dom import minidom
from collections import namedtuple

Vertex = namedtuple("Vertex", ["id", "x", "y", "key"])
Edge = namedtuple("Edge", ["src", "dst", "weight"])


class Partition:
    def __init__(self, size):
        self._forest = [x for x in range(size)]

    @property
    def forest(self):
        """Return the forest"""
        return self._forest

    def add(self, e: Edge):
        """
        Add an edge to the partition

        Find the root of the source vertex tree
        Find the root of the destination vertex tree
        If they are different, set root of the destination vertex tree to the root of the source vertex tree
        """
        src = e.src
        dst = e.dst

        root_src = self._find_root(src)
        root_dst = self._find_root(dst)

        if root_dst != root_src:
            self._forest[root_dst] = root_src
        #raise NotImplementedError

    def _find_root(self, node: int) -> int:
        """
        Find root of tree that this node belongs to.

        The root of a tree is a node that has its value matching the index in the forest
        """
        while node != self._forest[node]:
            node = self._forest[node]
        return node
        #raise NotImplementedError

    def __str__(self) -> str:
        """Stringify the forest"""
        return str(self._forest)

    def __iter__(self):
        """Iterate over the forest"""
        return iter(self._forest)


def read_xml(filename: str) -> tuple:
    """Read XML representation of the graph"""
    vertices = {}  # {int: Vertex}
    edges = []  # [Edge]

    xml_doc = minidom.parse(filename)
    xml_graph = xml_doc.getElementsByTagName("Graph")[0]
    xml_vertices = xml_graph.getElementsByTagName("Vertices")[0].getElementsByTagName("Vertex")
    xml_edges = xml_graph.getElementsByTagName("Edges")[0].getElementsByTagName("Edge")

    # TODO: Add all vertices from the XML file to the dictionary of vertices
    for i in xml_vertices:
        id = i.getAttribute("id")
        x = i.getAttribute("x")
        y = i.getAttribute("y")
        key = i.getAttribute("label")
        vertices[id] = Vertex(id,float(x),float(y),key)
        #vertices = Vertex(id,float(x),float(y),key)


    # TODO: Add all edges from the XML file to the list of edges
    for i in xml_edges:
        src = i.getAttribute("source")
        dst = i.getAttribute("destination")
        weight = i.getAttribute("weight")
        edges.append(Edge(int(src),int(dst),float(weight)))

    return vertices, edges


def main():
    """Main function"""
    
    vertices, edges = read_xml("data/exercises/partition/neia.xml")
    # f = Partition(10)
    # print(type(f.forest))
    partition = Partition(len(vertices))
    print(", ".join([f"{x:2}" for x in range(len(vertices))]))
    for edge in sorted(edges, key=lambda e: e.weight):
        partition.add(edge)
        print(", ".join([f"{x:2}" for x in partition]))
    print(", ".join([f"{x:2}" for x in range(len(vertices))]))
    print(partition.forest)


if __name__ == "__main__":
    main()
