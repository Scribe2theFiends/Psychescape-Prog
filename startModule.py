from formatModule import breakline,inbreakline,error
import saveModule as save
import roomModule as room
import time
import sys
import varModule as var

#TITLE
def start():
    time.sleep(0.4)
    createdBy()
    print("\n")
    for char in "                              _______   _    _   _____\n                             |__   __| | |  | | |  ___|\n                                | |    | |__| | | |_ \n                                | |    |  __  | |  _|\n                                | |    | |  | | | |___\n                                |_|    |_|  |_| |_____|\n\n\n ____      ___  __     __   _____   _____      ___    _____    ___    ____    _____\n|  _ \    / __| \ \   / /  /  ___| |  ___|    / __|  /  ___|  / _ \  |  _ \  |  ___|\n| |_| |  / /     \ \ / /  /  /     | |_      / /    /  /     / |_| \ | |_| | | |_\n|  __/   | |      \ V /   | |      |  _|     | |    | |      |  _  | |  __/  |  _|\n| |      _\ \      | |    \  \___  | |___    _\ \   \  \___  | | | | | |     | |___\n|_|     |___/      |_|     \_____| |_____|  |___/    \_____| |_| |_| |_|     |_____|":
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.04)
    print("\n")
    print("|", end="\r")
    time.sleep(0.25)
    print("/", end="\r")
    time.sleep(0.25)
    print("-", end="\r")
    time.sleep(0.25)
    print("\\", end="\r")
    time.sleep(0.25)
    print("|", end="\r")
    time.sleep(0.25)
    print("/", end="\r")
    time.sleep(0.25)
    print("-", end="\r")
    time.sleep(0.25)
    print("\\", end="\r")
    time.sleep(0.25)
    for char in "COMPLETED!!!!\n":
        print(char, end="")
        sys.stdout.flush()
        time.sleep(0.125)
    breakline()
    startCommand()

#STARTING COMMAND

def startCommand():
    answer = input("Type (start) to start. Type (load) to load a previous save. Type (help) for help. => ")
    if answer.lower().strip() == "start":
        charCreation()
        var.doTurn = False
        room.mine()
    elif answer.lower().strip() == "help":
        startHelpScreen()
    elif answer.lower().strip() == "load":
        inbreakline()
        save.load()
    else:
        error()
        reStartCommand()

#RESTARTING COMMAND

def reStartCommand():
    answer = input("Type (start) to start. Type (load) to load a previous save. Type (help) for help.\nIf you would like to quit the game, kill it through the exit button in the top right corner of the program. => ")
    if answer.lower().strip() == "start":
        charCreation()
        var.doTurn = False
        room.mine()
    elif answer.lower().strip() == "help":
        startHelpScreen()
    elif answer.lower().strip() == "load":
        inbreakline()
        save.load()
    else:
        error()
        reStartCommand()

#START SCREEN HELP

def startHelpScreen():
    inbreakline()
    print("  When you are able to enter a command you will see a \"=>\"")
    print("  You can see what you have to enter for a command to work as it is encased within parentheses \"()\"")
    print("  Some commands can be executed from anywhere in-game, and therefor are not listed with the other commands.")
    print("    One such example is the (inventory) command, which lets you see your inventory.")
    print("    Another command is the (help) command, that shows different information in game than it does here.")
    print("  When typing your command, don't worry about if you accidentally added a space or capitalized, your command will be processed all the same. If you are playing and find that this is not the case, please contact me to fix the potential bug. Screenshots of you command are much appreciated :)")
    breakline()
    reStartCommand()

def createdBy():
    for char in "CREATED BY AMARANTHUS STUDIOS": 
        print(char, end='') 
        sys.stdout.flush() 
        time.sleep(0.4)

def waitTime():
    time.sleep(0.1)
    print("")

def charCreation():
    breakline()
    print("Now it is time for some character creation. First, choose your alignment. Your alignment will decide what sorts of alchemy you can perfom. Ice alignment of course will align you to, well Ice, and Fire alignment to Fire. Fire is more centered on dealing continuous damage to your enemy, while Ice is more centered around slowing and stopping your enemy. Your alignment will also determine which elemental damage type you will be proficient in, pyro or cryo damage. (proficiency just means you will be able to level up faster in that skill)")
    print("\n  (fire)")
    print("  (ice)")
    answer = input("\nChoose your alignment => ")
    if answer.lower().strip() == "fire":
        var.alignment = 2
        charCreationII()
    elif answer.lower().strip() == "ice":
        var.alignment = 1
        charCreationII()
    else:
        error()
        charCreation()

def charCreationII():
    inbreakline()
    print("Now you can choose which physical damage type you are proficient in. Each has it's use against different types of enemies, with some being resistant to different types of damage and weak to others.")
    print("\n  (piercing)")
    print("  (blunt)")
    print("  (slashing)")
    answer = input("\nChoose your physical damage proficiency => ")
    if answer.lower().strip() == "piercing":
        var.physicalProficiency = 1
        charCreationIII()
    elif answer.lower().strip() == "blunt":
        var.physicalProficiency = 2
        charCreationIII()
    elif answer.lower().strip() == "slashing":
        var.physicalProficiency = 3
        charCreationIII()
    else:
        error()
        charCreationII()

def charCreationIII():
    inbreakline()
    print("One final thing. Choose if you wish to be proficient in ranged or melee combat. Ranged combat is useful for ambush and hunting, while melee is slightly stronger.")
    print("\n  (melee)")
    print("  (ranged)")
    answer = input("\nChoose your type proficiency => ")
    if answer.lower().strip() == "melee":
        var.typeProficiency = 1
    elif answer.lower().strip() == "ranged":
        var.typeProficiency = 2
    else:
        error()
        charCreationIII()