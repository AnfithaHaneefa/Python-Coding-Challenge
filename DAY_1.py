
# Day 1: Division and Square-root

# Write a function called divide_or_square that takes one argument (a number), 
# and returns the square root of the number if it is divisible by 5, 
# returns its remainder if it is not divisible by 5.
# For example, if you pass 10 as an argument, then your function should return 3.16 as the square root.




def divide_or_square(n):

    return round(n**0.5,2) if n%5==0 else n%5


n=int(input("enter a number:"))

print(divide_or_square(n))