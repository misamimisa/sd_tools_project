import streamlit as st
import pandas as pd
import plotly.express as px
import ipywidgets as widgets
from IPython.display import display
import seaborn as sns
import matplotlib.pyplot as plt

# Загружаем данные
df = pd.read_csv('vehicles_us.csv')

st.header('Used Cars in the USA — Dashboard')

# Добавляем чекбокс для отображения исходных данных
if st.checkbox('Show raw data'):
    st.write(df.head())

# Гистограмма распределения пробега
st.subheader('Distribution of Odometer Readings')
fig_odometer = px.histogram(df, x='odometer', nbins=30, title='Odometer Histogram')
st.plotly_chart(fig_odometer)

# Гистограмма распределения цен
st.subheader('Distribution of Prices')
fig_price = px.histogram(df, x='price', nbins=30, title='Price Histogram')
st.plotly_chart(fig_price)

# Диаграмма рассеяния цена-пробег
st.subheader('Scatter Plot: Odometer vs Price')
fig_scatter = px.scatter(df, x='odometer', y='price', color='condition', title='Odometer vs Price by Condition')
st.plotly_chart(fig_scatter)

# Ещё одна диаграмма рассеяния: год выпуска - цена
st.subheader('Scatter Plot: Year vs Price')
fig_year_price = px.scatter(df, x='model_year', y='price', color='condition', title='Model Year vs Price by Condition')
st.plotly_chart(fig_year_price)
