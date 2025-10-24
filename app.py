# app.py
# -*- coding: utf-8 -*-
import streamlit as st
from backend import haircut_advice

st.set_page_config(
    page_title="Jean-Michel Ciseaux ✂️",
    page_icon="💇‍♂️",
    layout="centered"
)

st.title("💇‍♂️ Jean-Michel Ciseaux – Assistant Coupe de Cheveux Piquant")
st.markdown(
    """
    Salut beauté ! 😎  
    Envoie-moi ta photo et je te sors **une coupe digne d’un génie capillaire en pleine crise artistique**.  
    *(Promis, je serai drôle... et peut-être un peu piquant 👀)*  
    """
)

uploaded_file = st.file_uploader(
    "Téléverse une photo de toi (format JPG ou PNG) :", 
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="Voici ta tête actuelle 😏", use_container_width=True)
    
    if st.button("✨ Obtenir la recommandation magique ✨"):
        with st.spinner("Jean-Michel observe ta chevelure sous toutes les coutures... 💭"):
            try:
                result = haircut_advice(uploaded_file.read())
                st.markdown("## 💬 Résultat de Jean-Michel Ciseaux :")
                st.write(result)
            except Exception as e:
                st.error(f"Une mèche s’est coincée dans le serveur : {e}")

st.markdown("---")
st.caption("Créé avec ❤️, Streamlit et Pixtral 12B. Ne pas prendre les conseils trop au sérieux 😜")
