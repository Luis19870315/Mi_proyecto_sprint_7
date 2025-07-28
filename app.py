import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') 

# Encabezado
st.header('DATOS DE VEHICULOS COMERCIALES')

# Aqui se muestra los primeros datos de vehiculos
if st.checkbox('Mostrar los primeros datos de la lista de vehiculos'):
    st.write(car_data.head(10))


if st.button('Histograma de Vehiculos por kilometraje recorrido'):
    st.write('Histograma de la columna odómetro o kilometraje recorrido')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig)

if st.button('Diagrama de Dispersión de Vehiculos'):
    st.write('Diagrama de dispersión entre: Kilometraje vs Precio')
    fig2 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig2)

# Versiónes  con checkboxes

if st.checkbox('CLICK PARA MOSTRAR EL HISTOGRAMA POR KILOMETRO RECORRIDO'):
    st.write('Histograma de Vehiculos por Kilometraje recorrido')
    fig3 = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig3)

if st.checkbox('CLICK PARA MOSTRAR LA DISPERSION ENTRE: KILOMETRAJE Y PRECIO'):
    st.write('Diagrama de dispersión de Vehiculos entre: kilometraje vs precio')
    fig4 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig4)
