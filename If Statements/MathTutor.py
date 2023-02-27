answer = 67

guess = int(input("Please guess my number: "))

# == - is equal
# > - greater < -less
#>= greater than or equal to  <= less than or equal
# != - not symbol
# or and

if guess > 100 or guess < 10:
    print("You are very cold")
elif guess > 10 and guess <40:
    print("You are warm")
else:
    print("you are correct")
    