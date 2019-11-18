#!/usr/bin/env python3
"""Dijkstra's algorithm usage"""

from pythonds3.graphs import Graph
import toml
import configparser


def read_toml(filename: str) -> Graph:
    """Read TOML config file"""
    config = configparser.ConfigParser()
    config.read(filename)
    return config
    #pass

def find_path(g: Graph, start: str) -> None:
    """Use Dijkstra's algorithm to find the shortest path from *start* to other vertices"""
    #pass


def main():
    pass


if __name__ == "__main__":
    main()
