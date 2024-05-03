import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Terzatel apps')

st.text("Hello, this is my app.")

st.write("This is a Streamlit app used to demonstrate interactive widgets and plots!")

user_input = st.text_input("Please enter your name")

if user_input:
    st.write(f"Hello, {user_input}! Welcome to the Streamlit app.")

number = st.slider("Select a number", 0, 100, 25)
st.write(f"You selected: {number}")

data = pd.DataFrame(
    np.random.randn(50, 2), 
    columns=['A', 'B']
)

st.write("Here is a simple plot of 50 random numbers:")
st.line_chart(data)

fig, ax = plt.subplots()
ax.hist(np.random.randn(100), bins=15, density=True, alpha=0.6, color='b')
st.pyplot(fig)

col1, col2 = st.columns(2)
with col1:
    st.checkbox("Check me out")
with col2:
    st.radio("Select One:", options=["Option 1", "Option 2", "Option 3"])

option = st.selectbox(
    'How would you rate this app?',
    ('Select an option', 'Awesome', 'Okay', 'Not good')
)

if option != 'Select an option':
    st.write('You selected:', option)

map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

st.map(map_data)

st.write("Thank you for visiting!")

