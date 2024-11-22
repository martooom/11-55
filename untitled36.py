import streamlit as st
import base64

# Función para convertir una imagen a base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Ruta de la imagen (asegúrate de que "valorant.jpg" esté en /content/)
image_fondo = "valorant.jpg"

# Convertir la imagen a base64
image_base64 = image_to_base64(image_fondo)

# Código CSS para establecer la imagen como fondo usando base64
st.markdown(
    f"""
    <style>
    body {{
        background-image: url('data:image_fondo;base64,{image_base64}');
        background-size: cover;
        background-position: center;
        height: 100vh;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Continuar con el resto de tu aplicación Streamlit
st.title("Mi aplicación con fondo")
st.write("¡Hola! Esto es un ejemplo de cómo establecer una imagen JPG como fondo.")
