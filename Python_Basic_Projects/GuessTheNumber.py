# GuessTheNumber.py
# Purpose: Use random module, for loop or any loop
# Program: Generate randowm number, Ask user to guess the user input
#Pseudocode
""" Randomly assign the value to variable
 Let user give the input 
 Check if the number is within a given range
 Compare the input with the given variable and let user know how close he is 
 Keep the counter for the number of guesses 
 End the program after the Guess is right """

import random
var=random.randint(1,7)
print(var)
guesscount=1
print('I am thinking of a number between 1 & 20')
for i in range(1,20):
    print('Take a guess')
    userinput=int(input())
    if userinput>20 or userinput<1:
        print('Wrong input: You need to selct the number between 1 and 20')
    elif userinput>var:
        print('your guess is too high')
    elif userinput<var:
        print('your guess is too low')
    elif userinput==var:
        print('your guess us correct')
        print('Good job! You guessed my number in '+ str(guesscount)+' guesses!')
        break
    guesscount+=1