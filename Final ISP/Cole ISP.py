import time
import msvcrt
from sys import exit
import os
import random
"""
cole hoover
january 10
battle simulator
"""

#ADDING METHODS FOR LATER

def cls():
    os.system("cls")
cls()

def gameover():
    print("┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼")
    print("███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀")
    print("██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼")
    print("██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀")
    print("██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼")
    print("███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄")
    print("┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼")
    print("███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼")
    print("██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼")
    print("██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼")
    print("██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼")
    print("███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄")
    print("┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼")
    print("┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼")
    print("┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼")
    print("┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼")
    print("┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼")
    print("┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼")
    print("┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼")
    print("┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼")
    print("┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼")
    print("┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼")
    print("┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼")
    print("┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼")
    print("┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼")

def clown1():
    print("            @-.              ")
    print("           _  )\\  _         ")
    print("          / \/ | \/ \        ")
    print("         @/`|/\/\/|`\@       ")
    print("            /~~~~~\          ")
    print("           |  ^ ^  |         ")
    print("           |   .   |         ")
    print("           | (\_/) |         ")
    print("        .- -\ \_/ /- -.      ")
    print("       / .-. \___/ .-. \     ")
    print("      @/` /.-.   .-.\ `\@    ")
    print("         @`   \ /   `@       ")
    print("               @             ")

def clown2():
    print("             _                   ")
    print("          (_)          _         ")
    print("          _         .=.   (_)    ")
    print("     (_)   _   //(`)_            ")
    print("          //`\/ |\ 0`\\          ")
    print("          ||-.\_|_/.-||          ")
    print("          )/ |_____| \(    _     ")
    print("         0   #/\ /\#  0   (_)    ")
    print("            _| o o |_            ")
    print("     _     ((|, ^ ,|))           ")
    print("    (_)     `||\_/||`            ")
    print("             || _ ||      _      ")
    print("             | \_/ |     (_)     ")
    print("         0.__.\   /.__.0         ")
    print("          `._  ` `  _.'          ")
    print("              / ;  \ \           ")
    print("           0'-' )/`'-0           ")
    print("               0`                ")

#telling user to put it in full screen

print("Please put console in full screen.")
ans = str(input("ARE YOU READY? (YEAH/NAH): "))
ans = ans.lower()
if ans == "yeah":
    print("Then lets get started...")
elif ans == "nah":
    print("well.. fine then bye")
    time.sleep(2)
    exit()
else:
    exit()
time.sleep(3)
cls()

#intro

print("█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█ ")
print("▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█ ▄ ▄ ▄")
print()
time.sleep(0.5)
print(" █▄▀ █ █▄░█ █▀▀   █▀█ █▀▀   ▀█▀ █░█ █▀▀   █▄░█ █▀▀ █▀▀ █▄▀ █░░ ▄▀█ █▀▀ █▀▀ █▀")
print(" █░█ █ █░▀█ █▄█   █▄█ █▀░   ░█░ █▀█ ██▄   █░▀█ ██▄ █▄▄ █░█ █▄▄ █▀█ █▄▄ ██▄ ▄█")
time.sleep(2)

#animation


print("%0s%30s" %("웃", "🎪"))
time.sleep(0.5)
cls()

print("%3s%27s" %("웃", "🎪"))
time.sleep(0.5)
cls()

print("%6s%24s" %("웃", "🎪"))
time.sleep(0.5)
cls()

print("%9s%21s" %("웃", "🎪"))
time.sleep(0.5)
cls()

print("%12s%18s" %("웃", "🎪"))
time.sleep(0.5)
cls()

print("%15s%15s" %("웃", "🎪"))
time.sleep(0.5)
cls()

print("%18s%12s" %("웃", "🎪"))
time.sleep(0.5)
cls()

print("%21s%9s" %("웃", "🎪"))
time.sleep(0.5)
cls()

print("%24s%6s" %("웃", "🎪"))
time.sleep(0.5)
cls()

print("%27s%3s" %("웃", "🎪"))
time.sleep(0.5)
cls()

print("%29s%1s" %("웃", "🎪"))
time.sleep(0.5)


#Ask user what they wanna do 

ans1 = str(input("Do you want to explore the circus? (yes/no):  "))
ans1 = ans1.lower()
cls()

if ans1 == "yes":
    print("You enter the spooky circus tent...")
    time.sleep(1)
    cls()
elif ans1 == "no":
    gameover()
    print("You died of heart attack")
    exit()
else:
    print("Please enter yes or no")
    exit()

#First fight introduced 

time.sleep(1)
print("█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀ ")
print("▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄ ")
print()
time.sleep(1)
print("  ▀█▀ █▀█   █▀▄▀█ █▄█   █░░ ▄▀█ █ █▀█")
print("  ░█░ █▄█   █░▀░█ ░█░   █▄▄ █▀█ █ █▀▄")
print()
time.sleep(1)
print("█  █░░ █░░   ▀█▀ █░█ █▀█ █▄░█   █▄█ █▀█ █░█   █ █▄░█ ▀█▀ █▀█   ")
print("█  █▄▄ █▄▄   ░█░ █▄█ █▀▄ █░▀█   ░█░ █▄█ █▄█   █ █░▀█ ░█░ █▄█ ▄ ▄ ▄  ")
print()
time.sleep(1.5)
print("█▀█ █▄░█ █▀▀   █▀█ █▀▀   █▀▄▀█ █▄█   █▀▀ █░░ █▀█ █░█░█ █▄░█ █▀ ")
print("█▄█ █░▀█ ██▄   █▄█ █▀░   █░▀░█ ░█░   █▄▄ █▄▄ █▄█ ▀▄▀▄▀ █░▀█ ▄█ ")
time.sleep(1)

for x in range (1,4):
    cls()
    clown1()

    print("\t█░█ ▄▀█")
    print("\t█▀█ █▀█")
    time.sleep(0.5)
    cls()

    clown2()

    print("\t█░█ ▄▀█")
    print("\t█▀█ █▀█")
    time.sleep(0.5)

#asking user if they want to fight

ans2 = str(input("Do you want to fight or run away? (fight/run): "))
ans2 = ans2.lower()

if ans2 == "fight":
    cls()
    time.sleep(0.5)
    print("Clown boss: So you wanna fight huh?")
    time.sleep(2)
    print("You: yeah")
    time.sleep(2)
    print("Clown boss: Well first you're going to have to go through my minions...")
    time.sleep(2)
    cls()
elif ans2 == "run":
    cls()
    print("You ran away")
    time.sleep(2)
    print("But tripped on a stick and died...")
    gameover()
    exit()
else:
    cls()
    print("please type 'fight' or 'Run'")
    exit()
cls()

print("\t\t\t3️⃣")
time.sleep(0.5)
print("\t\t\t2️⃣")
time.sleep(0.5)
print("\t\t\t1️⃣")
time.sleep(0.5)
print("\t\t█▀▀ █ █▀▀ █░█ ▀█▀ ")
print("\t\t█▀░ █ █▄█ █▀█ ░█░ ")
print()
print()
time.sleep(1)

#FIRST FIGHT

#GENERATES YOUR AND ENEMY HEALTH

YourHealth = random.randint(70,100)
ClownArmyHealth = random.randint(35,50)

while YourHealth >0 and ClownArmyHealth >0:
    #Prints Your and Clown army health
    cls()
    print("\t\tYou:\t\tClown Army:")
    print("%21s%1s%17s%1s" %("Health: ", YourHealth, "Health: ", ClownArmyHealth))

    print("\t\t웃""\t\t🤡🤡🤡🤡🤡🤡")

    #Ask for user choice

    ans3 = str(input("\nWhat do you do? (Attack/Defend/Run): "))
    ans3 = ans3.lower()
    time.sleep(0.5)
    
    #If user picks attack, run

    if ans3 == "attack":

        #generates random attacks

        attack1 = random.randint(15,30)
        ClownArmyHealth = ClownArmyHealth - attack1

        clownattack1 = random.randint(15,30)
        YourHealth = YourHealth - clownattack1

        #displays message with corosponding attack strength
        if attack1 >=15 and attack1 <20:
            print("\nYou lobbed a pebble at them, small attack")
            print("Minus", attack1, "Health!!")
        

        elif attack1 >=20 and attack1 <25:
            print("\nYou tossed a rock at them, medium attack")
            print("Minus", attack1, "Health!!")

        elif attack1 >25 and attack1 <31:
            print("\nYou wipped a bolder at them, big attack")
            print("Minus", attack1, "Health!!")

        time.sleep(1)

        if clownattack1 >=15 and clownattack1 <20:
            print("\nThey threw pies at you, small attack")
            print("Minus", clownattack1, "Health!!")
            
        elif clownattack1 >=20 and clownattack1 <25:
            print("\nThey lauched juggling balls at you, medium attack")
            print("Minus", clownattack1, "Health!!")

        elif clownattack1 >25 and clownattack1 <31:
            print("\nThey launched themselves at you with canons, big attack")
            print("Minus", clownattack1, "Health!!")

        time.sleep(3.75)

    #If user picks defend, run

    elif ans3 == "defend":

        #generates attacks

        attack1 = random.randint(5,17)
        ClownArmyHealth = ClownArmyHealth - attack1

        clownattack1 = random.randint(0,20)
        YourHealth = YourHealth - clownattack1

        #displays message with corosponding attack strength

        if attack1 >=5 and attack1 <10:
            print("\nYou push them while defending, little damage")
            print("Minus", attack1, "Health!!")
        

        elif attack1 >=10 and attack1 <=17:
            print("\nYou charge them while defending, big damage")
            print("Minus", attack1, "Health!!")

        time.sleep(1)


        if clownattack1 == 0:
            print("\nYou blocked their attack!")
            print("Minus", clownattack1, "Health!!!")
            
        elif clownattack1 >=1 and clownattack1 <10:
            print("\nYou kinda blocked their attack!")
            print("Minus", clownattack1, "Health!!")

        elif clownattack1 >=10 and clownattack1 <20:
            print("\nYou barely blocked their attack")
            print("Minus", clownattack1, "Health!!")

        time.sleep(3.75)

    #If user picks run, run

    #RUN ANIMATION
    elif ans3 == "run":
        print("%15s%15s" %("웃", "🤡🤡🤡🤡🤡🤡"))
        time.sleep(0.5)
        cls()

        print("%14s%14s" %("웃", "🤡🤡🤡🤡🤡🤡"))
        time.sleep(0.5)
        cls()

        print("%13s%10s" %("웃", "🤡🤡🤡🤡🤡🤡"))
        time.sleep(0.5)
        cls()

        print("%12s%8s" %("웃", "🤡🤡🤡🤡🤡🤡"))
        time.sleep(0.5)
        cls()

        print("%12s%6s" %("웃", "🤡🤡🤡🤡🤡🤡"))
        time.sleep(0.5)
        cls()

        print("%11s%4s" %("웃", "🤡🤡🤡🤡🤡🤡"))
        time.sleep(0.5)
        cls()

        print("%10s%2s" %("웃", "🤡🤡🤡🤡🤡🤡"))
        time.sleep(0.5)
        cls()

        print("%8s%1s" %("웃", "🤡🤡🤡🤡🤡🤡"))
        time.sleep(0.5)
        cls()
        
        print("☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️")
        time.sleep(1)
        gameover()
        print("You got caught and turned into a clown")
        time.sleep(3)
        exit()

#checking win/loss 
  
if YourHealth >0 and ClownArmyHealth <=0:
    cls()
    print("CLOWN ARMY HAS BEEN DEFEATED!!!!!")
    time.sleep(0.5)
if YourHealth <0:
    print("you got killed by clown")
    gameover()
    exit()

#asking user to continue or not

print("%15s" %("웃"))
ans4 = str(input("Do you want to continue? (yes/no): "))
cls()

#Checking answer and displaying text based on ans
if ans4 == "yes":
    print("You you continue through spooky circus tent...")
    time.sleep(1)
    cls()
elif ans4 == "no":
    gameover()
    print("You tried to leave but got lost and starved to death")
    exit()
else:
    print("Please enter yes or no")
    exit()

#cut scene animation

print("%0s%30s" %("웃", "👴"))
time.sleep(0.5)
cls()

print("%3s%27s" %("웃", "👴"))
time.sleep(0.5)
cls()

print("%6s%24s" %("웃", "👴"))
time.sleep(0.5)
cls()

print("%9s%21s" %("웃", "👴"))
time.sleep(0.5)
cls()

print("%12s%18s" %("웃", "👴"))
time.sleep(0.5)
cls()

print("%15s%15s" %("웃", "👴"))
time.sleep(0.5)
cls()

print("%18s%12s" %("웃", "👴"))
time.sleep(0.5)
cls()

print("%21s%9s" %("웃", "👴"))
time.sleep(0.5)
cls()

print("%24s%6s" %("웃", "👴"))
time.sleep(0.5)
cls()

print("%27s%3s" %("웃", "👴"))
time.sleep(0.5)
cls()

print("%29s%1s" %("웃", "👴"))
time.sleep(0.5)
cls()

#dialoge for story

print("Old Merchant: NOT SO FAST YOUNG SEEDLING!")
time.sleep(2)
print("You: What do you want sir?")
time.sleep(2)
print("Old Merchant: ARE YOU GOING TO FIGHT CORNELIUS THE CLOWN!?")
time.sleep(2)
print("You: Thats the plan")
time.sleep(2)
print("Old Merchant: WOULD YOU LIKE TO CHOOSE AN ITEM TO HELP ON YOUR PERILOUS QUEST YOUNG SQWIRE?")
time.sleep(2)
print("You: yeah why not")
time.sleep(3)
cls()

#shows options

print("Old Merchant: CHOOSE WISELY YOUNG WHIPPERSNAPPER!!")

print("%30s%30s%30s" %("💗", "🗡️", "🛡️"))
print("%39s%27s%33s" %("Heart of healing", "Dagger of doom", "Shield of sheltering"))
print("%36s%29s%30s" %("+45 Health", "+30 Damage", "+20 Defence"))

#Creating damage and defence variable for items

YourDamage = 0
YourDefence = 0
ans5 = str(input("Which do you pick: "))
ans5 = ans5.lower()
time.sleep(1)

#Checks answer and displaying and updating coorsponding variables
if ans5 == "heart of healing":
    print("Old Merchant: WISE CHOICE YOUNG MOPPET")
    time.sleep(0.5)
    print("+45 Health")
    time.sleep(0.5)
    YourHealth = YourHealth + 45
    print("Your health:", YourHealth)
    time.sleep(2)
elif ans5 == "dagger of doom":
    print("Old Merchant: I SEE YOU LIKE BIG DAMAGE YOUNG WIFFLET")
    time.sleep(0.5)
    print("+30 Damage")
    time.sleep(0.5)
    YourDamage = YourDamage + 30
    time.sleep(2)
elif ans5 == "shield of sheltering":
    print("Old Merchant: AH, CHOSING TO STAY SAFE YOUNG BANTLING")
    time.sleep(0.5)
    print("+20 Defence")
    time.sleep(0.5)
    YourDefence = YourDefence + 20
    time.sleep(2)

cls()

#more dialoge

print("Old Merchant: I WISH YOU THE BEST OF LUCK YOUNGLING")
time.sleep(2)

cls()

print("You enter the main cirus room...")
time.sleep(2)
cls()

#more and more dialoge

print("Ganderf: fie! thee've gotten stout'r cornelius!")
time.sleep(2)
print("Cornelius the clown: I think you just got weaker GANDERF!!!")
time.sleep(2)
print("\t\t\t\t💥💥💥🎪💥💥💥")
time.sleep(2)
print("GANDERFS SPELL BOOK GOES FLYING INTO A BUSH OUTSIDE")
time.sleep(2)
cls()

#book goes flying in the bush animation

print("%0s%30s" %("📕", "🌳"))
time.sleep(0.5)
cls()


print("%6s%24s" %("📕", "🌳"))
time.sleep(0.5)
cls()


print("%12s%18s" %("📕", "🌳"))
time.sleep(0.5)
cls()


print("%18s%12s" %("📕", "🌳"))
time.sleep(0.5)
cls()


print("%24s%6s" %("📕", "🌳"))
time.sleep(0.5)
cls()


print("%29s%1s" %("📕", "🌳"))
time.sleep(0.5)
cls()

#more dialoge

print("(Ganderf sees you)")
time.sleep(1)
print("Ganderf: Greetings young sir, I might not but f'r thy aid")
time.sleep(4)
print("         I has't weaken'd c'rnelius the clown but that gent remains undeaft'd")
time.sleep(4)
print("         Prithee killeth that gent f'r me")
time.sleep(4)
print("You: Of course I will the lengendary uncopyrightable ganderf!")
time.sleep(4)
print("Ganderf: I wilt findeth mine own spelleth booketh anon, I give you luck")
time.sleep(4)
cls()

print("(GANDALF LEAVES IN SEARCH OF HIS LOST SPELL BOOK!!!!")
time.sleep(2.5)
cls()

print("▄▀█ █░█    █░░ █▀█ █▀█ █▄▀ █▀   █░░ █ █▄▀ █▀▀   █ ▀█▀ █▀   ░░█ █░█ █▀ ▀█▀   █▄█ █▀█ █░█   ▄▀█ █▄░█ █▀▄   █▀▄▀█ █▀▀  ") 
print("█▀█ █▀█    █▄▄ █▄█ █▄█ █░█ ▄█   █▄▄ █ █░█ ██▄   █ ░█░ ▄█   █▄█ █▄█ ▄█ ░█░   ░█░ █▄█ █▄█   █▀█ █░▀█ █▄▀   █░▀░█ ██▄  ")

for x in range (1,4):
    cls()
    clown1()

    print("\t█░█ ▄▀█")
    print("\t█▀█ █▀█")
    time.sleep(0.5)
    cls()

    clown2()

    print("\t█░█ ▄▀█")
    print("\t█▀█ █▀█")
    time.sleep(0.5)

print("You: Im coming for you cornelius!!!!")
time.sleep(2)
cls()

time.sleep(2)
print("\n𝓣𝓲𝓹: 𝓠𝓾𝓲𝓬𝓴𝓵𝔂 𝓽𝔂𝓹𝓮 𝓽𝓱𝓮 𝓬𝓸𝓻𝓻𝓮𝓬𝓽 𝓵𝓮𝓽𝓽𝓮𝓻𝓼 𝓽𝓸 𝔀𝓲𝓷!")
time.sleep(3)
cls()

print("\t\t\t3️⃣")
time.sleep(0.5)
print("\t\t\t2️⃣")
time.sleep(0.5)
print("\t\t\t1️⃣")
time.sleep(0.5)
print("\t\t█▀▀ █ █▀▀ █░█ ▀█▀ ")
print("\t\t█▀░ █ █▄█ █▀█ ░█░ ")
print()
print()
time.sleep(1)

#FIGHT SCENE 2

time.sleep(1)

#ADDING CORNELIUS HEALTH

CorneliusHealth = 3

#While loop for fight

while YourHealth >0 and CorneliusHealth >0:
    userANS = ("FILL TEXT")
    
    #print hearts based on health

    if CorneliusHealth == 3:
        print("%10s%3s%25s" %("Your Health:", YourHealth, "Cornelius Health: 💗 💗 💗"))
        clown1()
    elif CorneliusHealth == 2:
        print("%10s%3s%25s" %("Your Health:", YourHealth, "Cornelius Health: 💗 💗"))
        clown1()
    elif CorneliusHealth == 1:
        print("%10s%3s%25s" %("Your Health:", YourHealth, "Cornelius Health: 💗"))
        clown1()
    time.sleep(1)

    #Generates random number

    randomNum = random.randint(1,3)

    #based on random number do 1 of 3 actions

    if randomNum == 1:
        #cornelius attacks prompts for user input to block
        print("CORNELIUS ATTACKS YOU!!!")
        print("TYPE BLOCK!!!")
        starttime = time.time()
        while time.time() - starttime <1:
            if msvcrt.kbhit():
                userANS=input()
                break

        userANS = userANS.lower()

        cls()

        #based on user input do actions

        if userANS == "block":
            print("You Blocked His Attack!! NICE!!!")
            time.sleep(1)
        else:
            print("You didnt block in time! oh no!")
            time.sleep(1)
            Cattack1 = random.randint(15,30)
            YourHealth = YourHealth - Cattack1
            
            if Cattack1  <=15 and Cattack1 <20:
                print("\nCornelius inflates you with helium!! Light damage!!")
                print("Minus",Cattack1,"Health!!")
                time.sleep(2)
                cls()
            
            
            elif Cattack1 >=20 and Cattack1 <25:
                print("\nCornelius smashes you with a ballon hammer!! Medium damage!!")
                print("Minus",Cattack1,"Health!!")
                time.sleep(2)
                cls()

            elif Cattack1 >25 and Cattack1 <31:
                print("\nCornelius throws a bowling ball at you!! BIG DAMAGE!!")
                print("Minus",Cattack1,"Health!!")
                time.sleep(2)
                cls()
    
    #allows you to attack cornelius

    elif randomNum == 2:
        print("YOU ATTACK CORNELIUS!!")
        print("TYPE ATTACK")

        starttime = time.time()
        while time.time() - starttime < 1:
            if msvcrt.kbhit():
                userANS=input()
                break
        
        userANS = userANS.lower()

        cls()

        #checking user input

        if userANS == "attack":
            print("You attacked him!!!")
            CorneliusHealth = CorneliusHealth - 1
            print("Nice shot!")  
            time.sleep(2) 
        else:
            print("OH NO! Cornelius blocked your attack!")
            time.sleep(2)
    
    #cornelius attacks prompts for user input

    elif randomNum == 3:
        print("CORNELIUS JUMPS YOU")
        print("TYPE DODGE!")
        timeout = 2
        starttime = time.time()
        while time.time() - starttime < 1:
            if msvcrt.kbhit():
                userANS=input()
                break

        userANS = userANS.lower()
        
        #based on user answer display 
        cls()
        if userANS == "dodge":
            print("You barely dodged his attack")
            print("PHEW")
            
            time.sleep(1)

        else:

            print("You didnt dodge in time! oh no!")
            time.sleep(0.5)

            Cattack1 = random.randint(15,30)
            YourHealth = YourHealth - Cattack1
            
            if Cattack1  <=15 and Cattack1 <20:
                print("\nCornelius inflates you with helium!! Light damage!!")
                print("Minus",Cattack1,"Health!!")
                time.sleep(2)
            
            
            elif Cattack1 >=20 and Cattack1 <25:
                print("\nCornelius smashes you with a ballon hammer!! Medium damage!!")
                print("Minus",Cattack1,"Health!!")
                time.sleep(2)

            elif Cattack1 >25 and Cattack1 <31:
                print("\nCornelius !! BIG DAMAGE!!")
                print("Minus",Cattack1,"Health!!")
                time.sleep(2)
    
    # checking winner
    if YourHealth >0 and CorneliusHealth <=0:
        cls()
        print("CORNELIUS HAS BEEN SLAIN!!!!!")
        time.sleep(3)
    
    if YourHealth <=0 and CorneliusHealth >=0:
        print("you got clowned on")
        time.sleep(0.5)
        print("too bad so sad")
        gameover()
        time.sleep(3)
        exit()

#party time

for x in range (1,3):
    print("🎉 웃  ")
    time.sleep(0.5)
    cls()
    print("🎊웃🎊")
    time.sleep(0.5)
    cls()

for x in range(1,4):
    print("ha")
    time.sleep(0.5)


#cut scene cornelius grows

time.sleep(1)
print("\nyou're stronger than I thought...")
time.sleep(2)
print("But unfortunately...")
time.sleep(2)
print("You're not strong enough!! ")
time.sleep(2)
print("           ")
print("          {_} ")
print("          / \ ")
print("       /\/___\/\ ")
print("      /  /^o^\  \ ")
print("      \  \'-'/  / ")
print("       '-/vvv\-' ")
print("\tha")

time.sleep(2.5)

print("            ")
print("           {_} ")
print("           /*\ ")
print("          /_*_\ ")
print("         {('o')} ")
print("      C{{([^*^])}}D ")
print("          [ * ] ")
print("         /  Y  \ ")
print("        _\__|__/_ ")
print("       (___/ \___) ")
print("\tHa")

time.sleep(3)

print("       ,            _..._            , ")
print("      {'.         .'     '.         .'} ")
print("     { ~ '.      _|=    __|_      .'  ~} ") 
print("    { ~  ~ '-._ (___________) _.-'~  ~  } ")
print("   {~  ~  ~   ~.'           '. ~    ~    } ") 
print("  {  ~   ~  ~ /   /\     /\   \   ~    ~  } ")
print("  {   ~   ~  /    __     __    \ ~   ~    } ")
print("   {   ~  /\/  -<( o)   ( o)>-  \/\ ~   ~} ")
print("    { ~   ;(      \/ .-. \/      );   ~ } ")
print("     { ~ ~\_  ()  ^ (   ) ^  ()  _/ ~  } ")
print("      '-._~ \   (`-._'-'_.-')   / ~_.-' ")
print("              \     \`-'/     / ")
print("               `\    '-'    /' ")
print("                 `\       /' ")
print("                   '-...-' ")

print("\tHA ")

time.sleep(3)

print("                                  ,;;;;;;, ")
print("                                ,;;;'""`;;\ ")
print("                              ,;;;/  .'`',;\ ")
print("                            ,;;;;/   |    \|_ ")
print("                           /;;;;;    \    / .\ ") 
print("                         ,;;;;;;|     '.  \/_/ ")
print("                        /;;;;;;;|       \ ")
print("             _,.---._  /;;;;;;;;|        ;   _.---.,_ ")
print("           .;;/      `.;;;;;;;;;|         ;'      \;;, ")
print("         .;;;/         `;;;;;;;;;.._    .'         \;;;. ") 
print("        /;;;;|          _;- `       ` -;_          |;;;;\ ")
print("       |;;;;;|.---.   .'  __.- ``` -.__  '.   .---.|;;;;;| ") 
print("       |;;;;;|     `\/  .'/__\     /__\'.  \/`     |;;;;;| ")
print("       |;;;;;|       |_/ //  \\   //  \\ \_|       |;;;;;| ") 
print("       |;;;;;|       |/ |/    || ||    \| \|       |;;;;;| ")
print("        \;;;;|    __ || _  .-.\| |/.-.  _ || __    |;;;;/ ")
print("         \jgs|   / _\|/ = /_o_\   /_o_\ = \|/_ \   |;;;/ ")
print("          \;;/   |`.-     `   `   `   `     -.`|   \;;/ ")
print("         _|;'    \ |    _     _   _     _    | /    ';|_ ")
print("        / .\      \\_  ( '--'(     )'--' )  _//      /. \ ")
print("        \/_/       \_/|  /_   |   |   _\  |\_/       \_\/ ")
print("                      | /|\\  \   /  //|\ | ")
print("                      |  | \'._'-'_.'/ |  | ")
print("                      |  ;  '-.```.-'  ;  | ")
print("                      |   \    ```    /   | ")
print("    __                ;    '.-------.'    ;                __ ")
print("   /\ \_         __..--\     `-----'     /--..__         _/ /\ ")
print("   \_'/\`''---''`..;;;;.'.__,       ,__.',;;;;..`''---''`/\'_/ ")
print("        '-.__'';;;;;;;;;;;,,'._   _.',,;;;;;;;;;;;''__.-' ")
print("             ``''--; ;;;;;;;;..` `..;;;;;;;; ;--''``   _ ")
print("        .-.       /,;;;;;;;';;;;;;;;;';;;;;;;,\    _.-' `\ ")
print("      .'  /_     /,;;;;;;'/| ;;;;;;; |\';;;;;;,\  `\     '-'| ")
print("     /      )   /,;;;;;',' | ;;;;;;; | ',';;;;;,\   \   .'-./ ")
print("     `'-..-'   /,;;;;','   | ;;;;;;; |   ',';;;;,\   `` ")
print("              | ;;;','     | ;;;;;;; |  ,  ', ;;;'| ")
print("             _\__.-'  .-.  ; ;;;;;;; ;  |'-. '-.__/_ ")
print("            / .\     (   )  \';;;;;'/   |   |    /. \ ") 
print("            \/_/   (`     `) \';;;'/    '-._|    \_\/ ")
print("                    '-/ \-'   '._.'         ` ")
print("                               /.`\ ")
print("                               \|_/ ")

print("\t█░█ ▄▀█ ▄▀█ ▄▀█ ▄▀█")
print("\t█▀█ █▀█ █▀█ █▀█ █▀█")
time.sleep(3)

#dialoge

print("I've never lost a game of rock paper scissors before")
time.sleep(1)
print("And im not going to start today!")
time.sleep(2)
cls()

print("█▀ ▀█▀ ▄▀█ █▀▀ █▀▀   ▀█")
print("▄█ ░█░ █▀█ █▄█ ██▄   █▄")

time.sleep(1)
print("\t\t\t3️⃣")
time.sleep(0.5)
print("\t\t\t2️⃣")
time.sleep(0.5)
print("\t\t\t1️⃣")
time.sleep(0.5)
print("\t\t█▀▀ █ █▀▀ █░█ ▀█▀ ")
print("\t\t█▀░ █ █▄█ █▀█ ░█░ ")
print()
print()
time.sleep(1)
cls()

#reset cornelius health to 100
Corneliushealth = 100

while YourHealth >0 and Corneliushealth >0:

    #displays your and cornelius health

    cls()
    print("%25s%18s"%("(STAGE 2) Cornelius:","You:"))
    print("%17s%1s%24s%1s" %("Health: ", Corneliushealth, "Health: ",YourHealth))
    print("\t\t\t\t\t웃")
    print(clown2())

    #Choosing computer choice of rock paper or scissors
    #Also generates potenial attacks

    ComputerChoice = random.randint(1,3)
    Cornattack = random.randint(15,25)
    Cornattack = Cornattack - YourDefence
    Youattack = random.randint(30,40)
    Youattack = Youattack + YourDamage

    #Changes int to paper rock or scissors
    ComputerMove = "paper"
    if ComputerChoice == 1:
        ComputerMove = "rock"
    if ComputerChoice == 2:
        ComputerMove = "paper"
    if ComputerChoice == 3:
        ComputerMove = "scissors"

    
    #ask user of input

    Userchoice = str(input("Rock, Paper or Scissors: "))
    Userchoice = Userchoice.lower()
    
    #shows both moves
    if Userchoice == "rock" or "paper" or "scissors":
        print("You picked", Userchoice, "And Cornelius picked", ComputerMove)
        time.sleep(0.5)
    else:
        #guardes spelling

        print("Check spelling") 
        time.sleep(1)
        exit()

    #Rock options, compare user and computer options and display message with damage if nessecary
    if Userchoice == "rock" and ComputerMove == "rock":
        time.sleep(1)
        print("TIE!!")
    elif Userchoice == "rock" and ComputerMove == "paper":
        print("PAPER COVERS ROCK!!")
        time.sleep(1)
        YourHealth = YourHealth - Cornattack
        print("CORNELIUS ATTACKS YOU!! MINUS", Cornattack, "HEALTH!!!")
    elif Userchoice == "rock" and ComputerMove == "scissors":
        print("ROCK SMASHES SCISSORS")
        time.sleep(1)
        Corneliushealth = Corneliushealth - Youattack
        print("YOU ATTACK CORNELIUS!!! MINUS", Youattack, "HEALTH!!!")


    #Paper options, compare user and computer options and display message with damage if nessecary
    if Userchoice == "Paper" and ComputerMove == "Paper":
        time.sleep(1)
        print("TIE!!")
    elif Userchoice == "paper" and ComputerMove == "scissors":
        print("SCISSORS CUT PAPER!!")
        time.sleep(1)
        YourHealth = YourHealth - Cornattack
        print("CORNELIUS ATTACKS YOU!! MINUS", Cornattack, "HEALTH!!!")
    elif Userchoice == "paper" and ComputerMove == "rock":
        print("PAPER COVERS ROCK!!")
        time.sleep(1)
        Corneliushealth = Corneliushealth - Youattack
        print("YOU ATTACK CORNELIUS!!! MINUS", Youattack, "HEALTH!!!")

    #Scissors options, compare user and computer options and display message with damage if nessecary
    if Userchoice == "Scissors" and ComputerMove == "Scissors":
        time.sleep(1)
        print("TIE!!")
    elif Userchoice == "scissors" and ComputerMove == "rock":
        print("ROCK CRUSHES SCISSORS!!")
        time.sleep(1)
        YourHealth = YourHealth - Cornattack
        print("CORNELIUS ATTACKS YOU!! MINUS", Cornattack, "HEALTH!!!")
    elif Userchoice == "scissors" and ComputerMove == "paper":
        print("SCISSORS CUT PAPER!!")
        time.sleep(1)
        Corneliushealth = Corneliushealth - Youattack
        print("YOU ATTACK CORNELIUS!!! MINUS", Youattack, "HEALTH!!!")

    time.sleep(3)

cls()

#check winner

if YourHealth > 0 and Corneliushealth <=0:
    print("YOU GOT HIM!!!!!!!!!")
    time.sleep(2)

if Corneliushealth > 0 and YourHealth <=0:
    print("You got smoked by cornelius")
    gameover()
    exit()

#dialodge

print("You: Finally, he is down for good!")
time.sleep(2)
print("Cornelius: how.. is this possible...")
time.sleep(2)
print("Cornelius: this can't be")
time.sleep(2)
print("Cornelius: spare me please, I become a friendly clown i promise!!")
time.sleep(2)


#Final question for user

ans6 = str(input("Finish him? (yes/no):"))

ans6 = ans6.lower()


#final cut screen
if ans6 == "yes":
    print("%1s%19s" %("웃","🤡🃏"))
    time.sleep(0.5)
    cls()

    print("%2s%18s" %("웃","🤡🃏"))
    time.sleep(0.5)
    cls()


    print("%4s%16s" %("웃","🤡🃏"))
    time.sleep(0.5)
    cls()


    print("%6s%14s" %("웃","🤡🃏"))
    time.sleep(0.5)
    cls()


    print("%8s%12s" %("웃","🤡🃏"))
    time.sleep(0.5)
    cls()


    print("%10s%10s" %("웃","🤡🃏"))
    time.sleep(0.5)
    cls()


    print("%12s%8s" %("웃","🤡🃏"))
    time.sleep(0.5)
    cls()


    print("%14s%6s" %("웃","🤡🃏"))
    time.sleep(0.5)
    cls()


    print("%16s%4s" %("웃","🤡🃏"))
    time.sleep(0.5)
    cls()


    print("%18s%2s" %("웃","🤡🃏"))
    time.sleep(1)
    print("You: ALAKAZAMO!")
    time.sleep(2)
    cls()

    print("%18s%2s" %("웃","💥"))
    time.sleep(0.5)
    cls()

    print("%18s%2s" %("웃","💥💥💥"))
    time.sleep(0.5)
    cls()

    print("%18s%2s" %("웃","💥💥💥💥💥"))
    time.sleep(1)
    cls()

    print("%18s%2s" %("웃","⚰️"))
    time.sleep(2)
    cls()

    print("YOU WONNNNN!!!!!")
    time.sleep(2)
    print("Conrats you may continue to the next game!!!")
    time.sleep(2)
    print("King of the necklaces 2")
    time.sleep(2)
    print("Release date: Probably soon like friday or something")
    time.sleep(2)
    #game ends
    exit()

#other decision option

if ans6 == "no":
    print("You leave and cornelius lives a happy life as a good clown attending birthday parties!") 
    time.sleep(3)
    print("YOU WONNNNN!!!!!")
    time.sleep(2)
    print("Conrats you may continue to the next game!!!")
    time.sleep(2)
    print("King of the necklaces 2")
    time.sleep(2)
    print("Release date: Probably soon like friday or something")
    time.sleep(2)
    #game ends
    exit()