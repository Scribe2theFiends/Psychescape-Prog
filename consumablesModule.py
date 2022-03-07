from random import randint
import varModule as var

#FOOD

def eatJigglers():
    print("You look around and quickly find a nice area on the ground to kneel on. Unwrapping the cloth, you watch the glob of gelatinous—somthing—jiggle around the center of the cloth on your folded legs. Digging in with your fingers, you peel away the chewier outside and eat it first before eating the less stale, more savory center.")
    var.wellness += 10

def eatDarkTreeSap():
    print("You reach into your pocket and pull out the small container that holds the sugary sap in it. Untying it, you pull apart the two halfs with some resistance, and pull the sticky glob of sap out of the box. It sticks to you hand so well that when you shake it some it doesn't come off, only stretches a bit, sticking your fingers together. Taking bites out of the glob, you feel like you are chewing pitch, every time you pull your jaw apart threatening to yank out your teeth. But it's so deliciously sugary, it tastes even sweeter than blood-honey from a Tusked-Delicacy. Over time, it melts in your mouth, your chewing having not made any impact on it. You suck the remaining sap off your fingers and get ready to move again.")
    var.wellness += 6

def eatBloodboilBerries():
    print("You pull out the berries and carefully unwrap them, the cloth clinging to itself with the hardened wax, a good amount of which has hardened at the bottom. You pluck the now room-temperature berries out of the cloth and pop them into your mouth one by one, the wax squishing, but holding the juices inside it for a while before it all gushes out into your mouth, filling it with sweet juices. As you chew on the sweet waxes for a while, feeling the tiny seeds inside crunch surprisingly every now and then, before you swallow the large glob, feeling it slide all the way down your throat into your stomach.")
    potentialWax = randint(1, 3)
    if potentialWax == 3:
        print("There is enough wax left over in the cloth to warrant keeping, in case you could use it for something else or maybe sell it.")
        var.bloodboilWax += 1
    var.wellness += 10

def eatDarkTreeFruit():
    print("You pull one of the fruits out of your pack, finding it's warmth has long since left it. Taking a quick sniff of the fruit to see if it's still ripe, you find that it still smells the same as when you picked it. You take your first bite, slicing through the fruit with little resistance, finding the skin thin and the flesh smooth. There's very little juice in the fruit but the flesh itself is sugary, as well as easy enough to manipulate you can squish it against the roof of you mouth into paste. You dig at the flesh of the fruit until your finger scrapes against the smooth pit. You push the flesh into your mouth before scooping out the pit and throwing it aside before continuing on with your meal. After you finish you wipe your hands on your clothes and continue on with what you were doing.")
    var.wellness += 16

def eatHwerFshErrFruit():
    print("You pull the fruit of of your pocket, and holding it in your hand you carefully look it over, a teardrop-shaped fruit that holds a great resemblance to a glowing ember, with a charcoal black skin and a shifting glow inside it. You give it a squeeze and find the skin too hard to warp much by squeezing it. taking a bite out of it, the skin crunches and you spit out the hard outer shell, now able to see the inside glowing brighter. You flake off other bits of the shell until you hold the insides in your hand, glowing bright, with some of the glowing juice oozing out of it a bit. You pull out a section of the fruit ans shove it in your mouth. struggling to chew the whole section at first, you soon feel you mouth growing warm, the sweet juices aren't warm themselves, but it somewhow gives you a sensation like your mouth is warm and cosy. Swallowing brings that sensation all the way down your throat until you feel the warmth settle into th epit fo your stomach, and you finish up the rest of the fruit quickly, the sweet, tangy, warm flavor soothing you and calming you down. Once you're done, you find yourself wanting more, but who knows the next time you may find another fruit.")
    var.wellness += 24

def eatFlatbread():
    print("You unwrap the flatbread, the honey on it long since having soaked into the bread, leaving a crunchy reddish stain. You eat the bread, crunchy where there's honey, and chewy where there isn't")
    var.wellness += 8

#DRINK

def drinkMeatStew():
    print("You open the flask and down the now lukewarm stew, full of unknown meat and unknown veggies. Stopping to chew whenever you get something too chunky to swallow. The soup has somehow become even more granular but is still just as savoury.")
    var.wellness += 12
  
#NON-RAHN

def usePyrohallucinogen():
    print("You pull out the pyrohallucinogen, a large mash pill, and pop it into your mouth, chewing and grinding it into a rough paste before swallowing. Shortly afterwards, you begin seeing sparks drift through your vision, certain objects burning to become a glowing ember, and even some things bursting into flame.")
    var.wellness -= 6
    var.pyrohallucinogenStat = 1
    var.pyrohallucinogenDecay = 12

def useCryohallucinogen():
    print("You pull out the cryohallucinogen, a large mash pill, and pop it into your mouth, chewing and grinding it into a rough paste before swallowing. Shortly afterwards, you begin seeing frost gather on the ground and other surfaces, certain object completely glazed over, and even some things being frozen solid.")
    var.wellness -= 6
    var.cryohallucinogenStat = 1
    var.cryohallucinogenDecay = 12