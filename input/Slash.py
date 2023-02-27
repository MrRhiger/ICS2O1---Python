while (True):
    try:
        x = int(input("Please enter a number: "))
        while x <0:
            x = int(input("Please enter a positive number: "))
        break
    except ValueError:
        print("A number please")

for y in range(6):
    print(y)
else:
    print("done")








