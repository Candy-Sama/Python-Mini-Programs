def user_choice():
    #Variables
    
    #inital variables    
    choice = 'Wrong' #initialise the variable as a false non-digit
    acceptable_range = range(0,10)
    within_range = False
    
    #Check for two conditions in while loop
    #digit OR within_range == False
    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter a number (0-10): ") 
        #What the player writes will be checked. If it's not a digit, the while loop will keep running
        
        #digit check
        if choice.isdigit() == False:
            print("Sorry, that is not a valid input!") 
            #if it's not a digit, print out this line
        
        #range check 
        # (By the time it comes to this line, you are assuming choice.isdigit() == true)
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry, that is not a valid number!")
                within_range = False
    
        

    return int(choice)