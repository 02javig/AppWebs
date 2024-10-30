import streamlit as st

def mostrar():
    # Título principal
    st.title("ℹ️ Acerca de Javig")
    st.write("---")

    # Subtítulo
    st.subheader("Nuestra Historia")
    
    st.write(
        """
        En **Javig**, somos un equipo apasionado por la tecnología y la innovación. 
        Fundada en 2024, nuestra misión es proporcionar soluciones digitales 
        que aceleren el crecimiento de los negocios de nuestros clientes.
        """
    )
    


    # Servicios destacados
    st.write("---")
    st.write("### 💼 Nuestros Valores")
    st.columns((1, 2))[1].write(
        """
        - **Innovación**: Estamos a la vanguardia de la tecnología.  
        - **Compromiso**: Nos comprometemos con el éxito de nuestros clientes.  
        - **Excelencia**: Buscamos siempre la perfección en cada proyecto.
        """
    )

    # Formulario de contacto
    st.write("---")
    st.write("## 📬 ¿Interesado en saber más?")
    nombre = st.text_input("Tu nombre")
    email = st.text_input("Tu email")
    mensaje = st.text_area("Escribe tu mensaje")
    if st.button("Enviar"):
        st.success("¡Gracias por contactarnos! Te responderemos pronto.")

    # Pie de página
    st.write("---")
    st.write("Made with by **JAVIG**")

