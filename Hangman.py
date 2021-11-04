# definitions of lists used in code 
letters = []
printed_Letters = []
incorrect_Guess = []
easy_word_List = ["Grape", "One", "Hi"]
medium_word_List = ["Coding", "Hangman", "Python"]
hard_word_List = ["Prosperity", "Kingdom", "Characters"]

import os
import sys
import random

# introduction section
print(" "*48, "-"*11)
print(" "*50, "Hangman")
print(" "*48, "-"*11)
print("Instructions:")
print("Guess the letters in the secret word to solve the puzzle by typing in different characters on your keyboard.")
print("You will be able to choose the number of different tries to guess all the characters in the word. This number ")
print("includes repeated characters. The difficulty can also be chosen. The default value is medium. ")
print()

# selecting from different modes
game_Mode = input("Would you like to play in single player mode? (Yes/No) ")
if game_Mode == "Yes" or "yes":
    print()
    game_Setting = input("Select difficulty (Easy/Medium/Hard) ")
    if game_Setting == "Easy":
        word = easy_word_List[random.randint(0,2)]
    if game_Setting == "Medium":
        word = medium_word_List[random.randint(0,2)]
    if game_Setting == "Hard":
        word = hard_word_List[random.randint(0,2)]
    else:
        print("Difficutly has been set to default value")
        word = medium_word_List[random.randint(0,2)]
    guess_Number = int(input("Choose a number of possible guesses (5-50) "))
    if guess_Number > 50 or guess_Number < 5:
        print("Number of guesses has been set to default value")
        guess_Number == 15
    print()
    input("Press enter to continue")
elif game_Mode == "No" or "no":
    guess_Number = 15
    print()
    word = input("Player 1: Type the word that will be guessed: ")
    print()
    input("Player 2 press enter to continue")

for x in word:
    x = x.lower() # shifts all characters to lower case 
    letters.extend(x) # adds individial letters to list
printed_Letters.extend('_'*len(letters)) # adds dashes to another list

while printed_Letters.count("_") != 0: # while there are still dashes in printed_List (all letters haven't been found)
    # clear the screen and then print the guessed letters and incorrect guesses
    os.system('cls') 
    print(*printed_Letters)
    print()
    print(" "+"-"*15)
    print(*incorrect_Guess)
    print(" "+"-"*15)
    print()
    guess = input("Guess a letter: ")
    guess = guess.lower()
    guess_Number = guess_Number - 1 # decreases the number of tries remaining by one
    # if there are no more tries remaining
    if guess_Number == -1:
        os.system('cls')
        print("You have failed. Word was:", word)
        sys.exit()
    for x in guess:
        if letters.count(x) == 0 and printed_Letters.count(x) == 0: # if the letter isn't in original list or printed list 
            # if the value has not already been attempted
            if incorrect_Guess.count(x) == 0: 
                input("Letter is not in the word")
                print("You have", guess_Number, "tries remaining")
                input()
                incorrect_Guess.extend(x) # add it to incorrect guess list 
                os.system('cls')
            # if the value has been attempted
            else:
                input("This value has been attempted before")
                print("You have", guess_Number, "tries remaining")
                input()
                os.system('cls')
        if printed_Letters.count(x) != 0 and letters.count(x) == 0: # if the letter is in the word but has already been tried
            input("This letter has been attempted before")
            print("You have", guess_Number, "tries remaining")
            input()
            os.system('cls')
        while letters.count(x) != 0: # if the letter hasn't been attempted and is correct
            letter_Number = letters.index(x) # find its position in the list
            printed_Letters[letter_Number] = letters[letter_Number] # change the value of one of the printed values into the letter
            letters[letter_Number] = ""
            os.system('cls')
# If all letters have been guessed 
print()
print("~ Congratulations ~")
print()
print("The word is ", *printed_Letters, sep = '')
print()





            
            