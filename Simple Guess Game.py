# Simple Guess Game
import random as rd

guessStart = 0 
numToguess = rd.randint(0,25)

print("Welcome to my Guess the number game.")
print("You'll have 10 tries to guess the correct number!")


for guessStart in range(10):
    userInput = int(input("Guess a number from 0 to 25:  "))

    if userInput < numToguess:
        print("Your number is too lower.. guess higher!")
    
    if userInput > numToguess:
        print("Your number is too high... guess lower!")
    
    if userInput == numToguess:
        break
    
if userInput != numToguess:
    print("No more tries! the number to guess was " + str(numToguess))

if userInput == numToguess:
    print("Congrats! you correctly guessed the number.")
