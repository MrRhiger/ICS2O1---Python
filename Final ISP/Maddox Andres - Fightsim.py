import random
import time
"""
Andres Arias and Maddox Fisher
Jan 25th
A program that can be used as a “monster fighting” simulation
"""
















player_hp = 100
scorpion_monster = random.randint(100,150)
wolf_monster = random.randint(100,150)
bandit_monster = random.randint(100,120)
anubis_boss = random.randint(150,200)
anubis_damage = random.randint(50,200)
hydra_boss = random.randint(150,250)
hydra_damage = random.randint(50,100)
sphinx_boss = random.randint(200,350)
sphinx_damage = random.randint(10,50)
maddox_Boss = 10000000000
maddox_damage = 10000000000
andres_Boss = 10000000000
andres_damage = 10000000000
genocide = 2 # Kills
pacifist = 0 # Kills
neutral = 1 # Kills
kills = 0
shotgun = random.randint(5,50)
rifle = random.randint(5,35)
revolver = random.randint(5,10)
weapons = "shotgun,rifle,revolver"
wooden_Armor = 50
chainmail_Armor = 150
iron_Armor = 200
Armor = 0
glass_Cannon =   "a shotgun and some wooden armor"
hot_damn = "a rifle and some chainmail armor"
steel_Peashooter = "a revolver and some iron armor"
dev_Armor = 100000000 #health
dev_gun = 100000000 #Dammage
dev_stuff = "DEV GUN, DEV ARMOR"




















print("You are about to embark on a journey beyond your wildest dreams")
time.sleep(2)
print("Each of your decisions lead to a different outcome")
time.sleep(2)
print("So choose wisely")
time.sleep(3)




while True:#NAME OF PLAYER
    name_player = input("Please enter your name:")
    if not name_player.isalpha():
        print("Please enter only your name no numbers")
    else:
        break












final_boss = "Sphinx"




#THE BEGINNING OF LOTS OF DIALOGUE
print("Welcome to the tale of")
time.sleep(1)
print(name_player,"in",end="",flush=True)
time.sleep(1)
print(".",end="",flush=True)
time.sleep(1)
print(".",end="",flush=True)
time.sleep(1)
print(".")
time.sleep(1.5)
print("╭━━━━┳╮╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━╮╱╭╮\n┃╭╮╭╮┃┃╱╱╱╱╱┃╭━╮┃╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭╯╭╯╰╮\n╰╯┃┃╰┫╰━┳━━╮┃╰━━┳━━┳━╮╭━╯┣━━╮╭━━┳╯╰╮╰╮╭╋┳╮╭┳━━╮\n╱╱┃┃╱┃╭╮┃┃━┫╰━━╮┃╭╮┃╭╮┫╭╮┃━━┫┃╭╮┣╮╭╯╱┃┃┣┫╰╯┃┃━┫\n╱╱┃┃╱┃┃┃┃┃━┫┃╰━╯┃╭╮┃┃┃┃╰╯┣━━┃┃╰╯┃┃┃╱╱┃╰┫┃┃┃┃┃━┫\n╱╱╰╯╱╰╯╰┻━━╯╰━━━┻╯╰┻╯╰┻━━┻━━╯╰━━╯╰╯╱╱╰━┻┻┻┻┻━━╯")
































 
time.sleep(2)
print("All around you is darkness")
time.sleep(1)
open_eyes = str(input("Do you open your eyes?(Y/N) "))
if open_eyes == "y" or open_eyes == "Y" or open_eyes == "Yes" or open_eyes == "yes":#WHAT THIS DOES IS BASICALLY SHOW YOU AN ANGEL BUT IF YOU TYPE ANYTHING OTHER THAN YES IT WILL NOT SHOW YOU THE ANGEL
    print("A wall of light comes over you as you open your eyes")
    time.sleep(1.5)
    print("You see an angelic figure approach")
    time.sleep(1)
    print(" _")
    time.sleep(0.2)
    print(" \\")
    time.sleep(0.2)
    print("  \\")
    time.sleep(0.2)
    print("   \\            <*****> ")
    time.sleep(0.2)
    print("    \\     .=^=.  .""",".  .=^=.")
    time.sleep(0.2)
    print("     \\    /```\\ (/a a\)//``` \\")
    time.sleep(0.2)
    print("      \\ {{      (  L  )      }}")
    time.sleep(0.2)
    print("       \\ { _  __ \ = /       }}")
    time.sleep(0.2)
    print("        \\ /@.---,/'-'\,---.  }}")
    time.sleep(0.2)
    print("        /(&\ |`-._/\_.-'|  \ }}")
    time.sleep(0.2)
    print("       (@ \&\|    ||    |\  \}}")
    time.sleep(0.2)
    print("        {{ \ |___o()o___| >  )}")
    time.sleep(0.2)
    print("        {{  `|__((<>))__|` .'}}")
    time.sleep(0.2)
    print("        {{   \   o\/o   /``  }}")
    time.sleep(0.2)
    print("        {{  ,'\   ||   / ',  }}")
    time.sleep(0.2)
    print("        {{.'   \  ||  /|   '.}}")
    time.sleep(0.2)
    print("               |'.||.' |")
    time.sleep(0.2)
    print("               |    :  |")
    time.sleep(0.2)
    print("               |    :  |")
    time.sleep(0.2)
    print("               |    :  |")
    time.sleep(0.2)
    print("               |    :  |")
    time.sleep(0.2)
    print("               |    :  |")
    time.sleep(0.2)
    print("               |    :  |")
    time.sleep(0.2)
    print("               |____:__|")
    time.sleep(0.2)
    print("                (_/ \_)")
















#EVEN MORE DIALOGUE ;-;
time.sleep(2)
print("You hear a voice call to you")
time.sleep(1)
print(name_player,end="",flush=True)
time.sleep(0.2)
print(".",end="",flush=True)
time.sleep(0.2)
print(".",end="",flush=True)
time.sleep(0.2)
print(".\n")
time.sleep(1)
print("You have been chosen to be the one to send a message to the mighty sphinx",end="",flush=True)
time.sleep(0.2)
print(".",end="",flush=True)
time.sleep(0.2)
print(".",end="",flush=True)
time.sleep(0.2)
print(".\n")
time.sleep(1)
time.sleep(2)
print("I will now give you weapons for this dangerous mission")
time.sleep(1.5)
print("I implore you NOT to kill those you defeat")
time.sleep(2)




#FINALLY DIALOGUE IS DONE
















class_choosing = 100
















while class_choosing > 3 and class_choosing != 123 and class_choosing >= 0: # THIS MAKES IT SO THAT YOU CHOOSE WHAT WEAPONS AND ARMORS YOU GET AND TO MAKE IT BALANCED WE GET WEAKEST ARMOR HIGHEST DAMMAGE AND HIGHEST DAMAGE AND WEAKEST WEAPON
    try:
        print("If you wish to use",glass_Cannon,"input 1","If you wish to use",hot_damn,"imput 2", "If you wish to use",steel_Peashooter,"input 3" )
        class_choosing = int(input("Please choose a class here: "))
    except ValueError:
        print("No letters please")
































if class_choosing == 123: # PRETTY SELF EXPLANATORY BUT IF YOU CHOOSE 1 2 OR 3 YOU GET THOSE CLASS TYPES
    print("**!YOU'VE CHOSEN DEV KIT!**")
    Armor = dev_Armor
    weapon =  dev_gun
elif class_choosing == 1:
    print("You've chosen to wield",glass_Cannon)
    Armor = wooden_Armor
    weapon = shotgun
elif class_choosing == 2:
    print("You've chosen to wield",hot_damn)
    Armor = chainmail_Armor
    weapon = rifle
elif class_choosing == 3:
    print("You've chosen to wield",steel_Peashooter)
    Armor = iron_Armor
    weapon = revolver
































for x in range (1,3,1): #GAME LOOP
    enemy = random.randint(1,3)#CHOOSES RANDOM MONSTER
    if enemy == 1:
        enemy = scorpion_monster
        enemy_name = "A Scorpion"
        enemy_art = " ___    ___\n( _<    >_ ) \n//        \\ \n\\___..___// \n `-(    )-' \n   _|__|_ \n  /_|__|_\ \n  /_|__|_\ \n  /_\__/_\ \n   \ || /  _) \n     ||   ( )\n     \\___//\n      `---'"
    elif enemy == 2:
        enemy = wolf_monster
        enemy_name = "A wild Wolf"
        enemy_art = "        _\n       / \      _-'\n     _/|  \-''- _ /\n__-' { |          \ \n    /             \ \n    /       o.  |o }\n    |            \ ;\n                  ',\n       \_         __\ \n         ''-_    \.//\n           / '-____'\n          /\n        _'\n      _-'"
    elif enemy == 3:
        enemy = bandit_monster
        enemy_name = "A mean BANDIT"
        enemy_art = "                  _-'-_\n          /       \n              /          \n            /             \      \n       \___|_______________|____/\n           =               |   \n          _=            __/\n         / _\           (O)\n        | | \            _  \n        | |/            (____)\n         \__/          /   |\n          /           /   __)\n         /    \       \    _)                             \n        \      \           /                             \n      \/ \      \_________/      ___________________________, \n       \/ \      /            \-'    ==== __________________|\n        \/ \    /           __/___  ====_/\n         \/ \  /           (O____)\\_(_)\n                          (O_ ____)\n                           (O____)"
















    if x ==1: #CHOOSE DESERT OR CAVE FIRST AND THEN LEFT OR RIGHT
        print("Now, where would you like to start your quest?")
        left_or_Right = input("(Desert | Cave): ")
        while (left_or_Right != "D" and left_or_Right != "d" and left_or_Right != "Desert" and left_or_Right != "desert" and left_or_Right != "cave" and left_or_Right != "C" and left_or_Right != "c" and left_or_Right != "Cave"):
            print("Please try again")
            left_or_Right = input("(Desert | Cave): ")
    elif x ==2:
        left_or_Right = input("Where do you want to go? (LEFT | RIGHT): ")
        while (left_or_Right != "R" and left_or_Right != "r" and left_or_Right != "Right" and left_or_Right != "right" and left_or_Right != "left" and left_or_Right != "L" and left_or_Right != "l" and left_or_Right != "Left"):
            print("Please try again")
            left_or_Right = input("Where do you want to go? (LEFT | RIGHT): ")        
































    print("You've encountered", enemy_name) #THE ACTUAL GAME SOURCE
    print(enemy_art)
    player_hp = 100+Armor
    full_player_hp = player_hp
    mercy_times = 0
    while player_hp > 0 and enemy > 0 and mercy_times != 5:
        print(name_player,"HP:", player_hp)
        print("Enemy HP:", enemy)
        player_attack = random.randint(0, 50) + weapon
        enemy_attack = random.randint(30, 60)
        print("What would you like to do(1 = attack, 2 = dodge, 3 = Mercy, 4 = heal, 5 = run away)")
        player_fighting_decision = 6
        while player_fighting_decision != 1 and player_fighting_decision != 2 and player_fighting_decision != 3 and player_fighting_decision != 4 and player_fighting_decision != 5:
            try:
                player_fighting_decision = int(input(": "))
                break
            except ValueError:
                print("Sorry please only type in numbers")
       
        if player_fighting_decision != 1 and player_fighting_decision != 2 and player_fighting_decision != 3 and player_fighting_decision != 4 and player_fighting_decision != 5:
            print("Sorry i cant use this")
            while player_fighting_decision != 1 and player_fighting_decision != 2 and player_fighting_decision != 3 and player_fighting_decision != 4 and player_fighting_decision != 5:
                try:
                    player_fighting_decision = int(input("Please choose between 1,5: "))
                    break
                except ValueError:
                    print("Sorry please only type in numbers")








        if player_fighting_decision == 1:
            enemy -= player_attack
            print(name_player,"deals", player_attack, "damage to",enemy_name,end=".",flush=True)
            print("   ")
            player_hp -= enemy_attack
            print(enemy_name,"deals", enemy_attack, "damage to",name_player,end=".",flush=True)
            print(enemy_art)
            print("   ")
            print(name_player,"HP:", player_hp)
            print("Enemy HP:", enemy)
            input("Continue: ")
        elif player_fighting_decision == 2:
            print("You decided to dodge")
            did_enemy_miss = random.randint(1,2) #if equal to 2 enemy missed but if enemy equals 1 he did not miss
            if did_enemy_miss == 1:
                player_hp -= enemy_attack
                print(enemy_name,"deals", enemy_attack, "damage to",name_player,end=".",flush=True)
                print(enemy_art)
                print("   ")
                print(name_player,"HP:", player_hp)
                print("Enemy HP:", enemy)
                input("Continue: ")
            elif did_enemy_miss == 2:
                print("you lucky ducky",enemy_name,"Missed!")
                print(name_player,"HP:", player_hp)
                print("Enemy HP:", enemy)
        elif player_fighting_decision == 3:
            print("You decided to have mercy on the enemy")
            mercy_times = mercy_times+1
            player_hp -= enemy_attack
            print(enemy_name,"deals", enemy_attack, "damage to",name_player,end=".",flush=True)
            print(enemy_art)
            print("   ")
            print(name_player,"HP:", player_hp)
            print("Enemy HP:", enemy)
            input("Continue: ")
        elif player_fighting_decision == 4:
            healing_of_player = random.randint(50,100)
            if  player_hp == full_player_hp or player_hp > full_player_hp:
                print("sorry you cant heal anymore")
            else:
                player_hp = player_hp+healing_of_player
                print("you healed",healing_of_player,"Of health")
        elif player_fighting_decision == 5:
            did_player_run_away = random.randint(1,2)#If its 1 then they ran away if its 2 the enemy didnt let them run away and killed them
            print(did_player_run_away)
            if did_player_run_away == 1:
                print("you ran away like a wimp")
                player_alive = 2
                break
            elif did_player_run_away == 2:
                print("youve tried to run away but the enemy didnt let you escape")
                print("he tortures you and you die")
                print(" _.---,._,'")
                print("/' _.--.<")
                print("  /'     `'")
                print("/' _.---._____")
                print("\.'   ___, .-'`")
                print("    /'    \\             .")
                print("  /'       `-.          -|-")
                print(" |                       |")
                print(" |                   .-'~~~`-.")
                print(" |                 .'         `.")
                print(" |                 |   Game    |")
                print(" |                 |    Over   |")
                print(" |                 |           |")
                print("   \              \\|           |//")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                player_alive = 1
                exit()








        print()
   
   
    if player_hp <= 0 : #YOU HAVE DIED SCREEN
        print(" _.---,._,'")
        print("/' _.--.<")
        print("  /'     `'")
        print("/' _.---._____")
        print("\.'   ___, .-'`")
        print("    /'    \\             .")
        print("  /'       `-.          -|-")
        print(" |                       |")
        print(" |                   .-'~~~`-.")
        print(" |                 .'         `.")
        print(" |                 |   Game    |")
        print(" |                 |    Over   |")
        print(" |                 |           |")
        print("   \              \\|           |//")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        player_alive = 1
        break
    elif enemy <=0 or mercy_times == 5: #MAKES IT SO THAT IF YOU DEFEATED THE ENEMY YOU HAVE THE OPPORTUNITY TO KILL IT
        player_alive = 2
        if mercy_times == 5:
            print("The enemy got really tired and quit")
            death_decision = input("Do you want to kill the enemy? (Y|N): ")
        else:
            print("Player has defeated the enemy!")
            death_decision = input("Do you want to kill the enemy? (Y|N): ")
















   
    #IF THEY TYPE YES OR NO IT WILL CONVERT TO AN INTEGER
    if player_alive == 2:
        while (death_decision != "y" and death_decision != "Y" and death_decision != "yes" and death_decision != "Yes" and death_decision != "N" and death_decision != "n" and death_decision != "No" and death_decision != "no"):
            print("Please try again")
            death_decision = input("Do you want to kill the enemy? (Y|N): ")












        if death_decision == "y" or death_decision == "Y" or death_decision == "yes" or death_decision == "Yes":
            death_decision = 1
   
        elif death_decision == "N" or death_decision == "n" or death_decision == "No" or death_decision == "no":
            death_decision = 2
   #IF YOU KILL ALL  THE MONSTERS YOU GET THE GENOCIDE RUN AND FIGHT AN ALMOST UNBEATABLE BOSS
        if (death_decision == 1):
            kills = kills+1
            print("You have slaughtered", enemy_name)
            time.sleep(1)
            print(" _")
            time.sleep(0.2)
            print(" \\")
            time.sleep(0.2)
            print("  \\")
            time.sleep(0.2)
            print("   \\            <*****> ")
            time.sleep(0.2)
            print("    \\     .=^=.  .""",".  .=^=.")
            time.sleep(0.2)
            print("     \\    /```\\ (/D D\)//``` \\")
            time.sleep(0.2)
            print("      \\ {{      (  L  )      }}")
            time.sleep(0.2)
            print("       \\ { _  __ \ n /       }}")
            time.sleep(0.2)
            print("        \\ /@.---,/'-'\,---.  }}")
            time.sleep(0.2)
            print("        /(&\ |`-._/\_.-'|  \ }}")
            time.sleep(0.2)
            print("       (@ \&\|    ||    |\  \}}")
            time.sleep(0.2)
            print("        {{ \ |___o()o___| >  )}")
            time.sleep(0.2)
            print("        {{  `|__((<>))__|` .'}}")
            time.sleep(0.2)
            print("        {{   \   o\/o   /``  }}")
            time.sleep(0.2)
            print("        {{  ,'\   ||   / ',  }}")
            time.sleep(0.2)
            print("        {{.'   \  ||  /|   '.}}")
            time.sleep(0.2)
            print("               |'.||.' |")
            time.sleep(0.2)
            print("               |    :  |")
            time.sleep(0.2)
            print("               |    :  |")
            time.sleep(0.2)
            print("               |    :  |")
            time.sleep(0.2)
            print("               |    :  |")
            time.sleep(0.2)
            print("               |    :  |")
            time.sleep(0.2)
            print("               |    :  |")
            time.sleep(0.2)
            print("               |____:__|")
            time.sleep(0.2)
            print("                (_/ \_)")
            print("    ")
            time.sleep(1)
            print("Do not kill!")
        elif (death_decision == 2): # YOU DIDN'T KILL IT GOOD JOB
            kills = kills+0
            print("You had mercy on",enemy_name) #
            print("           ")








# THIS CHOOSES THE BOSS YOU FACE
if kills == 2:
    final_boss = "Anubis"
    final_boss_health = anubis_boss
    final_boss_Damage = anubis_damage
    final_boss_art= "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡇⠀⢠⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡇⢠⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⢸⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡀⠙⠛⠃⠘⠻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠐⠚⣛⣛⣁⡀⠹⣿⣿⣶⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⣠⣴⠶⠿⠛⠛⠛⠛⠛⠀⢻⣿⣿⣤⣀⣙⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⣈⣁⣤⣴⣶⠶⠿⠿⠿⠿⠇⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⡄⠀\n⠀⠀⠐⠛⢉⣉⣠⣤⣤⣶⣶⣶⣶⣦⠀⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠛⠉⠀⠀\n⠀⠀⡾⠛⠉⠉⠉⠙⠻⢿⣿⣿⣿⣿⡀⢹⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡇⠘⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡇⠀⣾⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⢿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠀⠀⠸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠀⠀⠀⠋⠁⠀⠀"
elif kills == 0:
    final_boss = "the Sphinx"
    final_boss_health = sphinx_boss
    final_boss_Damage = sphinx_damage
    final_boss_art= "              ___\n                     .///.\n                    /|<> <>!\ \n                   /-|  ^  !-\ \n                  /-- \_=_/ --\ \n                  )---| W |---(\n                 /-\--| W |--/-\ \n                (_-_--|_-_|--___)\n               (-___  -_-- _-- -_)\n               )-_ _--_ _ ___--__|\n               (___ --__  __ __--(\n              /-_  / __ -_ -__  \_\ \n             _>/  -- /|___| _ \ -_ )\n            /--  _ - _/ _ \>\ -  -- \ \n           ( / / /   > |~l \   \ \ \_)\n        jjs| |-' | |/  "
elif kills == 1:
    final_boss = "the Hydra"
    final_boss_health = hydra_boss
    final_boss_Damage = hydra_damage
    final_boss_art = "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⣠⣦⣄⣀⣴⣦⣄⣈⣻⣿⣿⣿⣿⣿⣿⡇⠀\n⠀⠀⠀⠀⠀⠀⣀⡀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀\n⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⠁⠀⠀⠀⠀⠀⠸⢿⣿⣷⣄⣀⠀⠀\n⠀⠀⠀⣶⣶⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀\n⠀⣀⣠⣿⣿⣿⡿⠟⠁⠀⢀⣄⣀⣠⣦⣀⣠⣄⠀⢹⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⣿⣿⣿⣿⡿⠁⣰⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀\n⠀⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⠟⠛⠉⠉⠉⠉⠙⢻⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀\n⠀⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⠁⠀⠀⠹⠛⠁⠀⠀⠀\n⠀⣿⣿⣿⣿⣿⣿⣿⣧⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⠄⠀⠀⠀⠀⠀⠀⠀\n⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⡄⠀⠀⢀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⣿⣿⣿⣿⡿⠟⠛⠛⠛⠻⠿⣿⣿⣷⣤⣆⠀⣈⠻⣿⣿⣿⣿⣶⣶⣶⠆⠀⠀\n⠀⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠉⠉⠀⠀⠀\n⠀⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠹⢿⣿⣷⣄⣀⠀⠀⠀⠀\n⠀⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀"
















#THESE ARE SECRET BOSSES




if name_player == "Maddox":
    final_boss = "Andres"
    final_boss_health = andres_Boss
    final_boss_Damage = andres_damage
    final_boss_art = "⠀⠀⠀⣀⣠⣴⠖⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⡶⠚⢻⡁⢀⠃⣀⠤⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⡤⢤⠴⠖⠒⠒⠒⣦⠀\n⡇⠀⠈⢣⢸⡜⠁⠀⣠⠽⢦⡀⣀⡤⠶⠚⠋⠉⠁⠀⠀⠀⠀⢷⣿⣷⡀⠀⠘⡆\n⠘⣄⠀⣀⡿⣇⡠⠊⣀⡴⠚⠉⠁⣾⣿⣷⡄⠀⠀⠀⠀⠀⠀⢸⣿⣯⣄⠀⠀⢳\n⠴⠚⠋⠁⠀⣨⠷⠋⠹⡀⠀⠀⠀⣿⣿⣿⡃⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⣸\n⠀⠀⠀⠀⡞⠁⠀⠀⠀⠣⡀⠀⠀⠘⣿⣿⣿⣧⠀⠀⠀⠀⠀⣼⡁⢀⣸⣇⡠⣿\n⠀⠀⢀⡴⢻⡀⠀⠀⠀⠀⠘⠦⡀⠀⠈⠛⠛⠃⠀⠀⠀⡠⠊⠀⠈⠁⠀⠀⢀⡇\n⠀⠀⣾⠁⠀⣷⡀⠀⠀⠀⠀⢀⣈⣑⠒⠂⠤⠄⠒⠒⣉⣀⣀⠀⠀⠀⠀⠀⡼⠁\n⠀⠀⣿⠀⠀⢧⠳⣄⠀⠀⠀⡿⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣠⠞⠁⠀\n⠀⠀⠘⣆⠀⢈⣙⣿⢷⣤⡀⠑⢄⡀⠀⠀⠙⠄⠉⠻⣿⡿⠟⢁⣠⣾⣅⣀⠀⠀\n⠀⠀⠀⠈⣳⠋⡾⠁⡼⠀⠙⣷⣦⣬⣉⣒⣒⣒⣋⣉⣡⣤⣶⣿⣿⣿⣿⣿⣿⣷\n⠀⠀⠀⠀⡇⠀⡇⠀⢇⠀⢠⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛\n⠀⠀⠀⠀⠳⣤⢷⣤⣾⣿⣿⣿⠶⢦⡖⠚⠛⠻⢿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⣄\n⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⡇⠀⢹⠐⠒⠀⠀⠹⣏⠀⠀⠀⠀⠀⠀⠀⠀⢸"
elif name_player == "Andres":
    final_boss = "Maddox"
    final_boss_health = maddox_Boss
    final_boss_Damage = maddox_damage
    final_boss_art = "𓆞"
   
if player_alive == 2:#BOSS DIALOGUE
    time.sleep(2)
    print("As you walk up to the pyramid", final_boss," appears!")
    time.sleep(1)
    print(final_boss_art)
    time.sleep(2)
    if name_player == "Andres":
        print("Its you",end="",flush=True)
        time.sleep(0.2)
        print(".",end="",flush=True)
        time.sleep(0.2)
        print(".",end="",flush=True)
        time.sleep(0.2)
        print(".\n")
        print("My old arch nemesis")
        time.sleep(2)
        print("You shall face my wrath")
        time.sleep(2)
        print("")
    elif name_player == "Maddox":
        print("Your fighting the guy who wrote the code")
        time.sleep(2)
        print("So uhh theres no dialogue just fight me already")
        time.sleep(2)
        print("")
    elif kills == 2:
        print("You have slaughtered too many to be allowed to pass!")
        time.sleep(2)
        print("")
    elif kills == 0:
        print("What are you doing in my pyramid!")
        time.sleep(2)
        print("")
    elif kills == 1:
        print("A portal appears underfoot")
        time.sleep(2)
        print("You find yourself in a barren field, with no colour")
        time.sleep(2)
        print("You see",final_boss,"fly down")
        time.sleep(2)
        print("RAHGHAHGAHGAHEHAGEHGEHURHAGEURHSAHg")
        time.sleep(2)
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⣠⣦⣄⣀⣴⣦⣄⣈⣻⣿⣿⣿⣿⣿⣿⡇⠀\n⠀⠀⠀⠀⠀⠀⣀⡀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀\n⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⠁⠀⠀⠀⠀⠀⠸⢿⣿⣷⣄⣀⠀⠀\n⠀⠀⠀⣶⣶⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀\n⠀⣀⣠⣿⣿⣿⡿⠟⠁⠀⢀⣄⣀⣠⣦⣀⣠⣄⠀⢹⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⣿⣿⣿⣿⡿⠁⣰⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀\n⠀⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⠟⠛⠉⠉⠉⠉⠙⢻⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀\n⠀⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⠁⠀⠀⠹⠛⠁⠀⠀⠀\n⠀⣿⣿⣿⣿⣿⣿⣿⣧⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⠄⠀⠀⠀⠀⠀⠀⠀\n⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⡄⠀⠀⢀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⣿⣿⣿⣿⡿⠟⠛⠛⠛⠻⠿⣿⣿⣷⣤⣆⠀⣈⠻⣿⣿⣿⣿⣶⣶⣶⠆⠀⠀\n⠀⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠉⠉⠀⠀⠀\n⠀⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠹⢿⣿⣷⣄⣀⠀⠀⠀⠀\n⠀⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀")
        time.sleep(2)








    player_hp = 100+Armor#BOSS FIGHT
    full_player_hp = player_hp
    while player_hp > 0 and final_boss_health > 0 and mercy_times != 5:
        print(name_player,"HP:", player_hp)
        print("BOSS HP:", final_boss_health)
        player_attack = random.randint(0, 50) + weapon
        print("What would you like to do(1 = attack, 2 = dodge, 3 = Mercy, 4 = heal, 5 = run away)")
        player_fighting_decision = 6
        while player_fighting_decision != 1 and player_fighting_decision != 2 and player_fighting_decision != 3 and player_fighting_decision != 4 and player_fighting_decision != 5:
            try:
                player_fighting_decision = int(input(": "))
                break
            except ValueError:
                print("Sorry please only type in numbers")
       
        if player_fighting_decision != 1 and player_fighting_decision != 2 and player_fighting_decision != 3 and player_fighting_decision != 4 and player_fighting_decision != 5:
            print("Sorry i cant use this")
            while player_fighting_decision != 1 and player_fighting_decision != 2 and player_fighting_decision != 3 and player_fighting_decision != 4 and player_fighting_decision != 5:
                try:
                    player_fighting_decision = int(input("Please choose between 1,5: "))
                    break
                except ValueError:
                    print("Sorry please only type in numbers")








        if player_fighting_decision == 1: #attack
            final_boss_health -= player_attack
            print(name_player,"deals", player_attack, "damage to",final_boss,end=".",flush=True)
            print("   ")
            player_hp -= final_boss_Damage
            print(final_boss,"deals", final_boss_Damage, "damage to",name_player,end=".",flush=True)
            print("   ")
            print(final_boss_art)
            print(name_player,"HP:", player_hp)
            print("BOSS HP:", final_boss_health)
            input("Continue: ")
        elif player_fighting_decision == 2:
            print("You decided to dodge")
            did_enemy_miss = random.randint(1,2) #if equal to 2 enemy missed but if enemy equals 1 he did not miss
            if did_enemy_miss == 1:
                player_hp -= final_boss_Damage
                print(final_boss,"deals", final_boss_Damage, "damage to",name_player,end=".",flush=True)
                print("   ")
                print(final_boss_art)
                print(name_player,"HP:", player_hp)
                print("BOSS HP:", final_boss_health)
                input("Continue: ")
            elif did_enemy_miss == 2:
                print("you lucky ducky",final_boss,"Missed!")
                print(name_player,"HP:", player_hp)
                print("BOSS HP:", final_boss_health)
        elif player_fighting_decision == 3:
            print("You decided to have mercy on the enemy")
            mercy_times = mercy_times+1
            player_hp -= final_boss_Damage
            print(final_boss,"deals", final_boss_Damage, "damage to",name_player,end=".",flush=True)
            print("   ")
            print(final_boss_art)
            print(name_player,"HP:", player_hp)
            print("BOSS HP:", final_boss_health)
            input("Continue: ")
        elif player_fighting_decision == 4:
            healing_of_player = random.randint(50,100)
            if  player_hp == full_player_hp or player_hp > full_player_hp:
                print("sorry you cant heal anymore")
            else:
                player_hp = player_hp+healing_of_player
                print("you healed",healing_of_player,"Of health")
        elif player_fighting_decision == 5:
            did_player_run_away = random.randint(1,2)#If its 1 then they ran away if its 2 the enemy didnt let them run away and killed them
            print(did_player_run_away)
            if did_player_run_away == 1: #  diaoulgeu of you failing mission
                time.sleep(1)
                print(" _")
                time.sleep(0.2)
                print(" \\")
                time.sleep(0.2)
                print("  \\")
                time.sleep(0.2)
                print("   \\            <*****> ")
                time.sleep(0.2)
                print("    \\     .=^=.  .""",".  .=^=.")
                time.sleep(0.2)
                print("     \\    /```\\ (/D D\)//``` \\")
                time.sleep(0.2)
                print("      \\ {{      (  L  )      }}")
                time.sleep(0.2)
                print("       \\ { _  __ \ n /       }}")
                time.sleep(0.2)
                print("        \\ /@.---,/'-'\,---.  }}")
                time.sleep(0.2)
                print("        /(&\ |`-._/\_.-'|  \ }}")
                time.sleep(0.2)
                print("       (@ \&\|    ||    |\  \}}")
                time.sleep(0.2)
                print("        {{ \ |___o()o___| >  )}")
                time.sleep(0.2)
                print("        {{  `|__((<>))__|` .'}}")
                time.sleep(0.2)
                print("        {{   \   o\/o   /``  }}")
                time.sleep(0.2)
                print("        {{  ,'\   ||   / ',  }}")
                time.sleep(0.2)
                print("        {{.'   \  ||  /|   '.}}")
                time.sleep(0.2)
                print("               |'.||.' |")
                time.sleep(0.2)
                print("               |    :  |")
                time.sleep(0.2)
                print("               |    :  |")
                time.sleep(0.2)
                print("               |    :  |")
                time.sleep(0.2)
                print("               |    :  |")
                time.sleep(0.2)
                print("               |    :  |")
                time.sleep(0.2)
                print("               |    :  |")
                time.sleep(0.2)
                print("               |____:__|")
                time.sleep(0.2)
                print("                (_/ \_)")
                print("    ")
                time.sleep(1)
                print("You have failed your mission")
                time.sleep(2)
                print(" _.---,._,'")
                print("/' _.--.<")
                print("  /'     `'")
                print("/' _.---._____")
                print("\.'   ___, .-'`")
                print("    /'    \\             .")
                print("  /'       `-.          -|-")
                print(" |                       |")
                print(" |                   .-'~~~`-.")
                print(" |                 .'         `.")
                print(" |                 |   Game    |")
                print(" |                 |    Over   |")
                print(" |                 |           |")
                print("   \              \\|           |//")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                player_alive = 2
                exit()








        elif final_boss_health <=0:
            print("You have defeated",final_boss,"but at what cost?",end="",flush=True)
            time.sleep(0.2)
            print(".",end="",flush=True)
            time.sleep(0.2)
            print(".",end="",flush=True)
            time.sleep(0.2)
            print(".\n")
            time.sleep(1.5)
            print("╭━━━━┳╮╱╱╱╱╱╭━━━╮╱╱╱╱╭┳━━━╮\n┃╭╮╭╮┃┃╱╱╱╱╱┃╭━━╯╱╱╱╱┃┃╭━╮┃\n╰╯┃┃╰┫╰━┳━━╮┃╰━━┳━╮╭━╯┣╯╭╯┃\n╱╱┃┃╱┃╭╮┃┃━┫┃╭━━┫╭╮┫╭╮┃╱┃╭╯\n╱╱┃┃╱┃┃┃┃┃━┫┃╰━━┫┃┃┃╰╯┃╱╭╮\n╱╱╰╯╱╰╯╰┻━━╯╰━━━┻╯╰┻━━╯╱╰╯")
        elif mercy_times == 5:
            print(final_boss,"wheezes")
            yn = input("Would you like to explain why you're here? (Y/N)")
            if yn == "y" or yn == "Y" or yn == "Yes" or yn == "yes":
                print("You explain to him that you're on an important mission") 
                time.sleep(2)
                print("He lets you pass")
                time.sleep(2)            
                print("YOU WIN (GOOD ENDING)")
            elif yn == "n" or yn == "N" or yn == "No" or yn == "no":
                print(" _.---,._,'")
                print("/' _.--.<")
                print("  /'     `'")
                print("/' _.---._____")
                print("\.'   ___, .-'`")
                print("    /'    \\             .")
                print("  /'       `-.          -|-")
                print(" |                       |")
                print(" |                   .-'~~~`-.")
                print(" |                 .'         `.")
                print(" |                 |   Game    |")
                print(" |                 |    Over   |")
                print(" |                 |           |")
                print("   \              \\|           |//")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")































