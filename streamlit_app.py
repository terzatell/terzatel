import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title('Мини сайт для визуализации данных')

    # Возможность загрузки файла пользователем
    uploaded_file = st.file_uploader("Загрузите CSV файл", type="csv")
    if uploaded_file is not None:
        # Чтение данных
        data = pd.read_csv(uploaded_file)
        
        # Отображение данных в таблице
        st.write("Просмотр загруженных данных:")
        st.dataframe(data)

        # Построение графика, если данные позволяют
        if 'Страна' in data.columns and 'Показатель' in data.columns:
            st.write("График по показателям:")
            fig = px.bar(data, x='Страна', y='Показатель', title='Показатели по странам')
            st.plotly_chart(fig)
        else:
            st.error("CSV файл должен содержать колонки 'Страна' и 'Показатель'")
    else:
        st.info("Пожалуйста, загрузите файл в формате CSV.")

if __name__ == "__main__":
    main()
