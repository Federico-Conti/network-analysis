# https://networkx.org/nx-guides/content/exploratory_notebooks/facebook_notebook.html

# Nodes 0, 107, 348, 414, 686, 698, 1684, 1912, 3437, 3980
# are the ones whose friends list will be examined. That means that they are in the spotlight of this analysis. Those nodes are considered the spotlight nodes
 
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from random import randint
import pickle
import os

# Load the Facebook dataset
facebook = pd.read_csv(
    "data/facebook_combined.txt.gz",
    compression="gzip",
    sep=" ",
    names=["start_node", "end_node"],
)

print(facebook.head())

G = nx.from_pandas_edgelist(facebook, "start_node", "end_node")

# Visualize the graph

# fig, ax = plt.subplots(figsize=(15, 9))
# ax.axis("off")
# plot_options = {"node_size": 10, "with_labels": False, "width": 0.15}
# nx.draw_networkx(G, pos=nx.random_layout(G), ax=ax, **plot_options)
# plt.show()

# pos = nx.spring_layout(G, iterations=15, seed=1721)
# fig, ax = plt.subplots(figsize=(15, 9))
# ax.axis("off")
# nx.draw_networkx(G, pos=pos, ax=ax, **plot_options)
# plt.show()

print(f"Number of nodes: {G.number_of_nodes()}")

print(f"Number of edges: {G.number_of_edges()}")

print(f"Average degree: {np.mean([d for _ , d in G.degree()])}")

# print(f"Graph diameter: {nx.diameter(G)}")

shortest_path_file = "data/shortest_path_lengths.pkl" # dict-of-dict that maps a node u to all other nodes in the network, 

# Compute and save shortest path lengths if not already saved
if not os.path.exists(shortest_path_file):
    shortest_path_lengths = dict(nx.all_pairs_shortest_path_length(G))
    print(shortest_path_file)
    with open(shortest_path_file, "wb") as f:
        pickle.dump(shortest_path_lengths, f)
else:
    with open(shortest_path_file, "rb") as f:
        shortest_path_lengths = pickle.load(f)

# Use the loaded shortest path lengths to compute diameter
diameter = max(nx.eccentricity(G, sp=shortest_path_lengths).values())
print(f"Graph diameter == Max eccentricity: {diameter}")


# Compute the average shortest path length for each node
# More efficient than computing nx.average_shortest_path_length(G)

average_path_lengths = [
    np.mean(list(spl.values())) for spl in shortest_path_lengths.values()
]
print(f"Average shortest path length: {np.mean(average_path_lengths)}")


# We know the maximum shortest path length (the diameter), so create an array
# to store values from 0 up to (and including) diameter
path_lengths = np.zeros(diameter + 1, dtype=int)

# Extract the frequency of shortest path lengths between two nodes
for pls in shortest_path_lengths.values():
    pl, cnts = np.unique(list(pls.values()), return_counts=True) #pl is the path length, cnts is the count of occurrences
    path_lengths[pl] += cnts

# Express frequency distribution as a percentage (ignoring path lengths of 0)
freq_percent = 100 * path_lengths[1:] / path_lengths[1:].sum()

# Plot the frequency distribution (ignoring path lengths of 0) as a percentage
fig, ax = plt.subplots(figsize=(15, 8))
ax.bar(np.arange(1, diameter + 1), height=freq_percent)
ax.set_title(
    "Distribution of shortest path length in G", fontdict={"size": 35}, loc="center"
)
ax.set_xlabel("Shortest Path Length", fontdict={"size": 22})
ax.set_ylabel("Frequency (%)", fontdict={"size": 22})
plt.show()


print("Density of the graph: ", nx.density(G))
print("Number of connected components: ", nx.number_connected_components(G))