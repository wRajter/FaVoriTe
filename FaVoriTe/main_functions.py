import pandas as pd
import random
from unidecode import unidecode


def get_data(path='/home/lubo/code/wRajter/FaVoriTe/FaVoriTe/data/top100.csv', size=100):
    '''returns the dictionary of words with its corresponding translation, you can optionally specify number of words you want to use'''
    words = pd.read_csv(path)
    words_resized = words.head(size)
    return words_resized.to_dict(orient="records")

def random_word(dict_words):
    '''returns a random word and its translated version'''
    return (random.choice(dict_words))

def first_lang_word(current_word, first_lang):
    '''returns a German version of a given word'''
    return (current_word[first_lang].lower())

def second_lang_word(current_word, second_lang):
    '''returns a Slovak version of a given word'''
    return (current_word[second_lang].lower())

def clean_lower(word):
    '''returns word witout diactitics and lowercase'''
    return unidecode(word).lower() # unidecode removes diacritics

def answer_split(second_lang):
    '''returns list of possible answers if multiple answers in current word'''
    answer_split = second_lang.split('/')   # split into possible answers if more than one
    list_answers = [clean_lower(word)
                        for word
                        in answer_split] # removing diacritics and making lowercase letters
    return list_answers

def check_answer(user_input, list_answers):
    '''checkes if the user answer was correct or not.
    Please specify: current_word, user_input, list_answers'''
    user_input_prep = clean_lower(user_input)
    if user_input_prep in list_answers:
        return True
    else:
        return False


if __name__ == '__main__':
    dict_words = get_data()
    current_word = random_word(dict_words)
    print(f'germam version: {first_lang_word(current_word, "German")}')
    user_input = input(f'please translate {second_lang_word(current_word, "English")} into German:   ')
    list_answers = answer_split(current_word, 'German')
    output = check_answer(current_word, user_input, list_answers, 'English')
    print(output)
