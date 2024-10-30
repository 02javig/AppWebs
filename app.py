import streamlit as st
from vistas import home, acerca_de, ventas, chatbot  # Importa las vistas

# Configuración del sidebar para navegación con íconos
st.sidebar.title("🧭 Navegación")
opcion = st.sidebar.selectbox(
    "Selecciona una vista:",
    [
        "🏠 Inicio",  
        "🛒 Ventas", 
        "🤖 Chatbot",
        "ℹ️ Acerca de"
    ]
)

# Lógica para mostrar la vista correspondiente
if opcion == "🏠 Inicio":
    home.mostrar()  # Llama a la función `mostrar` de home.py
elif opcion == "ℹ️ Acerca de":
    acerca_de.mostrar()
elif opcion == "🛒 Ventas":
    ventas.mostrar()
elif opcion == "🤖 Chatbot":
    chatbot.mostrar()


