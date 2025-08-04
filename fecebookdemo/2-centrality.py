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

