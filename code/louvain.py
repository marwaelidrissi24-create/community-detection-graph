# Louvain community detection
import pickle
import networkx as nx
import community.community_louvain as community_louvain
import matplotlib.pyplot as plt
import os

# 1️⃣ Load the graph created by P2
with open("data/social_graph.pkl", "rb") as f:
    G = pickle.load(f)

print("Graph loaded")
print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

# 2️⃣ Apply Louvain algorithm
partition = community_louvain.best_partition(G)

# partition = {node: community_id}
num_communities = len(set(partition.values()))
print("Number of detected communities:", num_communities)

# 3️⃣ Compute modularity
modularity = community_louvain.modularity(partition, G)
print("Modularity:", modularity)

# 4️⃣ Display communities (text)
print("\nCommunities:")
communities = {}
for node, comm in partition.items():
    communities.setdefault(comm, []).append(node)

for comm, nodes in communities.items():
    print(f"Community {comm}: {nodes}")

# 5️⃣ Visualization
pos = nx.spring_layout(G, seed=42)
colors = [partition[node] for node in G.nodes()]

plt.figure(figsize=(10, 8))
nx.draw(
    G,
    pos,
    node_color=colors,
    with_labels=True,
    node_size=900,
    cmap=plt.cm.Set3,
    edge_color="gray"
)
plt.title("Community detection using Louvain algorithm")
plt.savefig("figures/louvain_communities.png")
plt.show()