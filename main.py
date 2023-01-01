#importing the random module
import random

#creating a list of characters to choose from
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"

#creating an empty string to store the password
password = ""

#asking the user for the length of the password they want to generate 
length = int(input("How long do you want your password to be? "))

#using a for loop to generate a random character from the list and add it to the empty string 
for i in range(length): 
    password += random.choice(characters) 

 #printing out the generated password  
print("Your new password is:",password)