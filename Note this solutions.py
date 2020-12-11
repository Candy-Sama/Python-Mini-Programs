#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False



#my answer
def spy_game(nums):
    check_one = False
    check_two = False
    
    for every_num in nums:
        if (every_num == 0 and check_one == True):
            check_two = True
        elif (every_num == 0):
            check_one = True
        elif (every_num == 7 and check_one == True and check_two == True):
            return True
        elif (check_one == True or check_two == True):
            pass
        else:
            check_one = False
            check_two = False
    return False


#solution given
def spy_game_better(num):
    code = [0,0,7,'x']
    
    for every_num in num:
        if every_num == code[0]:
            code.pop(0)
            
    return len(code) == 1

# spy_game([1,2,4,0,0,7,5]) --> True
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game_better([1,2,4,0,0,7,5]))

# spy_game([1,0,2,4,0,5,7]) --> True
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game_better([1,0,2,4,0,5,7]))

# spy_game([1,7,2,0,4,5,0]) --> False
print(spy_game([1,7,2,0,4,5,0]))
print(spy_game_better([1,7,2,0,4,5,0]))
