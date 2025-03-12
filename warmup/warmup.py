import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Create a graph (Zachary's Karate Club graph)
G = nx.karate_club_graph()

# Basic properties
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_dict = dict(G.degree())

# Compute the diameter (only for connected graphs)
if nx.is_connected(G):
    diameter = nx.diameter(G)
else:
    diameter = "Graph is not connected"

# Print properties
print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")
print(f"Diameter: {diameter}")
print("Adjacency List:")
for node, neighbors in G.adjacency():
    print(f"{node}: {list(neighbors)}")


plt.figure(figsize=(8,6))
nx.draw_circular(G, with_labels=True)
plt.title("Graph Visualization")
plt.savefig("karate_club_graph.png")
plt.show()



# The degree distribution shows how many nodes have a certain degree (number of connections).
degrees = np.array(list(degree_dict.values()))
plt.figure(figsize=(7,5))
plt.hist(degrees, bins=range(min(degrees), max(degrees)+2), align='left', color='skyblue', edgecolor="black")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.title("Degree Distribution")
plt.xticks(range(min(degrees), max(degrees)+1))
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.savefig("karate_club_graph-DD.png")
plt.show()
