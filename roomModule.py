#ROOM MODULE

#IMPORT

import varModule as var
from formatModule import breakline,error,inbreakline
import uiModule as ui
import saveModule as save
import crystalCaveModule as crystalCave
import mineModule as Rmine
import commonAreaModule as RcommonArea
import companyStoreModule as RcompanyStore
import messHallModule as RmessHall
import mineGatesModule as RmineGates
import scripExchangeModule as RscripExchange
import darkForestModule as RdarkForest
import imperfectionModule as Rimperfection
import mercantileModule as Rmercantile
from timeModule import turnInc

#CHEATROOM

def cheatRoom():
    breakline()
    turnInc()
    var.currentRoom = 160
    print("You pull away a slab of rock and slip behind it, letting it fall back into place.")
    print("You find yourself in a small cave covered entirely in crystals of varying shades of blue and orange.")
    print("You are in the cheatroom.")
    print("\n  You can harness the forces here change reality (cheat).")
    print("  You can leave the cheatroom (exit).")
    answer = input("\nEnter cheat command here => ")
    if answer.lower().strip() == "cheat":
        crystalCave.cheating()
    elif answer.lower().strip() == "exit":
        mine()
    elif answer.lower().strip() == "inventory":
        ui.inventory()
        cheatRoom()
    elif answer.lower().strip() == "help":
        ui.help()
        cheatRoom()
    elif answer.lower().strip() == "codex":
        ui.codex()
        cheatRoom()
    elif answer.lower().strip() == "save":
        save.save()
        cheatRoom()
    elif answer.lower().strip() == "skills":
        ui.skills()
        cheatRoom()
    elif answer.lower().strip() == "stats":
        ui.stats()
        cheatRoom()
    elif answer.lower().strip() == "act":
        ui.act()
        cheatRoom()
    else:
        error()
        cheatRoom()

#MINE

def mine():
    breakline()
    turnInc()
    var.currentRoom = 1
    print("You stand in the mine, a place where demons toil every day in order to dig out anything precious from the ground for a measly amount of scrip.")
    print("\n  You can mine here with your pick (mine).")
    print("  You can go exit to the mine entrance (exit).")
    answer = input("\nEnter command => ")
    if answer.lower().strip() == "exit":
        mineEntrance()
    elif answer.lower().strip() == "mine":
        Rmine.mining()
    elif answer.lower().strip() == "cheatroom":
        cheatRoom()
    elif answer.lower().strip() == "inventory":
        ui.inventory()
        mine()
    elif answer.lower().strip() == "help":
        ui.help()
        mine()
    elif answer.lower().strip() == "codex":
        ui.codex()
        mine()
    elif answer.lower().strip() == "save":
        save.save()
        mine()
    elif answer.lower().strip() == "act":
        ui.act()
        mine()
    elif answer.lower().strip() == "stats":
        ui.stats()
        mine()
    elif answer.lower().strip() == "skills":
        ui.skills()
        mine()
    else:
        error()
        mine()

#MINE ENTRANCE

def mineEntrance():
    breakline()
    turnInc()
    var.currentRoom = 2
    print("You stand in front of the mine entrance, hearing the chipping of metal and rock down below.")
    print("\n  You can enter the mine to do some work (enter).")
    print("  You can go west to the scrip exchange (west).")
    print("  You can go south to the gates of the work site (south).")
    print("  You can go east to the common area (east).")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "enter":
        mine()
    elif answer.lower().strip() == "west":
        scripExchange()
    elif answer.lower().strip() == "south":
        mineGates()
    elif answer.lower().strip() == "east":
        commonArea()
    elif answer.lower().strip() == "inventory":
        ui.inventory()
        mineEntrance()
    elif answer.lower().strip() == "help":
        ui.help()
        mineEntrance()
    elif answer.lower().strip() == "codex":
        ui.codex()
        mineEntrance()
    elif answer.lower().strip() == "save":
        save.save()
        mineEntrance()
    elif answer.lower().strip() == "act":
        ui.act()
        mineEntrance()
    elif answer.lower().strip() == "stats":
        ui.stats()
        mineEntrance()
    elif answer.lower().strip() == "skills":
        ui.skills()
        mineEntrance()
    else:
        error()
        mineEntrance()

#COMMON AREA

def commonArea():
    breakline()
    turnInc()
    var.currentRoom = 3
    print("The common area stands in the middle of a couple buildings, and many people hang around here when not working.")
    print("\n  You can go west to the mine entrance (west).")
    print("  You can go inside the company store, where you can purchase goods and turn in mining scrip for U= [Unified Currency], at whatever exchange rate the company deems right (enterstore).")
    print("  You can go to the mess hall and buy some food (enterhall).")
    print("  It looks like there is someone off in the corner of the open space, leaning on a table that also happens to contain a large pile of numerous minerals. Every now and then you see them entice a passerby into betting on a game of Fiendish Gamble, often betting with the minerals available on the table, sometimes with scrip, and rarely with U=. (gambler)")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "west":
        mineEntrance()
    elif answer.lower().strip() == "enterstore":
        companyStore()
    elif answer.lower().strip() == "enterhall":
        messHall()
    elif answer.lower().strip() == "gambler":
        inbreakline()
        RcommonArea.lossGambling()
        commonArea()
    elif answer.lower().strip() == "inventory":
        ui.inventory()
        commonArea()
    elif answer.lower().strip() == "help":
        ui.help()
        commonArea()
    elif answer.lower().strip() == "codex":
        ui.codex()
        commonArea()
    elif answer.lower().strip() == "save":
        save.save()
        commonArea()
    elif answer.lower().strip() == "act":
        ui.act()
        commonArea()
    elif answer.lower().strip() == "skills":
        ui.skills()
        commonArea()
    elif answer.lower().strip() == "stats":
        ui.stats()
        commonArea()
    else:
        error()
        commonArea()

#COMPANY STORE

def companyStore():
    breakline()
    turnInc()
    var.currentRoom = 4
    print("As you open the door to the company store a gong rings out. The large woman behind the counter looks to you, then looks back to whatever she is doing behind the counter. \"If you want to buy something, please figure out what you want to get before you ask me for something. If you want to exchange scrip for unity, please make sure you have enough scrip before you try to make a transaction. In short, don't waste my time.\"")
    print("\n  You can leave the store (exit).")
    print("  You can exchange mining scrip for U= (exchange).")
    print("  You can buy things from the store here (buy).")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "exit":
        commonArea()
    elif answer.lower().strip() == "exchange":
        RcompanyStore.unityExchange()
    elif answer.lower().strip() == "buy":
        RcompanyStore.shop()
    elif answer.lower().strip() == "inventory":
        ui.inventory()
        companyStore()
    elif answer.lower().strip() == "help":
        ui.help()
        companyStore()
    elif answer.lower().strip() == "codex":
        ui.codex()
        companyStore()
    elif answer.lower().strip() == "save":
        save.save()
        companyStore()
    elif answer.lower().strip() == "act":
        ui.act()
        companyStore()
    elif answer.lower().strip() == "skills":
        ui.skills()
        companyStore()
    elif answer.lower().strip() == "stats":
        ui.stats()
        companyStore()
    else:
        error()
        companyStore()

def messHall():
    breakline()
    turnInc()
    var.currentRoom = 5
    print("You step into the mess hall, a rather small room filled with noise with a counter where you can buy food. Demons don't need to eat, but it's fun to most of them, everyone likes a bit of flavor now and then.")
    print("\n  You can exit the building (exit).")
    print("  You can buy some food (buy).")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "exit":
        commonArea()
    elif answer.lower().strip() == "buy":
        RmessHall.food()
    elif answer.lower().strip() == "inventory":
        ui.inventory()
        messHall()
    elif answer.lower().strip() == "help":
        ui.help()
        messHall()
    elif answer.lower().strip() == "codex":
        ui.codex()
        messHall()
    elif answer.lower().strip() == "save":
        save.save()
        messHall()
    elif answer.lower().strip() == "act":
        ui.act()
        messHall()
    elif answer.lower().strip() == "skills":
        ui.skills()
        messHall()
    elif answer.lower().strip() == "stats":
        ui.stats()
        messHall()
    else:
        error()
        messHall()
        
#MINE GATES

def mineGates():
    var.currentRoom = 7
    breakline()
    turnInc()
    print("When you get close to the gates, you see a guard and everyone's favorite Gzahn'Kath-In, Ren'Shaw.")
    var.knowsGzahnKathIhn = True
    if var.visitedMineGates == False:
        RmineGates.firstVisit()
    else:
        if var.shownMinePermit == False:
            RmineGates.returnVisitF()
        else:
            RmineGates.returnVisitT()

#CROSSROADS

def crossroads():
    breakline()
    turnInc()
    var.currentRoom = 8
    print("You stand at a crossroads.")
    print("There is a sign. It reads \"South: Town of Ysair-In    North: Garl-Hath Mines\"")
    print("\n  You can go north to the gates of the mine (north).")
    print("  You can go south to the very outskirts of a quaint little town (south).")
    print("  You can go east to the dark forest (east).")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "north":
        mineGates()
    elif answer.lower().strip() == "east":
        darkForest()
    elif answer.lower().strip() == "south":
        outskirts()
    elif answer.lower().strip() == "inventory":
        ui.inventory()
        crossroads()
    elif answer.lower().strip() == "help":
        ui.help()
        crossroads()
    elif answer.lower().strip() == "codex":
        ui.codex()
        crossroads()
    elif answer.lower().strip() == "save":
        save.save()
        crossroads()
    elif answer.lower().strip() == "act":
        ui.act()
        crossroads()
    elif answer.lower().strip() == "skills":
        ui.skills()
        crossroads()
    elif answer.lower().strip() == "stats":
        ui.stats()
        crossroads() 
    else:
        error()
        crossroads()

#SCRIP EXCHANGE

def scripExchange():
    breakline()
    turnInc()
    var.currentRoom = 6
    print("You stand before the scrip exchange. There is a scrawny man behind the counter who will give you scrip in accordance to what the company deems what you exchange is worth.")
    print("\n  You can go east to the  mine entrance (east).")
    print("  You can exchange things you have mined for mine scrip (exchange).")
    answer = input("\nEnter command => ")
    if answer.lower().strip() == "east":
        mineEntrance()
    elif answer.lower().strip() == "exchange":
        inbreakline()
        RscripExchange.exchange()
    elif answer.lower().strip() == "inventory":
        ui.inventory()
        scripExchange()
    elif answer.lower().strip() == "help":
        ui.help()
        scripExchange()
    elif answer.lower().strip() == "codex":
        ui.codex()
        scripExchange()
    elif answer.lower().strip() == "save":
        save.save()
        scripExchange()
    elif answer.lower().strip() == "act":
        ui.act()
        scripExchange()
    elif answer.lower().strip() == "skills":
        ui.skills()
        scripExchange()
    elif answer.lower().strip() == "stats":
        ui.stats()
        scripExchange()
    else:
        error()
        scripExchange()

#DARK FOREST

def darkForest():
    breakline()
    turnInc()
    var.currentRoom = 9
    print("You walk a little ways into the forest, and dark trees quickly close in around you. There's very little light reaching down to the forest floor, and the ground is littered with leaves of varying tints of black, with different colors such as brown and reddish mixed in occaisionally. You'd better be careful not to get lost here.")
    print("\n  You may go west to the crossroads (west).")
    print("  You can walk through the forest (walk).")
    answer = input("\nEnter command => ")
    if answer.lower().strip() == "west":
        crossroads()
    elif answer.lower().strip() == "walk":
        inbreakline()
        RdarkForest.wanderForest()
    elif answer.lower().strip() == "inventory":
        ui.inventory()
        darkForest()
    elif answer.lower().strip() == "codex":
        ui.codex()
        darkForest()
    elif answer.lower().strip() == "help":
        ui.help()
        darkForest()
    elif answer.lower().strip() == "save":
        save.save()
        darkForest()
    elif answer.lower().strip() == "act":
        ui.act()
        darkForest()
    elif answer.lower().strip() == "skills":
        ui.skills()
        darkForest()
    elif answer.lower().strip() == "stats":
        ui.stats()
        darkForest()
    else:
        error()
        darkForest()

#Outskirts

def outskirts():
    breakline()
    turnInc()
    var.currentRoom = 10
    print("You walk up to the outskirts of a sparse town, with the outskirts of the town being even sparcer. The most busy thing here seems to be the Nonx-Ran'Yev-tsir, a sign displaying the name as simply \"Imperfection\"  which is currently somewhat busy. There are some other houses around, but you probably shouldn't just go into them uninvited.")
    #add in ____ bar here, to add to the codex.
    print("\n  You may go north to the crossroads (north).")
    print("  You may go west to the mercantile district. (west)")
    print("  You may enter Imperfection (imperfection).")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "north":
        crossroads()
    elif answer.lower().strip() == "west":
        mercantile()
    elif answer.lower().strip() == "imperfection":
        imperfection()
    elif answer.lower().strip() == "inventory":
        ui.inventory()
        outskirts()
    elif answer.lower().strip() == "help":
        ui.help()
        outskirts()
    elif answer.lower().strip() == "codex":
        ui.codex()
        outskirts()
    elif answer.lower().strip() == "save":
        save.save()
        outskirts()
    elif answer.lower().strip() == "act":
        ui.act()
        outskirts()
    elif answer.lower().strip() == "stats":
        ui.stats()
        outskirts()
    elif answer.lower().strip() == "skills":
        ui.skills()
        outskirts()
    else:
        error()
        outskirts()

#IMPERFECTION

def imperfection():
    breakline()
    turnInc()
    var.currentRoom = 11
    print("Upon entering Imperfection, you find it much less busy than you intially thought. There's a large area set along the back full of various things for the creation of varying Nonx-Ran.There are also varying patrons wandering around, you could talk to them if you want, maybe catch wind of something soon to come.")
    print("\n  You may (order) something.")
    print("  You may (ask) around for information.")
    print("  You may (exit) the building.")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "exit":
        outskirts()
    elif answer.lower().strip() == "ask":
        Rimperfection.chatter()
        imperfection()
    elif answer.lower().strip() == "order":
        Rimperfection.order()
    elif answer.lower().strip() == "inventory":
        ui.inventory
        imperfection()
    elif answer.lower().strip() == "help":
        ui.help()
        imperfection()
    elif answer.lower().strip() == "codex":
        ui.codex()
        imperfection()
    elif answer.lower().strip() == "save":
        save.save()
        imperfection()
    elif answer.lower().strip() == "act":
        ui.act()
        imperfection()
    elif answer.lower().strip() == "stats":
        ui.stats()
        imperfection()
    elif answer.lower().strip() == "skills":
        ui.skills()
        imperfection()
    else:
        imperfection()

#MERCANTILE

def mercantile():
    breakline()
    turnInc()
    var.currentRoom = 12
    print("You make your way into the mercantile district, only to find what you would expect to be a bustling center of commerce to be relatively quiet. The only store that seems to be open is an armoury shop advertising that they sell various weapons and other equipment pieces.")
    print("\n  You may go east to the outskirts. (east)")
    print("  You may enter the armoury. (armoury)")
    print("  You may enter the general store. (gstore)")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "east":
        outskirts()
    elif answer.lower().strip() == "armoury":
        Rmercantile.armoury()
    elif answer.lower().strip() == "gstore":
        Rmercantile.justEntered = True
        Rmercantile.generalStore()
    elif answer.lower().strip() == "inventory":
        ui.inventory()
        mercantile()
    elif answer.lower().strip() == "help":
        ui.help()
        mercantile()
    elif answer.lower().strip() == "codex":
        ui.codex()
        mercantile()
    elif answer.lower().strip() == "save":
        save.save()
        mercantile()
    elif answer.lower().strip() == "act":
        ui.act()
        mercantile()
    elif answer.lower().strip() == "stats":
        ui.stats()
        mercantile()
    elif answer.lower().strip() == "skills":
        ui.skills()
        mercantile()
    else:
        error()
        mercantile()