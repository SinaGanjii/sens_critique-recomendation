# Projet de Recommandation NLP avec Embeddings

## Description du Projet

Ce projet implémente un système de recommandation de critiques de films basé sur la similarité sémantique. L'objectif principal est de trouver des commentaires similaires en utilisant des techniques de traitement du langage naturel (NLP) et des modèles de transformation de phrases.

## Objectif

Le projet vise à :
- Analyser un dataset de critiques de films (Fight Club)
- Nettoyer et préparer les données textuelles
- Créer des embeddings vectoriels des critiques
- Calculer la similarité entre les critiques pour des recommandations
- Fournir une interface interactive pour tester le système

## Structure du Projet

```
sens_critique(recomendatio_NLP_embeding)/
├── fightclub_critiques.csv          # Dataset principal
├── interstellar_critique.csv        # Dataset secondaire
├── lab_1.ipynb                      # Notebook d'exploration et développement
├── product_typ/                     # Code de production
│   ├── main.py                      # Interface utilisateur interactive
│   ├── preper_f.py                  # Classe de préparation des données
│   └── __pycache__/                 # Cache Python
└── README.md                        # Documentation
```

## Dataset

Le dataset principal `fightclub_critiques.csv` contient :
- **1000 critiques** de films
- **Colonnes** :
  - `id` : Identifiant unique
  - `rating` : Note attribuée (1-10)
  - `review_hits` : Nombre de vues de la critique
  - `review_content` : Contenu textuel de la critique
  - `review_title` : Titre de la critique (supprimé lors du preprocessing)
  - `gen_review_like_count` : Nombre de likes
  - `user_id` : Identifiant de l'utilisateur

## Approche Technique

### 1. Préprocessing des Données
- Suppression des colonnes non nécessaires (dates, noms d'utilisateurs, URLs, titres)
- Nettoyage des balises HTML dans le contenu des critiques
- Gestion des valeurs nulles
- **Filtrage des critiques courtes** : Suppression des critiques < 20 caractères
- Vérification des doublons

### 2. Modèle d'Embedding
- **Modèle utilisé** : `paraphrase-multilingual-MiniLM-L12-v2`
- **Bibliothèque** : Sentence Transformers
- **Avantages** :
  - Support multilingue
  - Optimisé pour la similarité sémantique
  - Léger et efficace
  - Dimension des embeddings : 384

### 3. Stratégie de Recommandation
- **Content-based filtering** : Basé sur le contenu des critiques
- **Similarité cosinus** : Calcul de la similarité entre embeddings
- **Seuil de qualité** : Filtrage des résultats avec similarité > 0.6
- **Top-K recommandations** : Retour des 5 critiques les plus similaires

### 4. Améliorations Implémentées
- **Détection intelligente du HTML** : Utilisation de BeautifulSoup uniquement si nécessaire
- **Filtrage des critiques courtes** : Élimination des critiques non pertinentes
- **Seuil de similarité** : Amélioration de la qualité des recommandations
- **Interface interactive** : Boucle while pour tester plusieurs critiques

## Dépendances

```python
pandas
sentence-transformers
beautifulsoup4
numpy
scikit-learn
torch
```

## Installation

```bash
pip install pandas sentence-transformers beautifulsoup4 scikit-learn
```

## Utilisation

### 1. Exploration et Développement
```bash
# Ouvrir le notebook Jupyter
jupyter notebook lab_1.ipynb
```

### 2. Interface Interactive
```bash
# Exécuter le système de recommandation
cd product_typ
python main.py
```

### 3. Utilisation du Code
```python
from preper_f import PreperData
import pandas as pd

# Charger les données
data = pd.read_csv('fightclub_critiques.csv', encoding="utf-8")

# Initialiser le système
preper = PreperData(data)
preper.preper_data()

# Nettoyer le contenu
preper.data["review_content"] = preper.data["review_content"].apply(preper.clean_special_character)

# Créer les embeddings
preper.transform_data()

# Trouver des critiques similaires
similar_reviews = preper.find_top_5_similar_reviews("J'adore ce film!")
print(similar_reviews)
```

## Fonctionnalités

### Classe PreperData
- `preper_data()` : Préparation et filtrage des données
- `clean_special_character()` : Nettoyage intelligent du texte
- `transform_data()` : Création des embeddings
- `find_top_5_similar_reviews()` : Recherche de critiques similaires

### Interface Interactive
- Boucle while pour tester plusieurs critiques
- Commande 'exit' pour quitter
- Affichage des scores de similarité
- Gestion d'erreurs robuste

## Résultats

- **Embeddings vectoriels** : 384 dimensions pour chaque critique
- **Similarité cosinus** : Calcul entre toutes les paires de critiques
- **Recommandations** : Top 5 critiques les plus similaires
- **Qualité améliorée** : Filtrage des critiques courtes et seuil de similarité

## Exemple de Sortie

```
Système de recommandation prêt!

Entrez votre critique pour le film de fightclub (ou 'exit' pour quitter): J'adore ce film!

Recherche de critiques similaires à: 'J'adore ce film!'

Top 5 critiques similaires:
Score: 0.723
Critique: Ce film est absolument génial, je le recommande vivement...
Score: 0.689
Critique: Une œuvre magistrale qui m'a profondément marqué...
```

## Développement

Le projet a été développé en deux phases :
1. **Exploration** : Notebook Jupyter pour l'analyse et le développement
2. **Production** : Code modulaire avec interface utilisateur

## Notes Techniques

- **Performance** : Le modèle est chargé une seule fois au démarrage
- **Mémoire** : Les embeddings sont stockés en mémoire pour des calculs rapides
- **Robustesse** : Gestion des erreurs et validation des entrées utilisateur





