import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv') 

# Configuración de la página
img = Image.open('logo.png')
st.set_page_config(page_title='Auto Cars TRIPLETEN', page_icon=img)

# Encabezado
st.header('DATOS DE VEHÍCULOS COMERCIALES')

# Mostrar los primeros datos
if st.checkbox('Mostrar los primeros datos de la lista de vehículos'):
    st.write(car_data.head(10))

# Botón: Histograma por kilometraje
if st.button('Histograma de vehículos por kilometraje recorrido'):
    st.write('Histograma de la columna "odometer" (kilometraje recorrido)')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig)

# Botón: Diagrama de dispersión
if st.button('Diagrama de dispersión de vehículos'):
    st.write('Dispersión entre kilometraje (odometer) y precio')
    fig2 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig2)

# Checkbox: Mostrar histograma
if st.checkbox('Mostrar histograma por kilometraje recorrido'):
    st.write('Histograma de vehículos por kilometraje recorrido')
    fig3 = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig3)

# Checkbox: Mostrar dispersión
if st.checkbox('Mostrar dispersión entre kilometraje y precio'):
    st.write('Dispersión entre kilometraje (odometer) y precio')
    fig4 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig4)



# Mi_proyecto_sprint_7
# En la aplicación es importa



# Mi_proyecto_sprint_7
# En la aplicación es importante porque conocemos los niveles de ventas de los diferentes vehículos por su marca, modelo, precio y el kilometraje que tienen recorrido.
