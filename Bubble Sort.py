def bubbleSort(numberList):
  import sys
  numbers = numberList
  sizeOfList = len(numbers)
  swap = False
  for totalLoops in range(sizeOfList - 1):
    for position in range(sizeOfList - 1):
      if numbers[position] > numbers[position+1]:
        temp = numbers[position]
        numbers[position] = numbers[position+1]
        numbers[position+1] = temp
        swap = True
    print(numbers)
    if swap == False:
      sys.exit()
    else:
      swap = False

numbers9 = [77,65,32,1,150,49,63,2,99]
bubbleSort(numbers9)
