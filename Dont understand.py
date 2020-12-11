def count_primes_better(max_num): #[input = 25]
    # Check to see if it's 0 or 1 as input
    if max_num < 2: 
        return 0
    
    # otherwise, if it's 2 or greater
    
    primes = [2] #list to store our primes. Since we know 2 is already a prime, add it in
    
    # x is a counter to use when going up to the inputted num
    # Reason why we start at 3, and using 2 inside the list, 
    # is that we start with an odd number
    # Even numbers are divisible by 2, so they aren't prime num by default
    x = 3
    
    # while x is going thru every odd number up to input num
    while x <= max_num: #Start at 3 because if input num is 2, this while loop will fail, and since we have 2 inside the list nothing changed 
        # Check if x is prime first
        for y in range(3,x,2): # y is a possible multiple of x essentially, start at 3 because even numbers are not necessary  
                               # y will list out values from 3 to x (excluding x and even numbers between 3 to x) that will try to divide x
                               # odd numbers cannot be divided by even numbers, that's why they are excuded from the possible values of y
                               
            if x%y == 0: #if x is divisible by y, then it's not a prime number
                x += 2 #because we started from an odd number, we can just + 2 to go to the next odd number
                break
        else: #this else can be use with for loops because ONLY python allows it, take note!
            primes.append(x)
            x += 2 #same reasoning as above: because started from an odd num, we can skip the even number
    
    print(primes) #for debugging
    return len(primes)

"""
let say max_num = 7

first loop
x = 3
y = 0

2nd loop
x = 5
y = 3

3rd loop
x = 7
y = 3, 5
"""