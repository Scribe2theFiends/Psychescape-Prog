from formatModule import inbreakline
import varModule as var
import roomModule as room

def mining():
    inbreakline()
    import random
    miningAward = random.randint(1,100)
    if 0 < miningAward <= 50:
        print("  You get nothing!")
    elif 50 < miningAward <= 64:
        print("  You find a [1] CHUNK OF COAL")
        var.coalCount += 1
        print(f"  You have {var.coalCount} CHUNK[S] OF COAL")
    elif 64 < miningAward <= 74:
        print("  You find a [1] NODULE OF ICHOR")
        var.ichorCount += 1
        print(f"  You have {var.ichorCount} NODULES OF ICHOR")
    elif 74 < miningAward <= 82:
        print("  You find a [1] naturally occuring vein of common arson salts. You quickly dig them out and tie them in a parcel.")
        var.commonArsonSalts += 1
        print(f"  You have {var.commonArsonSalts} PARCEL[S] OF COMMON ARSON SALTS")
    elif 82 < miningAward <= 89:
        print("  You find a [1] LARGE CHUNK OF COAL")
        var.largeCoalCount += 1
        print(f"  You have {var.largeCoalCount} LARGE CHUNK[S] OF COAL")
    elif 89 < miningAward <= 94:
        print("  You find a [1] naturally occuring vein of rare arson salts. You quickly dig them out and tie them in a parcel.")
        var.rareArsonSalts += 1
        print(f"  You have {var.rareArsonSalts} PARCEL[S] OF RARE ARSON SALTS")
    elif 94 < miningAward <= 98:
        print("  You find a [1] LARGE ICHOR NODULE")
        var.largeIchorCount += 1
        print(f"  You have {var.largeIchorCount} LARGE NODULE[S] OF ICHOR")
    elif 98 < miningAward <= 100:
        print("  You find a [1] SCULPTURE GRADE ICHOR NODULE")
        var.sculptureGradeIchorCount += 1
        print(f"  You have {var.sculptureGradeIchorCount} SCULPTURE GRADE ICHOR NODULE[S]")
    room.mine()