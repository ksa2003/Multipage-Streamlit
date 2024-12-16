import streamlit as st
# rappel comment executer une app streamlit 


# Configurer votre application streamlit
st.set_page_config(
  
    layout="wide"
 
)

# titre de l'application
# "⚡ Système de Recommandation Pokémon ⚡"
st.title("⚡ Système de Recommandation Pokémon ⚡")



# Découper la page en 3 colonnes : celle du mileu prendra 6 * plus d'espace
col1, col2, col3 = st.columns([1,6,1])

# Centrer le text sur la colonne 2

# en sous titre afficher  :"Attrapez-les tous... mais stratégiquement ! 🕵️‍♂️"
# ensuitre afficher le détail de text

with col2 :
    st.markdown(
    """
        Bienvenue, Dresseur Pokémon ! 🧢  
        Dans ce monde, même les Pokémon légendaires ont des jours de repos...  
        Mais pas de panique, nous sommes là pour vous aider à trouver **les remplaçants parfaits** ! 🎯

        ### 🛠️ Fonctionnalités :
        - **Choisissez un Pokémon légendaire** parmi vos favoris (Mewtwo, Lugia... 🎆).  
        - **Obtenez 3 recommandations** de Pokémon non légendaires tout aussi redoutables ! 💥  
        - **Optimisez votre équipe** pour écraser vos adversaires, même sans vos stars. 🏆

        Alors, prêt(e) à découvrir vos alliés secrets ?  
        **Cliquez dans le menu à gauche et commencez l'aventure ! 🚀**
        """
    
    )