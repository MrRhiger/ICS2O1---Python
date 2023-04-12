import time

"""
Chris Rhiger
November 14th 2022
This is an introduction to inputting in python 
"""
counter = 0

while True:
    try:
        num1 = int(input("Please enter a number: "))
        break
    except ValueError:
        counter = counter + 1
        if (counter ==1):
            print("Silly head I said a number")
        elif (counter ==2):
            print("OK are you listening, I said a number")
        elif (counter ==3):
            print("Are you serious right now?")
        elif (counter > 3):
            print("Yep I am done, there is no hope for you")

print("Here is your number omg so cool: ", num1)

while True:
    try:
        num2 = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Silly head I said a number")