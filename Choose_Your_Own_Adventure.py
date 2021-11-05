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
