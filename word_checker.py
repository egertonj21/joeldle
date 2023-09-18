# allows user to input a 5 letter word, confirm that it is : 5 letters and an acceptable word
# checks inputted word against pre-selected word highlight correct letters / word
# TODO allow caps/lower case words, make a quit/give-up option


import word_pick, csv

chosen_word = word_pick.word_picker()

char_array = list(chosen_word[0])

# print("Chosen word:", chosen_word)
# print("Character array:", char_array)

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

while True:

    user_input = input("Enter a word: ")
    user_array = list(user_input)
    match_letters = 0
    match_array =[0,0,0,0,0]

# Check if the input word is in the list
    if user_input == 'QUIT':
        print('The word was ', char_array)
        break
    
    elif len(user_input) != 5:
        print('Your word is not 5 letters long')
    elif is_word_in_list(user_input, word_list):
        print("this is an acceptable word.")
        for i in range(len(user_array)):
            if user_array[i] == char_array[i]:
                match_letters += 1
                match_array[i] = 1
            else:
                match_array[i] = 0
        print('Correct Letters ', match_letters)
        print('Letter in Correct Position', match_array)
        print('Your word', user_array)
        # print('PC word',char_array)
        common_elements = [item for item in user_array if item in char_array]
        count = len(common_elements)
        print("the humber of similar elements is:", count)
        print(common_elements)
        if match_array == [1,1,1,1,1]:
            print('Well Done, game over')
            break
    

    else:
        print(user_input," is not an acceptable word.")