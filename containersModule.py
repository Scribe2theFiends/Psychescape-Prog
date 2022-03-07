import varModule as var
from consumablesModule import drinkMeatStew

def checkFlasks(index):
    fluids = ["MEAT STEW"]
    position = 0
    empty = False
    for x in range(len(var.flaskContent)):
        if var.flaskContent[position] == "EMPTY":
            empty = True
        position += 1
    position = 0
    if empty == True:
        print(f"You pour the {fluids[index]} into an empty flask.")
        var.flaskContent[var.flaskContent.index("EMPTY")] = fluids[index]
    else:
        print("Your flask[s] are full. Choose from the following to empty or consume.")
        for x in range(len(var.flaskContent)):
            print(var.flaskContent[position])
            position += 1
        position = 0
        fluidRemoved = input("\nEnter command here => ")
        if fluidRemoved.lower().strip() not in var.flaskContent:
            error()
            checkFlasks(index)
        else:
            answer = input("(drop) or (consume)? => ")
            if answer.lower().strip() == "drop":
                var.flaskContent[var.flaskContent.index(fluidRemoved)] = index
            elif answer.lower().strip() == "consume":
                if fluidRemoved == "MEAT STEW":
                    drinkMeatStew()
                    var.flaskContent[var.flaskContent.index(fluidRemoved)] = index