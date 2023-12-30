import networkx as nx
from math import prod

print('--- Day 25: Snowverload ---')

G = nx.Graph()
with open('input.txt', 'r') as f:
    for line in f:
        left, right = line.split(':')
        for node in right.strip().split():
            G.add_edge(left, node)

G.remove_edges_from(nx.minimum_edge_cut(G))
print('Answer: ', prod([len(c) for c in nx.connected_components(G)]))
