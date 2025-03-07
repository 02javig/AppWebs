import streamlit as st
from Forms.contacto import contact_form

def ver_form_contacto():
    # Ventana modal para el formulario de contacto
    contact_form()

def mostrar():
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image("img/javig.jpeg", width=230)
    with col2:
        st.title("Jadder Viachica", anchor=False)
        st.write(
            "Analista de datos senior, que ayuda a las empresas apoyando la toma de decisiones basada en datos. "
            "Especializado en Ciencia de Datos."
        )
    
    # Botón para mostrar el formulario de contacto en la ventana modal
    if st.button("Contacto"):  
        ver_form_contacto()

    # --- Experiencia y calificaciones ---
    st.write("\n")
    st.subheader("Experiencia y calificaciones", anchor=False)
    st.write("""
    - 7 años de experiencia extrayendo información útil a partir de datos.
    - Fuerte experiencia práctica y conocimiento en Python y Excel.
    - Buen conocimiento de los principios estadísticos y sus respectivas aplicaciones.
    - Excelente jugador de equipo y con un fuerte sentido de iniciativa en las tareas.
    """)

    # --- HABILIDADES ---
    st.write("\n")
    st.subheader("Habilidades", anchor=False)
    st.write("""
    - Programación: Python (Scikit-learn, Pandas), SQL, VBA
    - Visualización de Datos: PowerBi, MS Excel, Plotly
    - Modelado: Logistic regression, linear regression, decision trees
    - Base de Datos: Postgres, MongoDB, MySQL
    """)

# Llama a la función principal
mostrar()

