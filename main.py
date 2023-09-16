# attempt at throwing together a working wordle in python

while True:
    print('1. Play')
    print('2. Exit')
    user_input = input('Select an option: ')

    try:
        option = int(user_input)
    except ValueError:
        print('Invalid input. Please enter a valid option (1 or 2).')
        continue  # Go back to the start of the loop

    if option == 1:
        # Add code here for the "Play" option
        print('Starting the game...')
    elif option == 2:
        print('Exiting the program. Goodbye!')
        break  # Exit the loop and end the program
    else:
        print('Invalid option. Please enter 1 or 2.')