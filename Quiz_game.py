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

    