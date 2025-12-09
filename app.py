import pandas as pd
import plotly.express as px
import streamlit as st

# título / cabeçalho do app
st.header('Dashboard de anúncios de carros')

# carregar os dados
car_data = pd.read_csv('vehicles_us.csv')

st.write('Visualização simples das primeiras linhas do conjunto de dados:')
st.write(car_data.head())

# botão para histograma
hist_button = st.button('Criar histograma da quilometragem')

if hist_button:
    st.write('Histograma da coluna odometer (quilometragem)')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# botão para gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão Preço vs Quilometragem')

if scatter_button:
    st.write('Gráfico de dispersão: preço em função da quilometragem')
    fig2 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig2, use_container_width=True)