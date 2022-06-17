from nbformat import write
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
    lang_trainer = st.sidebar.selectbox('Select the language for a word that you will translate.', ['English', 'German', 'Slovak'])
    lang_user = st.sidebar.selectbox('Select the language in which you want to answer', ['English', 'German', 'Slovak'])
    size = st.sidebar.slider(label='Number of words you want to train with', min_value=10, max_value=100, value=10, step=10)
    data = mf.get_data(size=size)



if "input_text" not in st.session_state:
    st.session_state['input_text'] = ''

if 'current_word' not in st.session_state:
    st.session_state['current_word'] = mf.random_word(data)


with train:
    st.header('Your Workout 🏋️🧠')
    next_word = st.button('Gimme a word')
    if next_word:
        st.session_state['current_word'] = mf.random_word(data)

    user_input = st.text_input(f'Please translate {mf.german_word(st.session_state["current_word"])} into Slovak', key="input_text")
    if st.session_state['input_text'] == '':
        st.write('')
    else:
        user_input = st.session_state.input_text
        list_answers = mf.answer_split(st.session_state["current_word"])
        st.write(mf.check_answer(st.session_state["current_word"], user_input, list_answers))
