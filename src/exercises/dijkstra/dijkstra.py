#!/usr/bin/env python3
"""Dijkstra's algorithm usage"""

from pythonds3.graphs import Graph
import toml
import os


# x = ((toml.load('./data/exercises/dijkstra/network.toml')))
# #print(type(x['routers']))
# y = x['routers']
# for item in y:
#     print(type(item))
# print('')        
# print(y[0]) #it's t

def read_toml(filename: str) -> Graph:
    """Read TOML config file"""

    load_file = toml.load(filename)
    contents = load_file['routers']
    #add file contents to dictionary
    dict_names = dict()
    for items in contents:
        dict_names[items['address']] = items['name']
        neighbors = contents[0]['neighbors']
    new_dict = dict_names.copy()
    



    return toml.load(filename)
    
    
  

def find_path(g: Graph, start: str) -> None:
    """Use Dijkstra's algorithm to find the shortest path from *start* to other vertices"""

    g.dijkstra(start)
    
   


def main():
    x = read_toml(filename='./data/exercises/dijkstra/network.toml')
    print(x)
    #pass


if __name__ == "__main__":
    main()
