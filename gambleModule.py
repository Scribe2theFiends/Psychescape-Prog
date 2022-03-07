#IMPORT

import random
import varModule as var
from formatModule import inbreakline
from random import randint

#VARIABLES



#GAMBLE

def fiendishGamble():
    inbreakline()
    yourFlatRoll = randint(1,2)
    yourFlatPlace = randint(1,20)
    yourKnuckleboneRoll = randint(1,4)
    yourKnucklebonePlace = randint(1,20)
    yourDieRoll = randint(1,6)
    yourDiePlace = randint(1,20)
    yourEightsideRoll = randint(1,8)
    yourEightsidePlace = randint(1,20)
    theirFlatRoll = randint(1,2)
    theirFlatPlace = randint(1,20)
    theirKnuckleboneRoll = randint(1,4)
    theirKnucklebonePlace = randint(1,20)
    theirDieRoll = randint(1,6)
    theirDiePlace = randint(1,20)
    theirEightsideRoll = randint(1,8)
    theirEightsidePlace = randint(1,20)
    if 0 < yourFlatPlace <= 10:
        yourFlatTotal = yourFlatRoll * 1
        yourFlatZone = "first"
    elif 10 < yourFlatPlace <= 16:
        yourFlatTotal = yourFlatRoll * 2
        yourFlatZone = "second"
    elif 16 < yourFlatPlace <= 19:
        yourFlatTotal = yourFlatRoll * 4
        yourFlatZone = "third"
    elif yourFlatPlace == 20:
        yourFlatTotal = yourFlatRoll * 8
        yourFlatZone = "fourth"
    if 0 < yourKnucklebonePlace <= 10:
        yourKnuckleboneTotal = yourKnuckleboneRoll * 1
        yourKnuckleboneZone = "first"
    elif 10 < yourKnucklebonePlace <= 16:
        yourKnuckleboneTotal = yourKnuckleboneRoll * 2
        yourKnuckleboneZone = "second"
    elif 16 < yourKnucklebonePlace <= 19:
        yourKnuckleboneTotal = yourKnuckleboneRoll * 4
        yourKnuckleboneZone = "third"
    elif yourKnucklebonePlace == 20:
        yourKnuckleboneTotal = yourKnuckleboneRoll * 8
        yourKnuckleboneZone = "fourth"
    if 0 < yourDiePlace <= 10:
        yourDieTotal = yourDieRoll * 1
        yourDieZone = "first"
    elif 10 < yourDiePlace <= 16:
        yourDieTotal = yourDieRoll * 2
        yourDieZone = "second"
    elif 16 < yourDiePlace <= 19:
        yourDieTotal = yourDieRoll * 4
        yourDieZone = "third"
    elif yourDiePlace == 20:
        yourDieTotal = yourDieRoll * 8
        yourDieZone = "fourth"
    if 0 < yourEightsidePlace <= 10:
        yourEightsideTotal = yourEightsideRoll * 1
        yourEightsideZone = "first"
    elif 10 < yourEightsidePlace <= 16:
        yourEightsideTotal = yourEightsideRoll * 2
        yourEightsideZone = "second"
    elif 16 < yourEightsidePlace <= 19:
        yourEightsideTotal = yourEightsideRoll * 4
        yourEightsideZone = "third"
    elif yourEightsidePlace == 20:
        yourEightsideTotal = yourEightsideRoll * 8
        yourEightsideZone = "fourth"
    yourTotal = yourFlatTotal + yourKnuckleboneTotal + yourDieTotal + yourEightsideTotal
    print(f"You shake your tosses up in your hand for a bit before dropping them into the center of the circle. They clatter around for a short time before coming to stop.")
    print(f"  The flat lands on {yourFlatRoll} in the {yourFlatZone} zone, giving you {yourFlatTotal} points.")
    print(f"  The knucklebone lands on {yourKnuckleboneRoll} in the {yourKnuckleboneZone} zone, giving you {yourKnuckleboneTotal} points.")
    print(f"  The die lands on {yourDieRoll} in the {yourDieZone} zone, giving you {yourDieTotal} points.")
    print(f"  The eightside lands on {yourEightsideRoll} in the {yourEightsideZone} zone, giving you {yourEightsideTotal} points.")
    print(f"  Your point total is {yourTotal} points.")
    if 0 < theirFlatPlace <= 10:
        theirFlatTotal = theirFlatRoll * 1
        theirFlatZone = "first"
    elif 10 < theirFlatPlace <= 16:
        theirFlatTotal = theirFlatRoll * 2
        theirFlatZone = "second"
    elif 16 < theirFlatPlace <= 19:
        theirFlatTotal = theirFlatRoll * 4
        theirFlatZone = "third"
    elif theirFlatPlace == 20:
        theirFlatTotal = theirFlatRoll * 8
        theirFlatZone = "fourth"
    if 0 < theirKnucklebonePlace <= 10:
        theirKnuckleboneTotal = theirKnuckleboneRoll * 1
        theirKnuckleboneZone = "first"
    elif 10 < theirKnucklebonePlace <= 16:
        theirKnuckleboneTotal = theirKnuckleboneRoll * 2
        theirKnuckleboneZone = "second"
    elif 16 < theirKnucklebonePlace <= 19:
        theirKnuckleboneTotal = theirKnuckleboneRoll * 4
        theirKnuckleboneZone = "third"
    elif theirKnucklebonePlace == 20:
        theirKnuckleboneTotal = theirKnuckleboneRoll * 8
        theirKnuckleboneZone = "fourth"
    if 0 < theirDiePlace <= 10:
        theirDieTotal = theirDieRoll * 1
        theirDieZone = "first"
    elif 10 < theirDiePlace <= 16:
        theirDieTotal = theirDieRoll * 2
        theirDieZone = "second"
    elif 16 < theirDiePlace <= 19:
        theirDieTotal = theirDieRoll * 4
        theirDieZone = "third"
    elif theirDiePlace == 20:
        theirDieTotal = theirDieRoll * 8
        theirDieZone = "fourth"
    if 0 < theirEightsidePlace <= 10:
        theirEightsideTotal = theirEightsideRoll * 1
        theirEightsideZone = "first"
    elif 10 < theirEightsidePlace <= 16:
        theirEightsideTotal = theirEightsideRoll * 2
        theirEightsideZone = "second"
    elif 16 < theirEightsidePlace <= 19:
        theirEightsideTotal = theirEightsideRoll * 4
        theirEightsideZone = "third"
    elif theirEightsidePlace == 20:
        theirEightsideTotal = theirEightsideRoll * 8
        theirEightsideZone = "fourth"
    theirTotal = theirFlatTotal + theirKnuckleboneTotal + theirDieTotal + theirEightsideTotal
    print(f"They shake their tosses up in their hand for a bit before dropping them into the center of the circle. They clatter around for a short time before coming to stop.")
    print(f"  The flat lands on {theirFlatRoll} in the {theirFlatZone} zone, giving them {theirFlatTotal} points.")
    print(f"  The knucklebone lands on {theirKnuckleboneRoll} in the {theirKnuckleboneZone} zone, giving them {theirKnuckleboneTotal} points.")
    print(f"  The die lands on {theirDieRoll} in the {theirDieZone} zone, giving them {theirDieTotal} points.")
    print(f"  The eightside lands on {theirEightsideRoll} in the {theirEightsideZone} zone, giving them {theirEightsideTotal} points.")
    print(f"  Your point total is {theirTotal} points.")
    if yourTotal > theirTotal:
        print(f"You win by {yourTotal - theirTotal} points!")
        var.fiendishGambleOutcome = "won"
        inbreakline()
    elif theirTotal > yourTotal:
        print(f"Your lose by {theirTotal - yourTotal} points!")
        var.fiendishGambleOutcome = "lost"
        inbreakline()
    elif yourTotal == theirTotal:
        print("You tie! What a chance!")
        var.fiendishGambleOutcome = "tied"
        inbreakline()