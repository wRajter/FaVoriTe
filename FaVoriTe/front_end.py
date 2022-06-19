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
    select_first_lang = st.sidebar.selectbox('Select the language for a word that you will translate.', ['English', 'German', 'Slovak'])
    select_second_lang = st.sidebar.selectbox('Select the language in which you want to answer', ['German', 'English', 'Slovak'])
    size = st.sidebar.slider(label='Number of words you want to train with', min_value=10, max_value=100, value=10, step=10)
    data = mf.get_data(size=size, first_lang=select_first_lang, second_lang=select_second_lang)


if 'current_word' not in st.session_state:
    st.session_state['current_word'] = mf.random_word(data)


with train:
    st.header('Your Workout 🏋️🧠')
    next_word = st.button('Gimme a word')
    if next_word:
        st.session_state['current_word'] = mf.random_word(data)

    word_in_both_langs = st.session_state["current_word"]

    st.write(word_in_both_langs)

    word_first_lang = word_in_both_langs[select_first_lang]
    word_second_lang = word_in_both_langs[select_second_lang]
    possible_answers = mf.answer_split(word_second_lang)

    user_input = st.text_input(f'Please translate {word_first_lang} into {select_second_lang}', key="input_text")
    if st.session_state['input_text'] == '':
        st.write('')
    else:
        user_input = st.session_state.input_text
        if mf.check_answer(user_input, possible_answers):
            st.write(f"### Correct! 😀👌🎉\n#### {word_first_lang} means {', '.join(possible_answers)}")
        else:
            st.write(f"### {word_first_lang} means {', '.join(possible_answers)} 👩‍🏫")
