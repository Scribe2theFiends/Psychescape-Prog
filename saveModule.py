#SAVE MECHANIC


#IMPORT

import varModule as var
from formatModule import uibreakline,inbreakline,breakline,error
import startModule as start
import roomModule as room

#SIMPLE SAVE MECHANIC

def simpleSave():
    uibreakline()
    print("This will create a code for you to input if you run the program again. Please have something to take notes with before saving")
    print("\n  You can (save)")
    print("  You can (exit)")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "save":
        print("The following numbers must be entered in the order you recieved them. Do not merge the numbers into one single number. It will not be processed that way. You may also want to mark down the version you are playing, as they will not be backwards compatible.")
        print(f"{var.scripCount}")
        print(f"{var.unifiedCount}")
        print(f"{var.ichorCount}")
        print(f"{var.largeIchorCount}")
        print(f"{var.sculptureGradeIchorCount}")
        print(f"{var.coalCount}")
        print(f"{var.largeCoalCount}")
        print(f"{var.commonArsonSalts}")
        print(f"{var.rareArsonSalts}")
        print(f"{var.jigglers}")
        print(f"{var.bloodboilWax}")
        print(f"{var.bloodboilBerries}")
        print(f"{var.darkTreeSap}")
        print(f"{var.darkTreeFruit}")
        print(f"{var.hwerFshErrFruit}")
        if var.hasMinePermit == True:
            print("1")
        else:
            print("0")
        if var.shownMinePermit == True:
            print("1")
        else:
            print("0")
        if var.visitedMineGates == True:
            print("1")
        else:
            print("0")
        if var.knowsGzahnKathIhn == True:
            print("1")
        else:
            print("0")
        if var.knowsSrsh == True:
            print("1")
        else:
            print("0")
        if var.knowsBloodboil == True:
            print("1")
        else:
            print("0")
        if var.hasCheated == True:
            print("1")
        else:
            print("0")
        print(f"{var.currentRoom}")
        print("\nIf you are done copying this down, please enter (done).")
        answer =input("Enter command here =>  ")
        if answer.lower().strip() == "done":
            breakline()
        else:
            breakline()
            simpleSave()
    elif answer.lower().strip() == "exit":
        breakline()
    else:
        breakline()
        simpleSave()

#SIMPLE LOAD MECHANIC

def simpleLoad():
    print("In order to load a previous save, you must have a save code somewhere. If you have one of these, you may (continue), if you don't you want to (exit).")
    answer = input("\nEnter command here =>  ")
    if answer.lower().strip() == "exit":
        start.reStartCommand()
    elif answer.lower().strip() == "continue":
        print("You must enter the numbers you received in the order they were recieved.")
        scripValue = input("Enter value => ")
        var.scripCount = scripValue
        unifiedValue = input("Enter value => ")
        var.unifiedCount = unifiedValue
        ichorValue = input("Enter value => ")
        var.ichorCount = ichorValue
        largeIchorValue = input("Enter value => ")
        var.largeIchorCount = largeIchorValue
        sculptureGradeIchorValue = input("Enter value => ")
        var.sculptureGradeIchorCount = sculptureGradeIchorValue
        coalValue = input("Enter value => ")
        var.coalCount = coalValue
        largeCoalValue = input("Enter value => ")
        var.largeCoalCount = largeCoalValue
        commonArsonSaltsValue = input("Enter value => ")
        var.commonArsonSalts = commonArsonSaltsValue
        rarearsonSaltsValue = input("Enter value => ")
        var.rareArsonSalts = rarearsonSaltsValue
        jigglersValue = input("Enter value => ")
        var.jigglers = jigglersValue
        bloodboilWaxValue = input("Enter value => ")
        var.bloodboilWax = bloodboilWaxValue
        bloodboilBerriesValue = input("Enter value => ")
        var.bloodboilBerries = bloodboilBerriesValue
        darkTreeSapValue = input("Enter value => ")
        var.darkTreeSap = darkTreeSapValue
        darkTreeFruitValue = input("Enter value => ")
        var.darkTreeFruit = darkTreeFruitValue
        hwerFshErrFruitValue = input("Enter value => ")
        var.hwerFshErrFruit = hwerFshErrFruitValue
        hasMinePermitValue = input("Enter value => ")
        if hasMinePermitValue != "0" and hasMinePermitValue != "1":
            loadError()
        else:
            var.hasPermit = hasMinePermitValue
        shownMinePermitValue = input("Enter value => ")
        if shownMinePermitValue != "0" and shownMinePermitValue != "1":
            loadError()
        else:
            var.shownMinePermit = shownMinePermitValue
        visitedMineGatesValue = input("Enter value => ")
        if visitedMineGatesValue != "0" and visitedMineGatesValue != "1":
            loadError()
        else:
            var.visitedMineGates = visitedMineGatesValue
        knowsGzahnKathIhnValue = input("Enter value => ")
        if knowsGzahnKathIhnValue != "0" and knowsGzahnKathIhnValue != "1":
            loadError()
        else:
            var.knowsGzahnKathIhn = knowsGzahnKathIhnValue
        knowsSrshValue = input("Enter value => ")
        if knowsSrshValue != "0" and knowsSrshValue != "1":
            loadError()
        else:
            var.knowsSrsh = knowsSrshValue
        knowsBloodboilValue = input("Enter value => ")
        if knowsBloodboilValue != "0" and knowsBloodboilValue != "1":
            loadError()
        else:
            var.knowsBloodboil = knowsBloodboilValue
        hasCheatedValue = input("Enter value => ")
        if hasCheatedValue != "0" and hasCheatedValue != "1":
            loadError()
        else:
            var.hasCheated = hasCheatedValue
        currentRoomValue = input("Enter value => ")
        if currentRoomValue != "160" and currentRoomValue != "1" and currentRoomValue != "2" and currentRoomValue != "3" and currentRoomValue != "4" and currentRoomValue != "5" and currentRoomValue != "6" and currentRoomValue != "7" and currentRoomValue != "8" and currentRoomValue != "9" and currentRoomValue != "10":
            loadError()
        else:
            currentRoom = currentRoomValue
        breakline()
        print("Loading game...")
        if currentRoom == "160":
            room.cheatRoom()
        elif currentRoom == "1":
            room.mine()
        elif currentRoom == "2":
            room.mineEntrance()
        elif currentRoom == "3":
            room.commonArea()
        elif currentRoom == "4":
            room.companyStore()
        elif currentRoom == "5":
            room.messHall()
        elif currentRoom == "6":
            room.scripExchange()
        elif currentRoom == "7":
            room.mineGates()
        elif currentRoom == "8":
            room.crossroads()
        elif currentRoom == "9":
            room.darkForest()
        elif currentRoom == "10":
            room.outskirts()
    else:
        error()

#LOAD ERROR

def loadError(error):
    inbreakline()
    print("Error; " + error + " is incorrect.")
    breakline()
    start.reStartCommand()


def save():
    uibreakline()
    print("This will create a code for you to input if you run the program again. Please have something to take notes with before saving")
    print("\n  You can (save)")
    print("  You can (exit)")
    answer = input("\nEnter command here => ")
    uibreakline()
    if answer.lower().strip() == "save":
        print("The following string should be copied onto something in the way that it is recieved. You will also want to mark down the version you are playing, as they will not be backwards compatible.\n")
        if var.hasCheated == False:
            hasCheatedValue = 0
        else:
            hasCheatedValue = 1
        if var.visitedMineGates == False:
            visitedMineGateValue = 0
        else:
            visitedMineGateValue = 1
        if var.hasMinePermit == False:
            hasMinePermitValue = 0
        else:
            hasMinePermitValue = 1
        if var.shownMinePermit == False:
            shownMinePermitValue = 0
        else:
            shownMinePermitValue = 1
        if var.knowsGzahnKathIhn == False:
            knowsGzahnKathIhnValue = 0
        else:
            knowsGzahnKathIhnValue = 1
        if var.knowsAshKrahn == False:
            knowsAshKrahnValue = 0
        else:
            knowsAshKrahnValue = 1
        if var.knowsBahnAr == False:
            knowsBahnArValue = 0
        else:
            knowsBahnArValue = 1
        if var.knowsBorchTrahfl == False:
            knowsBorchTrahflValue = 0
        else:
            knowsBorchTrahflValue = 1
        if var.knowsYeelTsur == False:
            knowsYeelTsurValue = 0
        else:
            knowsYeelTsurValue = 1
        if var.knowsBloodboil == False:
            knowsBloodboilValue = 0
        else:
            knowsBloodboilValue = 1
        if var.knowsFtNagYen == False:
            knowsFtNagYenValue = 0
        else:
            knowsFtNagYenValue = 1
        if var.knowsDarkTree == False:
            knowsDarkTreeValue = 0
        else:
            knowsDarkTreeValue = 1
        if var.knowsHwerFshErrTree == False:
            knowsHwerFshErrTreeValue = 0
        else:
            knowsHwerFshErrTreeValue = 1
        if var.knowsSrsh == False:
            knowsSrshValue = 0
        else:
            knowsSrshValue = 1
        if var.foundGreatTree == False:
            foundGreatTreeValue = 0
        else:
            foundGreatTreeValue = 1
        print(f"{var.scripCount}~{var.unifiedCount}~{var.ichorCount}~{var.largeIchorCount}~{var.sculptureGradeIchorCount}~{var.coalCount}~{var.largeCoalCount}~{var.commonArsonSalts}~{var.rareArsonSalts}~{var.bloodboilWax}~{var.jigglers}~{var.bloodboilBerries}~{var.darkTreeSap}~{var.darkTreeFruit}~{var.hwerFshErrFruit}~{hasMinePermitValue}~{shownMinePermitValue}~{visitedMineGateValue}~{knowsGzahnKathIhnValue}~{knowsAshKrahnValue}~{knowsBahnArValue}~{knowsYeelTsurValue}~{knowsBorchTrahflValue}~{knowsFtNagYenValue}~{knowsBloodboilValue}~{knowsDarkTreeValue}~{knowsHwerFshErrTreeValue}~{knowsSrshValue}~{foundGreatTreeValue}~{var.currentRoom}~{hasCheatedValue}")
        var.doTurn = False
    elif answer.lower().strip() == "exit":
        print("Closing the menu")
        var.doTurn = False
    else:
        breakline()
        save()

def load():
    print("In order to load a previous save, you must have a save code somewhere. If you have a save code from a previous version, please use the save-code updater to update your save code. If you have a usuable save-code, you may (continue), if you don't you want to (exit).")
    answer = input("\nEnter command here =>  ")
    if answer.lower().strip() == "exit":
        breakline()
        start.reStartCommand()
    elif answer.lower().strip() == "continue":
        uibreakline()
        print("Please enter your save code.")
        saveCode = input("\nEnter save-code here => ")
        scripCountValue,unifiedCountValue,ichorCountValue,largeIchorCountValue,sculptureGradeIchorCountValue,coalCountValue,largeCoalCountValue ,commonArsonSaltsValue,rareArsonSaltsValue,bloodboilWaxValue,jigglersValue,bloodboilBerriesValue,darkTreeSapValue,darkTreeFruitValue,hwerFshErrFruitValue,hasMinePermitValue,shownMinePermitValue,visitedMineGatesValue,knowsGzahnKathIhnValue,knowsAshKrahnValue,knowsBahnArValue,knowsYeelTsurValue,knowsBorchTrahflValue,knowsFtNagYenValue,knowsBloodboilValue,knowsDarkTreeValue,knowsHwerFshErrTreeValue,knowsSrshValue,foundGreatTreeValue,currentRoomValue,hasCheatedValue = saveCode.split('~')
        var.scripCount = int(scripCountValue)
        var.unifiedCount = int(unifiedCountValue)
        var.ichorCount = int(ichorCountValue)
        var.largeIchorCount = int(largeIchorCountValue)
        var.sculptureGradeIchorCount = int(sculptureGradeIchorCountValue)
        var.coalCount = int(coalCountValue)
        var.largeCoalCount = int(largeCoalCountValue)
        var.commonArsonSalts = int(commonArsonSaltsValue)
        var.rareArsonSalts = int(rareArsonSaltsValue)
        var.bloodboilWax = int(bloodboilWaxValue)
        var.jigglers = int(jigglersValue)
        var.bloodboilBerries = int(bloodboilBerriesValue)
        var.darkTreeSap = int(darkTreeSapValue)
        var.darkTreeFruit = int(darkTreeFruitValue)
        var.hwerFshErrFruit = int(hwerFshErrFruitValue)
        if int(hasMinePermitValue) == 1 or int(hasMinePermitValue) == 0:
            if int(hasMinePermitValue) == 1:
                var.hasMinePermit = True
            else:
                var.hasMinePermit = False
        else:
            loadError("hasMinePermit")
        if int(shownMinePermitValue) == 1 or int(shownMinePermitValue) == 0:
            if int(shownMinePermitValue) == 1:
                var.shownMinePermit = True
            else:
                var.shownMinePermit = False
        else:
            loadError("shownMinePermit")
        if int(visitedMineGatesValue) == 1 or int(visitedMineGatesValue) == 0:
            if int(visitedMineGatesValue) == 1:
                var.visitedMineGates = True
            else:
                var.visitedMineGates = False
        else:
            loadError("visitedMineGates")
        if int(knowsGzahnKathIhnValue) == 1 or int(knowsGzahnKathIhnValue) == 0:
            if int(knowsGzahnKathIhnValue) == 1:
                var.knowsGzahnKathIhn = True
            else:
                var.knowsGzahnKathIhn = False
        else:
            loadError("knowsGzahnKathIhn")
        if int(knowsAshKrahnValue) == 1 or int(knowsAshKrahnValue) == 0:
            if int(knowsAshKrahnValue) == 1:
                var.knowsAshKrahn = True
            else:
                var.knowsAshKrahn = False
        else:
            loadError("knowsAshKrahn")
        if int(knowsBahnArValue) == 1 or int(knowsBahnArValue) == 0:
            if int(knowsBahnArValue) == 1:
                var.knowsBahnAr = True
            else:
                var.knowsBahnAr = False
        else:
            loadError("knowsBahnAr")
        if int(knowsYeelTsurValue) == 1 or int(knowsYeelTsurValue) == 0:
            if int(knowsYeelTsurValue) == 1:
                var.knowsYeelTsur = True
            else:
                var.knowsYeelTsur = False
        else:
            loadError("knowsYeelTsur")
        if int(knowsBorchTrahflValue) == 1 or int(knowsBorchTrahflValue) == 0:
            if int(knowsBorchTrahflValue) == 1:
                var.knowsBorchTrahfl = True
            else:
                var.knowsBorchTrahfl = False
        else:
            loadError("knowsBorchTrahfl")
        if int(knowsFtNagYenValue) == 1 or int(knowsFtNagYenValue) == 0:
            if int(knowsFtNagYenValue) == 1:
                var.knowsFtNagYen = True
            else:
                var.knowsFtNagYen = False
        else:
            loadError("knowsFtNagYen")
        if int(knowsBloodboilValue) == 1 or int(knowsBloodboilValue) == 0:
            if int(knowsBloodboilValue) == 1:
                var.knowsBloodboil = True
            else:
                var.knowsBloodboil = False
        else:
            loadError("knowsBloodboil")
        if int(knowsDarkTreeValue) == 1 or int(knowsDarkTreeValue) == 0:
            if int(knowsDarkTreeValue) == 1:
                var.knowsDarkTree = True
            else:
                var.knowsDarkTree = False
        else:
            loadError("knowsDarkTree")
        if int(knowsHwerFshErrTreeValue) == 1 or int(knowsHwerFshErrTreeValue) == 0:
            if int(knowsHwerFshErrTreeValue) == 1:
                var.knowsHwerFshErrTree = True
            else:
                var.knowsHwerFshErrTree = False
        else:
            loadError("knowsHwerFshErrTree")
        if int(knowsSrshValue) == 1 or int(knowsSrshValue) == 0:
            if int(knowsSrshValue) == 1:
                var.knowsSrsh = True
            else:
                var.knowsSrsh = False
        else:
            loadError("knowsSrsh")
        if int(foundGreatTreeValue) == 1 or int(foundGreatTreeValue) == 0:
            if int(foundGreatTreeValue) == 1:
                var.foundGreatTree = True
            else:
                var.foundGreatTree = False
        else:
            loadError("foundGreatTree") 
        if int(currentRoomValue) == 160 or int(currentRoomValue) == 1 or int(currentRoomValue) == 2 or int(currentRoomValue) == 3 or int(currentRoomValue) == 4 or int(currentRoomValue) == 5 or int(currentRoomValue) == 6 or int(currentRoomValue) == 7 or int(currentRoomValue) == 8 or int(currentRoomValue) == 9 or int(currentRoomValue) == 10 or int(currentRoomValue) == 11:
            var.currentRoom = int(currentRoomValue)
            var.doTurn = False
            if var.currentRoom == 160:
                room.cheatRoom()
            elif var.currentRoom == 1:
                room.mine()
            elif var.currentRooom == 2:
                room.mineEntrance()
            elif var.currentRoom == 3:
                room.commonArea()
            elif var.currentRoom == 4:
                room.companyStore()
            elif var.currentRoom == 5:
                room.messHall()
            elif var.currentRoom == 6:
                room.scripExchange()
            elif var.currentRoom == 7:
                room.mineGates()
            elif var.currentRoom == 8:
                room.crossroads()
            elif var.currentRoom == 9:
                room.darkForest()
            elif var.currentRoom == 10:
                room.outskirts()
            elif var.currentRoom == 11:
                room.imperfection()
        else:
            loadError("currentRoom")
        if int(hasCheatedValue) == 1 or int(hasCheatedValue) == 0:
            if int(hasCheatedValue) == 1:
                var.hasCheated = True
            else:
                var.hasCheated = False
        else:
            loadError("hasCheated")
    else:
        loadError("the string length")