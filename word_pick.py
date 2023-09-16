# picks a random word from the seperate words file and splits it into it's individual letters

import csv, random

def word_picker():
    csv_file = "words.csv"
    data = []

    with open(csv_file, mode = 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    chosen_word = random.choice(data)
    return chosen_word
chosen_word = word_picker()

char_array = list(chosen_word[0])

print("Chosen word:", chosen_word)
print("Character array:", char_array)


