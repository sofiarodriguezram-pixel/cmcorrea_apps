import streamlit as st

# Configuración general
st.set_page_config(page_title="Aplicaciones de Inteligencia Artificial", layout="wide")

# Fondo morado claro con CSS
st.markdown(
    """
    <style>
    body {
        background-color: #e6ccff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título principal
st.title("Aplicaciones de Inteligencia Artificial")

# Barra lateral
with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial")
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.write(parrafo)

# Enlace general
url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"👉 [Enlace para páginas y ejercicios]({url_ia})")

# Columnas
col1, col2, col3 = st.columns(3)

# ---- Columna 1 ----
with col1:
    st.subheader("Conversión de Texto a Audio")
    st.write("En la siguiente enlace usaremos una aplicación de conversión de texto a audio.") 
    st.write("[Texto a voz](https://9jxqgjkrh3xxuydqumj9nq.streamlit.app/)")

    st.subheader("Traductor de Voz")
    st.write("En la siguiente enlace veremos cómo se traduce en diferentes idiomas.") 
    st.write("[Traductor de voz](https://traductor-vpyprhasbpcbvzsb4huls7.streamlit.app/)")

    st.subheader("Entrenando Modelos")
    st.write("En la siguiente enlace veremos cómo puedes usar tu modelo entrenado.") 
    st.write("[Entrenamiento de modelos](https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/)")

# ---- Columna 2 ----
with col2:
    st.subheader("Conversión de Voz a Texto")
    st.write("En la siguiente enlace veremos una aplicación que usa la conversión de voz a texto.") 
    st.write("[Voz a texto](https://traductor-ab0sp9f6fi.streamlit.app/)")

    st.subheader("Reconocimiento Óptico de Caracteres (OCR)")
    st.write("En el siguiente enlace veremos cómo se pueden reconocer caracteres ópticos.") 
    st.write("[OCR - Reconocimiento de texto](https://ocrtrabajo.streamlit.app/)")

    st.subheader("Análisis Inteligente de PDF con RAG")
    st.write("En el siguiente enlace veremos cómo se analiza un PDF con IA.") 
    st.write("[Análisis de PDF con RAG](https://chatpdfsof.streamlit.app/)")

# ---- Columna 3 ----
with col3:
    st.subheader("Reconocimiento de Dígitos Escritos a Mano")
    st.write("En la siguiente enlace veremos una aplicación que reconoce dígitos escritos a mano.") 
    st.write("[Reconocimiento de dígitos](https://wffsu6ifdgp2mgwmfym4vx.streamlit.app/)")

    st.subheader("Tablero Inteligente")
    st.write("En la siguiente enlace veremos un tablero inteligente.") 
    st.write("[Tablero Inteligente](https://drawrecog-ycoqpoyxksaeat62zyfgbr.streamlit.app/)")

    st.subheader("Mi Primera App")
    st.write("En la siguiente enlace veremos una aplicación básica creada con Streamlit.") 
    st.write("[Mi primera App](https://bbfpukst4yubuwgxyopbub.streamlit.app/)")

# ---- Secciones adicionales ----
st.subheader("Demo de TF-IDF con Preguntas y Respuestas")
st.write("En la siguiente enlace veremos una demo de TF-IDF con preguntas y respuestas.")
st.write("[Demo TF-IDF](https://8jvaepvgwvk6qdgwpgagd5.streamlit.app/)")

st.subheader("Detección de Objetos en Imágenes")
st.write("En la siguiente enlace veremos detección de objetos en imágenes.")
st.write("[Detección de objetos](https://hadxm3j5sok3cfzuqz6kx5.streamlit.app/)")

st.subheader("Interfaces Multimodales")
st.write("En la siguiente enlace veremos cómo funcionan las interfaces multimodales.")
st.write("[Interfaces multimodales](https://voicectrl-deb4asn8kjzwstxygan6ct.streamlit.app/)")

st.subheader("Análisis de Imagen con IA")
st.write("En la siguiente enlace veremos cómo se realiza el análisis de imágenes con inteligencia artificial.")
st.write("[Análisis de imagen](https://visionapp-tejimzlfu27punjn8a4qdl.streamlit.app/)")
