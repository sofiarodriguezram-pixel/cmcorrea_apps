import streamlit as st
from PIL import Image
st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Aplicaciones con Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Conversión de Texto a Audio")
 image = Image.open('txt_to_audio2.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace usaremos una aplicacion Conversión de Texto a Audio") 
 url = "https://9jxqgjkrh3xxuydqumj9nq.streamlit.app/"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader("TRADUCTOR DE VOZ")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como se traduce en diceferente idiomas .") 
 url = "https://traductor-vpyprhasbpcbvzsb4huls7.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Entrenando Modelos")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

with col2: 
 st.subheader("Conversión de voz a texto")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
 url = "https://traductor-ab0sp9f6fi.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("Reconocimiento Óptico de Caracteres")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos como se pueden reconocer caracteres opticos.") 
 url = "https://ocrtrabajo.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Análisis Inteligente de PDF con RAG")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos se analiza un PDF.") 
 url = "https://chatpdfsof.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Reconocimiento de Dígitos escritos a mano")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que reconoce de Dígitos escritos a mano.") 
 url = "https://wffsu6ifdgp2mgwmfym4vx.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Tablero Inteligente")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos un Tablero Inteligente.") 
 url = "https://drawrecog-ycoqpoyxksaeat62zyfgbr.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Mi primera App")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos Mi primera App.") 
 url = "https://bbfpukst4yubuwgxyopbub.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")




