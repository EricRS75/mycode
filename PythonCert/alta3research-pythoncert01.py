#!/usr/bin/python3
"""This program is meant to be a triva game written
by Eric R. Schechter for a Python certification"""

import re
import os
import crayons
from random import randint

def main():
    #Clearing the screen
    os.system('clear')
    #Inital title
    print(crayons.yellow("This is a trivia game drawing from a broad list of categories."))
    #Entering the name of the player    
    name = input("Please enter your name: ")
    # The variable i is meant to be the number of questions available
    i = 0
    #Loading all questions into memory and counting them
    with open('TrivaQuestions.txt', 'r') as game_data:
        myQuestions =  []
        questions = game_data.readlines()
        for question in questions:
            i = i + 1
            myQuestions.append(question)
    print(crayons.yellow(f"Ok {name}, there are a total of {i} possible questions available to you."))
    
    number = int(input("How many would you like to take? "))
    correct = 0
    for g in range(number):
        #Grab a question at random from the stack
        ask = (myQuestions[(randint(1,i))])
        #Split the string into the question and answers
        quest = list(re.findall('"([^"]*)"', ask))

        #Setting the numberi and the title for the question
        level = g + 1 
        print(crayons.blue(f"Question {level} of {number}"))
        #printing out the question
        print (quest[0])
        #Possible is the number of possible answers
        possible = len(quest)-1
        #print(crayons.blue(f"There are {possible} possible answer(s)"))
           
        response = input(crayons.blue(">"))      
        #Checking for the answer in the range if there is more than one acceptablw
        if (response in quest):
            #Answer is correct
            print(crayons.green("Correct"))
            print(" ")
            #Number of correct is incremented
            correct = correct + 1
        else:
            #Answer was incorrect
            print(crayons.red("Incorrect -  The answer(s) is: "))
            #Print answer here
            for a in (n+1 for n in range(possible)):
                print(crayons.red(quest[a]))
            print(" ")
            

    #Final Output
    print(crayons.yellow(f"Ok {name}, you got {correct} question(s) correct out of {number}."))
    print(f"Your final score is: ",  end='')
    score = (correct/number)*100
    print(score, end='')
    print("%")

    print("Your game has been logged")


# Calling the main function
main()
