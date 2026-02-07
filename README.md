# Détection de communautés dans un graphe social

## Description
Ce projet vise à détecter des communautés dans un graphe social à l’aide des concepts de la théorie des graphes et d’algorithmes de détection de communautés.

## Structure du projet
- `code/` : scripts Python
- `data/` : datasets et graphe sauvegardé
- `figures/` : visualisations
- `rapport/` : rapport final

## Graphe social
Le graphe est généré à partir d’un dataset CSV représentant des relations sociales entre utilisateurs.
Il s’agit d’un graphe simple et non orienté.

## Outils
- Python 3.8+
- NetworkX
- Matplotlib
- Pandas
- python-louvain

## Installation

1. Clonez le dépôt.
2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

Le projet se compose de deux scripts principaux à exécuter dans l'ordre :

1. **Construction du graphe :**
   ```bash
   python code/graph_construction.py
   ```
   Ce script lit le fichier CSV, crée le graphe, calcule ses propriétés et le sauvegarde dans `data/social_graph.pkl`.

2. **Détection de communautés :**
   ```bash
   python code/louvain.py
   ```
   Ce script charge le graphe sauvegardé, applique l'algorithme de Louvain et génère une visualisation dans `figures/louvain_communities.png`.

## Auteurs
Projet réalisé par un groupe de 4 étudiants.




