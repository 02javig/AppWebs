import re
import time
import streamlit as st
# import requests  # pip install requests si es necesario

def is_valid_email(email):
    # Patrón de expresiones regulares básico para la validación de correo electrónico
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Nombres y Apellidos")
        email = st.text_input("Correo electrónico")
        message = st.text_area("Su Mensaje")
        submit_button = st.form_submit_button("Enviar")

    if submit_button:
        # Validaciones de los campos
        if not name:
            st.error("Por favor, escriba su nombre.", icon="🧑")
            st.stop()

        if not email:
            st.error("Por favor, escriba su dirección de correo electrónico.", icon="📨")
            st.stop()

        if not is_valid_email(email):
            st.error("La dirección de correo electrónico no es válida.", icon="📧")
            st.stop()

        if not message:
            st.error("Por favor, escriba un mensaje.", icon="💬")
            st.stop()