
# Day 2: Strings to Integers

# Write a function called convert_add that takes a list of strings as an argument
# and converts it to integers and sums the list. 
# For example ['1', '3', '5'] should be converted to [1, 3, 5] and summed to 9.



def convert_add(list_string):
    
    return sum(map(int,list_string))

list_string=input('enter the number : ').split()
print(convert_add(list_string))

