# functions
def my_Function1():
    print()
    print("----Start of Output ---------------------------")
    print()
    print("Hello World")
    print()
    print("----End of Output -----------------------------")
    print()
    print()
    print()
    input("Press Enter to continue")

def my_Function2():
    print()
    print("----Start of Output ---------------------------")
    print()
    print("Hello World")
    input("------> Program paused - press enter to continue")
    print("Goodbye World")
    print()
    print("----End of Output -----------------------------")
    print()
    print()
    print()
    input("Press Enter to continue")

def my_Function3():
    print()
    print("----Start of Output ---------------------------")
    print()
    print("Hello World")
    username = input("What is your name ? ")
    print("Goodbye " + username)
    print()
    print("----End of Output -----------------------------")
    print()
    print()
    print()
    input("Press Enter to continue")

def my_Function4():
    print()
    print("----Start of Output ---------------------------")
    print()
    teacherName = input("Teacher's name (try Mr Horan) ")
    if teacherName == "Mr Horan":
        print("You are lucky, he is a great teacher.")
    else:
        print(teacherName + " is an okay teacher")
    print()
    print("----End of Output -----------------------------")
    print()
    print()
    print()
    input("Press Enter to continue")

def my_Function5():
    print()
    print("----Start of Output ---------------------------")
    print()
    for x in range(1, 500):
        print(x)
    print()
    print("----End of Output -----------------------------")
    print()
    print()
    print()
    input("Press Enter to continue")

def my_Function6():
    print()
    print("----Start of Output ---------------------------")
    print()
    subjectName = input("What is the name of this subject ")
    while subjectName != "IST":
        print("Not Correct - try again")
        subjectName = input("What is the name of this subject ")
        if subjectName == "IST":
            break
    print()
    print("Congratulations!!")
    print()
    print()
    print()
    print("----End of Output -----------------------------")
    print()
    print()
    print()
    input("Press Enter to continue")

def my_Functionx():
    print()
    print("----Start of Output ---------------------------")
    print()
    print("invalid option")
    print()
    print("----End of Output -----------------------------")
    print()
    print()
    print()
    input("Press Enter to continue")

def my_Function():
    print()
    print("----Start of Output ---------------------------")
    print()
    print()
    print("----End of Output -----------------------------")
    print()
    print()
    print()
    input("Press Enter to continue")

# main section of code
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
x = input("Enter an option ")
if x == "1":
    my_Function1()
elif x == "2":
    my_Function2()
elif x == "3":
    my_Function3()
elif x == "4":
    my_Function4()
elif x == "5":
    my_Function5()
elif x == "6":
    my_Function6()
elif x == "x":
    my_Functionx()
else:
    my_Function()