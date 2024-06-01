import streamlit as st

st.title("Aplicaciones de Inteligencia Artificial")

st.subheader("Conversión de texto a voz")
texto_del_enlace = "Texto a voz"
url = "https://imultimod.streamlit.app/"
st.write(f"check out this [link]({url})")
st.markdown(f"{texto_del_enlace}")
