from formatModule import inbreakline,error
import varModule as var
import roomModule as room

def food(): 
    inbreakline()
    print("You can buy food here with your scrip. The following item are on the menu;")
    print("\n  Jigglers: 5 scrip. Some sort of gelatinous blob plopped out of a bowl that was left to set sometime earlier this month. Fun to throw at other people, supposedly only the outer layer ever goes bad. (jigglers)")
    print("  You can leave the counter (leave).")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "leave":
        var.doTurn = False
        room.messHall()
    elif answer.lower().strip() == "jigglers":
        inbreakline()
        if var.scripCount >= 5:
            print("  You buy yourself one [1] jiggler.")
            var.scripCount -= 5
            inbreakline()
            print("    You can eat it (now).")
            print("    You can eat it (later).")
            answer  = input("Enter command =>")
            inbreakline()
            if answer == "now":
                print("You take the plate and bring the jiggler to a corner to sit down and eat it. You peel away the chewier outside and eat it first before eating the more savory center.")
                var.doTurn = False
                var.wellness += 10
                room.messHall()
            elif answer == "later":
                print("You wrap the jiggler up in some cloth scraps and shove it in your pocket. As you walk away you can feel it wobbling in there somewhat unpleasantly.")
                var.jigglers += 1
                var.doTurn = False
                room.messHall()
            else:
                print("Your command was not understood. Jiggler automatically added to your inventory.")
                var.jigglers += 1
                var.doTurn = False
                room.messHall()
        else:
            print("  You don't have enough scrip to buy that.")
            var.doTurn = False
            room.messHall()
    else:
        error()
        var.doTurn = False
        room.messHall()