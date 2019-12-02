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

    file_load = toml.load(filename)
    contents = file_load["routers"]
    address = dict()
    for item in contents:
        address[item['address']] = item['name']
    neighbors = contents[0]['neighbors']
    address_copy = address.copy()

    for item in neighbors:
        new_dict = item['address']
        name = address_copy[new_dict]
        item['name'] = name
    for item in contents:
        n = item['neighbors']
    

    data = Graph() #Trying to add dictionary values to data so it can be called in find path function.
    data.set_vertex(item['name'])
    for i in n:
        i['name'] = address[i['address']]
        data.add_edge(item['name'], i['name'], i['cost'])
    return data
    
    
  

def find_path(g: Graph, start: str) -> None:
    """Use Dijkstra's algorithm to find the shortest path from *start* to other vertices"""
    g.dijkstra(start)
    
   


def main():
    x = read_toml(filename='./data/exercises/dijkstra/network.toml')
    #print(x) #- vertex is t.
    print(find_path(x, x.get_vertex('t')))
    #pass


if __name__ == "__main__":
    main()
