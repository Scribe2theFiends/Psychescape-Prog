import varModule as var
from formatModule import breakline,inbreakline,error
import roomModule as room
import fightModule as fight
import timeModule as time

def armoury():
    breakline()
    print("You step into the armoury, looking about at all of their wares, various things lining the walls, shields, maces, swords, a gruff looking man stands behind the counter, and you can hear ruslting and clanging coming from somewhere in the back. \"Look before you ask for anything here, we're still getting a bit set up. So we are only selling a few things.\" The man says as you look around. \"We don't want to sell everything and then not be able to get more stock. Feel free to look at what's on that board over on the far wall for what we are willing to currently sell. Also if you want to try out some of your equipment, there's a dummy over in that corner I was thinking of getting rid of you can use.\"")
    print("\n  You may buy some equipment. (buy)")
    print("  You can train with the dummy. (train)")
    print("  You may exit the building. (exit)")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "exit":
        var.doTurn = False
        room.mercantile()
    elif answer.lower().strip() == "buy":
        armouryStore()
    elif answer.lower().strip() == "train":
        var.doTurn = False
        training()
    else:
        error()
        armoury()

def armouryStore():
    inbreakline()
    print("Currently what the armoury will sell is quite limited.")
    print("\n  You can buy (weapons)")
    print("  You can buy (ammunition)")
    print("  You can (exit) this menu.")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "weapons":
        armouryStoreWeapons()
    elif answer.lower().strip() == "ammunition":
        armouryStoreAmmunition()
    elif answer.lower().strip() == "exit":
        armoury()
    else:
        error()
        armouryStore()

def armouryStoreWeapons():
    inbreakline()
    if var.hasBow == False:
        print("Bow = 10 unity (bow)")
    if var.hasSling == False:
        print("Sling = 8 unity (sling)")
    print("Chakram = 4 unity (chakram)")
    if var.hasSword == False:
        print("Sword = 8 unity (sword)")
    if var.hasMace == False:
        print("Mace = 10 unity (mace)")
    print("Dagger = 6 Unity (dagger)")
    print("You can (exit) this menu.")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "sling":
        inbreakline()
        if var.hasSling == False:
            if var.unifiedCount >= 8:
                print("You purchase one [1] SLING.")
                var.hasSling = True
                var.unifiedCount -= 8
            else:
                print("You do not have enough money to buy that!")
        else:
            print("You already have a sling.")
        armouryStoreWeapons()
    elif answer.lower().strip() == "bow":
        inbreakline()
        if var.hasBow == False:
            if var.unifiedCount >= 10:
                print("You purchase one [1] BOW.")
                var.hasBow = True
                var.unifiedCount -= 10
            else:
                print("You do not have enough money to buy that!")
        else:
            print("You already have a bow.")
        armouryStoreWeapons()
    elif answer.lower().strip() == "chakram":
        inbreakline()
        if var.unifiedCount >= 4:
            print("You purchase one [1] CHAKRAM")
            var.chakrams += 1
            var.unifiedCount -= 4
        else:
            print("You do not have enough money to buy that!")
        armouryStoreWeapons()
    elif answer.lower().strip() == "sword":
        inbreakline()
        if var.hasSword == False:
            if var.unifiedCount >= 8:
                print("You purchase one [1] SWORD.")
                var.hasSword = True
                var.unifiedCount -= 8
            else:
                print("You don't have enough money to buy that!")
        else:
            print("You already have a sword.")
        armouryStoreWeapons()
    elif answer.lower().strip() == "mace":
        inbreakline()
        if var.hasMace == False:
            if var.unifiedCount >= 10:
                print("You purchase one [1] MACE.")
                var.hasMace = True
                var.unifiedCount -= 10
            else:
                print("You don't have enough money to buy that!")
        else:
            print("You already have a mace.")
        armouryStoreWeapons()
    elif answer.lower().strip() == "dagger":
        inbreakline()
        if var.unifiedCount >= 6:
            print("You purchase one [1] DAGGER.")
            var.daggers += 1
            var.unifiedCount -= 6
        else:
            print("You don't have enough money to buy that!")
        armouryStoreWeapons()
    elif answer.lower().strip() == "exit":
        inbreakline()
        print("Exiting the menu.")
        armouryStore()
    else:
        error()
        armouryStoreWeapons()

def armouryStoreAmmunition():
    inbreakline()
    print("4 arrows = 3 unity (arrows)")
    print("6 shot = 3 unity (shot)")
    print("You can (exit) this menu.")
    answer = input("\nEnter command here => ")
    inbreakline()
    if answer.lower().strip() == "arrows":
        if var.unifiedCount >= 3:
            print("You purchase a bundle of arrows.")
            var.arrows += 4
            var.unifiedCount -= 3
        else:
            print("You don't have the money to buy that!")
        armouryStoreAmmunition()
    elif answer.lower().strip() == "shot":
        if var.unifiedCount >= 3:
            print("You purchase a handful of shot.")
            var.shot += 6
            var.unifiedCount -= 3
        else:
            print("You don't have enough money to buy that!")
        armouryStoreAmmunition()
    elif answer.lower().strip() == "exit":
        print("Closing the menu.")
        armouryStore()
    else:
        error()
        armouryStoreAmmunition()

def trainingIntro():
    inbreakline()
    print("You are now in a mock fight with the dummy. It will not fight back, and all EXP gains will be quartered ")

def training():
    time.turnInc()
    fight.playerFightStats()
    print("\n  You can end your training (end)")
    print("  You can attack! (attack)")
    print("  You can use your alchemical skills! (alchemy)")
    print("  You can change your weapon. (weapon)")
    answer = input("\nEnter command here => ")
    fight.playerFightStats()
    if answer.lower().strip() == "end":
        fight.recovery()
        armoury()
    elif answer.lower().strip() == "attack":
        var.EXPdiluter = 4
        fight.attack()
        print(f"\nYou do {var.finalAttack} damage!")
        training()
    elif answer.lower().strip() == "weapon":
        fight.switchWeapon()
        training()
    elif answer.lower().strip() == "alchemy":
        fight.alchemy()
        training()
    else:
        var.doTurn = False
        error()
        training()

#GENERAL STORE

justEntered = False

def generalStore():
    global justEntered
    if justEntered == True:
        breakline()
        print(f"As you step into the general store, a bell rings, and a not two seconds later a figure is at your side. turning to look you see a glowingly happy face just about a foot away from your own. \"Greetings! How are you today?! {var.talkList[0]} Well either way welcome to Hrath-Ryn's General Store! I hope you can find what you need, and if you can't, {var.talkList[1]}\" She points to the counter where a demon leans on their elbow looking bored. He gives you a quick look and then returns to looking at the counter. \"He's not very good with people he doesn't know, but he's nice. He'll even jingle the bell for you!\" She gives a little bow and quickly bounds away behind some curtains.")
        justEntered = False
        inbreakline()
    else:
        breakline()
    print("You stand in a general store. It seem s that variety of things are sold here, but only a few look useful to you right now.")
    print("\n  You can buy something. (buy)")
    print(f"  You may approach {var.talkList[2]}. (approach)")
    print("  You may jingle the bell on the counter. (jingle)")
    print("  You may exit the store. (exit)")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "buy":
        generalStoreStore()
    elif answer.lower().strip() == "approach":
        ...
    elif answer.lower().strip() == "jingle":
        ...
    elif answer.lower().strip() == "exit":
        room.mercantile()
    else:
        error()
        generalStore()

#GENERAL STORE STORE

def generalStoreStore():
    inbreakline()
    print(f"As you browse the wares and think about your purchases, {var.talkList[2]} eyes follow you, his tails flicking about behind him, boredly fidgeting with each other.")
    if var.flasks < 2:
        print("\n  Flask = 4 U= (flask)")
    if var.pouchs < 4:
        print("  Pill Pouch = 4 U= (pouch)")
    print("  You may exit this menu. (exit)")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "flask" and var.flasks < 2 and var.unifiedCount > 3:
        inbreakline()
        purchased("flask")
        var.flasks += 1
        var.flaskContent.append("EMPTY")
        generalStoreStore()
    elif answer.lower().strip() == "flask" and var.flasks < 2 and var.unifiedCount < 4:
        inbreakline()
        cantPurchase("flask","U=")
        generalStoreStore()
    elif answer.lower().strip() == "pouch" and var.pouchs < 4 and var.unifiedCount > 3:
        inbreakline()
        purchased("flask")
        var.pouchs += 1
        var.pouchContent.append("EMPTY")
        generalStoreStore()
    elif answer.lower().strip() == "pouch" and var.pouchs < 4 and var.unifiedCount < 4:
        inbreakline()
        cantPurchase("flask","U=")
    elif answer.lower().strip() == "exit":
        inbreakline()
        print("Exiting the menu.")
        generalStore()
    else:
        error()
        generalStoreStore()

#PURCHASED

def purchased(name):
    print(f"You purchased a {name}.")

def cantPurchase(name,currency):
    print(f"You do not have enough {currency} to purchase a {name}.")

#APPROACH SHO'TSAHL
shoTalked = False

def approachShoTsahl():
    global talked
    inbreakline()
    print(f"You walk up to {var.talkList[2]}, his tails stop fidgeting and he raises his head from his hands, still looking bored. \"What is it?\"")
    print(f"\n  You may talk to {var.talkList[2]} (talk)")
    print(f"  You may look at {var.talkList[2]}'s appearance. (look)")
    print("  You may leave him alone. (exit)")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "talk":
        ...
    elif answer.lower().strip() == "look":
        ...
    elif answer.lower().strip() == "exit":
        inbreakline()
        if shoTalked == False:
            print(f"You hear {var.talkList[2]} mumble \"Why do they have to be so weird?\" under his breath as you walk away.")
        else:
            print(f"Before you turn around to leave, you hear {var.talkList[2]} say ")