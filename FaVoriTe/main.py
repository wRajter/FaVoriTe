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

def checking_answer(user_input, current_word):
        user_input_prep = clean_lower(user_input)
        answer_split = slovak_word(current_word).split('/')   # split into possible answers if more than one
        answer_adjusted = [unidecode(word.lower())
                           for word
                           in answer_split] # removing diacritics and making lowercase letters
        return answer_adjusted
        # if user_input in answer_adjusted:
        #     self.question.config(text=f"Správne!\n{self.current_word['German']} znamená {', '.join(answer_adjusted)}")
        #     self.check_button.config(text="Dalšie slovo", command=self.next_word)
        #     self.translation_entry.bind('<Shift_R>', self.next_word)
        # else:
        #     self.question.config(text=f"'{self.current_word['German']}' znamená {', '.join(answer_adjusted)}")
        #     self.check_button.config(text="Dalšie slovo", command=self.next_word)
        #     self.translation_entry.bind('<Shift_R>', self.next_word)



if __name__ == '__main__':
    current_word = random_word()
    print(slovak_word(current_word))
    user_input = input(f'please translate {german_word(current_word)} into slovak')
    answer_adjusted = checking_answer(user_input, current_word)
    print(answer_adjusted)
