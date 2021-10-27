print(" ------------------------------------------------")
print("|                                                |")
print("|    06whileLoop                                 |")
print("|    Name : Lia Wigglesworth                     |")
print("|    Version : 01                                |")
print("|                                                |") 
print(" ------------------------------------------------")
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