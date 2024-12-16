import streamlit as st
import pandas as pd
from sklearn.neighbors import NearestNeighbors


#titre de la page
#"Page 3 - Recommandation"

## afficher le text suivant
#"Découvrez les Pokémon non légendaires les plus similaires à votre sélection légendaire ! ✨"


# Charger les données
df = pd.read_csv("data/pokemon_clean.csv")

# Choisir un Pokémon légendaire en utilisant la selectbox
#choice = ...

# Séparer les données légendaires et non légendaires
#df_leg =  ...
#df_non_leg = ...

# Colonnes utilisées pour l'entrainement du modèle
# conserver tous sauf : ['types', 'Name', 'Generation', 'Legendary']

#X_non_leg = ...
#X_leg = ...

# Entraîner le modèle Nearest Neighbors sur 3 voisin
#model = ...


# Trouver les voisins les plus proches de la selection de pokemon


# Récupérer les recommandations
#df_reco = ...


#afficher en sous titre
#"Voici les 3 Pokémon recommandés pour .... "



# Afficher les recommandations sous forme de colonnes avec les info de la recommandation
# "Name",'types', 'HP', "Attack", "Defense", "Speed", 'Sp. Atk', 'Sp. Def'


