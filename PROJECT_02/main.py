# Write a program that generates the randoom number and aks user to guess it
# if the player guess the number greater than it it prints "Lower number Please",if player guess the lower number it asks player for a greater number.
# When the player guess the correct number ,the program displays the number of attempts to reach the correct number

import random

n=random.randint(1,100)
a=-1
guesses=0
while a!=n:

    guesses=guesses+1
    a=int(input("Guess a Number:"))

    if(a<n):
        print("Enter the Greater Number")
    elif(a>n):    
        print("Enter the Smaller Number")
    elif(a==n):
        print("Congratulations!! , You have Guessed it Correctly")    

print(f"You have guessed in {guesses} times")