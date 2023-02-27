grades = []

num = int(input("How many grades do you want to enter? "))

for x in range(num):
    mark = int(input("Enter grade (out of 100) "))
    grades.append(mark)

grades.sort()

print("The highest grade enter was: ", grades[len(grades)-1])