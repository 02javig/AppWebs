import streamlit as st
from vistas import home, acerca_de, ventas, chatbot  # Importa las vistas

# Configuración del sidebar para navegación
st.sidebar.title("Navegación")
opcion = st.sidebar.selectbox(
    "Selecciona una vista:",
    ["Inicio", "Acerca de", "Ventas", "Chatbot"]
)

# Lógica para mostrar la vista correspondiente
if opcion == "Inicio":
    home.mostrar()  # Llama a la función `mostrar` de home.py
elif opcion == "Acerca de":
    acerca_de.mostrar()
elif opcion == "Ventas":
    ventas.mostrar()
elif opcion == "Chatbot":
    chatbot.mostrar()

