1#a program that can be used as a “monster fighting” simulation. Have a ran#a program that can be used as a “monster fighting” simulation. Have a random variable for health for the monster and the
# “good guy”. Each character has a weapon that does a random amount of damage. The program should loop until somebody wins.
# Make sure you have an ‘enter’ input so we can see how each fight goes.
#Ayden
#jan 9
import random
import time
playerdie =0
chance50 = random.randint(1,2)
traderrep =0
Enemychance = 0#random enemy
buyop= 0
enemy =2
bop=0
shield=0
dragoncombat =0
spear=0
jus =0
sword = 0
print("Wellcom you The cave of monsters!")#start code
time.sleep(1)
print("You wake up in a weird world but you see a man near by and decide to walk over to him.")
time.sleep(3)
print("He tells you that monsters from a cave have been terrorising the village for some time now.")
time.sleep(3)
print("He said he will pay you a large some of gold if you take care of them (he tells you where they are) and that the merchant sells weapons.")
time.sleep(6)
print("So you walk over to him.")
time.sleep(1)
print("Hello I am a merchant.")
time.sleep(0.5)
playername = input("What is your name traveler?")
time.sleep(1)
print("Hello", playername)
time.sleep(1)
while True:#gets gold
    try:         
        gold = int(input("How much gold do you have?"))
        time.sleep(1)
        break
    except ValueError:
        time.sleep(1)
        print(":(")
        time.sleep(3)
        print("You fool I said gold.")
while True:#the traider douts the player has more than 100 gold
    if gold > 100:
        print("Your lying, you're dressed in rags there's no way you have that much gold")
        time.sleep(1)
        while True:
                try:        
                    gold = int(input("How much gold do you have?"))
                    time.sleep(1)
                    break
                except ValueError:
                    time.sleep(1)
                    print(":(")
                    time.sleep(3)
                    print("You fool I said gold.")
    else:
        break
if gold >50 and chance50 ==2:#the traider will get angry
    print("YOU'RE GETTING ON MY NERVE",playername,"you don't have more than 50 gold.")
    time.sleep(1)
    while True:
        try:       
            gold = int(input("How much gold do you have FOOL?"))
            time.sleep(1)
            playerdie =1
            break
        except ValueError:
            time.sleep(1)
            print(":(")
            time.sleep(3)
            print("I SAID GOLD.")  
if gold <0:#punishes the player for puting -gold
    print("Your in debt.")
    print("The man whom you owe monney to kills you-_YOU DIED_-")
    exit()
if  playerdie == 1 and gold >50:#the traider will sell things to the player or will kill him
        print("YOU'VE DONE IN NOW BOY TIME TO -_DIE_-")
        time.sleep(3)
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢔⢒⡿⠯⠥⢦⣦⣾⣄⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⢮⠊⠁⠀⠀⠀⠀⠈⠉⠛⠳⡀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⣿⣝⡴⡔⠀⠀⠀⠀⠀⠀⠀⠀⠘⡀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣀⣀⣦⣶⣿⣿⣯⣿⢽⠁⢰⣢⣶⣦⣌⠠⠴⠆⠘⣀⠀⠀⠀\n⠀⠀⠀⠀⢀⠔⠁⠀⢂⠘⢻⢛⣛⠿⣝⠁⠀⠼⣁⡴⣖⣫⠙⠙⠿⡳⡅⠀⠀⠀\n⠀⠀⠀⢀⠂⠰⠀⠀⠈⡄⢠⢓⣺⢇⡇⣊⠐⠀⠉⠁⠲⠒⠀⠀⠀⠑⠅⠀⠀⠀\n⠀⠀⠀⣨⠀⡇⠀⠀⠀⠰⢸⠄⠄⣸⣷⡦⣄⢤⠄⢄⡀⣀⠤⠠⡀⠀⠈⡄⠀⠀\n⠀⠀⢠⠁⠙⣇⠀⠀⠀⠀⢾⠘⢠⣿⣟⣿⣿⣪⣮⣶⣸⣮⣖⣢⣌⠁⠀⠁⠀⠀\n⠀⠀⢸⠀⠀⢹⠀⠀⠀⠀⠸⠀⢝⣻⣯⣿⢿⡫⢺⡩⠍⣉⣉⣨⡗⠉⠂⠊⠀⠀\n⠀⠀⡈⠂⠀⣾⠀⠀⠀⠀⠀⠆⡸⣹⡿⣿⣯⣷⣱⣙⠫⠧⠷⣦⠀⠀⠀⠀⠀⠀\n⠀⢠⠇⠀⠀⢉⠀⠀⠀⠀⠀⠈⠕⣻⣿⣿⣿⣟⣿⣿⡷⣶⣾⠿⠒⡁⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠈⢇⠻⠽⣿⡿⢟⣿⣻⡟⠁⠰⣯⡕⡰⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⢩⠀⠀⠀⠀⠀⢀⠬⣍⠱⠨⠯⠛⠙⢏⠀⢀⡀⣨⡀⠤⢚⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀⠀⢠⠁⠀⠀⠀⠀⠀⢸⠄⠰⡶⠲⢦⠓⠍⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠡⡀⠀⠀⠀⠀⠀⠀⡄⠀⢀⠄⠊⠉⠙⠑⠒⠊⠉⠀⠀")
        time.sleep(1)
        print("What will you do? 1(run away), 2(throw hands with the traider), or 3(beg for your life).")
        while True:
            try:            
                combat = int(input("?"))
                while combat >3 or combat < 0:
                        print("Nope thats not an option.")
                        combat = int(input("?"))
                break
            except ValueError:
                time.sleep(1)
                print(":(")
                time.sleep(3)
                print("A number goof ball.")
        if combat == 1:
            print("You got away with your life. The trader was strong but wasn't too fast.")
            time.sleep(1)
            print("You find 37 gold in your pocket.")
            time.sleep(1)
            playerdie =playerdie -1
            traderrep= 1
            gold = 37
            print("You have", gold,"gold.")
        elif combat == 2:
            print("You were no match for him -_Your dead_- GAME OVER")
            time.sleep(1)
            exit()
        elif combat == 3:
            print("HE didn't care -_Your dead_- GAME OVER")
            time.sleep(1)
            exit()
if traderrep== 1:#if the player made the mercant mad and lives
    print("You find a well on you way to the cave and you see that there's a song on it.")
    time.sleep(1)
    print("It says:throw 5 gold in the well and your wishes will come true.")
    time.sleep(1)
    while True:
            try:
               
                time.sleep(1)
                well = int(input("Type 1 if you want to drop the gold or type 2 if you dont."))
               
                time.sleep(1)
                break
            except ValueError:
                time.sleep(1)
                print(":(")
                time.sleep(3)
                print("type a number ")    
    if well ==1:
        gold= gold -5
        print("You found a spear in the well")
        spear=1
time.sleep(1)
while traderrep < 1 and gold > 0:#the user gets a wepon
    
    print("Now time to buy things.")  
    time.sleep(1)
    print("What would you like to buy?")
    time.sleep(0.1)
    print("-------------------------")
    time.sleep(0.4)
    print("| -sword- -shield- -jus- |")
    time.sleep(0.4)
    print("|  -35-    -25-    -5-  |")
    time.sleep(0.4)
    print("|---1-------2-------3----|")
    time.sleep(0.1)
    print("|---------gold----------|")
    time.sleep(0.4)
    print("-------------------------")
    print("You have", gold,"gold.")
    while True:
        try:
            buyop = int(input("Pick 1, 2, or 3? or 4 for exit"))
            time.sleep(1)
            break
        except ValueError:
            time.sleep(1)
            print(":(")
            time.sleep(3)
            print("Type a number. ")
            #sword buying
    if buyop ==1 and gold >= 35 and sword ==0:
        print("You bought a sword.")
        time.sleep(1)
        sword =1
        while True:
            try:
                print("Would you like to buy another thing?")
                time.sleep(1)
                print("1yes 2no")
                time.sleep(1)
                bop = int(input("Pick 1 or 2?"))
                gold =gold -35
                time.sleep(1)
                break
            except ValueError:
                time.sleep(1)
                print(":(")
                time.sleep(3)
                print("Type a number.")
    elif sword == 1:
        time.sleep(1)
        print("You have a sword.")
        #shield buying
    if buyop ==2 and gold >= 25 and shield == 0:
        print("You bought a shield.")
        time.sleep(1)
        shield =1
        while True:
            try:
                print("Would you like to buy another thing?")
                time.sleep(1)
                print("1yes 2no")
                time.sleep(1)
                bop = int(input("Pick 1 or 2?"))
                gold =gold -25
                time.sleep(1)
                break
            except ValueError:
                time.sleep(1)
                print(":(")
                time.sleep(3)
                print("Type a number.")    
    elif shield ==1:
        time.sleep(1)
        print("You have a shield.")  
        #jus buy
    if buyop ==3 and gold >= 5 and jus < 3:
        print("You bought jus.")
        time.sleep(1)
        jus =1
        while True:
            try:
                print("Would you like to buy another thing?")
                time.sleep(1)
                print("1yes 2no")
                time.sleep(1)
                bop = int(input("Pick 1 or 2?"))
                gold =gold -5
                time.sleep(1)
                break
            except ValueError:
                time.sleep(1)
                print(":(")
                time.sleep(3)
                print("Type a number. ")    
    elif buyop ==4:
        break
    elif jus ==2:
        print("You have 2 jus.")    
    if bop == 2:
        break
print("You have entered the cave!")
time.sleep(2)
while enemy > 0:#random enemy code
    Enemychance = random.randint(1,4)
    if Enemychance == 1:#dragon
        print("You encounered a DRAGON!")
        time.sleep(1)
        print("                 ___====-_  _-====___\n           _--^^^#####//      \\#####^^^--_\n        _-^##########// (    ) \\##########^-_\n       -############//  |\^^/|  \\############-\n     _/############//   (@::@)   \\############\_\n    /#############((     \\//     ))#############\ \n   -###############\\    (oo)    //###############-\n  -#################\\  / VV \  //#################-\n -###################\\/      \//###################-\n_#/|##########/\######(   /\   )######/\##########|\#_\n|/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|\n`  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '\n   `   `  `      `   / | |  | | \   '      '  '   '\n                    (  | |  | |  )\n                   __\ | |  | | /__\n                  (vvv(VVV)(VVV)vvv)")
        if shield == 0:
            time.sleep(1)
            print("How can you beat a dragon if you can't block its fire with a shield -_YOU DIED_-")
            exit()
        elif shield == 1:
            time.sleep(1)
            print("Will you use the (1)sword or the (2) jus or (3) to use your shield.")
            time.sleep(1)
            while True:
                try:
                    time.sleep(1)
                    dragoncombat = int(input("Type 1 to use the sword and type 2 to use the jus type 3 to use your shield."))
                    time.sleep(1)
                    if dragoncombat >3 or dragoncombat < 0:
                        print("Nope thats not an option.")
                        dragoncombat = int(input("Type 1 to use the sword and type 2 to use the jus or type 3 to use the shield."))
                    elif dragoncombat < 0:
                        print("Nope thats not an option.")
                        dragoncombat = int(input("Type 1 to use the sword and type 2 to use the jus or type 3 to use the shield."))
                    while (dragoncombat == 1 and sword == 0) or (dragoncombat == 2 and jus == 0) or (dragoncombat == 3 and shield == 0 ):
                        print("You don't have that item, please enter an item that you have.")
                        dragoncombat = int(input("Type 1 to use the sword and type 2 to use the jus or type 3 to use the shield."))
                        if dragoncombat >3:
                            print("Nope thats not an option.")
                            dragoncombat = int(input("Type 1 to use the sword and type 2 to use the jus or type 3 to use the shield."))
                        elif dragoncombat < 0:
                            print("Nope thats not an option.")
                            vamcombat = int(input("Type 1 to use the sword and type 2 to use the jus or type 3 to use the shield."))
                    time.sleep(1)
                    break
                except ValueError:
                    time.sleep(1)
                    print(":(")
                    time.sleep(3)
                    print("Type a number.")  
            if dragoncombat == 1:
                print("You use your sword and cut the dragon's head off lucky.")
                time.sleep(1)
                print("He left behind 20 gold.")
                time.sleep(1)
                gold = gold +20
                print("You have", gold,"gold.")
                time.sleep(1)
            elif dragoncombat == 2:
                print("You throw the jus at him.")
                time.sleep(1)
                print("He laughs at your pathetic attempt on his life and leaves the cave, sparing your life.")
                time.sleep(1)
                print("He left behind 20 gold.")
                time.sleep(1)
                jus = jus -1
                gold = gold +20
                print("You have", gold,"gold.")
                time.sleep(1)
            elif dragoncombat == 3:
                print("You barely get away with your life, but you lost you shield.")
                time.sleep(1)
                shield = 0
            else:
                print("You used no items and -_YOU DIED_-")
                exit()
        enemy = enemy-1
    if Enemychance == 2:#VAMPIRE
        print("You encounered a VAMPIRE!")
        time.sleep(1)
        print("⠀⠀⠀⠀⠀  _______\n       /       \ \n  /  `\  /   \/  \ \n   |  _ \/   .==.==.\n  | (   \  /____\__\ \n   \ \      (_()(_()\n    \ \            '---._\n      \                   \_\n  /\ |`       (__)________/\n /  \|     /\___/\n|    \     \||VV\n|     \     \|^^^^,\n|      \     ______)\n\       \  /`\n         \(")
        if spear == 1 :
            time.sleep(1)
            print("You throw youre spear at him witout thinging and it some how landed on his heart and killed him.")
            time.sleep(1)
            print("He left behind 5 gold.")
            time.sleep(1)
            gold = gold +5
            print("You have", gold,"gold.")
            time.sleep(1)
        elif sword == 1 or jus > 0 or shield ==1:
            time.sleep(1)
            print("Will you use the (1)sword or the (2) jus or (3) use you shield (4) talk thing out.")
            time.sleep(1)
            while True:
                try:
                    time.sleep(1)
                    vamcombat = int(input("Type 1 to use the sword and type 2 to use the jus or type 3 to use the shield type 4 to talk things out?"))
                    if vamcombat >4:
                        print("Nope thats not an option.")
                        vamcombat = int(input("Type 1 to use the sword and type 2 to use the jus or type 3 to use the shield."))
                    elif vamcombat < 0:
                        print("Nope thats not an option.")
                        vamcombat = int(input("Type 1 to use the sword and type 2 to use the jus or type 3 to use the shield."))
                    while (vamcombat == 1 and sword == 0) or (vamcombat == 2 and jus == 0) or (vamcombat == 3 and shield == 0 ):
                        print("You don't have that item, please enter an item that you have.")
                        vamcombat = int(input("Type 1 to use the sword and type 2 to use the jus or type 3 to use the shield or type 4 to talk tings out."))
                        if vamcombat >4:
                            print("Nope thats not an option.")
                            vamcombat = int(input("Type 1 to use the sword and type 2 to use the jus or type 3 to use the shield."))
                        elif vamcombat < 0:
                            print("Nope thats not an option.")
                            vamcombat = int(input("Type 1 to use the sword and type 2 to use the jus or type 3 to use the shield."))
                    time.sleep(1)
                    break
                except ValueError:
                    time.sleep(1)
                    print(":(")
                    time.sleep(3)
                    print("Type a number.")  
            if vamcombat == 1:
                print("You attacked him with your sword but he shaterd your sword and sucked your blood -_YOU DIED_-")
                exit()  
            elif vamcombat == 2:
                print("You throw the jus at him.")
                time.sleep(1)
                print("He laughs at your pathetic attempt on his life, as his skin melts...")
                time.sleep(1)
                print("What a bad way to go.")
                time.sleep(1)
                print("Mabe your the monster in the cave.")
                time.sleep(1)
                print("He left behind 5 gold.")
                time.sleep(1)
                jus =jus-1
                gold = gold +5
                print("You have", gold, "gold.")
                time.sleep(1)
            elif vamcombat == 3:
                print("How can a shield stop a vampire? -_YOU DIED_-")
                exit()
            elif vamcombat ==4:
                print("You chat with the vampire and he dicides to leave the cave if you give him some of you blood.")
                time.sleep(1)
                print("Will you give him some of you blood?")
                time.sleep(1)
                while True:
                    try:
                        time.sleep(1)
                        blood = int(input("(1)yes (2)no"))
                        time.sleep(1)
                        break
                    except ValueError:
                        time.sleep(1)
                        print(":(")
                        time.sleep(3)
                        print("type a number ")  
                time.sleep(1)
                if blood== 1:
                    print("He sucked youre blood but you lived and the left the cave and giving you 3 gold.")
                    time.sleep(1)
                    gold = gold +3
                    print("You have",gold,"gold.")
                    time.sleep(1)
                elif blood ==2:
                    print("He did it anyway and killed you -_YOU DIED_-")
                    exit()
                else:
                    print("-_YOU DIED_-")
                    exit()
            else:
                print("You used no items and -_YOU DIED_-")
                exit()
        else:
            print("How can you kill him  without a weapon? -_YOU DIED_-")
            exit()
        enemy = enemy-1
    if Enemychance == 3:#goopster 
        print("You encounered THE GOOPSTER !")
        time.sleep(1)
        print("⠀⠀⠀⠀⠀⣠⡄⡀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠹⣿⣇⠀⠀⢻⡿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⣠⣾⠿⣿⣶⣴⣶⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⣰⠏⠈⠀⣿⢫⣩⣤⣙⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⢸⡟⠀⢀⣀⣿⣭⣿⡳⡟⠁⠀⠀⠀⢀⣤⣴⡷⣆⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢠⡏⠀⠀⠈⠁⣠⡿⠶⠿⠃⠀⠀⣠⠞⠋⠀⠀⠀⠉⠀⠉⠉⠳⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢸⠁⠀⠀⠀⢰⡏⠀⠀⠀⠀⢀⡾⡁⠀⠀⠀⠰⠶⢦⣀⠀⠀⠀⠀⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢸⠀⠀⠀⠀⠸⣇⠀⠀⠀⣠⠏⠀⠀⣄⡀⡼⠛⠓⢦⡈⠓⠀⠀⠀⠀⠘⢦⣀⡀⠀⠀⢀⣀⣀⣀⠀⠀⠀\n⠀⢸⠀⠀⠀⠀⠀⠉⠳⣄⣠⠏⠀⠀⠀⠛⢻⡇⠀⠀⠀⠳⣄⣤⣀⡀⠀⣀⣠⣬⡟⣠⡶⠛⠉⠉⠙⢷⡄⠀\n⠀⠸⣇⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠒⠦⠀⠀⠻⣄⡀⢀⣰⠋⠁⠘⣷⠋⠉⠀⣾⣷⠏⠀⠀⠀⣀⠀⠀⢷⠀\n⠀⠈⠷⡿⡄⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⡿⢤⠞⢳⡉⠉⠀⠀⠀⠀⠸⠦⠤⠾⣽⠁⡄⠀⡶⣶⡿⢀⡀⣿⡀\n⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠻⣄⣀⡴⢶⡀⢀⣀⣄⡀⣼⠀⠁⠈⡷⣿⣵⡄⠙⢹⠁\n⠀⠀⠀⠀⢹⣄⣤⡀⠀⣤⢠⣄⢀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⣱⣟⢽⣋⣀⣤⣄⣳⡿⣿⣰⣶⡟⠀\n⠀⠀⠀⠀⠀⠉⠘⡇⠀⠉⠀⠻⠞⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣃⣼⣴⠟⠉⠁⠈⠉⠀⢷⣿⠉⠁⠀\n⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠳⣄⠀⣠⠖⢢⣤⡾⢳⡄⣼⡿⢷⡮⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠙⠋⠠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n")
        print("⠀⠀⠀⠀⠀⠀⠀⣹⠂⠀⠀⠀⢶⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⣴⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣦⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⢿⡄⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⢹⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠈⢻⠂⠀⠀⠀⠀⣿⣧⡄⣰⡀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⡄⠀⠀⢡⣧⣾⠟⠀⠀⠀⠀⠀⣴⡦⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⣠⡟⠀⣤⣼⠁⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠈⠀⠀⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⣠⠤⠤⠖⠋⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡆⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⢠⠏⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⣀⡿⠲⢦⡀⠀⠀⠀⠀⠀⠈⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⣼⠀⠀⠀⠀⠀⠀⠀⢻⠋⠀⠀⠀⣠⡾⠁⠀⠀⢻⠀⠀⠀⠀⠀⠀⢀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⢧⡀⠀⠀⠀⡤⢤⣀⣀⣀⣀⣠⡾⠋⠀⠀⠀⠀⢸⡄⠀⠀⠀⢀⠀⢘⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠈⠛⠒⠛⠾⠃⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⠸⠾⠁⠈⠉⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠶⠶⣾⣄⠀⠀⠀⠀⠀⢰⣷⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠛⠛⠛⠛⠋⠀⠀")
        if sword == 1 or jus > 0 or shield ==1 or spear ==1:
            time.sleep(1)
            print("will you use the (1)sword or the (2) jus or (3) use you shield (4) use your spear.")
            time.sleep(1)
            while True:
                try:
                    time.sleep(1)
                    combat = int(input("Type 1 to use the sword and type 2 to use the jus or type 3 to use the shield type 4 to to use the spear?"))
                    if combat >4:
                        print("Nope thats not an option.")
                        combat = int(input("Type 1 to use the sword and type 2 to use the jus or type 3 to use the shield type 4 to use the spear."))
                    elif combat < 0:
                        print("Nope thats not an option.")
                        combat = int(input("Type 1 to use the sword and type 2 to use the jus or type 3 to use the shield."))
                    while (combat == 1 and sword == 0) or (combat == 2 and jus == 0) or (combat == 3 and shield == 0 ) or (combat == 4 and spear ==0):
                        print("You don't have that item, please enter an item that you have.")
                        combat = int(input("Type 1 to use the sword and type 2 to use the jus or type 3 to use the shield or type 4 to use the spear."))
                        if combat >3:
                            print("Nope thats not an option.")
                            combat = int(input("Type 1 to use the sword and type 2 to use the jus or type 3 to use the shield type 4 to use the spear."))
                        elif combat < 0:
                            print("Nope thats not an option.")
                            combat = int(input("Type 1 to use the sword and type 2 to use the jus or type 3 to use the shield type 4 to use the spear."))
                    time.sleep(1)
                    break
                except ValueError:
                    time.sleep(1)
                    print(":(")
                    time.sleep(3)
                    print("Type a number.")  
            if combat == 1:
                print("You attacked him with your sword but your sword can't cut goop and it ate you -_YOU DIED_-")
                exit()  
            elif combat == 2:
                print("You throw the jus at him.")
                time.sleep(1)
                print("He melts.")
                time.sleep(1)
                print("Jus is the way to go.")
                time.sleep(1)
                print("he left behind 40 gold.")
                time.sleep(1)
                jus = jus-1
                gold = gold +40
                print("You have", gold, "gold.")
                time.sleep(1)
            elif combat == 3:
                print("You throw your shield at the top of the cave?????")
                time.sleep(1)
                print("I don't know why you would do that but it worked.")
                time.sleep(1)
                print("Water came throgh the top of the cave and killed THE GOOPSTER.")
                time.sleep(1)
                print("He left behind 40 gold.")
                time.sleep(1)
                gold = gold +40
                print("You have", gold, "gold.")
                time.sleep(1)
            elif combat ==4:
                time.sleep(1)
                print("You trow youre spear at him and...")
                time.sleep(1)
                print("It did nothing hes made out of goop. He ate you.-_YOU DIED_-")
                exit()
            else:
                print("You used no items and -_YOU DIED_-")
                exit()
        else:
            print("How can you kill THE GOOPSTER without a weapon-_YOU DIED_-")
            exit()
        enemy = enemy-1
    if Enemychance == 4:#?¿?¿?¿?
        print("You encounered ?¿?¿?¿? !")
        time.sleep(1)
        if sword == 1 or jus > 0 or shield ==1 or spear ==1:
            time.sleep(1)
            print("     j                       k\n    .K                       Z.\n    jM.                     .Mk\n    WMk                     jMW\n    YMM.       ,,,,,,      .MMY\n    `MML;:''```      ```':;JMM'\n    /`JMMMk.           .jMMMk'\ \n    / `GMMMI'         `IMMMO' \ \n   /    ~~~'           `~~~    \ \n   /                           \ \n   |                           |\n   |      ;,           ,;      |\n   |      Tk           jT      |\n    |     `Mk   . .   jM'     |\n    |      YK.   Y   .ZY      |\n     \     `Kk   |   jZ'     /\n     \       `'  |  `'       /\n      \          |          /\n       \         |         /\n       \         |         /\n        \        |        /\n         \       |       /\n         \       |       /\n          \      |      /\n           \     |     /\n           \  |  |  |  /\n            \ {| | |} /")
            print("             \ ` | ' /\n              \  |  /\n              \  |  /\n               \   /\n                \ /\n                 ~   ")
            time.sleep(1)
            print("Will you use the (1)sword or the (2) jus or (3) use you shield (4) use the spear (5) to use your sword and the jus.")
            time.sleep(1)
            while True:
                try:
                    time.sleep(1)
                    combat = int(input("Type 1 to use the sword and type 2 to use the jus or type 3 to use the shield or type 4 to to use the spear type 5 to use your sword and the jus?"))
                    if combat >5:
                        print("Nope thats not an option.")
                        combat = int(input("Type 1 to use the sword and type 2 to use the jus or type 3 to use the shield or type 4 to to use the spear type 5 to use your sword and the jus."))
                    elif combat < 0:
                        print("Nope thats not an option.")
                        combat = int(input("Type 1 to use the sword and type 2 to use the jus or type 3 to use the shieldtype 4 to to use the spear type 5 to use your sword and the jus."))
                    while (combat == 1 and sword == 0) or (combat == 2 and jus == 0) or (combat == 3 and shield == 0 ) or (combat == 4 and spear ==0) or (combat ==5 and (sword == 0 or jus == 0)):
                        print("You don't have that item, please enter an item that you have.")
                        combat = int(input("Type 1 to use the sword and type 2 to use the jus or type 3 to use the shield or type 4 to to use the spear type 5 to use your sword and the jus."))
                        if combat >3:
                            print("Nope thats not an option.")
                            combat = int(input("Type 1 to use the sword and type 2 to use the jus or type 3 to use the shield or type 4 to to use the spear type 5 to use your sword and the jus."))
                        elif combat < 0:
                            print("Nope thats not an option.")
                            combat = int(input("Type 1 to use the sword and type 2 to use the jus or type 3 to use the shield type 4 to to use the spear type 5 to use your sword and the jus."))
                    time.sleep(1)
                    break
                except ValueError:
                    time.sleep(1)
                    print(":(")
                    time.sleep(3)
                    print("Type a number.")  
            if combat == 1:
                print("You attacked him with your sword but he doged it and stabed you in the back -_YOU DIED_-")
                exit()  
            elif combat == 2:
                print("You throw the jus at him.")
                time.sleep(1)
                print("It dose nothing -_YOU DIED_-")
                exit()
            elif combat == 3:
                print("You throw your shield at him.")
                time.sleep(1)
                print("It went throgh him -_YOU DIED_-")
                exit()
            elif combat ==4:
                time.sleep(1)
                print("You trow youre spear at him and...")
                time.sleep(1)
                print("It hit his week spot and killed him.") 
                print("He had 40 gold.")
                time.sleep(1)
                gold = gold +40
                print("You have", gold, "gold.")
            elif combat ==5:
                time.sleep(1)
                print("You put your jus on your sword.")
                time.sleep(1)
                print("It hit his week spot and killed him.") 
                print("He had 40 gold.")
                time.sleep(1)
                jus = jus-1
                gold = gold +40
                print("You have", gold, "gold.")
            else:
                print("How can you kill him without a weapon-_YOU DIED_-")
                exit()
        else:
            print("You used no items and -_YOU DIED_-")
            exit()
        enemy = enemy-1
combat=0
#ending code
print("You exit the cave and return to the village.")
print("(walking sounds)")
time.sleep(2)
print("The man from earlier confronts you and you tell him that you cleared the cave.")
time.sleep(3)
print("He tells you that his name is Andres and he promotes you to the grand consler of the town.(the head of the village)")
time.sleep(4)
print("He also gives you 200 gold")
time.sleep(1)
gold = gold +200
print("You have", gold, "gold.")
time.sleep(3)
if  spear ==1:#the trader REMEMBERs
    print("You Encounter the trader from earlier.")
    time.sleep(1)
    print("I REMEMBER BOY TIME TO -_DIE_-")
    time.sleep(1)
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢔⢒⡿⠯⠥⢦⣦⣾⣄⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⢮⠊⠁⠀⠀⠀⠀⠈⠉⠛⠳⡀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⣿⣝⡴⡔⠀⠀⠀⠀⠀⠀⠀⠀⠘⡀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣀⣀⣦⣶⣿⣿⣯⣿⢽⠁⢰⣢⣶⣦⣌⠠⠴⠆⠘⣀⠀⠀⠀\n⠀⠀⠀⠀⢀⠔⠁⠀⢂⠘⢻⢛⣛⠿⣝⠁⠀⠼⣁⡴⣖⣫⠙⠙⠿⡳⡅⠀⠀⠀\n⠀⠀⠀⢀⠂⠰⠀⠀⠈⡄⢠⢓⣺⢇⡇⣊⠐⠀⠉⠁⠲⠒⠀⠀⠀⠑⠅⠀⠀⠀\n⠀⠀⠀⣨⠀⡇⠀⠀⠀⠰⢸⠄⠄⣸⣷⡦⣄⢤⠄⢄⡀⣀⠤⠠⡀⠀⠈⡄⠀⠀\n⠀⠀⢠⠁⠙⣇⠀⠀⠀⠀⢾⠘⢠⣿⣟⣿⣿⣪⣮⣶⣸⣮⣖⣢⣌⠁⠀⠁⠀⠀\n⠀⠀⢸⠀⠀⢹⠀⠀⠀⠀⠸⠀⢝⣻⣯⣿⢿⡫⢺⡩⠍⣉⣉⣨⡗⠉⠂⠊⠀⠀\n⠀⠀⡈⠂⠀⣾⠀⠀⠀⠀⠀⠆⡸⣹⡿⣿⣯⣷⣱⣙⠫⠧⠷⣦⠀⠀⠀⠀⠀⠀\n⠀⢠⠇⠀⠀⢉⠀⠀⠀⠀⠀⠈⠕⣻⣿⣿⣿⣟⣿⣿⡷⣶⣾⠿⠒⡁⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠈⢇⠻⠽⣿⡿⢟⣿⣻⡟⠁⠰⣯⡕⡰⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⢩⠀⠀⠀⠀⠀⢀⠬⣍⠱⠨⠯⠛⠙⢏⠀⢀⡀⣨⡀⠤⢚⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀⠀⢠⠁⠀⠀⠀⠀⠀⢸⠄⠰⡶⠲⢦⠓⠍⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠡⡀⠀⠀⠀⠀⠀⠀⡄⠀⢀⠄⠊⠉⠙⠑⠒⠊⠉⠀⠀")
    time.sleep(1)
    print("What will you do? 1(run away), 2(throw hands with the traider), or 3(beg for your life).")
    while True:
        try:            
            combat = int(input("?"))
            while combat >3 or combat < 0:
                print("Nope thats not an option.")
                combat = int(input("?"))
            break
        except ValueError:
            time.sleep(1)
            print(":(")
            time.sleep(3)
            print("A number goof ball.")
    if combat == 1:
        print("He had a bow this time-_YOU DIED_-")
        time.sleep(1)
        exit()
    elif combat == 2:
        print("You out monuverd him and killed him with your spear") 
        time.sleep(1)
    elif combat == 3:
        print("HE didn't care -_Your dead_- GAME OVER")
        time.sleep(1)
        exit()
print("NOW YOU WILL DISIDE THE FATE OF THIS TOWN!")
time.sleep(3)
print("WIll you 1 suport the town and help it prosper or will you 2 sabotage the village for your own gain?")
time.sleep(0.5)
while True:#the fate of the wourld
        try:            
            fate = int(input("?"))
            while fate >2 or fate < 0:
                print("Nope thats not an option.")
                fate = int(input("?"))
            break
        except ValueError:
            time.sleep(1)
            print(":(")
            time.sleep(3)
            print("A number goof ball.")
if fate ==1:#Good ending
    print("The village goes on to be the best village in the country and prospers beyond your imagination due to your help.")
    print("Thank you", playername)
    time.sleep(2)
    print("THE END")
    exit()
elif fate ==2:#bad ending
    print("(spits in disgust)Mabe you are the monster in the cave that has come out to terrorize the village.")
    time.sleep(1)
    print("I hope your happy.")
    print(playername)
    time.sleep(2)
    print("THE END")
    exit()