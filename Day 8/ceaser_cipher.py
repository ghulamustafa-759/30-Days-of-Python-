

#double list is added for the case of last entry.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


msg = input("Enter Your message : ")
shif = int(input("Enter the shift number : "))

def ceaser(msg,shif,direction):
    if direction == 1:
      encrypt(msg,shif)
    elif direction == 2:
      decrypt(msg,shif)
    else:
      print("Please Enter a Valid choice .")
      
def encrypt(plain_text , shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The encoded text is : {cipher_text} ")


def decrypt(encrypted_text, shift_num):
  decipher_text = ""
  for letter in encrypted_text:
    place = alphabet.index(letter)
    new_place = place - shift_num
    new_letter = alphabet[new_place]
    decipher_text += new_letter
  print(f"The decoded text is : {decipher_text}")

direction = int(input("To encrypt choose 1, to decrypt choose 2.\n"))
ceaser(msg,shif,direction)


