#UI MODULE

#IMPORT

import varModule as var
from formatModule import uibreakline,error,uiError
from consumablesModule import eatJigglers,eatDarkTreeSap,eatBloodboilBerries,eatDarkTreeFruit,eatHwerFshErrFruit,eatFlatbread,usePyrohallucinogen,useCryohallucinogen

#ACT

def act():
    uibreakline()
    print("What would you like to do?")
    print("\n  You may (eat) a food item.")
    print("  You may (take) a nonx'ran.")
    print("  You may (exit) this command prompt.")
    answer = input("\nEnter command here => ")
    uibreakline()
    if answer.lower().strip() == "eat":
        if var.jigglers > 0:
            print("  JIGGLERS (jigglers)")
        if var.darkTreeSap > 0:
            print("  DARK TREE SAP (dtsap")
        if var.darkTreeFruit > 0:
            print("  DARK TREE FRUIT (dtfruit)")
        if var.bloodboilBerries > 0:
            print("  BLOODBOIL BERRIED (bberries)")
        print("  You may exit the menu (exit)")
        if var.hwerFshErrFruit > 0:
            print("  HWER'FSH'ERR FRUIT (hfruit)")
        if var.flatbread > 0:
            print("  FLATBREAD (bread)")
        answer = input("\nWhat would you like to eat? => ")
        uibreakline()
        if answer.lower().strip() == "jigglers" and var.jigglers >= 1:
            var.jigglers -= 1
            eatJigglers()
        elif answer.lower().strip() == "dtsap" and var.darkTreeSap >= 1:
            var.darkTreeSap -= 1
            eatDarkTreeSap()
        elif answer.lower().strip(
        ) == "bberries" and var.bloodboilBerries >= 1:
            var.bloodboilBerries -= 1
            eatBloodboilBerries()
        elif answer.lower().strip(
        ) == "dtfruit" and var.darkTreeFruit > 0:
            var.darkTreeFruit -= 1
            eatDarkTreeFruit()
        elif answer.lower().strip(
        ) == "hfruit" and var.hwerFshErrFruit > 0:
            eatHwerFshErrFruit()
        elif answer.lower().strip() == "bread" and var.flatbread > 0:
            eatFlatbread()
        elif answer.lower().strip() == "exit":
            print("Closing action menu")
        else:
            error()
            act()
    elif answer.lower().strip() == "take":
        if var.pyrohallucinogen > 0:
            print("\n  PYROHALLUCINOGEN (pyro)")
        if var.cryohallucinogen > 0:
            print("  CRYOHALLUCINOGEN (cryo)")
        print("You may ext the menu. (exit)")
        answer = input("\nEnter command here => ")
        uibreakline()
        if answer.lower().strip() == "pyro" and var.pyrohallucinogen > 0:
            var.pyrohallucinogen -= 1
            usePyrohallucinogen()
            
        elif answer.lower().strip() == "cryo" and var.cryohallucinogen > 0:
            var.cryohallucinogen -= 1
            useCryohallucinogen()
        elif answer.lower().strip() == "exit":
            print("Exiting the menu.")
    elif answer.lower().strip() == "exit":
        print("Closing action menu")
    else:
        error()
        act()
    var.doTurn = False


#CODEX


def codex():
    uibreakline()
    print(
        "The codex tells you information about the world. There are several sections in the codex you can access."
    )
    print(
        "\n  The dictionary section, providing definitions for demonic words that you don't understand (dictionary)."
    )
    print("  The fauna section of the codex (fauna).")
    print("  The flora section of the codex (flora).")
    print("  The mineralogy section of the codex (mineralogy).")
    print("  You may close the codex (close).")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "dictionary":
        uibreakline()
        if var.knowsSrsh == False:
            print("  You have recorded nothing here.")
        if var.knowsSrsh == True:
            print("  (srsh)")
        print("  You may close the codex (close)")
        answer = input("\nEnter command here => ")
        uibreakline()
        if answer.lower().strip() == "srsh" and var.knowsSrsh == True:
            print(
                "    Srsh is an onomonatopoeic word in the demon language, much like the word moo or buzz. Srsh represents the noise that a Gzahn'Kath-Ihn makes, something in between a serpentine hiss and a feline purr. When one is currently making said noise they Srsh*Veesh, which is represented as Srsh's [like purrs] for those who know english and aren't familiar with demonic."
            )
        elif answer.lower().strip() == "close":
            uibreakline()
            print("Closing the codex.")
        else:
            uiError()
            codex()
    elif answer.lower().strip() == "fauna":
        uibreakline()
        if var.knowsAshKrahn == False and var.knowsBahnAr == False and var.knowsBorchTrahfl == False and var.knowsFtNagYen == False and var.knowsGzahnKathIhn == False and var.knowsYeelTsur == False:
            print("  You have recorded nothing here.")
        if var.knowsAshKrahn == True:
            print("  Ash-Krahn (ashkrahn)")
        if var.knowsBahnAr == True:
            print("  Bahn-Ar (bahnar)")
        if var.knowsBorchTrahfl == True:
            print("  Borch-Trahfl (borchtrahfl)")
        if var.knowsFtNagYen == True:
            print("  Ft'Nag-Yen (ftnagyen)")
        if var.knowsGzahnKathIhn == True:
            print("  Gzahn'Kath-Ihn (gzahnkathihn)")
        if var.knowsYeelTsur == True:
            print("  Yeel'Tsur (yeeltsur)")
        print("  You may close the codex (close).")
        answer = input("\n  Enter command here => ")
        if answer.lower().strip(
        ) == "gzahnkathihn" and var.knowsGzahnKathIhn == True:
            uibreakline()
            print(
                "    A Gzahn'Kath-Ihn is a creature found in the Psychescape which looks like a predatory big cat from your world, but more reptillian, posessing no fur or external ears, it is covered entirely in smooth scales, with a tongue and eyes like a serpent. It's believed by some people that the Gzahn'Kath-Ihn were first born by Pra'Xiint'Nabaskia from her time as Kt'Hia-Ce'Theor's lover. However, this theory is widely discredited, with the Fiends themselves saying no such thing happened, but it lives on in some religious circles."
            )
        elif answer.lower().strip(
        ) == "ashkrahn" and var.knowsAshKrahn == True:
            uibreakline()
            print(
                "    An Ash-Krahn is a create found in the psychescape that is about the size of a house cat and looks vaguely similar ot a squirrel from your world. The Ash-Krahn posses four limbs that it uses for mobility, as well as an additional pair of limbs on the front that is used to stir up leaf clutter and detrius in their environment. This is used to fighten potential threats."
            )
        elif answer.lower().strip(
        ) == "bahnar" and var.knowsBahnAr == True:
            uibreakline()
            print(
                "    A Bahn-Ar is a wolf-like creature found in the Psychescape that possesses large bottom fangs, great night vision, and a black coat. The Bahn-Ar is a lone hunter, only coming together with a mate, and still spending little time together. It is well equiped to ambush and chase down it's prey, choosing to hunt when it is dark out."
            )
        elif answer.lower().strip(
        ) == "yeeltsur" and var.knowsYeelTsur == True:
            uibreakline()
            print(
                "    A Yeel'Tsur is a bipedal creature about the size of a small child, and looks much like an ape from your world. They live in small groups and are mostly scavengers. They will not prey aside from bugs and occaisionally small mammals, but will often be found eating discarded carcasses."
            )
        elif answer.lower().strip(
        ) == "borchtrahfl" and var.knowsBorchTrahfl == True:
            uibreakline()
            print(
                "    A Borch'Trahfl looks almost identical to a feral hog from your world. They are however smaller. They travel in groups for safety and will flee rather than fight if under attack."
            )
        elif answer.lower().strip(
        ) == "ftnagyen" and var.knowsFtNagYen == True:
            uibreakline()
            print(
                "    A Ft'Nag-Yen is a centipede-like creature that grows to be larger than a person. They are often found in pools of ichor, where they wait to ambush their prey with surprising speed. They hold the front section of their body upright, where they have several appendages meant for grasping and slashing at prey. They are able to stay submerged for a long time, and often will stay there when they are not hunting. Though it is not terribly popular, many enjoy the meat, which supposedly is make like the meat of a lobster from your world."
            )
        elif answer.lower().strip() == "close":
            uibreakline()
            print("Closing the codex.")
        else:
            uiError()
            codex()
    elif answer.lower().strip() == "flora":
        uibreakline()
        if var.knowsBloodboil == False and var.knowsDarkTree == False and var.knowsHwerFshErrtree == False:
            print("  You have recorded nothing here.")
        if var.knowsBloodboil == True:
            print("  Bloodboil (bloodboil)")
        if var.knowsDarkTree == True:
            print("  Dark Tree (darktree)")
        if var.knowsHwerFshErrTree == True:
            print("  Hwer'Fsh'Err (hwerfsherr)")
        print("  You may close the codex (close)")
        answer = input("\nEnter command here => ")
        if answer.lower().strip() == "close":
            uibreakline()
            print("Closing the codex.")
        elif answer.lower().strip(
        ) == "darktree" and var.knowsDarkTree == True:
            uibreakline()
            print(
                "    The Dark Tree is a tree that can be found in the Psychescape possessing an almost entirely black color scheme. These trees easily absorb heat during the day, allowing forests of them to remain warm even into the night. They also possess an extremely sugary sap and fruit which can be quite popular."
            )
        elif answer.lower().strip(
        ) == "bloodboil" and var.knowsBloodboil == True:
            uibreakline()
            print(
                "    The Bloodboil is a small shrub that is found in the Psychescape. It bears aggregate fruits similar to the raspberries from your world. However the plant also produces wax that will cover the fruit for protection. The fruits of this plant are always quite warm however, which causes the wax to slowly drip off of the fruit. The wax of the plant is gathered and used for things all the way from candles to sealing wax to being used in alchemical rituals."
            )
        elif answer.lower().strip(
        ) == "hwerfsherr" and var.knowsHwerFshErrTree == True:
            uibreakline()
            print(
                "    The Hwer\'Fsh\'Err is rare tree found in the Psychescape. The tree is entirely black, unless the flowers are in bloom or the fruits are ripe. There are rarely many flowers on the tree, with a mature specimen typically having at most two-dozen flowers. They flowers are large and bright orange, colored like fire and will actually glow dimly. The fruit, which is roughly tear-dropped and covered in a thin but hard shell, will be deep black but will begin to have the inside glow with an orange light, giving the impression of an ember. The juices inside the fruit are what actually glow orange, and are quite bright. Usually if the shell has been cracked it losses it glow and spoils quickly, but can last for a long time if the shell is intact."
            )
        else:
            uiError()
            codex()
    elif answer.lower().strip() == "mineralogy":
        print("You have recorded nothing here.")
        print("  You may close the codex (close)")
        answer = input("  Enter command here => ")
        uibreakline()
        if answer.lower().strip() == "close":
            print("Closing the codex.")
        else:
            uiError()
            codex()
    elif answer.lower().strip() == "close":
        print("Closing the codex.")
    else:
        uiError()
        codex()
    var.doTurn = False


#INVENTORY


def inventory():
    uibreakline()
    if var.hasCheated == True:
        print("  YOU ARE A DIRTY CHEATER. YOU HAVE BEEN CAUGHT CHEATING.\n")
        print("What inventory would you like to check?")
    else:
        print("What inventory would you like to check?")
    print("\n  Key Items (kitems)")
    print("  Trade Goods (tgoods)")
    print("  Food & Drink (f&d)")
    print("  Equipment (equipment)")
    print("  Currency (currency)")
    print("  Or exit this menu (exit)")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "kitems":
        keyItemsInventory()
    elif answer.lower().strip() == "tgoods":
        tradeGoodsInventory()
    elif answer.lower().strip() == "f&d":
        foodAndDrinkInventory()
    elif answer.lower().strip() == "currency":
        currencyInventory()
    elif answer.lower().strip() == "equipment":
        equipmentInventory()
    elif answer.lower().strip() == "exit":
        uibreakline()
        print("Closing the inventory.")
    else:
        uiError()
        inventory()
    var.doTurn = False


#KEY ITEMS INVENTORY


def keyItemsInventory():
    uibreakline()
    if var.hasCheated == True:
        print("YOU ARE A DIRTY CHEATER. YOU HAVE BEEN CAUGHT CHEATING.\n")
    print("  You have the following key items;")
    print("    1 PICKAXE")
    if var.hasMinePermit == True:
        print("    1 PERMIT TO LEAVE GROUNDS")


def tradeGoodsInventory():
    uibreakline()
    if var.hasCheated == True:
        print("YOU ARE A DIRTY CHEATER. YOU HAVE BEEN CAUGHT CHEATING.\n")
    print("  You have the following trade goods;")
    if var.ichorCount >= 1:
        print(f"    {var.ichorCount} NODULE[S] OF ICHOR")
    if var.largeIchorCount >= 1:
        print(f"    {var.largeIchorCount} LARGE NODULE[S] OF ICHOR")
    if var.sculptureGradeIchorCount >= 1:
        print(
            f"    {var.sculptureGradeIchorCount} SCULPTURE GRADE NODULE[S] OF ICHOR"
        )
    if var.coalCount >= 1:
        print(f"    {var.coalCount} CHUNK[S] OF COAL")
    if var.largeCoalCount >= 1:
        print(f"    {var.largeCoalCount} LARGE CHUNK[S] OF COAL")
    if var.commonArsonSalts >= 1:
        print(
            f"    {var.commonArsonSalts} PARCEL[S] OF COMMON ARSON SALTS"
        )
    if var.rareArsonSalts >= 1:
        print(f"    {var.rareArsonSalts} PARCEL[S] OF RARE ARSON SALTS")
    if var.bloodboilWax >= 1:
        print(f"    {var.bloodboilWax} LUMP[S] OF BLOODBOIL WAX")


def foodAndDrinkInventory():
    uibreakline()
    if var.hasCheated == True:
        print("YOU ARE A DIRTY CHEATER. YOU HAVE BEEN CAUGHT CHEATING.\n")
    print("  You have the following food and drink items;")
    if var.jigglers >= 1:
        print(f"    {var.jigglers} JIGGLERS")
    if var.darkTreeSap >= 1:
        print(f"    {var.darkTreeSap} CLUMP[S] OF DARK TREE SAP")
    if var.darkTreeFruit >= 1:
        print(f"    {var.darkTreeFruit} FRUIT[S] FROM A DARK TREE")
    if var.bloodboilBerries >= 1:
        print(f"    {var.bloodboilBerries} BLOODBOIL BERRY BUNCH[ES]")
    if var.hwerFshErrFruit >= 1:
        print(
            f"    {var.hwerFshErrFruit} FRUIT[S] FROM A HWER'FSH'ERR TREE"
        )


def currencyInventory():
    uibreakline()
    if var.hasCheated == True:
        print("YOU ARE A DIRTY CHEATER. YOU HAVE BEEN CAUGHT CHEATING.\n")
    print("  You have the following currencies;")
    if var.scripCount >= 1:
        print(f"    {var.scripCount} MINING SCRIP")
    if var.unifiedCount >= 1:
        print(f"    {var.unifiedCount} UNITY [U=]")


def equipmentInventory():
    uibreakline()
    if var.hasCheated == True:
        print("YOU ARE A DIRTY CHEATER. YOU HAVE BEEN CAUGHT CHEATING.\n")
    print("  You have the following equipment;")
    if var.hasBow == True:
        print("    1 BOW")
    if var.arrows > 0:
        print(f"    {var.arrows} ARROW[S]")
    if var.hasSling == True:
        print("    1 SLING")
    if var.shot > 0:
        print(f"    {var.shot} SHOT")
    if var.chakrams > 0:
        print(f"    {var.chakrams} CHAKRAM[S]")
    if var.hasMace == True:
        print("    1 MACE")
    if var.hasSword == True:
        print("    1 SWORD")
    if var.daggers > 0:
        print(f"    {var.daggers} DAGGER[S]")


#HELP


def help():
    uibreakline()
    print("What would you like help with? There are;")
    print("\n  Unlisted commands (commands)")
    print("  General Help (general)")
    print("  To exit this prompt type (exit).")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "commands":
        uibreakline()
        print("The following are unlisted commands;")
        print("  (inventory)")
        print("  (help)")
        print("  (codex)")
        print("  (save)")
        print("  (act)")
        print("  (stats)")
        print("  (skills)")
    elif answer.lower().strip() == "exit":
        uibreakline()
        print("Prompt closed.")
    elif answer.lower().strip() == "general":
        uibreakline()
        print("  When you are able to enter a command you will see a \"=>\"")
        print(
            "  You can see what you have to enter for a command to work as it is encased within parentheses \"()\""
        )
        print(
            "  Some commands can be executed any time you are in a base room, and therefor are not listed with the other commands."
        )
        print(
            "    One such example is the (inventory) command, which lets your see your inventory."
        )
        print(
            "    Another command is the (help) command, that shows different information in game than it does here."
        )
        print(
            "  When typing your command, don't worry about if you accidentally added a space or capitalized, your command will be processed all the same. If you are playing and find that this is not the case, please contact me to fix the potential bug. Screenshots of your command are much appreciated :) You can also feel free to correct my spell/grammar at any time you would like."
        )
    else:
        uiError()
        help()
    var.doTurn = False


def stats():
    uibreakline()
    print(f"HP: {var.currentHP}/{var.HP}")
    print(f"AP: {var.currentPotency}/{var.alchemicalPotency}")
    print(f"Wellness: {var.wellness}/100")
    if var.alignment == 1:
        alignment("Ice")
    elif var.alignment == 2:
        alignment("Fire")
    if var.currentWeapon == 1:
        weapon("Bow")
        ammunition("arrows")
    elif var.currentWeapon == 2:
        weapon("Sling")
        ammunition("shot")
    elif var.currentWeapon == 3:
        weapon("Chakram")
    elif var.currentWeapon == 4:
        weapon("Mace")
    elif var.currentWeapon == 5:
        weapon("Sword")
    elif var.currentWeapon == 6:
        weapon("Dagger")
    elif var.currentWeapon == 0:
        weapon("None")
    print("Status Effects:")
    if var.meadStat == 0 and var.pyrohallucinogenStat == 0 and var.cryohallucinogenStat == 0:
        print("  None")
    if var.meadStat == 1:
        print(f"  Mead: {var.meadDecay} turns left.\n  Melee dmg *2, Ranged dmg /2")
    if var.pyrohallucinogenStat == 1:
        print(f"  Pyrohallucinogen: {var.pyrohallucinogenDecay} turns left.\n  Pyro dmg *2, Cryo dmg /2")
    if var.cryohallucinogenStat == 1:
        print(f"  Cryohallucinogen: {var.cyrohallucinogenDecay} turns left.\n  Cryo dmg *2, Pyro dmg /2")
    var.doTurn = False


def weapon(equipped):
    print(f"Weapon: {equipped}")

def ammunition(type):
    if type == "arrow":
        count = var.arrows
    elif type == "shot":
        count = var.shot
    print(f"Ammo Type: {type}")
    print(f"Ammo Count: {count}")

def alignment(element):
    print(f"Alignment: {element}")


def skills():
    uibreakline()
    print("Vital skill:")
    print(
        f"  Level: {var.playerVitals},  EXP until next level: {var.vitalEXPneeded - var.vitalEXP}"
    )
    print("Alchemy skill:")
    print(
        f"  Level: {var.playerVitals},  EXP until next level: {var.alchemyEXPneeded - var.alchemyEXP}"
    )
    print("Piercing skill:")
    print(
        f"  Level: {var.piercingSkill},  EXP: until next level {var.piercingEXPneeded - var.piercingEXP}"
    )
    print("Blunt skill:")
    print(
        f"  Level: {var.bluntSkill},  EXP until next level: {var.bluntEXPneeded - var.bluntEXP}"
    )
    print("Slashing skill:")
    print(
        f"  Level: {var.slashingSkill},  EXP until next level: {var.slashingEXPneeded - var.slashingEXP}"
    )
    print("Pyro skill:")
    print(
        f"  Level: {var.pyroSkill},  EXP until next level: {var.pyroEXPneeded - var.pyroEXP}"
    )
    print("Cryo skill:")
    print(
        f"  Level: {var.cryoSkill},  EXP until next level: {var.cryoEXPneeded - var.cryoEXP}"
    )
    print("Ranged skill:")
    print(
        f"  Level: {var.rangedSkill},  EXP until next level: {var.rangedEXPneeded - var.rangedEXP}"
    )
    print("Melee skill:")
    print(
        f"  Level: {var.meleeSkill},  EXP until next level: {var.meleeEXPneeded - var.meleeEXP}"
    )
    var.doTurn = False
