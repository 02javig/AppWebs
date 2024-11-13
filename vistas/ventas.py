import streamlit as st
import pandas as pd
import plotly.express as px

def mostrar():
    st.subheader("Filtrar Datos y Captura de Datos")
    st.write("El procesamiento de datos a través de Ciencia de Datos usando Streamlit de Python")

    # Cargar los datos
    dfDatos = pd.read_csv('http://raw.githubusercontent.com/gcastano/datasets/main/gapminder_data.csv')

    # Mostrar la tabla de los registros
    st.metric("**Registros Totales**", len(dfDatos))
    st.dataframe(dfDatos, use_container_width=True)

    # Crear filtros
    continent_filter = st.multiselect(
        "Selecciona los continentes:",
        options=dfDatos['continent'].unique(),
        default=dfDatos['continent'].unique()
    )
    country_filter = st.text_input("Escriba el nombre del País (opcional):", value="")

    age_range = st.slider( 
        "Selecciona el Rango de Edad:", 
        min_value=int(dfDatos['median_age_year'].min()), 
        max_value=int(dfDatos['median_age_year'].max()), 
        value=(int(dfDatos['median_age_year'].min()), int(dfDatos['median_age_year'].max()))
    )

    # Filtrar los datos basados en las selecciones
    filtered_data = dfDatos[
        (dfDatos['continent'].isin(continent_filter)) &
        (dfDatos['country'].str.contains(country_filter, case=False, na=False)) &
        (dfDatos['median_age_year'] >= age_range[0]) &
        (dfDatos['median_age_year'] <= age_range[1])
    ]

    # Mostrar la tabla de los registros filtrados y la métrica actualizada 
    st.metric("**Registros Totales Filtrados**", len(filtered_data)) 
    st.dataframe(filtered_data, use_container_width=True)

    # Crear gráficos si hay datos filtrados
    if not filtered_data.empty:
        # Gráfico de Dispersión
        fig_scatter = px.scatter(
            filtered_data, x='mean_house_income', y='lifeExpectancy', color='continent', 
            title='Ingreso Medio del Hogar vs Esperanza de Vida',
            labels={'mean_house_income': 'Ingreso Medio del Hogar', 'lifeExpectancy': 'Esperanza de Vida'}
        )
        st.plotly_chart(fig_scatter)

        # Gráfico de Líneas
        fig_line = px.line(
            filtered_data, x='year', y='population', color='continent', 
            title='Población a lo Largo del Tiempo',
            labels={'year': 'Año', 'population': 'Población'}
        )
        st.plotly_chart(fig_line)

        # Gráfico de Barras
        fig_bar = px.bar(
            filtered_data, x='continent', y='population', color='continent', 
            title='Población por Continente',
            labels={'continent': 'Continente', 'population': 'Población'}
        )
        st.plotly_chart(fig_bar)
    else:
        st.warning("No hay datos para mostrar en los gráficos con los filtros seleccionados.")
        st.subheader("Consulta de Datos Interactiva")
        st.write("Realiza preguntas sobre los datos de población y otros indicadores.")
    
    # Selección de preguntas
    pregunta = st.selectbox(
        "Selecciona una pregunta:",
        [
            "¿Cuáles son los países con menos población?",
            "¿Cuáles son los países con mayor esperanza de vida?",
            "¿Cuáles son los continentes con mayor ingreso medio del hogar?",
            "¿Cuál es la población media por continente?"
        ]
    )

    # Procesar la pregunta seleccionada
    if pregunta == "¿Cuáles son los países con menos población?":
        resultado = dfDatos.nsmallest(10, 'population')[['country', 'population']]
        st.write("### Países con Menor Población")
        st.table(resultado)
    
    elif pregunta == "¿Cuáles son los países con mayor esperanza de vida?":
        resultado = dfDatos.nlargest(10, 'lifeExpectancy')[['country', 'lifeExpectancy']]
        st.write("### Países con Mayor Esperanza de Vida")
        st.table(resultado)
    
    elif pregunta == "¿Cuáles son los continentes con mayor ingreso medio del hogar?":
        resultado = dfDatos.groupby('continent')['mean_house_income'].mean().sort_values(ascending=False)
        st.write("### Ingreso Medio del Hogar por Continente")
        st.table(resultado)
    
    elif pregunta == "¿Cuál es la población media por continente?":
        resultado = dfDatos.groupby('continent')['population'].mean()
        st.write("### Población Media por Continente")
        st.table(resultado)

    # Visualización del resultado (opcional)
    if st.checkbox("Mostrar gráfico"):
        if pregunta in ["¿Cuáles son los países con menos población?", "¿Cuáles son los países con mayor esperanza de vida?"]:
            fig = px.bar(resultado, x='country', y=resultado.columns[1], title=pregunta)
            st.plotly_chart(fig)
        elif pregunta in ["¿Cuáles son los continentes con mayor ingreso medio del hogar?", "¿Cuál es la población media por continente?"]:
            fig = px.bar(resultado, x=resultado.index, y=resultado.values, title=pregunta)
            st.plotly_chart(fig)


