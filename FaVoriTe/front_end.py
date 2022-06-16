import streamlit as st
import main_functions as mf


header = st.container()
options = st.container()
dataset = st.container()
train = st.container()


with header:
    st.title('Welcome to FaVoriTe, your own Fast Vocabulary Trainer 🥋')


with options:
    st.header('Options')
    st.text('You can choose a deck of words that you want to learn.')
    lang_trainer = st.selectbox('Select the language in which you want to have words for translation displayed.', ['English', 'German', 'Slovak'])
    lang_user = st.selectbox('Select the language in which you want to answer', ['English', 'German', 'Slovak'])

with dataset:
    data = mf.get_data()




with train:
    st.header('Your Workout 🏋️🧠')
