def Scanner():
    while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("I said a number please.")
    return x

def area(x,y):
    size = x*y
    return size

x = Scanner()
y = Scanner()

print(area(x,y))

