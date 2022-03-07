import varModule as var
import roomModule as room
from formatModule import inbreakline,error
from random import randint
import containersModule as containers

def chatter():
    chatterValue = randint(1,4)
    inbreakline()
    if chatterValue == 1:
        print("\"You know, further into town there's this place where you can get all sorts of weapons? And I'm talking all sorts of stuff, slings, bows, daggers, maces, all sorts of quality lethal equipment. Good for roughing up demons or slaughtering prey.\"")
    elif chatterValue == 2:
        print("\"I hear that there's a place in town that'll help you build a place to life. I'm hoping I can save up enough to get a nice little house by an ichor pool, so I can take a nice warm dip when I just want to relax after a long day's worth of hard work.\"")
    elif chatterValue == 3:
        print("\"Be careful what you get here if you plan on doing much, or at least wait until you are in the right head to do anything important.\"")
    elif chatterValue == 4:
        print("\"Have you ever performed alchemy? No? Don't worry I feel you'll be able to quite soon.\"")
    var.doTurn = False

def order():
    inbreakline()
    print("You walk up to the counter, getting a good look at everything on the counter back there; bottles of liquid, dried goods, fruits, various containers and apparatuses for mixing and making food, drink, and Nonx'Ran")
    print("\"Take a good look at the menu before you decide to ask for anything, and make sure you can afford it, it's very rare I barter here. You pay before you get your stuff.\" says the demon from behind the bar, not even bothering to turn around to see you as they speak.")
    print("\n  You may check the menu for (food)")
    print("  You may check the menu for (drink)")
    print("  You may check the menu for Nonx'Ran (nonxran)")
    print("  You may exit this menu with (exit)")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "food":
        foodOrder()
    elif answer.lower().strip() == "drink":
        drinkOrder()
    elif answer.lower().strip() == "nonxran":
        nonxRanOrder()
    elif answer.lower().strip() == "exit":
        var.doTurn = False
        room.imperfection()
    else:
        error
        order()

def foodOrder():
    inbreakline()
    print("You can order the following.")
    print("\n  Simple bread, served with a side of basic sanguinary honey = 1 unity (bread)")
    print("  Meat stew of the day, varys depending on available meat = 2 unity (stew)")
    print("  You can exit this menu with (exit)")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "bread" and var.unifiedCount >= 1:
        var.unifiedCount -= 1
        inbreakline()
        print("You buy yourself one [1] FLATBREAD")
        print("  You can eat it (now).")
        print("  You can eat it (later).")
        answer = input("Enter command =>")
        inbreakline()
        if answer.lower().strip() == "now":
            print("You turn over the piece of flatbread, watching the honey slowly drip off of it before turning it right side up and eating it. It doesn't do much more than sate your hunger, but that's alright.")
            var.wellness += 8
        elif answer.lower().strip() == "later":
            print("You wrap up the the FLATBREAD and tuck it into a pocket for later use.")
            var.flatbread += 1
        else:
            print("Your command was not understood. FLATBREAD was added to the inventory")
            var.flatbread += 1
        foodOrder()
    elif answer.lower().strip() == "bread" and not var.unifiedCount >= 1:
        inbreakline()
        print("You don't have enough unity.")
        foodOrder()
    elif answer.lower().strip() == "stew" and var.unifiedCount >= 2:
        var.unifiedCount -= 2
        inbreakline()
        print("You buy yourself one [1] MEAT STEW")
        print("\n  You can eat it now. (now)")
        if var.flasks > 0:
            print("  You can put it in your flask for later. (later)")
        answer = input("\nEnter command => ")
        inbreakline()
        if answer.lower().strip() == "now":
            print("You look at the stew, full of unknown meat and unknown veggies. A simple stew, will do the job, but isn't that special or particularly tasty. You eat all the chunks first and finish by slurping the savoury but surprisingly granular broth down.")
            var.wellness += 12
        elif answer.lower().strip() == "later" and var.flasks > 0:
            containers.checkFlasks("MEAT STEW")            
        else:
            print("Your command was not understood. MEAT STEW was eaten")
            var.wellness += 12
        foodOrder()
    elif answer.lower().strip() == "stew" and not var.unifiedCount == 2:
        inbreakline()
        print("You don't have enough unity.")
        foodOrder()
    elif answer.lower().strip() == "exit":
        order()
    else:
        error()
        foodOrder()

#CHECK FLASKS


                    

def drinkOrder():
    inbreakline()
    print("You can order the following.")
    print("\n  Water = Free (water)")
    print("  Warm tea = 2 unity (tea)")
    print("  You may exit this menu with (exit)")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "water":
        if var.waterDrunk != 8:
            inbreakline()
            print("You get yourself a glass of water and quickly drink it down. Don't drink too much of this stuff.")
            var.waterDrunk += 1
            drinkOrder()
        else:
            inbreakline()
            print("You get yourself a glass of water and quickly drink it down, though you immediately regret it. You should have listened to not drinking too much, but you didn't and immediately wet you pants because you drank to much water.")
            var.waterDrunk = 0
            drinkOrder()
    elif answer.lower().strip() == "tea" and var.unifiedCount >= 2:
        var.unifiedCount -= 2
        inbreakline()
        print("You get yourself a warm mug of tea, and slowly sip it, relishing the warm feeling it brings not just in heat, but also in a spice sense. It sure feels good though, and it continues to feel good after you've finished")
        drinkOrder()
    elif answer.lower().strip() == "tea" and var.unifiedCount < 1:
        inbreakline()
        print("You do not have enough money.")
        drinkOrder()
    elif answer.lower().strip() == "exit":
        order()
    else:
        error()
        drinkOrder()

def nonxRanOrder():
    inbreakline()
    print("You may order the following")
    print("\n  Basic sanguinary mead = 4 unity (mead)")
    print("  Pyrohallucinogen = 4 Unity (pyro)")
    print("  Cryohallucinogen = 4 Unity (cryo)")
    print("  You may exit the menu with (exit)")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "mead" and var.unifiedCount >= 4:
        inbreakline()
        print("You buy yourself one [1] stein of mead.")
        var.scripCount -= 4
        inbreakline()
        print("You buy yourself a thing of deep red mead, and chug it down. You immediately get a terrible headache and things don't exactly seem to be working right, your vision, your thoughts, your movement, but who cares? You sure don't.")
        var.wellness -= 4
        var.meadStat = 1
        var.meadDecay = 10
        nonxRanOrder()
    elif answer.lower().strip() == "mead" and var.unifiedCount < 4:
        inbreakline()
        print("You do not have enough Unity.")
        nonxRanOrder()
    elif answer.lower().strip() == "pyro" and var.unifiedCount >= 4:
        inbreakline()
        print("You buy yourself one [1] pyrohallucinogen.")
        var.scripCount -= 4
        inbreakline()
        print("You buy yourself one [1] PYROHALLUCINOGEN")
        print("  You can take it (now).")
        print("  You can take it (later).")
        answer = input("Enter command =>")
        inbreakline()
        if answer.lower().strip() == "now":
            print("You roll the pyrohallucinogen, a large wadded up pill, around your palm absentmindedly, before you crunch on it until it's a paste and swallow. It's not long before you begin to see sparks fly about and small fires spring up in the tavern. The fires spread, demons are engulfed, the bottles behind the counter shatter and varying colors of flame sprout up. Eventually they all burn out and the scorch marks disappear, the hallucinations having worn off, and everything is back to normal.")
            var.wellness -= 6
            var.pyrohallucinogenStat = 1
            var.pyrohallucinogenDecay = 12
        elif answer.lower().strip() == "later":
            print("You tuck the PYROHALLUCINOGEN into a pocket for later use.")
            var.pyrohallucinogen += 1
        else:
            print("Your command was not understood. PYROHALLUCINOGEN was added to the inventory")
            var.pyrohallucinogen += 1
        nonxRanOrder()
    elif answer.lower().strip() == "pyro" and var.unifiedCount < 4:
        inbreakline()
        print("You don't have enough Unity.")
        nonxRanOrder()
    elif answer.lower().strip() == "cryo" and var.unifiedCount >= 4:
        inbreakline()
        print("You buy yourself one [1] cryohallucinogen.")
        var.scripCount -= 4
        inbreakline()
        print("You buy yourself one [1] CRYOHALLUCINOGEN.")
        print("  You can take it (now).")
        print("  You can take it (later).")
        answer = input("Enter command =>")
        inbreakline()
        if answer.lower().strip() == "now":
            print("You roll the cryohallucinogen, a large wadded up pill, around your palm absentmindedly before you crunch on it until it's a paste and swallow. It's not long before You begin to see ice crystals form of the bar counter. The The windows glaze over, as to the bottles behind the bar, several of them shattering. The ice glazes over almost everything and you can see exactly where you ought to hit something to make it shatter into a thousand pieces. Eventually everything thaws, and the hallucinations wear off, returning everything back to normal.")
            var.wellness -= 6
            var.cryohallucinogenStat = 1
            var.cyrohallucinogenDecay = 12
        elif answer.lower().strip() == "later":
            print("You tuck the CRYOHALLUCINOGEN into a pocket for later use.")
            var.cryohallucinogen += 1
        else:
            print("Your command was not undestood. CRYOHALLUCINOGEN was added to the inventory.")
            var.cryohallucinogen += 1
        nonxRanOrder()

    elif answer.lower().strip() == "cryo" and var.unifiedCount < 4:
        inbreakline()
        print("You do not have enough Unity.")
        nonxRanOrder()
    elif answer.lower().strip() == "exit":
        order()
    else:
        error()
        nonxRanOrder()