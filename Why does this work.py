"""def myfunc(*args):
    mylist = []
    x = len(args)
    for x in args:
        if (x%2 == 0):
            mylist.append(x)
    return mylist"""

#why does this work?
#problem 1: I thought tuples = list of (). In actuality tuples is () itself
"""
def myfunc(string):
    x = 0
    newstring = ''
    for every_letter in string:
        x += 1
        if ((x%2) != 0):
            every_letter = every_letter.upper()
            newstring += every_letter
        else:
            newstring += every_letter
    
    return newstring
"""
def myfunc(string):
    counter = 0
    newstring = ''
    for every_letter in string:
        counter += 1 
        if counter %2 == 0:
            newstring += every_letter.lower()
        else:
            newstring += every_letter.upper()
              
    return newstring

print(myfunc('hello'))
