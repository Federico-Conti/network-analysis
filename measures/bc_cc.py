import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# G = nx.read_adjlist("ex3.txt")

G = nx.read_adjlist("london_tube.txt", create_using=nx.DiGraph)

# Basic properties
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

# # Compute the diameter (only for connected graphs)
# if nx.is_connected(G):
#     diameter = nx.diameter(G)
# else:
#     diameter = "Graph is not connected"


degree = dict(sorted(dict(G.degree()).items(), key=lambda item: item[1], reverse=True))
betweeness = dict(sorted(nx.betweenness_centrality(G, normalized=False).items(), key=lambda item: item[1], reverse=True))
closeness = dict(sorted(nx.closeness_centrality(G).items(), key=lambda item: item[1], reverse=True))

# Print properties
print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")
# print(f"Diameter: {diameter}")
print(f"Degree: {degree}\n")
print(f"Betweeness: {betweeness}\n")
print(f"Closeness: {closeness}\n")

# print("Adjacency List:")
# for node, neighbors in G.adjacency():
#     print(f"{node}: {list(neighbors)}")


# Draw graph
pos = nx.spring_layout(G, seed=89)
options = {
    "node_color": "blue",
    "node_size": 20,
    "edge_color": "grey",
    "linewidths": 0,
    "width": 0.5,
}
nx.draw(G, pos, **options)
plt.show()
