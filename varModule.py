#VAR MODULE

#TIMING
turn = 0

wellness = 100

#CHARACTER

alignment = 0

piercingSkill = 0
piercingEXP = 0
piercingEXPneeded = 64
bluntSkill = 0
bluntEXP = 0
bluntEXPneeded = 64
slashingSkill = 0
slashingEXP = 0
slashingEXPneeded = 64
physicalProficiency = 0

cryoSkill = 0
cryoEXP = 0
cryoEXPneeded = 64
pyroSkill = 0
pyroEXP = 0
pyroEXPneeded = 64

rangedSkill = 0
rangedEXP = 0
rangedEXPneeded = 64
meleeSkill = 0
meleeEXP = 0
meleeEXPneeded = 64
typeProficiency = 0

playerVitals = 0
vitalEXP = 0
vitalEXPneeded = 64
HPbase = 32
HP = HPbase
currentHP = HPbase
alchemySkill = 0
alchemyEXP = 0
alchemyEXPneeded = 64
potencyBase = 16
alchemicalPotency = potencyBase
currentPotency = potencyBase

EXPdiluter = 1

#STATUS EFFECTS

pyrohallucinogenStat = 0
pyrohallucinogenDecay = 0
meadStat = 0
meadDecay = 0
cryohallucinogenStat = 0
cyrohallucinogenDecay = 0

#WEAPONS

currentWeapon = 0
hasSling = False
shot = 0
shotUsed = 0
hasBow = False
arrows = 0
arrowsUsed = 0
chakrams = 0
chakramsThrown = 0
hasMace = False
hasSword = False
daggers = 0

finalAttack = 0
enemyAttack = 0

#CONTAINERS

flasks = 0
flaskContent = []
pouchs = 0
pouchContent = []

#CURRENCY

scripCount = 0
unifiedCount = 0

#TRADE GOODS

ichorCount = 0
largeIchorCount = 0
sculptureGradeIchorCount = 0
coalCount = 0
largeCoalCount = 0
commonArsonSalts = 0
rareArsonSalts = 0
bloodboilWax = 0

#FOOD AND DRINK

jigglers = 0
bloodboilBerries = 0
darkTreeSap = 0
darkTreeFruit = 0
hwerFshErrFruit = 0
flatbread = 0
meatStew = 0

#DRUGS

pyrohallucinogen = 0
cryohallucinogen = 0

#ROOM VARIABLE

currentRoom = 0

#GENERAL STORE

talkList = ["Oh you're new. How're you doing?","just jingle the bell over there!","the man at the counter","It was nice to talk."]

#BOOLEAN VARIABLES

visitedMineGates = False
shownMinePermit = False
hasMinePermit = False

#KNOWLEDGE

knowsGzahnKathIhn = False
knowsAshKrahn = False
knowsBahnAr = False
knowsYeelTsur = False
knowsBorchTrahfl = False
knowsFtNagYen = False
knowsBloodboil =False
knowsDarkTree = False
knowsHwerFshErrTree = False
knowsSrsh = False

#FOUND PLACES

foundGreatTree = False

#CHEAT VARIABLE

hasCheated = False

def autoLevel():
    on = True
    global piercingSkill
    global piercingEXP
    global piercingEXPneeded
    global bluntSkill
    global bluntEXP
    global bluntEXPneeded
    global slashingSkill
    global slashingEXP
    global slashingEXPneeded
    global cryoSkill
    global cryoEXP
    global cryoEXPneeded
    global pyroSkill
    global pyroEXP
    global pyroEXPneeded
    global rangedSkill
    global rangedEXP
    global rangedEXPneeded
    global meleeSkill
    global meleeEXP
    global meleeEXPneeded
    global alchemySkill
    global alchemyEXP
    global alchemyEXPneeded
    global playerVitals
    global vitalEXP
    global vitalEXPneeded
    global HPbase
    global HP
    global potencyBase
    global alchemicalPotency
    global wellness
    while on == True:
        if piercingEXP > piercingEXPneeded:
            piercingSkill += 1
            piercingEXPneeded = round(piercingEXPneeded * 1.5 + 64)
        if bluntEXP > bluntEXPneeded:
            bluntSkill += 1
            bluntEXPneeded = round(bluntEXPneeded * 1.5 + 64)
        if slashingEXP > slashingEXPneeded:
            slashingSkill += 1
            slashingEXPneeded = round(slashingEXPneeded * 1.5 + 64)
        if cryoEXP > cryoEXPneeded:
            cryoSkill += 1
            cryoEXPneeded = round(cryoEXPneeded * 1.5 + 64)
        if pyroEXP > pyroEXPneeded:
            pyroSkill += 1
            pyroEXPneeded = round(pyroEXPneeded * 1.5 + 64)
        if rangedEXP > rangedEXPneeded:
            rangedSkill += 1
            rangedEXPneeded = round(rangedEXPneeded * 1.5 + 64)
        if meleeEXP > meleeEXPneeded:
            meleeSkill += 1
            meleeEXPneeded = round(meleeEXPneeded * 1.5 + 64)
        if alchemyEXP > alchemyEXPneeded:
            alchemySkill += 1
            alchemyEXPneeded = round(alchemyEXPneeded * 1.5 + 64)
        if vitalEXP > vitalEXPneeded:
            playerVitals += 1
            vitalEXPneeded = round(vitalEXPneeded * 1.5 + 64)
        if wellness > 100:
            wellness = 100
        if wellness < 0:
            wellness = 0
        HP = HPbase + playerVitals * 8
        alchemicalPotency = potencyBase + alchemySkill * 8
#DOESN'T NEED TO BE SAVED
    #WATER DRUNK

waterDrunk = 0

    #BLOODBOIL ENCOUNTER

bloodboilBerriesLeft = False
waxLeft = False

    #DARK TREE SAP ENCOUNTER

sapLeft = False

    #DARK TREE FRUIT ENCOUNTER

darkTreeFruitAmount = 0

    #HWER FSH ERR FRUIT ENCOUNTER

hwerFshErrFruitLeft = 0

    #GAMBLING

fiendishGambleOutcome = "Null"
    
    #LASTERROR

doTurn = True

    #FLARED

flared = 0

    #RIMED

rimed = 0

    #MEND COOLDOWN

mendCooldown = 0