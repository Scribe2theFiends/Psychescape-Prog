from formatModule import inbreakline,error
import roomModule as room
import varModule as var
import random

def wanderForest():
    exploreAward = random.randint(1,64)
    if 0 < exploreAward <= 20:
        print("You wander through the dark forest, the warm, dry air feeling wonderful on your skin. The small amount of light making its way through the pitch black leaves of the surrounding trees creates the illusion of the stars beaming down their light to the ground below. The time alone in the forest gives you time to think and contemplate yourself. Think of a few things you might change about yourself some day.")
        room.darkForest()
    elif 20 < exploreAward <= 30:
        print("As you wander along through the dark wood, you find a large pool of water. Not large enough to be a pond, it is large enough to keep the trees from growing in that area, leading to a much cooler environment that lets you see that it is in fact light outside of the forest. You take while to cool off before heading back into the hot, dry forest. Maybe some day you'll find your way back here, and you could see some animals, or take a nice fishing trip.")
        room.darkForest()
    elif 30 < exploreAward <= 40:
        randomAnimal = random.randint(1,16)
        if 0 < randomAnimal <= 5:
            print("You take a walk through the forest, and all is nice and peaceful for a while. That all changes when you hear the sound of something large barrelling through the underbrush in your direction. Images flash in your mind of what it might be, you can see the horn that was perfectly made to gore their prey, you can see the sinuous form of something bearing large, jagged teeth that could tear you to shreds in your mind. You start to turn too late, you can already see leaves and branches flying through the air and you freeze. The predator is obscured by the great mess it makes until it gets close, and swerves around you, doging you entirely. As it passes you can see that it is nothing more than a small animal, something long and furry, with strange appendages that throw up the terrain around it to make it seem much scarrier than it is. You recognise the Ash-Krahn, and realise that it posed no threat, nor would it to anything but critters that would fit into tha palm of your hand. Chuckling to yourself, you walk back to the edge of the forest.")
            var.knowsAshKrahn = True
            room.darkForest()
        elif 5 < randomAnimal <= 10:
            print("You take a walk through the forest, and all is nice and peaceful for a while. That all changes when you hear the sound of something large barrelling through the underbrush in your direction. Images flash in your mind of what it might be, you can see the horn that was perfectly made to gore their prey, you can see the sinuous form of something bearing large, jagged teeth that could tear you to shreds in your mind. You start to turn too late, you can already see the form coming now. A dark, canine form, large white teeth protruding from the bottom jaw over its lips. Ears that swivel to the side as it rushes you, listening for ambushes. You turn tail and flee, running as fast as you can trying to escape the Bahn-Ar, you can't fight this thing with your bare hands, not yet. You hear the thing tearing through the leaves behind you and push harder, your muscles straining, and keep going until you can't hear it anymore. You sit down under a tree, taking unsteady, heaving breaths, until you're rested enough to continue, and then you walk back towards the crossroads.")
            var.knowsBahnAr
            room.darkForest()
        elif 10 < randomAnimal <= 13:
            print("You take a walk through the forest, looking for anything that may be of interest, or maybe just enjoying the scenery. Either way, the walk is uneventful for a while, until you here the piercing \"HRAAAA\" of a Yeel'Tsur, creeping through the woods, you move close to the sound, listening for digging sounds. After some quiet slinking around, you come hear it, somethign digging through the underbrush, and you move toward the sound. You get close enough to see a hunched, bipedal form, digging with its forelimbs through the dirt and leaves, looking for something. It looks around briefly before leaning its face into the hole and sniffing. After a bit of snuffling it leans back up and digs some more, soon pulling out a root and gnawing on it. After eating its meal it goes back down on all fours and gallops away, screaming another \"HRAAAA,\" looking for another to share a meal with. Watching it run away reminds you that you have things to do, and shouldn't spend all day in the dark forest.")
            var.knowsYeelTsur = True
            room.darkForest()
        elif 13 < randomAnimal <= 16:
            print("Wandering through the hot woods, you look find yourself looking up at the trees. Their dark leaves shift around such as if night was a fog, and are quite beautiful in their rippling movements. You're startling from your observations by the sound of rustling leaves. A quick look towards the sound reveals a small herd of portly Borch'Trahfl moving along slowly. If you had something to hunt them with, it could help make you some money if you were to kill one or two. After you watch them waddle away, you wander a bit longer before turning around and heading back to where you started.")
            var.knowsBorchTrahfl
            room.darkForest()
    elif 40 < exploreAward <= 46:
        var.bloodboilBerriesLeft = True
        var.waxLeft = True
        foundBloodboil()
    elif 46 < exploreAward <= 52:
        var.sapLeft = True
        foundSap()
    elif 52 < exploreAward <= 57:
        witness = random.randint(1,4)
        if witness == 1:
            print("You wander through the forest for a while through the forest, enjoying the warm, dim environment. After a time you enjoyment is interrupted by a stench like great volume of rancid puss. The stench could only mean one thing, there's a pool of ichor nearby. You follow the stench all the way to the source, a large swampy area full of the thick, slimy ichor. You cautiously poke the yellowish fluid and look at the debris floating around in there. You walk around in the swampy area for a while, but it's not long before you hear the sound of something being dragged across the ground. Looking to the noise you find yourself staring directly at a Ft'Nag-Yen, a large, centipede-like creature dragging the mangled carcass of something indestinguishable with it's front appendages. Not wanting to have to fight one of these beasts bare-handed, you carefully creep away so as not to be seen, and then running back out of the forest when you think you are far enough away to make noise. You're going to need a weapon of some sort in order to stand a chance against one of those.")
            var.knowsFtNagYen = True
            room.darkForest()
        else:
            print("You wander through the forest for a while through the forest, enjoying the warm, dim environment. After a time you enjoyment is interrupted by a stench like great volume of rancid puss. The stench could only mean one thing, there's a pool of ichor nearby. You follow the stench all the way to the source, a large swampy area full of the thick, slimy ichor. You cautiously poke the yellowish fluid and look at the debris floating around in there. You wander about for a bit, listening to the weird schlucks and pops of the ichor swamp, very little sunlight ever reaching the ground here. After a time you get a little unnerved, fearing that there may be a Ft'Nag-Yen slithering around through the swamps somewhere, and hurriedly leave the area and return the where you came from.")
            room.darkForest()
    elif 57 < exploreAward <= 60:
        var.darkTreeFruitAmount = random.randint(2,6)
        foundDarkTreeFruit()
    elif 60 < exploreAward <= 63:
        print("As you wander along through the woods, you soon come to a wide open area. The canopy still covers the entirety of the sky, but there are few trees around the area, instead, an old, massive tree  stands in the center, blocking out the light for all of the other trees, and none have been able to spring up because of the massive giant. Walking up to it, you find that the tree is much too large to even wrap your arms around, and closer inspection reveals that there is even a crack in the side, allowing you to walk into the very trunk of the tree if you crouch a little. Once inside the relatively small space, you look around in the light, realising that the hole goes all the way up throught the top of the tree, lighting up the space. Maybe sometime later, you could find a way to get up there and look around.")
        var.foundGreatTree = True
        room.darkForest()
    elif exploreAward == 64:
        var.hwerFshErrFruitLeft = random.randint(1,2)
        var.knowsHwerFshErr = True
        foundHwerFruit()

def foundSap():
    print("Going for a stroll through the woods, you eventually come across a tree with a great gash in its bark, and a large clump of black, semi-translucent sap, that you know is almost all sugar.")
    var.knowsDarkTree = True
    print("")
    if var.sapLeft == True:
        print("  You may (eat) the sap.")
        print("  You may (take) the sap.")
    print("  You may (leave) the sap alone.")
    answer = input("\nEnter command here => ")    
    inbreakline()
    if answer.lower().strip() == "eat" and var.sapLeft == True:
        print("You grap a hold of the clump of sap that has been leaking out of the gash, wrapping your fingers around it to get a good grip, then you give it a good yank, only for it to stretch slightly and you to loose you grip, stumbling back a little. Afterwards you take a more calculated approach, grabbing the nodule and pulling slowly, letting it stretch away from the tree until you can jsut break the little bit holding it on. Instead of bothering to try to break it into pieces, you put the whole glob in your mouth and try to chew it immediately almost imobilizing your jaw. Only after some struggle are you able to pull your jaw apart again, but the amazingly sweet taste of it entertains your tongue in the mean time. After a sort bit of trying to work the sap, you can finally begin to chew in a somewhat normal manner, but you know you aren't breaking it up. The sap slowly melts in your mouth, the chewing only being something to keep you move busy until all of the sap has melted. Afterwards, you quickly suck at the little bit of sap left on your fingers before continuing on with your day.")
        var.sapLeft = False
        var.wellness += 6
        inbreakline()
        foundSap()
    elif answer.lower().strip() == "take" and var.sapLeft == True:
        print("You take out a little wooden carrying case and start to carefully push the sticky sap into it, being careful and slow about it, then closing the lid and squishing it down before pulling it away, sap pulling in a ever thinner strand until it snaps, and you tie the containre shut.")
        var.sapLeft = False
        inbreakline()
        foundSap()
    elif answer.lower().strip() == "leave":
        print("You decide to leave the tree alone, turning around and walking back to where you started.")
        room.darkForest()
    else:
        error()
        foundSap()

def foundBloodboil():
    print("You take a stroll through the forest to see if you can find anything, and eventually you do. As you meander through the woods, you come across a splash of bland color in the mostly monochrome wood, a rusty-brown colored bush with deep red colors on it in places. As you move closer you notice the deep red clumps are dripping their colors onto the ground, and a quick touch of the liquid finds it to be a warm, melted wax. A bloodboil plant you realise, the wax is useful and the berries are sweet, do you want to do anything with this plant?")
    var.knowsBloodboil = True
    print("")
    if var.bloodboilBerriesLeft == True:
        print("  You may (eat) the berries.")
        print("  You may take the berries (tberries).")
    if var.waxLeft == True:
        print("  You may take the wax (twax).")
    print("  You may leave the bush alone (leave).")
    answer = input("\nEnter command => ")
    inbreakline()
    if answer.lower().strip() == "eat" and var.bloodboilBerriesLeft == True:
        print("You pick yourself a bunch of berries and plop yourself down on the ground to enjoy them. The berries are warm in your hands, as warm as a living animal would be, and the wax slowly runs all over your hand as you hold them, so you begin to pop them into your mouth. The warm berries just taste like wax until you chew them, bursting the warm juice into your mouth, the hard seeds inside crunching on your teeth. You pop more berries in your mouth without swallowing, putting the whole handfull in your mouth. As you chew the sweet juices and the wax mix together into a sweet chewy glob, holding in the sweetness and flavor until you swallow the large chunk of wax, feeling it slide its way all down your throat, and into your stomach. You get up and rub the wax off of your hands, watching it pill up and fall away.")
        var.wellness += 10
        var.bloodboilBerriesLeft = False
        inbreakline()
        foundBloodboil()
    elif answer.lower().strip() == "tberries" and var.bloodboilBerriesLeft == True:
        print("You carefully pick the majority of the berries on the bush, place them into a carrying cloth, and wrap them up for later use, rubbing the wax off of your hands with the cloth before stowing them away.")
        var.bloodboilBerriesLeft = False
        var.bloodboilBerries += 1
        inbreakline()
        foundBloodboil()
    elif answer.lower().strip() == "twax" and var.waxLeft == True:
        print("You crouch to the ground, looking at the clumps of wax that form under the bush from the berries dripping their blood-red wax onto the ground. You pick up the clumps and take the big chunks of debris out of the wax, before tossing the clumps into a carrying case and tying it tightly shut.")
        var.waxLeft = False
        var.bloodboilWax += 1
        inbreakline()
        foundBloodboil()
    elif answer.lower().strip() == "leave":
        print("You decide to leave the bush alone and walk back to where you began.")
        room.darkForest()
    else:
        error()
        foundBloodboil()

def foundDarkTreeFruit():
    print("After some time of wandering through the forest, you happen upon one of the trees that happens to be bearing fruit. There are several ripe, deep-red fruits hanging from the tree. They all have a with a deep suture in them, making them somewhat reminiscent of a peach. There are several fruits that you can see within reach.")
    var.knowDarkTree = True
    print("")
    if var.darkTreeFruitAmount > 0:
        print("  You may (eat) a fruit.")
    if var.darkTreeFruitAmount > 0:
        print("  You may (take) a fruit.")
    print("  You may (leave) the tree alone")
    answer = input("\nEnter command here => ")
    inbreakline()
    if answer.lower().strip() == "eat" and var.darkTreeFruitAmount > 0:
        var.darkTreeFruitAmount -= 1
        print("You reach up and grab a hold of one of the fruits, finding it warm to the touch, and surprising smooth and supple. Snapping the stem without bruising the fruit. Taking a quick sniff of the fruit to see if it's actually ripe, you find that it smells sweet. You take your first bite, slicing through the fruit with little resistance, finding the skin thin and the flesh smooth. There's very little juice in the fruit but the flesh itself is warm and sugary, as well as easy enough to manipulate you can squish it against the roof of you mouth into paste. You dig at the flesh of the fruit until your finger scrapes against the smooth pit. You push the flesh into your mouth before scooping out the pit and throwing it aside before continuing on with your meal. After you finish you wipe your hands on your clothes and continue on with what you were doing.")
        inbreakline
        var.wellness += 16
        foundDarkTreeFruit()
    elif answer.lower().strip() == "take" and var.darkTreeFruitAmount > 0:
        var.darkTreeFruitAmount -= 1
        print("You reach up and grab a hold of one of the fruits, finding it warm to the touch, and surprising smooth and supple. Snapping the stem without bruising the fruit. You carefully wrap up the fruit in a cloth and stow it away.")
        var.darkTreeFruit += 1
        inbreakline()
        foundDarkTreeFruit()
    elif answer.lower().strip() == "leave":
        print("You decide to leave the tree alone and walk back to wher you came from.")
        room.darkForest()
    else:
      error()
      foundDarkTreeFruit()

def foundHwerFruit():
    print("On your walk through the woods, you come across a faint orange light glowing in the distance. Cautiously making your way up to it, you find a tree with a couple of fruits on it, some with a lsight orange glow. You happen to have found a rare tree, the Hwer'Fsh'Err, a somewhat sickly looking tree that grows fruits shaped like a teardrop that glow orange when ripe. There's some fruit you might be able to reach and might be ripe if you want.")
    print("")
    if var.hwerFshErrFruitLeft > 0:
        print("  You may (eat) a fruit.")
    if var.hwerFshErrFruitLeft > 0:
        print("  You may (take) a fruit.")
    print("  You may (leave)")
    answer = input("\nEnter command here => ")
    inbreakline()
    if answer.lower().strip() == "eat" and var.hwerFshErrFruitLeft > 0:
        var.hwerFshErrFruitLeft -= 1
        print("Looking at the fruits, you find one that is within reach, and quickly snap it off of the branch. Holding it in your hand you carefully look it over, a teardrop-shaped fruit that holds a great resemblance to a glowing ember, with a charcoal black skin and a shifting glow inside it. You give it a squeeze and find the skin too hard to warp much by squeezing it. taking a bite out of it, the skin crunches and you spit out the hard outer shell, now able to see the inside glowing brighter. You flake off other bits of the shell until you hold the insides in your hand, glowing bright, with some of the glowing juice oozing out of it a bit. You pull out a section of the fruit ans shove it in your mouth. struggling to chew the whole section at first, you soon feel you mouth growing warm, the sweet juices aren't warm themselves, but it somewhow gives you a sensation like your mouth is warm and cosy. Swallowing brings that sensation all the way down your throat until you feel the warmth settle into th epit fo your stomach, and you finish up the rest of the fruit quickly, the sweet, tangy, warm flavor soothing you and calming you down. Once you're done, you find yourself wanting more, but who knows the next time you may find another fruit.")
        inbreakline()
        var.wellness += 24
        foundHwerFruit()
    elif answer.lower().strip() == "take" and var.hwerFshErrFruitLeft > 0:
        var.hwerFshErrFruitLeft -= 1
        print("Looking at the fruits, you find one that is within reach, and quickly snap it off of the branch. Holding it in your hand you carefully look it over, a teardrop-shaped fruit that holds a great resemblance to a glowing ember, with a charcoal black skin and a shifting glow inside it. You give it a squeeze and find the skin too hard to warp much by squeezing it. You just toss it in your pocket for later, though you are tempted to eat it right now.")
        var.hwerFshErrFruit += 1
        inbreakline()
        foundHwerFruit()
    elif answer.lower().strip() == "leave":
        print("You go to leave the tree, but first, out of respect, you give it a little nod of the head, having known you've encountered something quite rare and special.")
        room.darkForest()
    else:
        error()
        foundHwerFruit()