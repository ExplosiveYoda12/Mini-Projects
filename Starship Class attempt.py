class starship:
    #class variables
    global craftHealth,craftDefence,craftOffence,craftTechnology,craftDiplomacy,craftCargo,craftMedical
    
    craftHealth = 2 #hp for ship
    craftDefence = 2 #defensive value in fights
    craftOffence = 2 #offensive value in attack
    craftTechnology = 2 #tech level creates multipliers for other attributes
    craftDiplomacy = 2 #chance of reward without fight
    craftCargo = 2 #storage capacity
    craftMedical = 2  #health regeneration
    
    def __init__(self, craftName, craftType, craftTier, craftAttributes): 

        self.craftName = craftName #random name generating from file
        self.craftType = craftType #ship class decides attribute levels
        self.craftTier = craftTier #tier decides rank of ship

    def displayStats(self): #simple display ship stats
        print("Name:", self.craftName)
        print("Class:", self.craftType)
        print("Tier:", self.craftTier)
        print("Health:", craftHealth)
        print("Defence:", craftDefence)
        print("Offense:", craftOffence)
        print("Technology:", craftTechnology)
        print("Diplomacy:", craftDiplomacy)
        print("Cargo Capacity:", craftCargo)
        print("Medical Facilities:", craftMedical) 

    def getMedical(self):
      return self.craftMedical

    def setMedical(self, newMedical):
      self.craftMedical = newMedical

bob = starship("bob","fighter",6,4)
bob.displayStats()
