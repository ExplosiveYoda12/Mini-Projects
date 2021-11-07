import random, sys
Playing = True
Points = 0

def horl(Points):
  if Points == 10:
    print("Congrats! You Win with 10 Points")
    exit()
  else:
    pass
  randNumStart = random.randint(1,20)
  randNumCompare = random.randint(1,20)
  print("Starting Number:",randNumStart)
  HorL = str(input("Higher(H) or Lower(L): ")).upper().strip()
  if HorL == "HIGHER" or HorL == "H":
    if randNumCompare > randNumStart:
        print("Correct, the number was",randNumCompare)
        Points += 1
        horl(Points)
    elif randNumCompare < randNumStart:
        print("Incorrect, the number was",randNumCompare)
        print("Your Final Score was", Points)
        Playing = False
    else:
        print("Error")
        horl(Points)
  elif HorL == "LOWER" or HorL == "L":
    if randNumCompare > randNumStart:
        print("Incorrect, the number was",randNumCompare)
        print("Your Final Score was", Points)
        Playing = False
    elif randNumCompare < randNumStart:
        print("Correct, the number was",randNumCompare)
        Points += 1      
        horl(Points)
    else:
        print("Error")
        horl(Points)
  else:
      print("Error")
      horl(Points)
horl(Points)
