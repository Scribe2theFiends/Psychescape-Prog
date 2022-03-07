from formatModule import inbreakline,error
import varModule as var
import roomModule as room

def exchange():
    print("What will you turn in?")
    print("\nYou can turn in;")
    if var.ichorCount > 0:
        print("\n  ICHOR NODULES (ichor)")
    if var.largeIchorCount > 0:
        print("  LARGE ICHOR NODULES (lichor)")
    if var.sculptureGradeIchorCount > 0:
        print("  SCULPTURE GRADE ICHOR NODULES (sgichor)")
    if var.coalCount > 0:
        print("  CHUNKS OF COAL (coal)")
    if var.largeCoalCount > 0:
        print("  LARGE CHUNKS OF COAL (lcoal)")
    if var.commonArsonSalts > 0:
        print("  PARCELS OF COMMON ARSON SALTS (carsonsalts)")
    if var.rareArsonSalts > 0:
        print("  PARCELS OF RARE ARSON SALTS (rasrsonsalts)")
    print("  You may exit the menu. (exit)")
    answer = input("\nEnter command here => ")
    inbreakline()
    if answer.lower().strip() == "ichor":
        if var.ichorCount >=  1:
            print("\nYou turn in a [1] NODULE OF ICHOR for 3 MINING SCRIP.")
            var.ichorCount -= 1
            var.scripCount += 3
            print(f"You have {var.ichorCount} NODULE[S] OF ICHOR.")
            print(f"You have {var.scripCount} MINING SCRIP.")
        else:
            inbreakline()
            print("You don't have any NODULES OF ICHOR to exchange.")
    elif answer.lower().strip() == "lichor":
        if var.largeIchorCount >=  1:
            print("\nYou turn in a [1] LARGE NODULE OF ICHOR for 11 MINING SCRIP.")
            var.largeIchorCount -= 1
            var.scripCount += 11
            print(f"You have {var.largeIchorCount} LARGE NODULE[S] OF ICHOR.")
            print(f"You have {var.scripCount} MINING SCRIP.")
        else:
            print("\nYou don't have any LARGE NODULES OF ICHOR to exchange.")
    elif answer.lower().strip() == "sgichor":
        if var.sculptureGradeIchorCount >=  1:
            print("\nYou turn in a [1] SCULPTURE GRADE NODULE OF ICHOR for 25 MINING SCRIP.")
            var.sculptureGradeIchorCount -= 1
            var.scripCount += 25
            print(f"You have {var.sculptureGradeIchorCount} SCULPTURE GRADE NODULE[S] OF ICHOR.")
            print(f"You have {var.scripCount} MINING SCRIP.")
        else:
            print("\nYou don't have any SCULPTURE GRADE NODULES OF ICHOR to exchange.")
    elif answer.lower().strip() == "coal":
        if var.coalCount >=  1:
            print("\nYou turn in a [1] CHUNK OF COAL for 1 MINING SCRIP.")
            var.coalCount -= 1
            var.scripCount += 1
            print(f"You have {var.coalCount} CHUNKS OF COAL.")
            print(f"You have {var.scripCount} MINING SCRIP.")
        else:
            print("\nYou don't have any CHUNKS OF COAL to exchange.")
    elif answer.lower().strip() == "lcoal":
        if var.largeCoalCount >=  1:
            print("\nYou turn in a [1] LARGE CHUNK OF COAL for 6 MINING SCRIP.")
            var.largeCoalCount -= 1
            var.scripCount += 6
            print(f"You have {var.largeCoalCount} LARGE CHUNKS OF COAL.")
            print(f"You have {var.scripCount} MINING SCRIP.")
        else:
            print("\nYou don't have any LARGE CHUNKS OF COAL to exchange.")
    elif answer.lower().strip() == "carsonsalts":
        if var.commonArsonSalts >=  1:
            print("\nYou turn in a [1] PARCEL OF COMMON ARSON SALTS for 4 MINING SCRIP.")
            var.commonArsonSalts -= 1
            var.scripCount += 4
            print(f"You have {var.commonArsonSalts} PARCELS OF COMMON ARSON SALTS.")
            print(f"You have {var.scripCount} MINING SCRIP.")
        else:
            print("\nYou don't have any PARCELS OF COMMON ARSON SALTS to exchange.")
    elif answer.lower().strip() == "rarsonsalts":
        if var.rareArsonSalts >=  1:
            print("\nYou turn in a [1] PARCEL OF RARE ARSON SALTS for 10 MINING SCRIP.")
            var.rareArsonSalts -= 1
            var.scripCount += 10
            print(f"You have {var.rareArsonSalts} PARCELS OF RARE ARSON SALTS.")
            print(f"You have {var.scripCount} MINING SCRIP.")
        else:
            print("\nYou don't have any PARCELS OF RARE ARSON SALTS to exchange.")
    elif answer.lower().strip() == "exit":
        print("Closing the menu.")
    else:
        error()
    var.doTurn = False
    room.scripExchange()