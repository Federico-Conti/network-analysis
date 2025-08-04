import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 100  # Number of nodes
p_values = [0.01, 0.05, 0.1, 0.3]  # Different probabilities for edge formation

# Create subplots for graph visualizations
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

for i, p in enumerate(p_values):
    # Generate Erdős–Rényi random graph
    G = nx.erdos_renyi_graph(N, p, seed=42)
    
    # Draw the graph
    plt.sca(axes[i])  # Set current axis
    pos = nx.spring_layout(G, seed=42)  # Layout for better visualization
    options = {
        "node_color": "blue",
        "node_size": 20,
        "edge_color": "grey",
        "linewidths": 0,
        "width": 0.5,
    }
    
    nx.draw(G, pos, **options)
    
    axes[i].set_title(f"G(N={N}, p={p})")
    axes[i].margins(0.20)
    axes[i].axis("off")
  
plt.tight_layout()
plt.show()

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

for i, p in enumerate(p_values):
    # Generate Erdős–Rényi random graph
    G = nx.erdos_renyi_graph(N, p, seed=42)
    
    
    theory_avg_degree = p * (N - 1)  # Theoretical average degree for Erdős–Rényi graph
    print(f"THE Average degree for p={p}: {theory_avg_degree:.2f}")
 
    emp_avg_degree = np.mean(degrees)
    print(f"EMP Average degree for p={p}: {emp_avg_degree:.2f}")
    
    # Compute degree distribution
    degrees = [d for _, d in G.degree()]
    degree_counts = np.bincount(degrees)
    degree_prob = degree_counts / sum(degree_counts)  # Normalize to get probability

    # Plot degree distribution
    axes[i].bar(range(len(degree_prob)), degree_prob, color="purple", alpha=0.7)
    axes[i].set_title(f"G(N={N}, p={p})")
    axes[i].set_xlabel("Degree k")
    axes[i].set_ylabel("P(k)")
    axes[i].set_xlim(0, max(degrees) + 2)

plt.tight_layout()
plt.show()