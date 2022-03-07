import varModule as var
import random
from math import floor
from formatModule import inbreakline,error
from random import randint

base = 0
rollsLeft = 0
alchemyScore = 0
usedSkills = []

def attack():
    var.finalAttack = 0
    if var.currentWeapon == 1:
        if var.arrows > 0:
            damage(2,1,4,"piercing","none","ranged")
            var.arrows -= 1
            var.arrowsUsed += 1
        else:
            print("\nYou don't have any arrows and do no damage!")
    elif var.currentWeapon == 2:
        if var.shot > 0:
            damage(2,1,3,"blunt","none","ranged")
            var.shot -= 1
            var.shotUsed += 1
        else:
            print("\nYou don't have any shot and do no damage!")
    elif var.currentWeapon == 3:
        if var.chakrams > 0:
            damage(2,1,4,"slashing","none","ranged")
            var.chakramsThrown += 1
            var.chakrams -= 1
        else:
            print("\nYou don't have any chakrams and do no damage!")
    elif var.currentWeapon == 4:
        damage(3,2,3,"blunt","none","melee")
    elif var.currentWeapon == 5:
        damage(3,1,3,"slashing","none","melee")
    elif var.currentWeapon == 6:
        damage(2,1,4,"piercing","none","melee")
    else:
        damage(2,1,2,"blunt","none","melee")

def damage(rolls,min,max,physical,elemental,sort):
    global base
    global rollsLeft
    global usedSkills
    rollsLeft = rolls
    base = 0
    baseRand(min,max)
    if physical == "slashing":
        physical = var.slashingSkill
        usedSkills.append("slashing")
    elif physical == "blunt":
        physical = var.bluntSkill
        usedSkills.append("blunt")
    elif physical == "piercing":
        physical = var.piercingSkill
        usedSkills.append("piercing")
    if elemental == "none":
        elemental = 0
    elif elemental == "fire":
        elemental = var.pyroSkill
        usedSkills.append("fire")
    elif elemental == "ice":
        elemental = var.cryoSkill
        usedSkills.append("ice")
    if sort == "ranged":
        sort = var.rangedSkill
        usedSkills.append("ranged")
    elif sort == "melee":
        sort = var.meleeSkill
        usedSkills.append("melee")
    finalAttack(base, physical, elemental, sort)
    expGain(damage)

#EXP GAIN

def expGain(type):
    global usedSkills
    global alchemyScore
    amountSkills = len(usedSkills)
    expGainPre = 0
    if type == "damage":
        expGainPre = var.finalAttack / amountSkills
    elif type == "alchemical":
        expGainPre = alchemyScore / amountSkills
    expgain = floor(expGainPre)
    if "slashing" in usedSkills:
        if var.physicalProficiency == 3:
            var.slashingEXP += floor((expgain * 1.5) / var.EXPdiluter)
        else:
            var.slashingEXP += floor(expgain / var.EXPdiluter)
    if "piercing" in usedSkills:
        if var.physicalProficiency == 1:
            var.piercingEXP += floor((expgain * 1.5) / var.EXPdiluter)
        else:
            var.piercingEXP += floor(expgain / var.EXPdiluter)
    if "blunt" in usedSkills:
        if var.physicalProficiency == 2:
            var.bluntEXP += floor((expgain * 1.5) / var.EXPdiluter)
        else:
            var.bluntEXP += floor(expgain / var.EXPdiluter)
    if "cryo" in usedSkills:
        if var.alignment == 1:
            var.cryoEXP += floor((expgain * 1.5) / var.EXPdiluter)
        else:
            var.cryoEXP += floor(expgain / var.EXPdiluter)
    if "pyro" in usedSkills:
        if var.alignment == 2:
            var.pyroEXP += floor((expgain * 1.5) / var.EXPdiluter)
        else:
            var.pyroEXP += floor(expgain / var.EXPdiluter)
    if "ranged" in usedSkills:
        if var.typeProficiency == 2:
            var.rangedEXP += floor((expgain * 1.5) / var.EXPdiluter)
        else:
            var.rangedEXP += floor(expgain / var.EXPdiluter)
    if "melee" in usedSkills:
        if var.typeProficiency == 1:
            var.meleeEXP += floor((expgain * 1.5) / var.EXPdiluter)
        else:
            var.meleeEXP += floor(expgain / var.EXPdiluter)
    if "alchemy" in usedSkills:
        var.alchemyEXP += floor(expgain / var.EXPdiluter)
    usedSkills.clear()

# BASERAND

def baseRand(minimum,maximum):
    global base
    global rollsLeft
    if rollsLeft > 0:
        rollsLeft -= 1
        base += randint(minimum,maximum)
        baseRand(minimum,maximum)

def enemyDamage(rolls,min,max,bonus):
    global base
    global rollsLeft
    rollsLeft = rolls
    baseRand(min,max)
    var.enemyAttack = base + bonus

def switchWeapon():
    inbreakline()
    if var.hasBow == False and var.hasSling == False and var.hasMace == False and var.hasSword == False and var.daggers == 0 and var.chakrams == 0:
        print("  You have no weapons to switch to.")
    if var.hasBow == True and var.currentWeapon != 1:
        print("  You may switch to the bow. (bow)")
    if var.hasSling == True and var.currentWeapon != 2:
        print("  You may switch to the sling. (sling)")
    if var.chakrams > 0 and var.currentWeapon != 3:
        print("  You may switch to the chakram. (chakram)")
    if var.hasMace == True and var.currentWeapon != 4:
        print("  You may switch to the mace. (mace)")
    if var.hasSword == True and var.currentWeapon != 5:
        print("  You may switch to the sword. (sword)")
    if var.daggers > 0 and var.currentWeapon != 6:
        print("  You may switch to the dagger. (dagger)")
    if var.currentWeapon != 0:
        print("  You may disarm. (disarm)")
    print("  You may (exit) this menu.")
    answer = input("\nEnter command here => ")
    inbreakline()
    if answer.lower().strip() == "exit":
        print("Exiting the menu.")
    elif answer.lower().strip() == "disarm":
        print("You disarm.")
        var.currentWeapon = 0
    elif answer.lower().strip() == "bow" and var.hasBow == True and var.currentWeapon != 1:
        equip("bow")
    elif answer.lower().strip() == "sling" and var.hasSling == True and var.currentWeapon != 2:
        equip("sling")
    elif answer.lower().strip() == "chakram" and var.chakrams > 0 and var.currentWeapon != 3:
        equip("chakram")
    elif answer.lower().strip() == "mace" and var.hasMace == True and var.currentWeapon != 4:
        equip("mace")
    elif answer.lower().strip() == "sword" and var.hasSword == True and var.currentWeapon != 5:
        equip("sword")
    elif answer.lower().strip() == "dagger" and var.daggers == True and var.currentWeapon != 6:
        equip("dagger")
    else:
        error()
        switchWeapon()

#EQUIP

def equip(name):
    print(f"You equip the {name}.")
    if name == "bow":
        var.currentWeapon = 1
    elif name == "sling":
        var.currentWeapon = 2
    elif name == "chakram":
        var.currentWeapon = 3
    elif name == "sword":
        var.currentWeapon = 5
    elif name == "mace":
        var.currentWeapon = 4
    elif name == "dagger":
        var.currentWeapon = 6

#CURRENT WEAPON

def currentWeapon(name):
    print(f"You are using your {name}.")

#CURRENT AMMO

def currentAmmo(name):
    if name == "arrows":
        ammo = var.arrows
    elif name == "shot":
        ammo = var.shot
    print(f"You have {ammo} {name}")

#WEAPON COUNT

def weaponCount(name):
    if name == "daggers":
        count = var.daggers
    elif name == "chakrams":
        count = var.chakrams
    print(f"You have {count} {name}")
  
#PLAYER STAT FIGHT

def playerFightStats():
    inbreakline()
    print("YOUR STATS:")
    print(f"  {var.currentHP}/{var.HP} HP")
    print(f"  {var.currentPotency}/{var.alchemicalPotency} AP")
    if var.currentWeapon == 1:
        currentWeapon("bow")
        currentAmmo("arrows")
    elif var.currentWeapon == 2:
        currentWeapon("sling")
        currentAmmo("shot")
    elif var.currentWeapon == 3:
        currentWeapon("chakram")
        weaponCount("chakrams")
    elif var.currentWeapon == 4:
        currentWeapon("mace")
    elif var.currentWeapon == 5:    
        currentWeapon("sword")
    elif var.currentWeapon == 6:
        currentWeapon("dagger")
        weaponCount("chakrams")
    elif var.currentWeapon == 0:
        currentWeapon("fists")

#RECOVERY

def recovery():
    inbreakline()
    global chakramsRecovered
    global arrowsRecovered
    global shotRecovered
    global chakrams
    global arrows
    global shot
    chakramsRecovered = 0
    arrowsRecovered = 0
    shotRecovered = 0
    chakrams = False
    arrows = False
    shot = False
    recoveryII()

def recoveryII():
    global chakrams
    global arrows
    global shot
    global chakramsRecovered
    global arrowsRecovered
    global shotRecovered
    if var.chakramsThrown > 0:
        chakrams = True
        var.chakramsThrown -= 1
        chance = random.randint(1,5)
        if chance != 1:
            chakramsRecovered += 1
        recoveryII()
    if var.arrowsUsed > 0:
        arrows = True
        var.arrowsUsed -= 1
        chance = random.randint(1,7)
        if chance != 1 and chance != 2 and chance != 3 and chance != 4:
            arrowsRecovered += 1
        recoveryII()
    if var.shotUsed > 0:
        shot = True
        var.shotUsed -= 1
        chance = random.randint(1,9)
        if chance != 1 and chance != 2 and chance != 3 and chance != 4 and chance != 5:
            shotRecovered += 1
        recoveryII()
    if chakrams == True or arrows == True or shot == True:
        if var.chakramsThrown == 0 and var.arrowsUsed == 0 and var.shotUsed == 0:
            recoveryIII()
        else:
            recoveryII()

def recoveryIII():
    global chakramsRecovered,arrowsRecovered,shotRecovered,chakrams,arrows,shot
    print("\nYou were able to recover:")
    if chakrams == True:
        print(f"  {chakramsRecovered} CHAKRAM[S]")
    if arrows == True:
        print(f"  {arrowsRecovered} ARROW[S]")
    if shot == True:
        print(f"  {shotRecovered} SHOT")
    var.chakrams += chakramsRecovered
    var.arrows += arrowsRecovered
    var.shot += shotRecovered
    chakramsRecovered = 0
    arrowsRecovered = 0
    shotRecovered = 0
    chakrams = False
    arrows = False
    shot = False

#FINAL ATTACK

def finalAttack(b,p,e,s):
    global usedSkills
    sortMod = 1
    elementalMod = 1
    if var.meadStat == 1:
        if "ranged" in usedSkills:
            sortMod = sortMod / 2
        elif "melee" in usedSkills:
            sortMod = sortMod * 2
    if var.pyrohallucinogenStat == 1:
        if "cyro" in usedSkills:
            elementalMod = elementalMod / 2
        elif "pyro" in usedSkills:
            elementalMod = elementalMod * 2
    if var.cryohallucinogenStat == 1:
        if "pyro" in usedSkills:
            elementalMod = elementalMod / 2
        elif "cryo" in usedSkills:
            elementalMod = elementalMod * 2
    var.finalAttack = b + p + (e * elementalMod) + (s * sortMod)

#ALCHEMY

def alchemy():
    global usedSkills
    global alchemyScore
    inbreakline()
    if var.alignment == 2:
        print("Flare: [DISABLE] 6 AP")
    elif var.alignment == 1:
        print("Rime: [DISABLE] 6 AP")
    if var.alchemySkill == 3 and var.mendCooldown == 0:
        print("Mend: [HEAL] 4 AP")
    if var.alchemySkill == 5 and var.alignment == 2:
        print("Scald: [ATTACK] 10 AP")
    elif var.alchemySkill == 5 and var.alignment == 1:
        print("Frigid Blast: [ATTACK] 10 AP")
    answer = input("\nEnter command here => ")
    inbreakline()
    if answer.lower().strip() == "flare" and var.currentPotency > 5 and var.alignment == 2:
        var.flared = random.randint(2,4) + floor((var.alchemySkill + var.pyroSkill) / 2)
        usedSkills.append("alchemy")
        usedSkills.append("pyro")
        print(f"The enemy has caught fire for {var.flared} turns.")
        alchemyScore = var.flared
        expGain("alchemical")
        var.currentPotency -= 6
    elif answer.lower().strip() == "rime" and var.currentPotency > 5 and var.alignment == 1:
        var.rimed = random.randint(2,4) + floor((var.alchemySkill + var.cryoSkill) / 2)
        usedSkills.append("cryo")
        usedSkills.append("alchemy")
        print(f"The enemy has been glazed in ice for {var.rimed} turns.")
        alchemyScore = var.rimed
        expGain("alchemical")
        var.currentPotency -= 6
    elif answer.lower().strip() == "mend" and var.alchemySkill > 2 and var.mendCooldown == 0 and var.currentPotency > 3:
        healed = 0
        healed += randint(1,3)
        healed += randint(1,3)
        healed += randint(1,3)
        healed += var.alchemySkill
        var.currentHP += healed
        print(f"You heal {healed} HP.")
        var.mendCooldown = 2
        alchemyScore = healed
        usedSkills.append("alchemy")
        expGain("alchemical")
        var.currentPotency -= 4
    elif answer.lower().strip() == "scald" and var.alchemicalPotency > 9 and var.alchemySkill > 4 and var.alignment == 2:
        damage = 0
        damage += randint(1,4)
        damage += randint(1,4)
        damage += var.pyroSkill
        damage += var.alchemySkill
        print(f"You deal {damage} damage.")
        alchemyScore = damage
        usedSkills.append("pyro")
        usedSkills.append("alchemy")
        expGain("alchemical")
        var.currentPotency -= 10
    elif answer.lower().strip() == "frigid blast" and var.alchemicalPotency > 9 and var.alignment == 1 and var.alchemySkill >4:
        damage = 0
        damage += randint(1,4)
        damage += randint(1,4)
        damage += var.cryoSkill
        damage += var.alchemySkill
        print(f"You deal {damage} damage.")
        alchemyScore = damage
        usedSkills.append("cryo")
        usedSkills.append("alchemy")
        expGain("alchemical")
        var.currentPotency -= 10