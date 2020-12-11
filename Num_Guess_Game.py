#Guessing Game Challenge
#Create a number guessing game with the following mechanics:

# Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
# - If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# - On a player's first turn, if their guess is
#   within 10 of the number, return "WARM!"
#   further than 10 away from the number, return "COLD!"
# - On all subsequent turns, if a guess is
#   closer to the number than the previous guess return "WARMER!"
#   farther from the number than the previous guess, return "COLDER!"
# - When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took! 

from random import randint

# Correct Number that is randomly generated between 1 and 100
correct_number = randint(1, 100)

# print(correct_number) #For debugging only

player_first_turn = True

guesses = [0] #A value to store first
game_is_active = True

while game_is_active: #Game Loop, this will keep running over and over until you're done and want to exit
    player_input = input("Please enter your guess! Type 'exit' to exit the game: ")

    
    if (player_input.lower() == 'exit'): #ensures that the string will always be lowercase to match the if condition
        print('Game will now exit')
        game_is_active = False

    elif (player_input.isnumeric() == False): #problem 1 solution: use .isnumeric() to check if the entire value has a number
        print('Invalid guess. Please input a proper number.')

    else: #if the player didn't ask to exit or gave a false number, then convert it to integer
        #problem 1: what can I do to check if it's just text and not a number?
        

        player_input = int(player_input) 
        if (player_input < 1 or player_input > 100): #If it's outside of the range
            print('OUT OF BOUNDS')
    
        else:
            guesses.append(player_input) #add it to the list
        
            if (player_input == correct_number):
                print(f'You have guessed the number successfully!. It took you {len(guesses)-1} tries!') #remove the very first value of 0 in the list, so it wont be inaccurate
                game_is_active = False

            elif (player_first_turn == True): #to check if it's the first turn
                if (abs(correct_number-player_input) <= 10):
                    print('WARM!')
                else:
                    print('COLD!')
                player_first_turn = False
            
            elif (player_first_turn == False): #if it's not the first urn
                if (abs(guesses[-2] - correct_number) > abs(player_input - correct_number)): #check the difference in the numbers. Absolute it so it wont return an error with negatives
                    print('WARMER!')
                else:
                    print('COLDER!')
#Problem no. 2: I keep making syntax errors. Gotta practice making more programs.