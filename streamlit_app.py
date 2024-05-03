import streamlit as st
import pandas as pd
import plotly.express as px

# Загрузка данных
@st.cache
def load_data(url):
    return pd.read_csv(url)

data_url = "https://github.com/terzatell/terzatel/edit/main/streamlit_app.py"
data = load_data(data_url)

# Визуализация данных
st.title('Визуализация данных о странах Центральной Азии')

fig = px.bar(data, x='Страна', y='Показатель', title='Показатели по странам')
st.plotly_chart(fig)

