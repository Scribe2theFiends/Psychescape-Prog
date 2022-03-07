from formatModule import inbreakline,error
import varModule as var
import gambleModule as gamble

def lossGambling():
    print("As you approach the table, the demon gets up, looking excited. \"Ah, you! Are you up for a gamble? I can match anything you've dug out of the mine, plus I also gamble with scrip and unity! What do you say, wanna see what the bones have to offer?\" The figure holds out the bones in his hand, waiting for your answer.")
    print("\n  Why not, in what way has gambling ever hurt? (yes)")
    print("  No, no way I'm going to lose my hard-earned loot to a slacker. (no)")
    answer = input("\nEnter command here => ")
    inbreakline()
    if answer.lower().strip() == "yes":
        print("You don't see any harm in a gamble, and grab the bones from their hand. \"Now that's what I'm talking about. Call me loss by the way, though it's not important, just as your name is unimportant to me, no offense. What are you going to gamble on?")
        print(" ")
        if var.scripCount > 0:
            print("  You can gamble with (scrip)")
        if var.unifiedCount > 0:
            print("  You can gamble with (unity)")
        if var.ichorCount > 0 or var.largeIchorCount >0 or var.sculptureGradeIchorCount > 0 or var.coalCount > 0 or var.largeCoalCount > 0 or var.commonArsonSalts > 0 or var.rareArsonSalts > 0:
            print("  You can gamble with (minerals)")
        print("  You can exit the menu with (exit)")
        answer = input("\nEnter command here => ")
        inbreakline()
        if answer.lower().strip() == "scrip" and var.scripCount > 0:
            print(f"\nHow much scrip do you want to bet? You have {var.scripCount} scrip.")
            answer = input("\nEnter amount here => ")
            inbreakline()
            if int(answer) <= var.scripCount and int(answer) > 0:
                print(f"You wager Loss {answer} scrip, and they match your bet with their own scrip, then you get ready to roll the bones and see who wins.")
                gamble.fiendishGamble()
                if var.fiendishGambleOutcome == "won":
                    print(f"You gain {answer} scrip.")
                    var.scripCount += int(answer)
                elif var.fiendishGambleOutcome == "lost":
                    print(f"You lose {answer} scrip.")
                    var.scripCount -= int(answer)
                elif var.fiendishGambleOutcome == "tied":
                    print("Due to the tie, neither of you gain or lose anything. Feel free to try again though.")
            else:
                print("You don't have that much scrip, come back when you do.")
                var.doTurn = False
        elif answer.lower().strip() == "unity" and var.unifiedCount > 0:
            print(f"How much unity do you want to bet? You have {var.unifiedCount} unity.")
            answer = input("Enter amount here => ")
            if int(answer) <= var.scripCount and int(answer) > 0:
                inbreakline()
                print(f"You wager Loss {answer} Unity, and they match your bet with their own Unity, then you get ready to roll the bones and see who wins.")
                gamble.fiendishGamble()
                if var.fiendishGambleOutcome == "won":
                    print(f"You gain {answer} Unity.")
                    var.unifiedCount += int(answer)
                elif var.fiendishGambleOutcome == "lost":
                    print(f"You lose {answer} Unity.")
                    var.unifiedCount -= int(answer)
                elif var.fiendishGambleOutcome == "tied":
                    print("Due to the tie, neither of you gain or lose anything. Feel free to try again though.")
        elif answer.lower().strip() == "minerals":
            print("You may choose from the following minerals to wager:")
            print(" ")
            if var.ichorCount > 0:
                print("  Nodule of Ichor (ichor)")
            if var.largeIchorCount > 0:
                print("  Large Nodule of Ichor (lichor)")
            if var.sculptureGradeIchorCount > 0:
                print("  Sculpture Grade Nodule of Ichor (sgichor)")
            if var.coalCount > 0:
                print("  Chunk of Coal (coal)")
            if var.largeCoalCount > 0:
                print("  Large Chunk of Coal (lcoal)")
            if var.commonArsonSalts > 0:
                print("  Parcel of Common Arson Salts (carsonsalts)")
            if var.rareArsonSalts > 0:
                print("  Parcel of Rare Arson Salts (rarsonsalts)")
            answer = input("\nEnter command here => ")
            inbreakline()
            if answer.lower().strip() == "ichor" and var.ichorCount > 0:
                print(f"You wager Loss a NODULE OF ICHOR, and they match your bet with their own, then you get ready to roll the bones and see who wins.")
                gamble.fiendishGamble()
                if var.fiendishGambleOutcome == "won":
                    print(f"You gain a NODULE OF ICHOR.")
                    var.ichorCount += 1
                elif var.fiendishGambleOutcome == "lost":
                    print(f"You lose a NODULE OF ICHOR.")
                    var.ichorCount -= 1
                elif var.fiendishGambleOutcome == "tied":
                    print("Due to the tie, neither of you gain or lose anything. Feel free to try again though.")
            elif answer.lower().strip() == "lichor" and var.largeIchorCount > 0:
                print(f"You wager Loss a LARGE NODULE OF ICHOR, and they match your bet with their own, then you get ready to roll the bones and see who wins.")
                gamble.fiendishGamble()
                if var.fiendishGambleOutcome == "won":
                    print(f"You gain a LARGE NODULE OF ICHOR.")
                    var.largeIchorCount += 1
                elif var.fiendishGambleOutcome == "lost":
                    print(f"You lose a LARGE NODULE OF ICHOR.")
                    var.largeIchorCount -= 1
                elif var.fiendishGambleOutcome == "tied":
                    print("Due to the tie, neither of you gain or lose anything. Feel free to try again though.")
            elif answer.lower().strip() == "sgichor" and var.sculptureGradeIchorCount > 0:
                print(f"You wager Loss a SCULPTURE GRADE NODULE OF ICHOR, and they match your bet with their own, then you get ready to roll the bones and see who wins.")
                gamble.fiendishGamble()
                if var.fiendishGambleOutcome == "won":
                    print(f"You gain a SCULPTURE GRADE NODULE OF ICHOR.")
                    var.sculptureGradeIchorCount += 1
                elif var.fiendishGambleOutcome == "lost":
                    print(f"You lose a SCULPTURE GRADE NODULE OF ICHOR.")
                    var.sculptureGradeIchorCount -= 1
                elif var.fiendishGambleOutcome == "tied":
                    print("Due to the tie, neither of you gain or lose anything. Feel free to try again though.")
            elif answer.lower().strip() == "coal" and var.coalCount > 0:
                print(f"You wager Loss a CHUNK OF COAL, and they match your bet with their own, then you get ready to roll the bones and see who wins.")
                gamble.fiendishGamble()
                if var.fiendishGambleOutcome == "won":
                    print(f"You gain a CHUNK OF COAL.")
                    var.coalCount += 1
                elif var.fiendishGambleOutcome == "lost":
                    print(f"You lose a CHUNK OF COAL.")
                    var.coalCount -= 1
                elif var.fiendishGambleOutcome == "tied":
                    print("Due to the tie, neither of you gain or lose anything. Feel free to try again though.")
            elif answer.lower().strip() == "lcoal" and var.largeCoalCount > 0:
                print(f"You wager Loss a LARGE CHUNK OF COAL, and they match your bet with their own, then you get ready to roll the bones and see who wins.")
                gamble.fiendishGamble()
                if var.fiendishGambleOutcome == "won":
                    print(f"You gain a LARGE CHUNK OF COAL.")
                    var.largeCoalCount += 1
                elif var.fiendishGambleOutcome == "lost":
                    print(f"You lose a LARGE CHUNK OF COAL.")
                    var.largeCoalCount -= 1
                elif var.fiendishGambleOutcome == "tied":
                    print("Due to the tie, neither of you gain or lose anything. Feel free to try again though.")
            elif answer.lower().strip() == "carsonsalts" and var.commonArsonSalts > 0:
                print(f"You wager Loss a PARCEL OF COMMON ARSON SALTS, and they match your bet with their own, then you get ready to roll the bones and see who wins.")
                gamble.fiendishGamble()
                if var.fiendishGambleOutcome == "won":
                    print(f"You gain a PARCEL OF COMMON ARSON SALTS.")
                    var.commonArsonSalts += 1
                elif var.fiendishGambleOutcome == "lost":
                    print(f"You lose a PARCEL OF COMMON ARSON SALTS.")
                    var.commonArsonSalts -= 1
                elif var.fiendishGambleOutcome == "tied":
                    print("Due to the tie, neither of you gain or lose anything. Feel free to try again though.")
            elif answer.lower().strip() == "rarsonsalts" and var.rareArsonSalts > 0:
                print(f"You wager Loss a PARCEL OF RARE ARSON SALTS, and they match your bet with their own, then you get ready to roll the bones and see who wins.")
                gamble.fiendishGamble()
                if var.fiendishGambleOutcome == "won":
                    print(f"You gain a PARCEL OF RARE ARSON SALTS.")
                    var.rareArsonSalts += 1
                elif var.fiendishGambleOutcome == "lost":
                    print(f"You lose a PARCEL OF RARE ARSON SALTS.")
                    var.rareArsonSalts -= 1
                elif var.fiendishGambleOutcome == "tied":
                    print("Due to the tie, neither of you gain or lose anything. Feel free to try again though.")
            else:
                error()
                lossGambling()
        elif answer.lower().strip() == "exit":
            print("Exiting the menu.")
            var.doTurn = False
        else:
          error()
          lossGambling()
    elif answer.lower().strip() == "no":
        print("As you tell them that you aren't willing to gamble anything, they begin to look disappointed, before turning away from you and looking for other people interested in gambling.")
        var.doTurn = False
    else:
        error()
        lossGambling()