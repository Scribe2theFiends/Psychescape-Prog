from formatModule import inbreakline,error
import varModule as var
import roomModule as room

def unityExchange():    
    inbreakline()
    print("The exchange rate of mining scrip to U= is 10 to 1.")
    answer = input("How much U= do you want to exchange scrip for? => ")
    if var.scripCount >= int(answer) * 10:
        inbreakline()
        print(f"You turn in {int(answer) * 10} scrip for {answer} U=.")
        var.scripCount -= int(answer) * 10
        var.unifiedCount += int(answer)
        var.doTurn = False
        room.companyStore()
    else:
        inbreakline()
        print("You walk up to the counter and ask to exchange your scrip only to find out that you don't have enough scrip. As you walk away you hear the woman mumble \"Waste of my time. Could be doing something better.\"")
        var.doTurn = False
        room.companyStore()
    
def shop():
  inbreakline()
  print("You can buy the following;")
  if var.hasMinePermit == False:
      print("\n  Permit to leave: This lets you leave the grounds. Costs 16 U= (permit).")
  print("  You may leave the counter (leave).")
  answer = input("\nEnter command here => ")
  if answer.lower().strip() == "leave":
      inbreakline()
      print("As you walk away from the counter, you hear the woman grumble to herself, \"Waste of time. All anyone ever does is waste my time.\"")
      var.doTurn = False
      room.companyStore()
  elif answer.lower().strip() == "permit" and var.hasMinePermit == False:
      if var.unifiedCount >= 16:
          inbreakline()
          print("\"Here you go, one permit to leave this hole of despair\" she says as she hands you the permit and takes your Unity.")
          var.hasMinePermit = True
          var.unifiedCount -= 16
          var.doTurn = False
          room.companyStore()
      else:
          inbreakline()
          print("\"You don't have enough Unity for that,\" she says and waves you away. \"At least they knew what they wanted\" you hear mumbled as you walk away.")
          var.doTurn = False
          room.companyStore()
  else:
      error()
      room.companyStore()