print("Enter a positive whole number: ")
NumberIn = int(input(""))
NumberOut = 0
Count = 0
while NumberIn > 0:
  Count +=1
  PartValue = NumberIn % 2
  NumberIn = NumberIn // 2
  for i in range (Count-1):
    PartValue *= 10
  NumberOut += PartValue
print("Result is:",NumberOut)
