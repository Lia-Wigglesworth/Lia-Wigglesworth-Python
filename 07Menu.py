# functions
def main_Function(): # the main function into which the variable can be entered 
    print(" ------------------------------------------------")
    print("|                                                |")
    print("|    07Menu                                      |")
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

def other_Function():
    print("invalid option")

# main section of code
import os
os.system('cls')
main_Function()

while x != "x":
    while x == "1":
        start_Function()
        my_Function1()
        end_Function()
        main_Function()
    while x == "2":
        start_Function()
        my_Function2()
        end_Function()
        main_Function()
    while x == "3":
        start_Function()
        my_Function3()
        end_Function()
        main_Function()
    while x == "4":
        start_Function()
        my_Function4()
        end_Function()
        main_Function()
    while x == "5":
        start_Function()
        my_Function5()
        end_Function()
        main_Function()
    while x == "6":
        start_Function()
        my_Function6()
        end_Function()
        main_Function()
    while x != "1" and x != "2" and x != "3" and x != "4" and x != "5" and x != "6" and x != "x":
            start_Function()
            other_Function()
            end_Function()
            main_Function()
else: 
    my_Functionx()