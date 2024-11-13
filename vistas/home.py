# Vista de la página home.py
import json
import requests  # pip install requests
import streamlit as st
from streamlit_lottie import st_lottie  # pip install streamlit-lottie

# Función para cargar animaciones desde archivo JSON
def get(path: str):
    with open(path, "r") as p:
        return json.load(p)

# Función para cargar animaciones desde URL
def get_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Función `mostrar` que contiene todo el contenido de la página de inicio
def mostrar():
    with st.container():
        st.subheader("Bienvenidos, Somos SOFTIA 👋")
        st.title("Creamos soluciones para acelerar tu negocio")
        st.write("""
            Somos unos apasionados de las tecnologías y la innovación, especializados en el sector de la digitalización y automatización de negocios. Nos gusta crear soluciones para resolver problemas y mejorar procesos.
        """)
        st.write("[Saber más >](https://streamlit.io/)")

    # Sobre nosotros
    with st.container():
        st.write("---")
        I_columna, R_columna = st.columns((2))
        with I_columna:
            st.header("Sobre nosotros 🔍")
            st.write("""
                Nuestro objetivo es poder aportar valor a los negocios ayudándoles a ahorrar tiempo y dinero a través de la implantación de nuevas tecnologías.
                Si esto suena interesante para ti puedes contactarnos a través del formulario al final de la página.
            """)
            st.write("[Más sobre nosotros >](https://streamlit.io/)")

        with R_columna:
            path = get("animacion/Animation.json")
            st_lottie(path)
            url = get_url("https://lottie.host/8611e424-5454-46ef-acc1-dbe8a675c7ed/GenBO7VdIL.json")
            st_lottie(url)

    # Servicios
    with st.container():
        st.write("---")
        st.header("Servicios")
        imagen_columna, texto_columna = st.columns((1, 2))
        with imagen_columna:
            st.image("img/disapp.jpg")
        with texto_columna:
            st.subheader("Diseño de aplicaciones")
            st.write("""
                Implementación de aplicaciones para optimizar procesos diarios.
            """)
            st.write("[Ver servicios > ](https://streamlit.io/)")

        # Otras secciones de servicios aquí, como Automatización y Visualización de datos.

    # Contactos
    with st.container():
        st.write("---")
        c_columna, inf_columna = st.columns((1, 2))
        with c_columna:
            st.subheader("📧Contactos")
            contacto_form = """
            <form action="https://formsubmit.co/manzanaresdionicio@gmail.com" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Escriba su nombre" required>
                <input type="email" name="email" placeholder="nombre@email.com" required>
                <textarea name="message" placeholder="Su mensaje"></textarea>
                <button type="submit">Enviar...</button>
            </form>
            """
            st.markdown(contacto_form, unsafe_allow_html=True)

    # Footer
    with st.container():
        st.write("---")
        p1, p2, p3 = st.columns((3))
        with p1:
            st.subheader("Contacto")
            st.write("***Direccion:*** Acoyapa, Chontales, Nicaragua")
            st.write("***Telefono:*** +(505) 0000-0000")
        with p2:
            st.subheader("Servicios")
            st.write("Diseño de aplicaciones")
            st.write("Automatización de procesos")
            st.write("Visualización de datos")
        with p3:
            st.subheader("Redes")
            st.markdown("[YOUTUBE](https://www.youtube.com/)")
            st.markdown("[Facebook](https://www.markdownguide.org/cheat-sheet/)")
            st.markdown("[Instagram](https://www.markdownguide.org/cheat-sheet/)")












  
  
  
