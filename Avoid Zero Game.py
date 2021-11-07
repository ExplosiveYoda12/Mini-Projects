import random as r,sys

#NOTE:
#Took multiple tries to do as coded it in different ways before, 
#Good problem that made me think
#Tried to add a rough AI for the computer in computerTurn()

number = r.randint(19,30)
validNumbers = [1,2,3]

def computerTurn(number):
  if (number-3) == 0:
    number -= 2
    compNumber = 2
  elif (number-2) == 0:
    number -= 1
    compNumber = 1
  else:
    compNumber = r.randint(1,3)
    number -= compNumber

  if number <= 0:
    print("The Computer caused the number to reach 0! You Win.")
    sys.exit()
  else:
    print("",compNumber,"Removed by Computer\n",number,"Left\n")
    chooseNumber(number,validNumbers)

def remove(number,numChoice):
  number -= numChoice
  if number <= 0:
    print("You caused the number to reach 0! Better luck next time.")
    sys.exit()
  else:
    print("\n",numChoice,"Removed,",number,"Left")
    computerTurn(number)

def chooseNumber(number,validNumbers):
  print("The Number is currently: ",number)
  numChoice = int(input("How Many do you want to remove? "))
  if numChoice in validNumbers:
    remove(number,numChoice)
  else:
    print("Number not between 1-3, Try again")
    chooseNumber(number,validNumbers)

chooseNumber(number,validNumbers)
