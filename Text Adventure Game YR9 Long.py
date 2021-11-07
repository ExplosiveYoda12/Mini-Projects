#YEAR 9 PROJECT: thus some may be inefficient & incomplete

import time
# The time module allows me to add gaps and pauses while running the code by using 'time.sleep(1)'
import random
# The random module allows me to add random number generators throughout the code 'random.randint('parameters')
import sys
#Used for slow type

#The whole game is not finished!

strength = 0
# Strength is a skill that increases damage in fights
intelligence = 0
# Intelligence will allow you to enter certain areas
stamina = 0
# Stamina is the energy levels of the player, certain tasks need a higher stamina to carry out.
skill_points = 5
# Skill Points allow the player to level their skills up
score = 0
# The score is they players tracker of how well they are doing, it adds up over time with certain tasks and collection of some items. The score allows the attempts to be compared as it will print at the end of the game / go.
player_health = 100
# The player ealth is the key factor and used heavily in boss fights, if they lose then they will die or fail the battle and so it must be used carefully. There will be ways to replenish it in the final game.
keep_inventory = False

#need adding into game
'''fire_sword
water_dagger
air_spear
earth_stick
staff_of_the_seven_warlocks'''

inventory = ['water_dagger']
# The inventory will be a place for the player to place there items that they have found and use them later on in the game. There will be a cap on the item limits.

#add health pick ups

# use tp("text") to slow type
def tp(text = 'invalid', t = 0.04):
  for x in text: 
    sys.stdout.write(x) #types letters
    sys.stdout.flush()
    time.sleep(t) #pausing for given time
      
'''_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________'''

def fight_or_flight(enemy,tier): #e.g.  fight_or_flight("nameofenemy,tiernumber")
  global willyoufight
  print("\nYou have encountered the",enemy,"!")
  willyoufight = input("Do you want to \'Fight\' for points or \'Flee\' to another day!\n")
  willyoufight = willyoufight.upper().strip() #.strip gets rid of all spaces
  if willyoufight == "FIGHT": #this decides what battle to fight depending on tier
    if tier == 1:
      Tier_1_Fight(enemy)
    elif tier == 2:
      Tier_2_Fight(enemy)
    elif tier == 3:
      Tier_1_Fight(enemy)
    elif tier == "boss":
      Boss_Fight(enemy)
    else:
      pass
  elif willyoufight == "FLEE":
    print("You ran away! Better luck next time! Your score is",score,"!\n")
    pass
  else:
    print("Invalid input...")
    fight_or_flight(enemy,tier)
    print("-------------------------------------------------------------")

def Tier_1_Fight(enemy):#This allows the enmey name to go in the parenthesis
  global name #usable in all functions with the variable globaled in the top of function
  global score
  global player_health 
  enemy1_health = 50 #Gives the player an advantage as double health of the enemy
  print("------------------------------------------")
  print("Welcome to the fight", name,"vs",enemy,"\n")
  while player_health > 0 and enemy1_health > 0:
    #if the player and enemy are alive then the loop plays
    player_strike = random.randint(0,25) #rigged odds 250% higher chance that the player win will
    enemy1_strike = random.randint(0,10) 
    if 'fire_sword' in inventory: #if the weapon fire_sword is in inventory then it will add a bonus to the player strike
      player_strike = player_strike + 4 #bonus means that the player has a better chance
      print("You used the Fire Sword for added bonus 4 damage!")
      pass #continues in the code
    if 'air_spear' in inventory:
      player_strike = player_strike + 4
      print("You used the Air Spear for added bonus 4 damage!")
      pass
    if 'earth_stick' in inventory:
      player_strike = player_strike + 4
      print("You used the Earth Stick for added bonus 4 damage!")
      pass
    if 'water_dagger' in inventory:
        player_strike = player_strike + 4
        print("You used the Water Dagger for added 4 bonus damage!")
        pass
    if 'staff_of_the_seven_warlocks' in inventory:
        player_strike = player_strike + 16 #better weapon
        print("You used the Staff of the Seven Warlocks for added 16 bonus damage!")
        pass
    if 'knife' in inventory:
        player_strike = player_strike + 2
        print("You used the knife for added 2 bonus damage!")
        pass
    if player_strike > enemy1_strike: #if players randomized number is higher than the enmy then this plays
      print("You just inflicted", player_strike, "on the ",enemy,"!")
      enemy1_health -= player_strike #the enemy is losing the health that way randomized so the game is winnable
      print("The",enemy,"now has",enemy1_health,"health left!\n")
      time.sleep(2) #creates a pause so you are not overwhelmed with all the stats at once
    else: #if the players randomized number is not greater than the enimies then it plays
      print("You have been injured", enemy1_strike, "points by the",enemy,"!")
      player_health -= enemy1_strike #player loses the amount of health that is inflicted
      print("You now have",player_health,"health left!\n")
      time.sleep(2)
  if player_health <= 0: #if the players health is greater than or equal to 0 then the game ends
    print("You have been hit by a critical shot")
    Game_End #runs the game end function
  else:
    print("You defeated the",enemy,"! Well done\n")
    score = score + 10 #adds a reward to score
    print("You have a score of",score,"!\n")
  print("-------------------------------------------------------------")

def Tier_2_Fight(enemy): #having enemy in brackets means that when fight is typed then name can be specified there and so does not have                           the same name each time, adds some customization
  global name
  global player_health #the players health is carried through the whole game then the player is left with health that health unless it is replenished with a health pick up in the game
  global score
  enemy1_health = 60 #enemy has 60 health
  print("------------------------------------------") #REST OF CODE SAME AS PREVIOUS FUNCTIONS
  print("Welcome to the fight", name,"vs ",enemy,"\n")
  while player_health > 0 and enemy1_health > 0:
    player_strike = random.randint(0,20)
    enemy1_strike = random.randint(0,12)
    if 'fire_sword' in inventory: #if the weapon fire_sword is in inventory then it will add a bonus to the player strike
      player_strike = player_strike + 8 #bonus means that the player has a better chance
      print("You used the Fire Sword for added bonus 8 damage!")
      pass #continues in the code
    if 'air_spear' in inventory:
      player_strike = player_strike + 8
      print("You used the Air Spear for added bonus 8 damage!")
      pass
    if 'earth_stick' in inventory:
      player_strike = player_strike + 8
      print("You used the Earth Stick for added bonus 8 damage!")
      pass
    if 'water_dagger' in inventory:
        player_strike = player_strike + 8
        print("You used the Water Dagger for added 8 bonus damage!")
        pass
    if 'staff_of_the_seven_warlocks' in inventory:
        player_strike = player_strike + 16 #better weapon
        print("You used the Staff of the Seven Warlocks for added 16 bonus damage!")
        pass
    if 'knife' in inventory:
        player_strike = player_strike + 2
        print("You used the knife for added 2 bonus damage!")
        pass
    if player_strike > enemy1_strike:
      print("You just inflicted", player_strike, "on the",enemy,"!")
      enemy1_health -= player_strike
      print("The",enemy,"now has",enemy1_health,"health left!\n")
      time.sleep(2)
    else:
      print("You have been injured", enemy1_strike, "points by the",enemy,"!")
      player_health -= enemy1_strike
      print("You now have",player_health,"health left!\n")
      time.sleep(2)
  if player_health <= 0:
    print("You have been hit by a critical shot")
    Game_End
  else:
    print("You defeated the",enemy,"! Well done\n")
    score = score + 20
    print("You have a score of",score,"!\n")
  print("-------------------------------------------------------------")

def Tier_3_Fight(enemy):
  global player_health , name
  global score
  enemy1_health = 70 #enemy has 70 health
  print("------------------------------------------") #COMMENTING SAME AS TWO FUNCTIONS PREVIOUS
  print("Welcome to the fight", name,"vs",enemy,"\n")
  while player_health > 0 and enemy1_health > 0:
    player_strike = random.randint(0,20)
    enemy1_strike = random.randint(0,15)
    if 'fire_sword' in inventory: #if the weapon fire_sword is in inventory then it will add a bonus to the player strike
      player_strike = player_strike + 8 #bonus means that the player has a better chance
      print("You used the Fire Sword for added bonus 8 damage!")
      pass #continues in the code
    if 'air_spear' in inventory:
      player_strike = player_strike + 8
      print("You used the Air Spear for added bonus 8 damage!")
      pass
    if 'earth_stick' in inventory:
      player_strike = player_strike + 8
      print("You used the Earth Stick for added bonus 8 damage!")
      pass
    if 'water_dagger' in inventory:
        player_strike = player_strike + 8
        print("You used the Water Dagger for added 8 bonus damage!")
        pass
    if 'knife' in inventory:
        player_strike = player_strike + 2
        print("You used the knife for added 2 bonus damage!")
        pass
    if 'staff_of_the_seven_warlocks' in inventory:
        player_strike = player_strike + 16 #better weapon
        print("You used the Staff of the Seven Warlocks for added 16 bonus damage!")
        pass
    if player_strike > enemy1_strike:
      print("You just inflicted", player_strike, "on the",enemy,"!")
      enemy1_health -= player_strike
      print("The",enemy,"now has",enemy1_health,"health left!\n")
      time.sleep(2)
    else:
      print("You have been injured", enemy1_strike, "points by the",enemy,"!")
      player_health -= enemy1_strike
      print("You now have",player_health,"health left!\n")
      time.sleep(2)
  if player_health <= 0:
    print("You have been hit by a critical shot")
    Game_End
  else:
    print("You defeated the",enemy,"! Well done\n")
    print("You have a score of",score,"!\n")
    print("-------------------------------------------------------------")

def Boss_Fight(enemy):
  global name , player_health , score
  enemy1_health = 200 #Extra health
  print("------------------------------------------")
  print("Welcome to the Supreme fight;", name,"vs The",enemy,"!!!\n")
  while player_health > 0 and enemy1_health > 0:
    player_strike = random.randint(0,20)
    enemy1_strike = random.randint(0,50) #Stacked against player
    if 'fire_sword' in inventory: #if the weapon fire_sword is in inventory then it will add a bonus to the player strike
      player_strike += 8 #bonus means that the player has a better chance
      print("You used the Fire Sword for added bonus 8 damage!")
      pass #continues in the code
    if 'air_spear' in inventory:
      player_strike += 8
      print("You used the Air Spear for added bonus 8 damage!")
      pass
    if 'earth_stick' in inventory:
      player_strike += 8
      print("You used the Earth Stick for added bonus 8 damage!")
      pass              #NEED TO GET THE W£EAPONS TO RECOGNISE
    if 'water_dagger' in inventory:
      player_strike += 8
      print("You used the Water Dagger for added 8 bonus damage!")
      pass
    if 'staff_of_the_seven_warlocks' in inventory:
      player_strike += 16 #better weapon
      print("You used the Staff of the Seven Warlocks for added 16 bonus damage!")
      pass
    if 'knife' in inventory:
        player_strike = player_strike + 2
        print("You used the knife for added 2 bonus damage!")
        pass
    if player_strike > enemy1_strike:
      print("You just inflicted", player_strike, "on the",enemy,"!")
      enemy1_health -= player_strike
      print("The",enemy,"now has",enemy1_health,"health left!\n")
      time.sleep(2)
    else:
      print("You have been injured", enemy1_strike, "points by the",enemy,"!")
      player_health -= enemy1_strike
      print("You now have",player_health,"health left!\n")
      time.sleep(2)
  if player_health <= 0:
    print("You have been hit by a critical shot\nThe",enemy,"has",enemy1_health,"health left!")
    Game_End
  else:
    print("You defeated the",enemy,"! Well done\n")
    score = score + 50
    print("You have a score of",score,"!\n")

'''_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________'''

def Start():
  global name
  #Asking for permission to start
  print("PYTHON TEXT ADVENTURE // ZAK ANDREWS // VERSION : ALPHA // VILLAGE STRAND INCOMPLETE // FOREST INCOMPLETE ")
  print("___________________________________________________________________________________________________________")
  startbutton = input("Type START to play: ")
  startbutton = startbutton.upper().strip()
  if startbutton == "START":
    gamemode()
  else: 
    #If invalid answer; repeat
    print('Invalid input')
    Start()

def gamemode():
  global skill_points, player_health
  print("\nChoose a Gamemode, \'Easy\', \'Normal\', \'Hard\' ") 
  gm = input("Gamemode >>> ")
  if gm.upper().strip() == "EASY":
    print("\nYou chose Easy,\nYou have extra Health and extra Skill points")
    skill_points += 3
    player_health += 30
    keep_inventory1()
  if gm.upper().strip() == "NORMAL":
    print("\nYou chose Normal,\nYou have normal Health and standard Skills")
    keep_inventory1()
  if gm.upper().strip() == "HARD":
    print("\nYou chose Hard,\nYou have less Health and less Skills")
    skill_points -= 2
    player_health -= 2
    keep_inventory1()
  else:
    print("Invalid Input...")
    gamemode()

def keep_inventory1():   
  global keep_inventory
  keep_inventory_choice = input("\nDo you want to keep inventory? (Y/N)")
  if keep_inventory_choice.upper().strip() == "Y" or keep_inventory_choice.upper().strip() == "YES":
    print("You have Keep Inventory on! If you die you lose points but keep the Stuff!")
    keep_inventory = True
    character_configuration()
  if keep_inventory_choice.upper().strip() == "N" or keep_inventory_choice.upper().strip() == "NO":
    print("You have Keep Inventory off! If you die you lose points and lose the Stuff!")
    keep_inventory = False
    character_configuration()
  else:
    print("Invalid Input...")
    keep_inventory1()
  
def character_configuration():            
  global name, strength, intelligence, stamina, skill_points
  name = str(input("\nUsername >>> "))
  print("\nWhat Skill would you like to improve?\n1 - Strength\n2 - Intelligence\n3 - Stamina\nYou have",skill_points,"Skill Points in Total.\n")
  while skill_points > 0:
    skill_choice = input("\nPlease enter a number to increase the Skill! ")
    print("You will be asked to choose multiple skill points;")
    if skill_choice != "":
      skill_choice = skill_choice[0]
    if skill_choice == "1":
      strength += 1
      print("Strength increased to",strength)
    elif skill_choice == "2":
      intelligence += 1
      print("Intelligence increased to",intelligence)
    elif skill_choice == "3":
      stamina += 1
      print("Stamina increased to",stamina)
    else:
      print("Invalid Input...")
      continue
    skill_points -= 1
  print("\nYour stats",name,"are as follows:\nStrength =",strength,"\nIntelligence =",intelligence,"\nStamina =",stamina)
  Introduction()

def Introduction():
  global name
  tp("\nFive weeks ago you found a mysterious map which told of an ancient treasure.\nYou journey far and wide to find the entrance, now you have found it.\nThe map says the treasure is near but now YOU must find it.\nUse your skills to pick up things and find where they are needed.\nAdventure awaits, good luck!\n ")
  time.sleep(2)
  choice1()
  
def choice1 ():  
  print("\n\nWhere would you like to start? Abandoned Village or Field")
  locationchoice = input("So, Village or Field\n")
  # converting to upper to reduce errors in case sensitivity
  locationchoice = locationchoice.upper().strip()
  if locationchoice == "VILLAGE": #not done
    villagescene() 
  elif locationchoice == "FIELD":
    fieldscene()
  else:
    print("Invalid Answer, please try again!")
    choice1()
  
def Game_End():
  global score, keep_inventory
  if keep_inventory == True:
    print("Oh no, You have been critically injured!\nYou got a score of",score,"\nYou have keep inventory so you don\'t lose anything!\n")
    score = 0
    choice1()
  else:
    print("Oh no, You have been critically injured!\nYou got a score of",score,"\nYour score will reset and Your inventory will empty!\n")
    score = 0
    inventory.clear()
    choice1()

def Game_won():
  global score
  print("YOU WIN!!! WITH A SCORE OF",score)
  quit
  
'''_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________'''

def villagescene ():
  print("-------------------------------------------------------------")
  print("\nThe Abandoned Village!\n")
  print("You look around and see a house to the north and a road to the west")
  villagechoice()
#put up here as wont fit inside

def bolderchoice ():
  global stamina , score
  choice = input("There is a bolder on the floor. Do you want to pick it up (Y/N) it will cost 10 stamina")
  choice = choice.upper().strip() 
  if choice == "Y":
    stamina = stamina - 10
    score = score + 10
    print("\nYou now have",stamina ," stamina left, if it runs out you cant move things!")
    print("Score =", score)
    print("You moved the rock, there is a sharp fragment of rock underneath!\nTo collect type \'pick up\'.")
    QQQ = input()
    
    if QQQ.upper.strip() == "pick up":
      print ("You picked up the rock")
      inventory.append("Rock_Fragment")
      
  elif choice == "N":
    pass
  else:
    bolderchoice()
  print("You encounter a Wolf!\nThis is a Tier 3 fight!")
  Tier_3_Fight("Wolf")



def villagechoice ():
  villagechoiceone = input()
  #asking for a direction
  if villagechoiceone.upper().strip() == "NORTH" :
    print("You enter the house")
    #house scene commences
    house()
  elif villagechoiceone.upper().strip() == "WEST" :
    print("You keep walking")
    bolderchoice()
  else:
    print("Invalid answer")
    #If invalid the choice plays again
    villagechoice()       

def house():
  pass 
  
'''______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________'''

def mineshaftscene ():
  global enemy, player_health
  print("-------------------------------------------------------------")
  print("\nThe Mineshaft Passgage!\n")
  print("You head towards the opening but a creature jumps out from a creavass!!\n")
  print("You encounter a Mutant Salamander!")
  print("This is a Tier 3 Fight!\nVery Hard...!")
  print("Player Health =",player_health,"\n")
  willyoufight = input("Do you want to \'Fight\' for points or \'Flee\' to another day!\nYou must beat the enemy to pass!")
  willyoufight = willyoufight.upper().strip()
  if willyoufight == "FIGHT":
    enemy1_health = 70 #enemy has 70 health
    print("------------------------------------------") 
    print("Welcome to the fight", name,"vs Mutant Salamander\n")
    while player_health > 0 and enemy1_health > 0:
      player_strike = random.randint(0,10)
      enemy1_strike = random.randint(0,25)
      if 'fire_sword' in inventory: #if the weapon fire_sword is in inventory then it will add a bonus to the player strike
        player_strike = player_strike + 8 #bonus means that the player has a better chance
        print("You used the Fire Sword for added bonus 8 damage!")
        pass #continues in the code
      if 'air_spear' in inventory:
        player_strike = player_strike + 8
        print("You used the Air Spear for added bonus 8 damage!")
        pass
      if 'earth_stick' in inventory:
        player_strike = player_strike + 8
        print("You used the Earth Stick for added bonus 8 damage!")
        pass
      if 'water_dagger' in inventory:
        player_strike = player_strike + 8
        print("You used the Water Dagger for added 8 bonus damage!")
        pass
      if 'knife' in inventory:
        player_strike = player_strike + 2
        print("You used the knife for added 4 bonus damage!")
        pass
      if 'staff_of_the_seven_warlocks' in inventory:
        player_strike = player_strike + 16 #better weapon
        print("You used the Staff of the Seven Warlocks for added 16 bonus damage!")
        pass
      if player_strike > enemy1_strike:
        print("You just inflicted", player_strike, "on the Mutant Salamander!")
        enemy1_health -= player_strike
        print("The Mutant Salamander now has",enemy1_health,"health left!\n")
        time.sleep(2)
      else:
        print("You have been injured", enemy1_strike, "points by the Mutant Salamander!")
        player_health -= enemy1_strike
        print("You now have",player_health,"health left!\n")
        time.sleep(2)
    if player_health <= 0:
      print("You have been hit by a critical shot")
      Game_End()
    else:
      print("You defeated the Mutant Salamander! Well done\n")
      print("You have a score of",score,"!\n")
      print("You have a health of",player_health,"!\n")
      print("\nYou defeated the Guardian and so walk to the huge chamber at the end!")
      print("-------------------------------------------------------------")
      print("\nThe Chamber!\n")
      tp("""You look all around you, above you is a great domed ceiling that has light pouring in from a small opening above.\nDirectly in front of you, and see two columns rising above all! In the middle of them are iron-clad gates and a plaque reading:

      To Open the gates you must aquire a key found in the depths of an underground catacomb!
      DO NOT DESPAIR HERE IS AN \'EPIC\' IMAGE TO GUIDE YOU! 

           /////
         ///   ///
        //       ////////////////////////
         ///   ////       //    //    //
           ////           /     /    //
      -The Watcher....\n\n
      """)
      #continue
      print("You approach the gate, there is a huge keyhole!\nTHERE IS A BOSS INSIDE")
      unlocked = False
      while unlocked != True:
        key = input("Please type \'insert\' to unlock the gate with the Key ")
        if key.upper().strip() == "INSERT":
          if "gatekey" in inventory: #when the player enters code it continues
            print("You unlock the gate")
            print("\nTHE GATES OF SILENT POWER HAVE OPENED!")
            unlocked = True 
            print("You enter and come across the BOSS; THE GUARDIAN") 
            Boss_Fight("THE GUARDIAN")
            Game_won()
          else:
            print("You do not have the key!\nPlease come back when you do\n")
            sure1 = input("Do you want to leave? The enemy will respawn and you leave the chamber! If you are sure type\'sure\'\n")
            if sure1.upper().strip() == "SURE":#checking you want to leave
              unlocked = True #stops the loop
              print("You leave the chamber")
              field2scene()
            else:
              continue
        else:
          continue
  elif willyoufight == "FLEE":
    print("You ran away! Better luck next time! Your score is",score,"!\n")
    print("The Salamander remains in the way!")
    time.sleep(2)
    print("You leave the mineshaft!\nIn an opening you see light, you go out and are in a field!")
    field2scene()
  else:
    print("Invalid input...")
    mineshaftscene()

'''______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________'''

def fieldscene ():
  print("-------------------------------------------------------------")
  print("\nThe Field!\n")
  print("You see a Scarecrow, it starts creeping towards you!")
  print("This is a Tier 1 Fight!")
  print("Player Health =",player_health,"\n")
  fight_or_flight("Scarecrow",1) #asking for a certain lvl and name
  print("The field stretches for a long way. To the \'West\' there is a Forest, to the \'East\' there is a Village and to the \'North\' there is another field.")
  print("\nDo you want to go West, East or North?\n")
  fieldchoice()

def fieldchoice():#asking direction
  choice2 = input("")
  choice2 = choice2.upper().strip()
  if choice2 ==  "WEST":
    forestscene()
  elif choice2 == "EAST":
    villagescene()
  elif choice2 == "NORTH":
    field2scene()
  else:
    print("Invalid input...")
    fieldchoice()

def forestscene():
  pass
  #code = 2364

def field2scene():
  global willyoufight
  print("-------------------------------------------------------------")
  print("\nThe Gloomy Field!\n")
  print("As you walk through the field you notice something gleaming to the \'West\' and a dark mass to the \'East\' the field you came from is to the \'South\'.")
  print("\nDo you want to go West, East or South?\n")
  gloomyfieldchoice()

def gloomyfieldchoice():
  choice3 = input("")
  choice3 = choice3.upper().strip()
  if choice3 == "WEST":
    shinycave()
  elif choice3 == "EAST":
    darkmarsh()
  elif choice3 == "SOUTH":
    fieldscene()
  else:
    print("Invalid input...")
    gloomyfieldchoice()
  
def shinycave():
  global didyouwin
  print("-------------------------------------------------------------")
  print("\nThe Shiny Cave\n")
  print("You have entered a small cave! You can see a vault door at the other end but there is a problem... An enemy is guarding it!")
  print("This is a Tier 2 Fight,")
  print("Player Health =",player_health,"\n")
  fight_or_flight2("Giant Slithering Snake",2)

def Tier_22_Fight(enemy):
  global name , player_health , score , didyouwin 
  didyouwin = 0
  enemy1_health = 60
  print("------------------------------------------")
  print("Welcome to the fight", name,"vs ",enemy,"\n")
  while player_health > 0 and enemy1_health > 0:
    player_strike = random.randint(0,20)
    enemy1_strike = random.randint(0,12)
    if player_strike > enemy1_strike:
      print("You just inflicted", player_strike, "on the",enemy,"!")
      enemy1_health -= player_strike
      time.sleep(1)
    else:
      print("You have been injured", enemy1_strike, "points by the",enemy,"!")
      player_health -= enemy1_strike
  if player_health <= 0:
    print("You have been hit by a critical shot")
    Game_End
  else:
    print("You defeated the",enemy,"! Well done\n")
    score = score + 20
    print("You have a score of",score,"!\n")
    didyouwin = 10
    shinycavedooropening()

def fight_or_flight2(enemy,tier): 
    print("\nYou have encountered the",enemy,"!")
    willyoufight = input("Do you want to \'Fight\' for points or \'Flee\' to another  day!\n")
    willyoufight = willyoufight.upper().strip()
    if willyoufight == "FIGHT":
      Tier_22_Fight("Giant Slithering Snake")
    elif willyoufight == "FLEE":
      print("You ran away! Better luck next time! Your score is",score,"!\n")
      print("The snake remains!")
      time.sleep(2)
      print("You leave the cave!")
      field2scene()
    else:
      print("Invalid input...")
      fight_or_flight()

def shinycavedooropening():
  global inventory
  #this is a script to open a door with a code
  print("You approach the door, there is a keypad")
  cracked = False
  while cracked != True:
    code = input("Please enter the four digit code ")
    if code == "1364": #when the player enters code it continues
      time.sleep(1)
      print("\nThe door opens, before you is a sword in a ring of fire!")
      cracked = True #ending loop
      swordpickup = input("Would you like to take the Sword? ")
      swordpickup = swordpickup.upper().strip()
      if swordpickup() == "YES": #puicking up sword
        print("You draw the Sword!\n")
        print(">>> YOU HAVE PICKED UP AN ELEMENTAL WEAPON; THE FIRE SWORD!!")
        inventory.append("fire_sword") #adding to inventory
        print("Your inventory consists of:",inventory)
        print("You leave the cave")
        field2scene()
      elif swordpickup() == "NO":
        print("Ok...Why...\nYou leave the cave")
        field2scene()
      else:
        continue
    else:
      quity = input("Would you like to try again?")
      if quity.lower().strip() == "n" or "no":
        sure = input("Are you sure? The enemy will respawn! If you are sure type\'sure\'\n")
        if sure.upper().strip() == "SURE":#checking you want to leave
          cracked = True #stops the loop
          print("You leave the cave")
          field2scene()
        else:
          continue

def darkmarsh():
  intelligence = 3
  print("-------------------------------------------------------------")
  print("\nThe Dark Marsh!\n")  
  print("You encounter a giant woodlouse!")
  print("This is a Tier 1 Fight!")
  print("Player Health =",player_health,"\n")
  fight_or_flight("Giant Woodlouse",1)
  print("The ground is deep and easy to sink in!")
  time.sleep(2)
  print("What Would you like to do:\n(1)Walk towards the path\n(2)Lay on the mud\n(3)Walk on the leaves\nChoose Quickly or you will SINK!!")
  if intelligence >= 2:   #skill level changes gameplay
    print("Using your intelligence you remember that walking will cause you to sink!")
    pass
  if intelligence >= 3:
    print("You read on a map that there is an Underground Cavern below you!")
    pass
  choice4()
  
def choice4():
  global choice3
  choice3 = input("\nChoice>>> ")
  if choice3 == "1":
    print("You start to walk towards the path.....")
    time.sleep(2)
    print("You start to sink!!")
    undergroundcavern()
  elif choice3 == "2":
    villagescene()
  elif choice3 == "3":
    undergroundcavern()
  elif choice3 == "4":
    print("You found a secret!\nYou walk towards a hole and into the mineshaft!")
    mineshaftscene()
  else:
    print("Invalid answer")
    choice4()

def undergroundcavern():
  print("-------------------------------------------------------------")
  print("\nThe Underground Cavern!\n")
  knifechoicey()
  print("You are at a crossroads\nTo the Right there is a shaft into the earth,\nto the Left there is a huge chamber...")
  crossroadscavern()

def knifechoicey(): 
  knifechoice = input("You see a knife emmbeded in the wall, do you want to pick it un (Y/N) ")
  if knifechoice.upper().strip() == "Y" or knifechoice.upper().strip() == "YES": #one or the other
    print("You collect the knife and sheath it in your belt!")
    inventory.append("knife")
    print("Your inventory consists of:",inventory)
    print("On the wall you see faint etchings...")
    time.sleep(2)
    print("As you peer closer you see the numbers 1364 scribed into the wall.....")
    time.sleep(2)
    print("and a cave drawn next to it.....!")
  elif knifechoice.upper().strip() == "N" or knifechoice.upper().strip() == "NO":
    print("You leave the knife and walk on...\n")
  else:
    print("Invalid Input...")
    knifechoice()

def crossroadscavern():
  directionatcross = input("So.... Right or Left? ")
  if directionatcross.upper().strip() == "R" or directionatcross.upper().strip() == "RIGHT":
    mineshaftscene()
  if directionatcross.upper().strip() == "L" or directionatcross.upper().strip() == "LEFT":
    villagescene()
  else:
    print("Invalid Input...")
    crossroadscavern()

def giantchamber():
  #key collection
  pass

'''____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________'''

Start()
