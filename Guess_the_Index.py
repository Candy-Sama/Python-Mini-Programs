from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess(): #method for player guess
    guess = '' #this variable will be a string
    while guess not in ['0','1','2']:
        guess = input("Pick an index number - 0, 1 or 2: ") #player guess will be returned in a string
        if (guess.isnumeric() ) and (0 <= abs(int(guess)) <= 2):
            return int(guess) #return the int version of player's guess
        else:
            print("Please input a correct number")
        
def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("Good Job, you've guessed the right position! \n The game will now exit")
        #problem 2: initially I tired to set the global variable "game_is_active = True" here, but all it did was create a variable within the function.
        return True
    else:
        print("Wrong guess, try again!")
        return False

def game_loop():
    """
        this will be the main game loop, all the game will be run inside here
        :return:
    """
    mylist = [' ','O',' '] #default values
    
    #shuffle the list first
    mixedup_list = shuffle_list(mylist)
    game_is_active = True

    while game_is_active: #Actual game logic
        inputed_guess = player_guess() #gets player's guess

        if check_guess(mixedup_list, inputed_guess): #checks, and if it's correct, it should break out of the while loop
            game_is_active = False
        else:
            pass
        #reviewing my code: I could just set the game_is_active = check_guess(mixedup_list, inputed_guess) instead

game_loop() #to begin the game loop