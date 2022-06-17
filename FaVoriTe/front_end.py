import streamlit as st
import main_functions as mf


header = st.container()
options = st.container()
dataset = st.container()
train = st.container()


with header:
    st.title('Welcome to FaVoriTe, your own Fast Vocabulary Trainer 🥋')


with options:
    st.sidebar.header('Options')
    lang_trainer = st.sidebar.selectbox('Select the language in which you want to have words for translation displayed.', ['English', 'German', 'Slovak'])
    lang_user = st.sidebar.selectbox('Select the language in which you want to answer', ['English', 'German', 'Slovak'])
    size = st.sidebar.slider(label='Number of words you want to train with', min_value=10, max_value=100, value=10, step=10)
    data = mf.get_data(size=size)
    st.write(len(data))



with train:
    st.header('Your Workout 🏋️🧠')
