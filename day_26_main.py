import pandas as pd

# with open('day_26_nato_phonetic_alphabet.csv') as alphabet:

#TODO 1. Create a dictionary in this format:
df = pd.read_csv('day_26_nato_phonetic_alphabet.csv')
# print(df)
alphabet_dictionary = {row.letter: row.code for (index, row) in df.iterrows()}
# print(alphabet_dictionary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = str(input('Enter word here: ')).upper()
user_list = [alphabet_dictionary[letter] for letter in user_input]
print(user_list)
