# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

#my answer
def summer_69(arr):
    sum_number = 0
    add_is_active = True
    
    for every_num in arr:
        if (every_num == 6):
            add_is_active = False
        elif (every_num == 9):
            add_is_active = True
        elif (add_is_active == True):
            sum_number = sum_number + every_num
    return sum_number


#optimised and given answer
def summer_69_better(arr):
    total = 0
    add = True
    
    for every_num in arr:
        while add: #if my add bool is true [First digit, so the bool is active]
            if every_num != 6: #if it's not 6 [eg. first digit is 3, so condition fulfilled]
                total += every_num #addon [adds on]
                break #get out of this while loop. Why? [It will keep adding on 3 over and over, thats why it needs to break]
            else: #if it ends up being 6, then stop this while loop
                add = False
    
        while not add: #while add is not active, run this loop
            if every_num != 9: #if the number isn't 9,
                break # get out of this and got to the next number in the array(via the for loop)
            else:
                add = True #if it is 9, the activate the bool,
                break #and break out of this number, so it can go to the next number.
                
    #note: the reason why while add loop is at the start, 
    # is because it has to check to see if there is a 6 first, 
    # to begin the bool cancellation.
    return total

# summer_69([1, 3, 5]) --> 9
print(summer_69_better([1, 3, 5]))

# summer_69([4, 5, 6, 7, 8, 9]) --> 9
print(summer_69_better([4, 5, 6, 7, 8, 9]))

# summer_69([2, 1, 6, 9, 11]) --> 14
print(summer_69_better([2, 1, 6, 9, 11]))