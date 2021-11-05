# Note: for the options 10 and 11, I have not altered them to fit in the menu, so it is likely that for option 11 the output 
# "No keywords found" will be generated. The actual code is titled 'Decryption'.

# functions
def main_Function(): # the main function into which the variable can be entered 
    print(" ------------------------------------------------")
    print("|                                                |")
    print("|    Final Test                                  |")
    print("|    Name : Lia Wigglesworth                     |")
    print("|    Version : 01                                |")
    print("|                                                |") 
    print(" ------------------------------------------------")

    print("1. Hello World")
    print("2. Goodbye World")
    print("3. Goodbye Person")
    print("4. Good Teacher")
    print("5. forLoop")
    print("6. whileLoop")
    print("7. string Loop")
    print("8. Convert to ascii")
    print("9. Encode a string")
    print("10. Encrypt a string")
    print("11. Decrypt a string")
    print("12. Quiz Game")
    print("13. Hangman")
    print("14. Choose Your Own Adventure")

    print("x. To Exit")
    global x
    x = input("Enter an option ")

def start_Function():
    print()
    print("----Start of Output ---------------------------")
    print()

def end_Function():
    print()
    print("----End of Output -----------------------------")
    print()
    print()
    print()
    input("Press Enter to continue")
    os.system('cls')

#the functions for the different options
def my_Function1():
    print("Hello World")

def my_Function2():
    print("Hello World")
    input("------> Program paused - press enter to continue")
    print("Goodbye World")

def my_Function3():
    print("Hello World")
    username = input("What is your name ? ")
    print("Goodbye " + username)

def my_Function4():
    teacherName = input("Teacher's name (try Mr Horan) ")
    if teacherName == "Mr Horan":
        print("You are lucky, he is a great teacher.")
    else:
        print(teacherName + " is an okay teacher")

def my_Function5():
    for x in range(1, 500):
        print(x)

def my_Function6():
    subjectName = input("What is the name of this subject ")
    while subjectName != "IST":
        print("Not Correct - try again")
        subjectName = input("What is the name of this subject ")
        if subjectName == "IST":
            break
    print()
    print()
    print("Congratulations!!")
    print()
    print()

def my_Function7():
    string = input("What is your string? ")
    for x in string:
        print (x)

def my_Function8():
    string = input("What is your string? ")
    for x in string:
        print(x, " = ", ord(x))

def my_Function9():
    string = input("What is your string? ")
    new_string  = [""]

    for x in string:
        y = chr(ord(x) + 1)
        new_string.append(y)
        print(x + "=" + y)
        print(*new_string, sep = "")

def my_Function10():
    characters = []
    import random

    text = input("Enter text to be encrypted here: ")
    random_Number = random.randint(1,4)
    for x in text:
        x = chr(ord(x) + random_Number)
        characters.append(x)
    beginning_Char = " ".join(characters[::2])
    end_Char = " ".join(characters[1::2])
    print(beginning_Char + " " + end_Char)

    outFileName="C:\\Users\\pc\\Documents\\Y9\\9IST3\\Python Assessment Files\\Text_Files\\encrypted_File.txt"
    outFile=open(outFileName, "w")
    outFile.write(beginning_Char + " " + end_Char)
    outFile.close() 

def my_Function11():
    # definition of lists used in code
    list = []
    final_characters = []
    beginning_characters = []
    decrypted_Code = []
    word_List = ["Hi", "hi", "Hello", "hello", "My", "my", "name", "is", "Lia", "Horan", "The" "the", "goodbye", "bye", "and", "this", "thank", "you"]

    # main function of code
    def my_Function():
        # clears the lists for when function is looped
        decrypted_Code.clear()
        list.clear()
        final_characters.clear()
        beginning_characters.clear()
        # changes the character by a certain amount and adds it to a list
        for y in characters:
            y = chr(ord(y) - my_Val)
            list.append(y)
        list2 = list[::2] # places every second value into another list
        x = (len(list2)) # finds the number of characters in this list
        # splits the text into two parts depending on if it is even or odd
        if (x % 2) != 0:
            final_characters.extend(list2[int(x/2+1):])
            beginning_characters.extend(list2[:int(x/2+1)])
            final_characters.append(" ")
        else:
            final_characters.extend(list2[int(x/2):])
            beginning_characters.extend(list2[:int(x/2)])
        a = 0 # the list item number
        char_Count = (len(beginning_characters)) # the number of characters in the first half
        while char_Count > 0: # loops through the two groups the encrypted text has been sorted into and alternates them to form a new order
            b = (beginning_characters[a] + final_characters[a])
            decrypted_Code.extend(b)
            a = a + 1
            char_Count = char_Count - 1 # using the number of characters it repeats until they have all be recorded

    def form_Words():
        a = 0 
        decrypted_Code.extend(" ") # add space to the end of decrypted code so that words can be seperated
        while decrypted_Code.count(" ") != 0:  # while there are spaces in the decrypted code 
            space = decrypted_Code.index(' ')
            decrypted_Code[a:space] = [''.join(decrypted_Code[a:space])] # merges everything up the space into one word
            decrypted_Code.remove(" ")
            a = a + 1

    def check_Words(): # identifies specific English words
        global words_Indentified
        words_Indentified = 0
        for x in decrypted_Code:
            if x in word_List:
                words_Indentified = words_Indentified + 1

    # main section of code
    with open("C:\\Users\\pc\\Documents\\Y9\\9IST3\\Python Assessment Files\\Text_Files\\encrypted_File.txt") as encrypted_File: # reads the file the encrypted text is contained in
        characters = encrypted_File.read()
    my_Val = 1
    my_Function()
    form_Words()

    #checks for key words
    with open("C:\\Users\\pc\\Documents\\Y9\\9IST3\\Python Assessment Files\\Text_Files\\word_List.txt") as dictionary: # reads the file the encrypted text is contained in
        for line in dictionary:
            word_List.extend(line)
            a = 0 
        word_List.extend("\n") # add a line break to end so that words can be seperated
        while word_List.count("\n") != 0:  # while there are line breaks in the word list
            linebreak = word_List.index('\n')
            word_List[a:linebreak] = [''.join(word_List[a:linebreak])] # merges everything up the space into one word
            word_List.remove("\n")
            a = a + 1
    words_Indentified = 0
    check_Words() 

    # indentifies the correct option
    while words_Indentified < 1: 
        my_Val = my_Val + 1
        my_Function()
        form_Words()
        check_Words()
        if my_Val > 5:
            print("No keywords were found")
            import sys
            sys.exit()
    print(*decrypted_Code)

def my_Function12():
    questions = ["What is the largest freshwater lake in the world?", "What is someone who shoes horses called?", "What is another word for lexicon?", "What is the world's biggest island?", "What is the world's largest ocean?", "What is the world's longest river?", "What is the capital city of Spain?", "Which actress has won the most Oscars?"]
    answers = ["Lake Superior", "Farrier", "Dictionary", "Greenland", "Pacific", "Nile", "Madrid", "Katharine Hepburn"]
    comments  = ["", "", "", " (As a continent, Australia is technically not considered an island.)", "", " (The Amazon is the largest by volume.)", "", " (with four Oscars and 12 total nominations)"]

    import random
    user_Score = 0
    total_Score = 0

    while questions != 0:
        x = random.randint(0,7) # generates random number
        user_Answer = input("Q" + str(total_Score + 1) + ": " + questions[x] + " ") # prints question and receives input
        if user_Answer == answers[x]: # if answer it correct:
            print()
            print("Correct!!" + comments[x])
            print()
            user_Score = user_Score + 1
            total_Score = total_Score + 1
        elif user_Answer == "": # if question was skipped
            print()
            print("Question skipped")
            input("A: " + answers[x] + " ")
            print()
        else: # if question was incorrect
            print()
            print("Incorrect :(")
            input("A: " + answers[x] + " ")
            print()
            total_Score = total_Score + 1
        # option to continue the game 
        continue_Option = input("Do you want to continue playing? ")
        if continue_Option == "No":
            print("Thank you for playing!")
            print("Your score was", user_Score , "/", total_Score)
            break
        elif continue_Option == "no":
            print()
            print("Thank you for playing!")
            print("Your score was", user_Score , "/", total_Score)
            print()
            break

def my_Function13():
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
    print(" O   O ")
    print("/|\\ /|\\")
    print(" /\\ /\\")
    print()
    print("The word is ", *printed_Letters, sep = '')
    print()

def my_Function14():
    # functions
    def part1():
        print("It is summertime again, vacation time. You go to your uncle's house. He takes you on a tour around the city. There are many old buildings, but the oldest of all is on Main Street. The address is 880. He says that it is haunted, but you don't believe him.")
        print("What action do you take? ")
        print("1. Go inside")
        print("2. Stay there")
        option = input()
        if option == "1":
            part2()
        else:
            part3()
    def part2():
        print("You say, 'I will go inside.' He says, 'I want to watch you.' You start up the stone steps of the old haunted house. You open the door and step inside and suddenly a sharp arrow streaks across in front of you! But it misses you.")
        print("What action do you take? ")
        print("1. Go up the staircase")
        print("2. Go through the swinging doors")
        option = input()
        if option == "1":
            part4()
        else:
            part5()
    def part3():
        print("You stay there. Then you decide to go home, have an ice cream, and go to bed.")
    def part4():
        print("You go up the stairs. You lean against the railing and it breaks. You fall and that's the end of you.")
    def part5():
        print("You go through the swinging doors. You walk through the room.")
        print("What action do you take? ")
        print("1. Go to the closet")
        print("2. Go into a passageway under the house?")
        option = input()
        if option == "1":
            part6()
        else:
            part7()
    def part6():
        print("You go into the closet. You fall through a trapdoor and break your leg. The walls are too smooth to climb. There is no other way up.")
    def part7():
        print("You go into a pasaageway under the house. You make your way along and it leads to a trapdoor that takes you back to where you started from. You meet a policeman at the top and he says to you, 'You were lucky to get out of there. Don't ever go in there again!' You go home and have some ice cream.")

    # main code
    import sys
    import os

    print("The Mystery of the Haunted House, By Paul Channel")
    print()
    part1()
    print()
    reset = input("Would you like to try again? ")
    if reset == "Yes":
        os.system('cls')
        part1()
    else:
        sys.exit()

def my_Functionx():
    print()
    print("----Start of Output ---------------------------")
    print()
    print()
    print("----End of Output -----------------------------")
    print()
    print()
    print()
    input("Press Enter to continue")

def invalid_Function():
    print("invalid option")

# main section of code
import os
os.system('cls')
main_Function()

while x != "x":
    if x == "1":
        start_Function()
        my_Function1()
        end_Function()
        main_Function()
    if x == "2":
        start_Function()
        my_Function2()
        end_Function()
        main_Function()
    if x == "3":
        start_Function()
        my_Function3()
        end_Function()
        main_Function()
    if x == "4":
        start_Function()
        my_Function4()
        end_Function()
        main_Function()
    if x == "5":
        start_Function()
        my_Function5()
        end_Function()
        main_Function()
    if x == "6":
        start_Function()
        my_Function6()
        end_Function()
        main_Function()
    if x == "7":
        start_Function()
        my_Function7()
        end_Function()
        main_Function()
    if x == "8":
        start_Function()
        my_Function8()
        end_Function()
        main_Function()
    if x == "9":
        start_Function()
        my_Function9()
        end_Function()
        main_Function()
    if x == "10":
        start_Function()
        my_Function10()
        end_Function()
        main_Function()
    if x == "11":
        start_Function()
        my_Function11()
        end_Function()
        main_Function()
    if x == "12":
        start_Function()
        my_Function12()
        end_Function()
        main_Function()
    if x == "13":
        start_Function()
        my_Function13()
        end_Function()
        main_Function()
    if x == "14":
        start_Function()
        my_Function14()
        end_Function()
        main_Function()
    if x != "1" and x != "2" and x != "3" and x != "4" and x != "5" and x != "6" and x != "7" and x != "8" and x != "9" and x != "10" and x != "11" and x != "12" and x != "13" and x != "14" and x != "x":
        start_Function()
        invalid_Function()
        end_Function()
        main_Function()
else: 
    my_Functionx()

