# code/louvain.py

import networkx as nx
import matplotlib.pyplot as plt
import pickle
import community as community_louvain  # pip install python-louvain

# 1️⃣ Charger le graphe créé par P2
with open("../data/social_graph.pkl", "rb") as f:
    G = pickle.load(f)

# 2️⃣ Appliquer l'algorithme Louvain
partition = community_louvain.best_partition(G)

# 3️⃣ Afficher les communautés détectées
print("Communautés détectées :")
for node, comm in partition.items():
    print(f"{node} -> Communauté {comm}")

# 4️⃣ Calculer la modularité
modularity = community_louvain.modularity(partition, G)
print(f"\nModularité du graphe : {modularity:.3f}")

# 5️⃣ Visualiser le graphe avec les communautés
plt.figure(figsize=(8,6))

# Couleurs par communauté
colors = [partition[node] for node in G.nodes()]
nx.draw(G, with_labels=True, node_color=colors, cmap=plt.cm.tab20, edge_color='gray', node_size=1000)

plt.title("Communautés détectées avec Louvain")
plt.savefig("../figures/louvain_communities.png")
plt.show()
