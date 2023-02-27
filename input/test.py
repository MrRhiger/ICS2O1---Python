print("Welcome to Mr. Rhigers Average Machine")
print("Please enter you name and the 2 class marks. I will find the average")

name = input("What is your name: ")
mark1 = int(input("Please enter your first grade: "))
mark2 = int(input("Please enter your first grade: "))

average = (mark1 + mark2)/2

print("hello {0:1s} you entered {1:1d} and {2:1d} the final average is {3:1.2f}.".format(name,mark1,mark2,average))