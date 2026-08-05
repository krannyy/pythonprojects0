alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs. // done

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text: # por cada letra dentro de la lista alphabet, haz lo siguiente:
        position = alphabet.index(letter) 
        new_position = (position + shift_amount) % len(alphabet) # this shifts (adds) the shift amount to our original position, which displays the final amount with the desired shift // le suma al integer anterior
        new_letter = alphabet[new_position] 
        cipher_text += new_letter 
    return cipher_text



#Now let's do the decode part // which is basically the reverse operation

def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for letter in original_text: # por cada letra dentro de original_text, haz lo siguiente:
        position = alphabet.index(letter) #dentro de la variable position, storea la position de cada element. Dentro de alphabet obten el indice (posicion) de la letra obtenida en original_text, se asigna la posicion a traves de alphabet, comparando ambas letras y se ve cual es el elemento con base en el input del usuario, se busca dentro de alphabet, y se obtiene la posicion desde alphabet
        new_decrypted_position = (position - shift_amount) % len(alphabet)
        new_decrypted_letter = alphabet[new_decrypted_position]
        decrypted_text += new_decrypted_letter
    return decrypted_text #this makes sure that the 


def caesar(direction, original_text, shift_amount):
    if direction == "encode":
        print(encrypt(original_text ,shift_amount))
    else:
        print(decrypt(original_text, shift_amount))

caesar(direction=direction, original_text=text, shift_amount=shift)