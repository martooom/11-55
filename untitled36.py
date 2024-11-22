import streamlit as st

# Ruta de la imagen (asegúrate de que "valorant.jpg" esté en /content/)
image_fondo = "valorant.jpg"

# Código CSS para establecer la imagen como fondo usando base64
st.markdown(
    f"""
    <style>
    body {{
        background-image: url('data:image_fondo,{image_base64}');
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
