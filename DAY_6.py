# Day 6: User Name Generator

# Write a function called user_name that generates a username from the user's email.
# The code should ask the user to input an email and the code should return everything before the @ sign as their user name. 
# For example, if someone enters ben@gmail.com, the code should return ben as their user name.



def user_name(email):

    for i in range(len(email)-1):

        if email[i]=='@':

            return email[:i]
        
email=input('enter the mailID:')

print(user_name(email))