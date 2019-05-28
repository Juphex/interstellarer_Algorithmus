# -*- coding: utf-8 -*-
"""
Created on Sat May 25 15:39:54 2019

@author: Christian Salamut
"""

import json
from collections import defaultdict

def dijsktra(initial, nodes, edges, distances):
  visited = {initial: 0}
  path = {}

  nodes = set(nodes)

  while nodes: 
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in edges[min_node]:
      weight = current_weight + distances[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path


        
if __name__ == "__main__":

    f = open("generatedGraph.json","r")
    data = f.read()
    data = json.loads(data)
    nodes = data["nodes"]
    edges = data["edges"]
    edges2 = defaultdict(list)
    nodes2 = []    
    distances = {}
    for i in range (0,1500):
        nodes2.append(str(i))
    for e in edges:
        edges2[str(e["source"])].append(str(e["target"]))
        edges2[str(e["target"])].append(str(e["source"]))

    for e in edges:
        distances[(str(e["source"]),str(e["target"]))] = e["cost"]
        #didirectional
        distances[(str(e["target"]),str(e["source"]))] = e["cost"]

    path1 = dijsktra("18",nodes2,edges2,distances)
