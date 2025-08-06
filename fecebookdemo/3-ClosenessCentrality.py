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

closeness_centrality = nx.centrality.closeness_centrality(
    G
)  # save results in a variable to use again
top_8 = (sorted(closeness_centrality.items(), key=lambda item: item[1], reverse=True))[:8]
print("Top Closeness centrality:", top_8)

average_distance_107 = 1 / closeness_centrality[107]
print(f"Average distance in hop from node 107 to all other nodes: {average_distance_107}") 



# plt.figure(figsize=(15, 8))
# plt.hist(closeness_centrality.values(), bins=60)
# plt.title("Closeness Centrality Histogram ", fontdict={"size": 35}, loc="center")
# plt.xlabel("Closeness Centrality", fontdict={"size": 20})
# plt.ylabel("Counts", fontdict={"size": 20})
# plt.show()


### FIG3

node_size = [
    v * 50 for v in closeness_centrality.values()
]  # set up nodes size for a nice graph representation

pos = nx.spring_layout(G, iterations=15, seed=1721)
plt.figure(figsize=(15, 8))
nx.draw_networkx(G, pos=pos, node_size=node_size, with_labels=False, width=0.15)
plt.axis("off")