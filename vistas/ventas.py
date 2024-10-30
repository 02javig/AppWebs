import streamlit as st
import pandas as pd
try:
    import matplotlib.pyplot as plt
except ImportError as e:
    st.error("Matplotlib no está instalado. Por favor, instala el paquete con: pip install matplotlib.")
    raise e


def mostrar():
    # Título principal
    st.title("📊 Panel de Ventas")
    st.write("---")

    # Resumen general
    st.subheader("Resumen de Ventas")
    st.metric("Ingresos Totales", "$120,000", "+8% desde el mes pasado")
    st.metric("Ventas Este Mes", "540 unidades", "+12% desde el mes pasado")

    # Gráfico de barras: Ventas mensuales
    st.write("### 🔍 Ventas Mensuales")
    ventas_mensuales = {
        "Mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
        "Ventas": [12000, 15000, 18000, 22000, 19000, 24000],
    }
    df_ventas = pd.DataFrame(ventas_mensuales)

    fig, ax = plt.subplots()
    ax.bar(df_ventas["Mes"], df_ventas["Ventas"], color="skyblue")
    ax.set_xlabel("Mes")
    ax.set_ylabel("Ingresos ($)")
    ax.set_title("Ingresos Mensuales")

    st.pyplot(fig)

    # Tabla de productos más vendidos
    st.write("### 🥇 Productos más Vendidos")
    productos = {
        "Producto": ["Producto A", "Producto B", "Producto C"],
        "Unidades Vendidas": [230, 180, 145],
        "Ingresos Generados": ["$11,500", "$9,000", "$7,250"],
    }
    df_productos = pd.DataFrame(productos)
    st.table(df_productos)

    # Proyecciones de ventas con slider
    st.write("### 🔮 Proyecciones de Ventas")
    incremento = st.slider("Porcentaje de crecimiento estimado:", 0, 50, 10)
    proyeccion = 24000 * (1 + incremento / 100)
    st.metric("Proyección para el próximo mes", f"${proyeccion:,.2f}")

    # KPI y estado de objetivos
    st.write("---")
    st.write("### 🎯 Estado de Objetivos de Ventas")
    st.progress(0.75)  # Ejemplo: 75% del objetivo cumplido

    # Botón de descarga de datos
    st.write("---")
    st.write("## 📥 Descargar Informe de Ventas")
    csv = df_ventas.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Descargar CSV",
        data=csv,
        file_name="informe_ventas.csv",
        mime="text/csv",
    )

    # Pie de página
    st.write("---")
    st.write("Made with by **JAVIG**")

