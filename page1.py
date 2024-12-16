import streamlit as st
import pandas as pd


#read csv data explore it in notebook
df = pd.read_csv("data/pokemon_clean.csv")


#isoler les pokemon legendaire
df_leg = df[df.Name.isin(["Mewtwo","Lugia" , "Rayquaza","Dialga","Palkia"])]



#afficher le message suivant en titre :
#"🔍 Description des Pokémon Légendaires"
st.title("🔍 Description des Pokémon Légendaires")

# afficher le messages suivant en sous titre
##  "Découvrez les caractéristiques de vos légendaires préférés ! 🐉✨"
st.subheader("Découvrez les caractéristiques de vos légendaires préférés ! 🐉✨")


# Pokémon légendaires avec leurs descriptions
legendary_pokemon = {
    "Mewtwo": "Mewtwo est un Pokémon cloné à partir de l'ADN de Mew. Il est connu pour sa puissance psychique incroyable et sa quête d'identité.",
    "Lugia": "Lugia est le gardien des océans et le chef des oiseaux légendaires. Il est aussi connu comme le Pokémon Plongée.",
    "Rayquaza": "Rayquaza est le Pokémon du ciel, capable de calmer les conflits entre Kyogre et Groudon grâce à sa puissance.",
    "Dialga": "Dialga est le Pokémon maître du temps, contrôlant son flux avec précision. Il est souvent lié à la création de l'univers Pokémon.",
    "Palkia": "Palkia est le Pokémon maître de l'espace, capable de plier les dimensions et de manipuler l'espace-temps."
}
# Pokémon légendaires avec leurs images
images = {
    "Mewtwo": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/150.png",
    "Lugia": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/249.png",
    "Rayquaza": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/384.png",
    "Dialga": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/483.png",
    "Palkia": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/484.png"
}
# Sélecteur pour choisir un Pokémon légendaire
legends = df_leg.Name
choices = st.selectbox("choisir votre pokemon légendaire",legends )




# Affichage de la description du Pokémon sélectionné
# Afficher le nom du pokemon séléctionné
st.markdown(f"###  Description de {choices} : ")
st.write(f"{legendary_pokemon[choices]}")


# Afficher l'image du pokemon
st.image(images[choices])

# récupérer les informations du pokemon selectionné
# utiliser le dataframe df_leg pour recupérer toute les infos du pokemon selectionné , faire un reset index de suite
df_selection = df_leg[df_leg.Name == choices].reset_index(drop=True)

# afficher les types du pokemon legendaire selectionné
#utiliser la methode markdown
st.markdown(f"### Type : {df_selection.loc[0, 'types']}")


#afficher les stat du pokemon legendaire selectionné
#les stats en question : 'HP', 'Attack', 'Sp. Atk', 'Defense', "Sp. Def", 'Speed'
#utiliser st.columns pour afficher les stats sur une seule ligne
#utiliser st.metric pour afficher chaque stat
names = ['HP', 'Attack', 'Sp. Atk', 'Defense', "Sp. Def", 'Speed']
cols = st.columns(len(names))

for col , name in zip(cols, names) :
    with col :
        st.metric(name, round(df_selection.loc[0,name ],2))
#st.write(cols)
#st.write(type(cols))
#with col1 :
   
#    st.metric("HP", round(df_selection.loc[0, 'HP'],2))

#col1.st.metric()

#à explorer : progress bar : https://github.com/sqlinsights/st-circular-progress