# Import des librairies
import networkx as nx
import matplotlib.pyplot as plt

# 1️⃣ Définir les utilisateurs (nodes)
users = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivan", "Judy"]

# 2️⃣ Définir des relations (edges)
edges = [
    ("Alice", "Bob"),
    ("Alice", "Charlie"),
    ("Bob", "David"),
    ("Charlie", "Eve"),
    ("David", "Eve"),
    ("Frank", "Grace"),
    ("Grace", "Hannah"),
    ("Hannah", "Ivan"),
    ("Ivan", "Judy"),
    ("Judy", "Frank"),
    ("Alice", "Frank"),
    ("Charlie", "Grace")
]

# 3️⃣ Créer le graphe
G = nx.Graph()
G.add_nodes_from(users)
G.add_edges_from(edges)

# 4️⃣ Calculer les propriétés
print("Nombre de nœuds:", G.number_of_nodes())
print("Nombre d'arêtes:", G.number_of_edges())
print("Densité:", nx.density(G))
print("Graphe orienté?", G.is_directed())

# 5️⃣ Dessiner le graphe
plt.figure(figsize=(8,6))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000)
plt.savefig("figures/social_graph.png")
plt.show()
