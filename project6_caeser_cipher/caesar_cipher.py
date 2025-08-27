alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(input_string, shift_number):
    cipher_text = ""
    for letter in input_string:
        if letter.isalpha():
            if letter.islower():
                pos = alphabets.index(letter)
                new_pos = (pos + shift_number) % len(alphabets)
                cipher_text += alphabets[new_pos]
            else:
                pos = alphabets.index(letter.lower())
                new_pos = (pos + shift_number) % len(alphabets)
                cipher_text += alphabets[new_pos].upper()
        else:
            cipher_text += letter
    print("-" * 40)
    print("Your Encoded Message :", cipher_text)
    print("-" * 40)

def decode(input_string, shift_number):
    plain_text = ""
    for letter in input_string:
        if letter.isalpha():
            if letter.islower():
                pos = alphabets.index(letter)
                new_pos = (pos - shift_number) % len(alphabets)
                plain_text += alphabets[new_pos]
            else:
                pos = alphabets.index(letter.lower())
                new_pos = (pos - shift_number) % len(alphabets)
                plain_text += alphabets[new_pos].upper()
        else:
            plain_text += letter
    print("-" * 40)
    print("Your Decoded Message :", plain_text)
    print("-" * 40)


while True:
    direction = input("Type 'encode' to encrypt, 'decode' to decrypt : ").lower()
    text = input("Type your message: ")
    shift = int(input("Type the shift number: "))

    if direction == "encode":
        encode(text, shift)
    elif direction == "decode":
        decode(text, shift)
    else:
        print("Invalid choice, try again!")

    again = input("Do you want to continue? (y/n): ").lower()
    if again == "n":
        print("Goodbye!")
        break
