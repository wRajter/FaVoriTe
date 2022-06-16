import pandas as pd
import random
from unidecode import unidecode


# Get Data
words = pd.read_csv('/home/lubo/code/wRajter/FaVoriTe/FaVoriTe/data/german_words_1500_SK.csv')
dict_words = words.to_dict(orient="records")


def random_word():
    '''returns a random word and its translated version'''
    return (random.choice(dict_words))

def german_word(current_word):
    '''returns a German version of a given word'''
    return (current_word["German"].lower())

def slovak_word(current_word):
    '''returns a Slovak version of a given word'''
    return (current_word["Slovak"].lower())

def clean_lower(word):
    '''returns word witout diactitics and lowercase'''
    return unidecode(word).lower() # unidecode removes diacritics

def answer_split(current_word):
    '''returns list of possible answers if multiple answers in current word'''
    answer_split = slovak_word(current_word).split('/')   # split into possible answers if more than one
    list_answers = [clean_lower(word)
                        for word
                        in answer_split] # removing diacritics and making lowercase letters
    return list_answers

def check_answer(current_word, user_input, list_answers):
    '''checkes if the user answer was correct or not.
    Please specify: current_word, user_input, list_answers'''
    user_input_prep = clean_lower(user_input)
    if user_input_prep in list_answers:
        return f"Správne!\n{german_word(current_word)} znamená {', '.join(list_answers)}"
    else:
        return f"{german_word(current_word)} znamená {', '.join(list_answers)}"


if __name__ == '__main__':
    current_word = random_word()
    print(f'slovak version: {slovak_word(current_word)}')
    user_input = input(f'please translate {german_word(current_word)} into slovak:   ')
    list_answers = answer_split(current_word)
    output = check_answer(current_word, user_input, list_answers)
    print(output)
