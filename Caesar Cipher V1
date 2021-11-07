def menu():
  cryptType = input("Would you like to Encrypt or Decrypt? ").upper()        
  if cryptType == "ENCRYPT" or cryptType == "E":
    encrypt()                                   
  elif cryptType == "DECRYPT" or cryptType == "D":
    decrypt()
  else:
    print("Error, try again")
    menu()
                            
def encrypt():
  alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  plaintext = input("Plaintext: ").lower()
  shift = int(input("Shift Value: "))
  shift = shift % 26
  ciphertext = ""
  for letter in plaintext:
    if letter == " ":
      ciphertext += " "    
    else:  
      position = alphabet.index(letter)
      newPosition = position + shift
      newPosition = newPosition % 26
      ciphertext += (alphabet[newPosition].upper())         
  print(ciphertext)

def decrypt():
  alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  crypttext = input("Ciphertext: ").lower()
  shift = int(input("Shifted Value: "))
  shift = shift % 26
  shift = -shift
  cleantext = ""
  for letter in crypttext:
    if letter == " ":
      cleantext += " "    
    else:  
      position = alphabet.index(letter)
      newPosition = position + shift
      newPosition = newPosition % 26
      cleantext += (alphabet[newPosition].upper())         
  print(cleantext)     
      
menu()
