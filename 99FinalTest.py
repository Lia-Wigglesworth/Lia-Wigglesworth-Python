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
    print("11. Encrypt a string")
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

    outFileName="C:\\Users\\pc\\Documents\\Y9\\9IST3\\Python Assessment Files\\encrypted_File.txt"
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
    with open("C:\\Users\\pc\\Documents\\Y9\\9IST3\\Python Assessment Files\\encrypted_File.txt") as encrypted_File: # reads the file the encrypted text is contained in
        characters = encrypted_File.read()
    my_Val = 1
    my_Function()
    form_Words()

    #checks for key words
    with open("C:\\Users\\pc\\Documents\\Y9\\9IST3\\Python Assessment Files\\word_List.txt") as dictionary: # reads the file the encrypted text is contained in
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
    if x != "1" and x != "2" and x != "3" and x != "4" and x != "5" and x != "6" and x != "7" and x != "8" and x != "9" and x != "x":
        start_Function()
        invalid_Function()
        end_Function()
        main_Function()
else: 
    my_Functionx()

