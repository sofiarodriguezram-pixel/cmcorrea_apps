import streamlit as st
from PIL import Image
st.title("Aplicaciones de Inteligencia Artificial.")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Conversión de texto a voz")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace usaremos una de las aplicaciones de Inteligencia Artificial") 
 url = "https://imultimod.streamlit.app/"
 st.write(f"Texto a voz: [Enlace]({url})")

with col2: 
 st.subheader("Conversión de voz a texto")
 image = Image.open('audio_to_txt.png')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
 url = "https://traductor-ab0sp9f6fi.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

with col3: 
 st.subheader("RAG")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que usa el análisis dentro de un contexto a partir de un documento (PDF).") 
 url = "https://chatpdf-cc.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

