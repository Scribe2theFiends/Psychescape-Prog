import varModule as var
import roomModule as room
from formatModule import inbreakline,error

def cheating():
    inbreakline()
    var.hasCheated = True
    print("  You can get items here. (create)")
    print("  You can gain knowledge here. (develop)")
    print("  You can exit this menu. (exit)")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "create":
        creation()
    elif answer.lower().strip() == "develop":
        development()
    elif answer.lower().strip() == "exit":
        print("Closing the menu.")
        room.cheatRoom()
    else:
        error()
        room.cheatRoom()

def creation():
    inbreakline()
    print("You can create items with the following commands.")
    print("\n  (ichor)")
    print("  (lichor)")
    print("  (sgichor)")
    print("  (coal)")
    print("  (lcoal)")
    print("  (carsonsalts)")
    print("  (rarsonsalts)")
    print("  (scrip)")
    print("  (unity) or (u=)")
    print("  (minepermit)")
    print("  (bberries)")
    print("  (bwax)")
    print("  (jigglers)")
    print("  (dtsap)")
    print("  (dtfruit)")
    print("  (hfefruit)")
    answer = input("\nEnter cheat command here => ")
    if answer.lower().strip() == "ichor":
        inbreakline()
        answer = input("Enter amount here => ")
        inbreakline
        var.ichorCount += int(answer)
        print(f"You create [{answer}] NODULE[S] OF ICHOR.")
    elif answer.lower().strip() == "lichor":
        inbreakline()
        answer = input("Enter amount here => ")
        inbreakline()
        var.largeIchorCount += int(answer)
        print(f"You create [{answer}] LARGE NODULE[S] OF ICHOR.")
    elif answer.lower().strip() == "sgichor":   
        inbreakline()
        answer = input("Enter amout here => ")
        inbreakline()
        var.sculptureGradeIchorCount += int(answer)
        print(f"You create [{answer}] SCULPTURE GRADE NODULE[S] OF ICHOR.")
    elif answer.lower().strip() == "coal":
        inbreakline()
        answer = input("Enter amount here => ")
        inbreakline()
        var.coalCount += int(answer)
        print(f"You create [{answer}] CHUNK[S] OF COAL.")
    elif answer.lower().strip() == "lcoal":
        inbreakline()
        answer = input("Enter amount here => ")
        inbreakline()
        var.largeCoalCount += int(answer)
        print(f"You create [{answer}] LARGE CHUNK[S] OF COAL.")
    elif answer.lower().strip() == "carsonsalts":
        inbreakline()
        answer = input("Enter amount here => ")
        inbreakline()
        var.commonArsonSalts += int(answer)
        print(f"You create [{answer}] PARCEL[S] OF COMMON ARSON SALTS.")
    elif answer.lower().strip() == "rarsonsalts":
        answer = input("Enter amount here => ")
        inbreakline()
        var.rareArsonSalts += int(answer)
        print(f"You create [{answer}] PARCEL[S] OF COMMON ARSON SALTS.")
    elif answer.lower().strip() == "scrip":
        inbreakline()
        answer = input("Enter amount here => ")
        inbreakline()
        var.scripCount += int(answer)
        print(f"You create [{answer}] SCRIP.")
    elif answer.lower().strip() == "unity" or answer.lower().strip() == "u=":
        inbreakline()
        answer = input("Enter amount here => ")
        inbreakline()
        var.unifiedCount += int(answer)
        print(f"You create [{answer}] U=")
    elif answer.lower().strip() == "minepermit":
        inbreakline()
        var.hasMinePermit = True
        print("You create a mine permit.")
    elif answer.lower().strip() == "bwax":
        inbreakline()
        answer = input("Enter amount here => ")
        inbreakline()
        var.bloodboilWax += int(answer)
        print(f"You create [{answer}] BLOODBOIL WAX.")
    elif answer.lower().strip() == "bberries":
        inbreakline()
        answer = input("Enter amount here => ")
        inbreakline()
        var.bloodboilBerries += int(answer)
        print(f"You create [{answer}] BLOODBOIL BERRIES.")
    elif answer.lower().strip() == "jigglers":
        inbreakline()
        answer = input("Enter amount here => ")
        inbreakline()
        var.jigglers += int(answer)
        print(f"You create [{answer}] JIGGLER[S].")
    elif answer.lower().strip() == "dtsap":
        inbreakline()
        answer = input("Enter amount here => ")
        inbreakline()
        var.darkTreeSap += int(answer)
        print(f"You create [{answer}] DARK TREE SAP.")
    elif answer.lower().strip() == "dtfruit":
        inbreakline()
        answer = input("Enter amount here => ")
        inbreakline()
        var.darkTreeFruit += int(answer)
        print(f"You create [{answer}] DARK TREE FRUITS.")
    elif answer.lower().strip() == "hfefruit":
        inbreakline()
        answer = input("Enter amount here => ")
        inbreakline()
        var.hwerFshErrFruit += int(answer)
        print(f"You create [{answer}] HWER'FSH'ERR FRUIT[S].")
    else:
        error()
    var.doTurn = False
    room.cheatRoom()

def development():
    inbreakline()
    print("You can learn the following.")
    print("\n  (omniscience)")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "omniscience":
        var.knowsAshKrahn = True
        var.knowsBahnAr = True
        var.knowsBloodboil = True
        var.knowsBorchTrahfl = True
        var.knowsDarkTree = True
        var.knowsFtNagYen = True
        var.knowsGzahnKathIhn = True
        var.knowsHwerFshErrTree = True
        var.knowsSrsh = True
        var.knowsYeelTsur = True
        inbreakline()
        print("You become omniscient.")
        var.doTurn = False
        room.cheatRoom()
