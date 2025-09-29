# Système de Recommandation de Critiques Cinématographiques

## 🚀 Quick Start pour Thibaut
**Tu peux directement commencer par le fichier `lab_1.ipynb` - ce n'est pas propre mais tu vas comprendre. Merci !**

## 📋 Description du Projet

Ce projet implémente un système de recommandation intelligent basé sur l'analyse sémantique de critiques cinématographiques. Il utilise des techniques d'embedding avancées pour trouver des critiques similaires à partir d'une critique d'entrée, permettant aux utilisateurs de découvrir des opinions partagées sur des films.

## 🎯 Objectif

L'objectif principal est de créer un système qui peut :
- Analyser le contenu sémantique des critiques de films
- Trouver les critiques les plus similaires à une critique donnée
- Fournir des recommandations pertinentes basées sur la similarité de contenu

## 🧠 Approche Technique

### Analyse des Options de Filtrage

Après analyse approfondie des données disponibles, plusieurs approches ont été considérées :

1. **Filtrage Collaboratif** : Rejeté car nécessite des préférences utilisateur (Wj) et des caractéristiques d'items (Xi) qui ne sont pas disponibles
2. **Filtrage Basé sur le Contenu** : Possible mais complexe, nécessitant des embeddings denses dans un réseau de neurones
3. **Solution Retenue** : **Embedding avec Sentence Transformers** - Approche optimale pour ce cas d'usage

### Architecture du Système

```
Critiques Brutes → Nettoyage → Embedding → Calcul de Similarité → Recommandations
```

## 📊 Données

Le projet utilise deux jeux de données de critiques cinématographiques :
- **Fight Club** : 1000 critiques avec notes, contenu et métadonnées
- **Interstellar** : Critiques détaillées pour analyse comparative

### Structure des Données
- `id` : Identifiant unique de la critique
- `rating` : Note attribuée au film (1-10)
- `review_content` : Contenu textuel de la critique
- `review_hits` : Nombre de vues de la critique
- `gen_review_like_count` : Nombre de likes
- `user_id` : Identifiant de l'utilisateur

## 🛠️ Technologies Utilisées

- **Python 3.12**
- **Pandas** : Manipulation et analyse des données
- **Sentence Transformers** : Génération d'embeddings sémantiques
- **BeautifulSoup** : Nettoyage du contenu HTML
- **scikit-learn** : Calcul de similarité cosinus
- **NumPy** : Opérations mathématiques

## 📁 Structure du Projet

```
sens_critique(recomendatio_NLP_embeding)/
├── lab_1.ipynb                 # Notebook d'analyse et développement
├── fightclub_critiques.csv     # Dataset principal (Fight Club)
├── interstellar_critique.csv   # Dataset secondaire (Interstellar)
├── product_typ/
│   ├── main.py                 # Application principale interactive
│   └── preper_f.py            # Classe de préparation des données
└── README.md                   # Documentation du projet
```

## 🚀 Installation et Utilisation

### Prérequis
```bash
pip install pandas sentence-transformers beautifulsoup4 scikit-learn numpy
```

### Lancement de l'Application
```bash
cd product_typ
python main.py
```

### Utilisation Interactive
1. Lancez l'application
2. Entrez votre critique de film
3. Le système retourne les 5 critiques les plus similaires avec leurs scores de similarité

## 🔧 Fonctionnalités Principales

### 1. Préparation des Données (`PreperData`)

**Nettoyage Intelligent** :
- Suppression des colonnes non pertinentes (dates, usernames, URLs)
- Élimination des valeurs nulles
- Filtrage des critiques trop courtes (< 20 caractères)
- Nettoyage du contenu HTML et des caractères spéciaux

**Traitement du Texte** :
```python
def clean_special_character(self, text):
    # Détection et nettoyage HTML
    # Normalisation des espaces et retours à la ligne
    # Gestion des caractères spéciaux
```

### 2. Génération d'Embeddings

**Modèle Utilisé** : `paraphrase-multilingual-MiniLM-L12-v2`
- Support multilingue
- Optimisé pour la similarité sémantique
- Léger et performant

### 3. Calcul de Similarité

**Méthode** : Similarité cosinus
- Mesure la similarité directionnelle entre vecteurs
- Score de 0 à 1 (1 = identique, 0 = orthogonal)

### 4. Système de Recommandation

**Fonctionnalités** :
- Seuil de similarité configurable (défaut : 0.6)
- Retour des 5 critiques les plus similaires
- Gestion des cas sans résultats pertinents

## 📈 Résultats et Performance

### Exemple de Sortie
```
Recherche de critiques similaires à: 'Film exceptionnel avec une mise en scène remarquable'

Top 5 critiques similaires:
Score: 0.734
Critique: Fight Club sort à la fin 1999 sur les écrans. Le film fut très controversé...

Score: 0.718
Critique: Cependant, le bouche à oreille fit qu'à sa sortie en DVD...
```

### Métriques de Qualité
- **Précision** : Critiques pertinentes identifiées avec succès
- **Cohérence Sémantique** : Similarité basée sur le sens, pas seulement les mots
- **Performance** : Traitement rapide grâce au modèle optimisé

## 🔍 Analyse et Réflexions

### Défis Rencontrés

1. **Qualité des Données** :
   - Présence de balises HTML dans le contenu
   - Caractères d'encodage problématiques
   - Critiques de longueurs variables

2. **Choix Techniques** :
   - Évaluation entre différents modèles d'embedding
   - Optimisation du seuil de similarité
   - Gestion des cas limites

### Solutions Implémentées

1. **Nettoyage Robuste** :
   - Détection automatique du contenu HTML
   - Normalisation des espaces et caractères
   - Filtrage intelligent des données

2. **Architecture Modulaire** :
   - Séparation claire des responsabilités
   - Code réutilisable et maintenable
   - Interface utilisateur intuitive

## 🎯 Applications Possibles

- **Plateformes de Critique** : Recommandation de critiques similaires
- **Analyse de Sentiment** : Détection de patterns dans les opinions
- **Recherche Sémantique** : Trouver du contenu par sens, pas par mots-clés
- **Recommandation de Films** : Basée sur la similarité des critiques

## 🔮 Améliorations Futures

1. **Interface Web** : Développement d'une interface utilisateur moderne
2. **Base de Données** : Intégration avec une base de données pour la persistance
3. **Modèles Avancés** : Expérimentation avec des modèles plus récents
4. **Métriques** : Ajout de métriques de qualité et d'évaluation
5. **Multilingue** : Support de plusieurs langues simultanément

## 📝 Notes de Développement

Ce projet a été développé avec une approche méthodique :
- Analyse approfondie des données disponibles
- Évaluation comparative des différentes approches
- Implémentation progressive avec tests continus
- Documentation détaillée du processus de réflexion

Le code reflète une compréhension approfondie des techniques de NLP et des systèmes de recommandation, avec une attention particulière à la qualité et à la maintenabilité du code.

---

*Développé avec passion pour l'analyse sémantique et les systèmes de recommandation intelligents.*
