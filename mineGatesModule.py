from formatModule import breakline,error,inbreakline
import varModule as var
import roomModule as room
import uiModule as ui
import saveModule as save

def firstVisit():
    inbreakline()
    print("As you get even closer, the guard steps forward. \"Sorry, I can't let you through, not unless you have a permit to leave.\"")
    print("\n  You can show your permit to the guard if you have one (show).")
    print("  You can ask about the permit (permit).")
    print("  You can pet Ren'Shaw (pet).")
    answer = input("\nEnter command here => ")
    if answer.lower().strip() == "permit":
        inbreakline()
        print("\"We aren't allowed to let you leave here without a permit. It's the rules on making sure that you don't take off with any mined minerals, which isn't allowed unless you have a permit. Before you could volunteer for a cavity search if you really wanted to leave, but then one guard had to take it too far, and now we aren't allowed to do that even. So now you aren't allowed to leave without a permit. You can buy them at the store to the east of the mine entrance.")
        print("\n  You could bring up the fact that he literally can't kill you. (can'tstopme)")
        print("  You can leave them alone (exit)")
        answer = input("\nEnter command here => ")
        if answer.lower().strip() == "exit":
            var.visitedMineGates = True
            var.doTurn = False
            room.mineGates()
        elif answer.lower().strip() == "can'tstopme":
            inbreakline()
            print("  You sneer and point out to the guard that they can't kill you, so what are they going to do to stop you?")
            print("  The guard lets out a huff, \"No I can't kill you, but Ren'Shaw and I can continuously tear you down from the gates and the walls and through you back in, strip you of any valuables we find on your person, and fine you for both scrip and money. Don't make us do that.\"")
            var.visitedMineGates = True
            var.doTurn = False
            room.mineGates()
        else:
            error()
            var.doTurn = False
            room.mineGates()
    elif answer.lower().strip() == "show":
        inbreakline()
        if var.hasMinePermit == True:
            print("  You flick out your permit and show it to the guard. \"Yep, that's a permit alright. Signed by Garl-Hath'Yern as shoddily as ever. You're free to go through whenever you so please.\"")
            var.visitedMineGates = True
            var.shownMinePermit = True
            var.doTurn = False
            room.mineGates()
        else:
            print("  You don't have a permit to show them.")
            var.doTurn = False
            room.mineGates()
    elif answer.lower().strip() == "pet":
        inbreakline()
        print("  You get close to Ren'Shaw, \"Hello Ren'Shaw, how are you doing today?\" You reach out and let her sniff your knuckles, a tongue flicking out and brushing them. She taps your hand with her nose, letting you know that she's fine with you petting her right now. You rub a hand along the smooth scales on top of her head as she Srsh's. You pull away and say \"Good Girl\" before leaving her alone.")
        var.knowsSrsh = True
        var.doTurn = False
        room.mineGates()
    else:
        error()
        var.doTurn = False
        room.mineGates()

def returnVisitF():
  inbreakline()
  print("As you get even closer, the guard steps forward. \"Sorry, I can't let you through, not unless you have a permit to leave.\"")
  print("\n  You can go north to the mine entrance (north).")
  print("  You can show your permit to the guard if you have one (show).")
  print("  You can ask about the permit (permit).")
  print("  You can pet Ren'Shaw (pet).")
  answer = input("\nEnter command here => ")
  if answer.lower().strip() == "permit":
      inbreakline()
      print("\n  \"We still aren't allowed to let you leave here without a permit. It's the rules on making sure that you don't take off with any mined minerals, which isn't allowed unless you have a permit. Before you could volunteer for a cavity search if you really wanted to leave, but then one guard had to take it too far, and now we aren't allowed to do that even. So now you aren't allowed to leave without a permit. You can buy them at the store to the east of the mine entrance, in case you needed reminding.\"")
      print("\n  You can bring up the fact that he literally can't kill you. (can'tstopme)")
      print("  You can leave them alone. (exit)")
      answer = input("\nEnter command here => ")
      if answer.lower().strip() == "exit":
          var.doTurn = False
          room.mineGates()
      elif answer.lower().strip() == "can'tstopme":
          inbreakline()
          print("\n  You sneer and point out to the guard that they can't kill you, so what are they going to do to stop you?")
          print("  The guard lets out a huff, \"No I can't kill you, but Ren'Shaw and I can continuously tear you down from the gates and the walls and through you back in, strip you of any valuables we find on your person, and fine you for both scrip and money. Don't make us do that.\"")
          var.doTurn = False
          room.mineGates()
      else:
          error()
          var.doTurn = False
          room.mineGates()
  elif answer.lower().strip() == "show" and var.hasMinePermit == True:
          inbreakline()
          print("  You flick out your permit and show it to the guard. \"Yep, that's a permit alright. Signed by Garl-Hath'Yern as shoddily as ever. You're free to go through whenever you so please.\"")
          var.visitedMineGates = True
          var.shownMinePermit = True
          room.mineGates()
  elif answer.lower().strip() == "show" and var.hasMinePermit == False:
      inbreakline()
      print("\n  You don't have a permit to show them.")
      var.doTurn = False
      room.mineGates()
  elif answer.lower().strip() == "pet":
      inbreakline()
      print("  You get close to Ren'Shaw, \"Hello Ren'Shaw, how are you doing today?\" You reach out and let her sniff your knuckles, a tongue flicking out and brushing them. She taps your hand with her nose, letting you know that she's fine with you petting her right now. You rub a hand along the smooth scales on top of her head as she Srsh's. You pull away and say \"Good Girl\" before leaving her alone.")
      var.knowsSrsh = True
      var.doTurn = False
      room.mineGates()
  elif answer.lower().strip() == "north":
      room.mineEntrance()
  elif answer.lower().strip() == "inventory":
      ui.inventory()
      room.mineGates()
  elif answer.lower().strip() == "help":
      ui.help()
      room.mineGates()
  elif answer.lower().strip() == "codex":
      ui.codex()
      room.mineGates()
  elif answer.lower().strip() == "save":
      save.simpleSave()
      room.mineGates()
  elif answer.lower().strip() == "act":
      ui.act()
      room.mineGates()
  elif answer.lower().strip() == "skills":
      ui.skills()
      room.mineGates()
  elif answer.lower().strip() == "stats":
      ui.stats()
      room.mineGates()
  else:
      error()
      var.doTurn = False
      room.mineGates()

def returnVisitT():
  inbreakline()
  print("A guard stands here at the gates with Ren'Shaw the Gzahn'Kath-In, they know t let you through without trouble now that you have shown your permit.")
  print("  You can go south to a crossroads (south).")
  print("  You can go north to the mine entrance (north).")
  print("  You can pet Ren'Shaw (pet).")
  answer = input("\nEnter command here => ")
  if answer.lower().strip() == "pet":
      inbreakline()
      print("  You get close to Ren'Shaw, \"Hello Ren'Shaw, how are you doing today?\" You reach out and let her sniff your knuckles, a tongue flicking out and brushing them. She taps your hand with her nose, letting you know that she's fine with you petting her right now. You rub a hand along the smooth scales on top of her head as she Srsh's. You pull away and say \"Good Girl\" before leaving her alone.")
      var.knowsSrsh = True
      var.doTurn = False
      room.mineGates()
  elif answer.lower().strip() == "south":
      room.crossroads()
  elif answer.lower().strip() == "north":
      room.mineEntrance()
  elif answer.lower().strip() == "inventory":
      ui.inventory()
      room.mineGates()
  elif answer.lower().strip() == "help":
      ui.help()
      room.mineGates()
  elif answer.lower().strip() == "codex":
      ui.codex()
      room.mineGates()
  elif answer.lower().strip() == "save":
      save.simpleSave()
      room.mineGates()
  elif answer.lower().strip() == "act":
      ui.act()
      room.mineGates()
  elif answer.lower().strip() == "stats":
      ui.stats()
      room.mineGates()
  elif answer.lower().strip() == "skills":
      ui.skills()
      room.mineGates()
  else:
      error()
      var.doTurn = False
      room.mineGates()