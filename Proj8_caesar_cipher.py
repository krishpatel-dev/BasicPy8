alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        elif char in number:
            position = number.index(char)
            new_position = position + shift_amount
            end_text += number[new_position]
        elif char in special_char:
            position = special_char.index(char)
            new_position = position + shift_amount
            end_text += special_char[new_position]
        else:
            end_text += char

    print(f"Here is the {cipher_direction}d result: {end_text}") 

from art import logo
print(logo)

should_continue = True

while should_continue:
    # direction = input("type 'encode' to encrypt, type 'decode; to decrypt: \n")
    # if direction not in ("encode", "decode"):
    #     print("Invalid direction!")
    #     continue
    while (direction:=input("type 'encode' to encrypt, type 'decode; to decrypt: \n")) not in ('encode','decode'):
        print("Invalid direction!")
    
    text = input("type your message: \n").lower()
    shift = int(input("type the shift number: \n"))
    shift %= 26

    caesar(start_text = text, shift_amount = shift, cipher_direction = direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_continue = False
        print("Goodbye")

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter 
#     print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text += new_letter 
#     print(f"The decoded text is {plain_text}")

# if direction == "encode":
#     encrypt(plain_text = text, shift_amount = shift)
# elif direction == "decode":
#     decrypt(cipher_text = text, shift_amount = shift)
# else:
#     print("Enter a valid direction!")  