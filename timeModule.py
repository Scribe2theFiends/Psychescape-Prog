import varModule as var

regenA = 0
regenB = 0
switch = 0

def turnInc():
    if var.doTurn == True:
        var.turn += 1
        var.wellness -= 1
        regeneration()
        statusDecay()
    else:
        var.doTurn = True
        

def regeneration():
    global regenA
    global regenB
    global switch
    wellnessPer = var.wellness / 100
    if wellnessPer >= 0 and wellnessPer < 0.125:
        regenA = 1
        regenB = 0
    elif wellnessPer >= 0.125 and wellnessPer < 0.25:
        regenA = 1
        regenB = 1
    elif wellnessPer >= 0.25 and wellnessPer < 0.375:
        regenA = 2
        regenB = 1
    elif wellnessPer >= 0.375 and wellnessPer < 0.5:
        regenA = 2
        regenB = 2
    elif wellnessPer >= 0.5 and wellnessPer < 0.625:
        regenA = 3
        regenB = 2
    elif wellnessPer >= 0.625 and wellnessPer < 0.75:
        regenA = 3
        regenB = 3
    elif wellnessPer >= 0.75 and wellnessPer < 0.875:
        regenA = 4
        regenB = 3
    elif wellnessPer >= 0.875 and wellnessPer <= 1:
        regenA = 4
        regenB = 4
    if switch == 0:
        var.currentHP += regenA
        var.currentPotency += regenB
        switch = 1
    elif switch == 1:
        var.currentPotency += regenA
        var.currentHP += regenB
        switch = 0
    if  var.currentPotency > var.alchemicalPotency:
        var.currentPotency = var.alchemicalPotency
    if var.currentHP > var.HP:
        var.currentHP = var.HP

def statusDecay():
    if var.meadDecay > 0:
        var.meadDecay -= 1
    if var.pyrohallucinogenDecay > 0:
        var.pyrohallucinogenDecay -= 1
    if var.cyrohallucinogenDecay > 0:
        var.cyrohallucinogenDecay -= 1
    if var.meadDecay == 0:
        var.meadStat = 0
    if var.pyrohallucinogenDecay == 0:
        var.pyrohallucinogenStat = 0
    if var.cyrohallucinogenDecay == 0:
        var.cryohallucinogenStat = 0