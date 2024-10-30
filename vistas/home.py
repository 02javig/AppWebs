import streamlit as st

def mostrar():
    # Inicio
    with st.container():
        st.subheader("Bienvenidos, somos Javig")
        st.title("Creamos soluciones para acelerar su negocio")
        st.write("Somos unos apasionados de las tenologías y la innovación, especialización en el sector de la digitalización y automatización de negocios. Nos gusta crear soluciones para resolver problemas y mejorar procesos. ")
        st.write("[Saber más >>>](https://www.ideasforchange.com/es/archivo-blog/claves-acelerar-negocio-innovacion)")

    # Sobre Nosotros
    with st.container():
        st.write("---")
        izquierda_columna, derecha_columna = st.columns((2, 1))
        
        with derecha_columna:
            st.image("img/javig.jpeg", caption="Javig")

        with izquierda_columna:
            st.subheader("Sobre Nosotros")
            st.write(
                """
                Nuestro objetivo es poder aportar valor a los negocios ayudandoles a ahorrar tiempo y dinero a través de la implantación de nuevas tecnologías como la inteligencia artifical, analisis de datos o implantación de software de automatización.

Seguramente te vamos a poder ayudar si:

-Tienes un negocio y quieres mejorar tus procesos de trabajo para ahorrar tiempo y dinero Tienes trabajadores que emplean parte de su jornada a realizar tareas repetitivas sin valor añadido

para tu negocio

No tienes claras las métricas de tu negocio y quieres tomar decisiones basadas en datos

-Quieres mejorar la experiencia de tus clientes

Usas herramientas de software antiguas o poco eficientes o procesos en los que usas papel y boligrafo

***Si esto suena interesante para ti puedes contactarnos a través del formulario que encontrarás al final de la página***
                """
            )
            st.write("[Saber más >>>](https://www.nomadia-group.com/es/recursos/blog/objetivos-comerciales-y-ejemplos-maximiza-tu-exito/)")

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
                Si en tus procesos diarios tienes que introducir información en diferentes fuentes de datos o bien tienes que trabajar con documentación en papel, es hora de pensar en implementar una aplicación en tu negocio para potenciar y optimizar el funcionamiento de los procesos diarias
        
                """
            )
            st.write("[Saber más >>>](https://dossetenta.com/los-diferentes-tipos-de-diseno-de-apps-y-cual-es-el-mejor-para-tu-empresa/#:~:text=El%20dise%C3%B1o%20de%20apps%20es,una%20experiencia%20de%20usuario%20satisfactoria.)")

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
                Aunque las computadoras son omnipresentes hoy día, todavía hay una cantidad significativa de operaciones manuales que se llevan a cabo a diario en empresas de todo el mundo. Esto puede afectar a todas las áreas de negocio, desde la producción y las ventas hasta el soporte de marketing y TI.

               Dado que las tareas manuales tediosas a menudo pueden estar sujetas a errores humanos, es recomendable reducirlas tanto como sea posible. Aquí, la automatización de procesos puede ser la respuesta. Con la automatización de procesos, puede optimizar los flujos de trabajo diarios que se ejecutan en sus departamentos, agilizar las operaciones, minimizar los errores, reducir los riesgos de seguridad y aumentar la productividad, y todo esto de una vez.
                """
            )
            st.write("[Saber más >>>](https://www.boc-group.com/es/blog/bpm/automatizacion-de-procesos-su-camino-hacia-la-eficiencia-operativa#:~:text=Con%20la%20automatizaci%C3%B3n%20de%20procesos,todo%20esto%20de%20una%20vez.)")

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
                La visualización de datos es la representación gráfica de información y datos. Al utilizar elementos visuales como cuadros, gráficos y mapas, las herramientas de visualización de datos proporcionan una manera accesible de ver y comprender tendencias, valores atípicos y patrones en los datos.

               En el mundo del big data, las herramientas y tecnologías de visualización de datos son esenciales para analizar grandes cantidades de información y tomar decisiones basadas en los datos..
                """
            )
            st.write("[Saber más >>>](https://www.tableau.com/es-mx/learn/articles/data-visualization#:~:text=La%20visualizaci%C3%B3n%20de%20datos%20ayuda,y%20resaltando%20la%20informaci%C3%B3n%20%C3%BAtil.)")



  
  
  
