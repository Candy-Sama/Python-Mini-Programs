list_of_numbers = [1,2,3,4,5,6]
program_is_running = True

#function to check to see if it returns true if any number in the list is even
def check_even(list_to_check):
    for each_num in list_to_check:
        if (each_num % 2 == 0):
            return True
        
#function to check to see if there's one specific or many numbers in the list is even
def check_even_list(list_to_check):
    even_number_list = []
    for each_num in list_to_check:
        if (each_num % 2 == 0):
            even_number_list.append(each_num)
    return even_number_list

#function to return a list of value-bools instead in a dictionary
def check_even_list_return_dict(list_to_check):
    even_number_dict = {}
    
    for each_num in list_to_check:
        if (each_num % 2 == 0):
            even_number_dict[f"{each_num}"] = "Even"
        else:
            even_number_dict[f"{each_num}"] = "Odd"
    return even_number_dict


print(f"Welcome to this simple program \nYou have this list {list_of_numbers}. \nYou have 3 options: \n1 - Check to see if there any even number in this list \n2 - Show all the even numbers \n3 - Show every number and see if each one is even or odd")

while program_is_running:
    player_input = input("Please write your option number here. Type Exit to exit. Your command? (1,2,3 or Exit): ")
    options = "You have 3 options: \n1 - Check to see if there any even number in this list \n2 - Show all the even numbers \n3 - Show every number and see if each one is even or odd"

    if (player_input.lower() == 'exit'): #ensures that the string will always be lowercase to match the if condition
        print('Program will now exit')
        program_is_running = False
    else:
        player_input = int(player_input)
        if (player_input == 1):
            result = check_even(list_of_numbers)
            print (result)
            print (options)
        elif (player_input == 2):
            result2 = check_even_list(list_of_numbers)

            for each_even_number in result2:
                print (each_even_number)
            
            print(f"The even numbers are {result2}")

            print (options)

            
        elif (player_input == 3):
            result3 = check_even_list_return_dict(list_of_numbers)
            for x,y in result3.items():
                print(f"{x} is the number, therefore it is {y}")

            print (options)



