# TODO allow user to input a 5 letter word, confirm that it is : 5 letters and an acceptable word
# TODO check inputted word against pre-selected word highlight correct letters / word


import word_pick, csv

chosen_word = word_pick.word_picker

char_array = list(chosen_word[0])

print("Chosen word:", chosen_word)
print("Character array:", char_array)

# Load words from the CSV file into a list
def load_words_from_csv(csv_file):
    words = []
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            words.extend(row)
    return words

# Function to check if a word is in the list
def is_word_in_list(input_word, word_list):
    return input_word in word_list

# Specify the CSV file containing the list of words
csv_file = "words.csv"

# Load words from the CSV file into a list
word_list = load_words_from_csv(csv_file)

# Get user input
user_input = input("Enter a word: ")

# Check if the input word is in the list
if is_word_in_list(user_input, word_list):
    print(f"'{user_input}' is in the list of words.")
else:
    print(f"'{user_input}' is not in the list of words.")