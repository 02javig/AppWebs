import streamlit as st

def mostrar():
    # Inicio
    with st.container():
        st.subheader("Bienvenidos, somos SOFTIA")
        st.title("Creamos soluciones para acelerar su negocio")
        st.write("Somos unos apasionados por las tecnologías y la innovación...")
        st.write("[Saber más >>>](https://tu-enlace.com)")

    # Sobre Nosotros
    with st.container():
        st.write("---")
        izquierda_columna, derecha_columna = st.columns((2, 1))

        with izquierda_columna:
            st.subheader("Sobre Nosotros")
            st.write(
                """
                Nuestro objetivo es aportar valor a los negocios:
                - ¿Tienes un negocio?
                - ¿Tienes trabajadores?
                - ¿No tienes claras las métricas?

                ***Si esto suena interesante, contáctanos.***
                """
            )
            st.write("[Saber más >>>](https://tu-enlace.com)")

    # Servicios
    with st.container():
        st.write("---")
        st.subheader("Servicios")

        imagen_columna, texto_columna = st.columns((1, 2))

        with imagen_columna:
            st.image("img/disapp.jpg", caption="Diseño de aplicaciones")

        with texto_columna:
            st.subheader("Diseño de aplicaciones")
            st.write(
                """
                Si en tus procesos diarios tienes que introducir información en 
                diferentes sistemas, nosotros podemos ayudarte a simplificar.
                """
            )
            st.write("[Saber más >>>](https://tu-enlace.com)")

    # Automatización de procesos
    with st.container():
        st.write("---")

        imagen_columna, texto_columna = st.columns((1, 2))

        with imagen_columna:
            st.image("img/autpro.jpg", caption="Automatización de procesos")

        with texto_columna:
            st.subheader("Automatización de procesos")
            st.write(
                """
                La automatización permite que tu negocio sea más eficiente y reduzca errores humanos.
                """
            )
            st.write("[Saber más >>>](https://tu-enlace.com)")

    # Visualización de Datos
    with st.container():
        st.write("---")

        imagen_columna, texto_columna = st.columns((1, 2))

        with imagen_columna:
            st.image("img/visdat.jpg", caption="Visualización de datos")

        with texto_columna:
            st.subheader("Visualización de Datos")
            st.write(
                """
                Aprovecha el poder de la visualización para tomar decisiones informadas.
                """
            )
            st.write("[Saber más >>>](https://tu-enlace.com)")



  
  
  
