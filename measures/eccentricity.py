import networkx as nx
import matplotlib.pyplot as plt
import numpy as np




"""
The eccentricity of a node v is the maximum distance from v to all other nodes in G.
The diameter is the maximum eccentricity.

Problemi con grafi diretti:
Grafo non fortemente connesso: Se il grafo non è fortemente connesso, non tutti i nodi sono raggiungibili tra loro. Ciò significa che per alcuni nodi l'eccentricità sarebbe infinita o non definita.
Distanze non simmetriche: Nei grafi diretti, la distanza da 𝑢  a 𝑣  può essere diversa da quella da 𝑣  a 𝑢 . Questo complica il calcolo dell'eccentricità, perché dipende fortemente dalla direzione degli archi.
"""

G = nx.Graph([(1, 2), (1, 3), (1, 4), (3, 4), (3, 5), (4, 5)])
# G = nx.DiGraph([(1, 2), (1, 3), (1, 4), (3, 4), (3, 5), (4, 5)]) 
ecc =  dict(nx.eccentricity(G))
print(f"Eccentricity: {ecc}")

diameter = nx.diameter(G)   
print(f"Diameter: {diameter}")

print("Adjacency List:")
for node, neighbors in G.adjacency():
    print(f"{node}: {list(neighbors)}")


# Draw graph
pos = nx.spring_layout(G, seed=89)

options = {
    "font_size": 26,
    "node_size": 1000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}
nx.draw_networkx(G, pos, **options)

# Set margins for the axes so that nodes aren't clipped
ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()