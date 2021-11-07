itemFind = input("Input Search nums")
items = ['1','3','5','7','9',]
for i in items:
  if itemFind.strip() == i:
    print("Found")  
  else:
    print("Not Found")
