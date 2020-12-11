# Create a Tic Tac Toe game.
# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board

#What do I need:
# Method to display the board
# Method to take in player input
# Method to decide which player is who: For example if player 1 chooses x, then player 1 goes first, else, player 2 goes first.
# Method to decide if the player has won or not

#list of variables to declare
is_game_running = False
player_spots = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "}
player1_name = 1
player1_icon = " "
player2_name = 2
player2_icon = " "

#method to see if the player wants to keep playing
def game_running(player1_name):
    keep_playing = 1
    keep_playing_bool_check = True

    while keep_playing not in ['Y','N']:
        if player1_name == 1: #check to see if the game has been initialised
            keep_playing = input("Do you want to play Tic Tac Toe? (Y/N): ").upper()
        else:
            keep_playing = input("Do you want to keep playing? (Y/N): ").upper()


    if keep_playing == 'Y':
        keep_playing_bool_check = True
    else:
        keep_playing_bool_check = False

    return keep_playing_bool_check

def instructions():
    pass


#method to display the board
def display_board():
    print ("    |   |   ")
    print (f"  {player_spots[7]} | {player_spots[8]} | {player_spots[9]} ")
    print ("    |   |   ")
    print ("-------------")
    print ("    |   |   ")
    print (f"  {player_spots[4]} | {player_spots[5]} | {player_spots[6]} ")
    print ("    |   |   ")
    print ("-------------")
    print ("    |   |   ")
    print (f"  {player_spots[1]} | {player_spots[2]} | {player_spots[3]} ")
    print ("    |   |   ")
display_board() #for debug

#method to get players to give their names
def get_player_name(player1_name,player2_name):
    #for debug
    print(f"{player1_name} and {player2_name}")

    while player1_name == 1:
        player1_name = input("Player 1, please input your name: ")
    else :
        print(f"Player 1, your name is {player1_name}.")


    while player1_name != 1 and player2_name == 2:
        player2_name = input("Player 2, please input your name: ")        
    else:
        print(f"Player 2, your name is {player2_name}.")

    #for debug
    print(f"{player1_name} and {player2_name}")

    return player1_name, player2_name

#method to get the players' chosen icon
def get_player_icon(player1_icon, player2_icon):
    #for debug
    print(f"{player1_icon} and {player2_icon}")

    while player1_icon not in ['X','O']:
        player1_icon = input("Player 1, please choose your icon (X or O is only allowed): ").upper()
    
    if player1_icon == 'X':
        player2_icon = 'O'
    else:
        player2_icon = 'X'

    print (f"Player 1's symbol is now {player1_icon}")
    print (f"Player 2's symbol is now {player2_icon}")
    return player1_icon, player2_icon

#method for 



while is_game_running:

    player1_name, player2_name = get_player_name(player1_name,player2_name) #setting the player's names
    player1_icon, player2_icon = get_player_icon(player1_icon,player2_icon) #setting the player's icons
    display_board()
    break

