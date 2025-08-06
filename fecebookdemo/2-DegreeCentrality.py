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

G = nx.from_pandas_edgelist(facebook, "start_node", "end_node")


degree_centrality = nx.centrality.degree_centrality(G)  
# nodes with the 8 highest degree centralities
top_8 = (sorted(degree_centrality.items(), key=lambda item: item[1], reverse=True))[:8]
print(top_8)

# number of neighbors for the nodes with the highest degree centralities
top_8_neighbors = (sorted(G.degree, key=lambda item: item[1], reverse=True))[:8]
print(top_8_neighbors)


# plt.figure(figsize=(15, 8))
# plt.hist(degree_centrality.values(), bins=25)
# plt.xticks(ticks=[0, 0.025, 0.05, 0.1, 0.15, 0.2])  # set the x axis ticks
# plt.title("Degree Centrality Histogram ", fontdict={"size": 35}, loc="center")
# plt.xlabel("Degree Centrality", fontdict={"size": 20})
# plt.ylabel("Counts", fontdict={"size": 20})
# plt.show()


### FIG2

# Now let’s check the users with highest degree centralities from the size of their nodes:
# Nodes with a higher degree centrality (i.e. with more direct connections) will have a higher value and thus be displayed larger in the graph.
node_size = [
    v * 1000 for v in degree_centrality.values()
]  # set up nodes size for a nice graph representation

pos = nx.spring_layout(G, iterations=15, seed=1721)
plt.figure(figsize=(15, 8))
nx.draw_networkx(G, pos=pos, node_size=node_size, with_labels=False, width=0.15)
plt.axis("off")
plt.show()