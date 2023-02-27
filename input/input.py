while(True):
    try:
        x = int(input("please enter a number: "))
        y = int(input("please enter a number: "))  
        z = int(input("please enter a number: ")) 
        break
    except ValueError:
        print("Please type a number not a letter")    



print("Your numbers are",x,y,z)

