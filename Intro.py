import streamlit as st
from PIL import Image

st.title("Aplicaciones de Inteligencia Artificial")
st.subheader("Conversión de texto a voz")
image = Image.open('txt_to_audio.png')
st.image(image, width=250)
st.write("En la siguiente enlace usaremos una de las aplicaciones de Inteligencia Artificial") 
texto_del_enlace = "Texto a voz"
url = "https://imultimod.streamlit.app/"
st.write(f"Texto a voz: [Enlace]({url})")
st.markdown(f"{texto_del_enlace}")
