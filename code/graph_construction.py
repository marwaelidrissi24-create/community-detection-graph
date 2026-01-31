# Import des librairies
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import os

# 1️⃣ Charger le dataset CSV
df = pd.read_csv("data/social_network.csv")

# 2️⃣ Créer un graphe simple non orienté
G = nx.Graph()

# 3️⃣ Ajouter les arêtes depuis le dataset
for _, row in df.iterrows():
    G.add_edge(row["User1"], row["User2"])

# 4️⃣ Calculer les propriétés du graphe
nombre_noeuds = G.number_of_nodes()
nombre_aretes = G.number_of_edges()
densite = nx.density(G)
degre_moyen = sum(dict(G.degree()).values()) / nombre_noeuds

print("Nombre de nœuds :", nombre_noeuds)
print("Nombre d'arêtes :", nombre_aretes)
print("Densité :", densite)
print("Degré moyen :", degre_moyen)
print("Graphe orienté ?", G.is_directed())

# 5️⃣ Sauvegarder le graphe pour P3 (pickle)
import pickle
os.makedirs("data", exist_ok=True)

with open("data/social_graph.pkl", "wb") as f:
    pickle.dump(G, f)

# 6️⃣ Visualisation du graphe
plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray", node_size=900)
plt.title("Graphe social")
plt.savefig("figures/social_graph.png")
plt.show()
