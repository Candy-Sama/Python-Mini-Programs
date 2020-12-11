import sys

#initialise variables
game_list = [0,1,2]
game_on = True

#method to display the list
def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)

#method to check for the player's position choice
def position_choice():

    #initial vairiables
    choice = 'wrong'
    acceptable_values = ['0','1','2']

    while choice not in acceptable_values:

        choice = input("Pick a position (0,1,2): ")

        if choice not in acceptable_values:
            print("Sorry, invalid position!")
    
    return int(choice)

#method to check for the replacement string of the player input
def replacement_choice(game_list,position):
    
    user_placement = input("Type a string to place at position: ")

    game_list[position] = user_placement

    return game_list

#method to check if player wants to keep on going
def gameon_choice():

    #initial vairiables
    choice = 'wrong'

    while choice.upper() not in ['Y','N']:

        choice = input("Keep playing? (Y or N): ")

        if choice.upper() not in ['Y','N']:
            print("Sorry, I don't understand - Please choose Y or N")
    
    if choice.upper() == "Y":
        return True
    else:
        return False


#Game loop
while game_on:

    display_game(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list, position)

    display_game(game_list)

    game_on = gameon_choice()