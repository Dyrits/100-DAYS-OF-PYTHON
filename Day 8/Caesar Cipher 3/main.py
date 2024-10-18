from art import logo
print(logo)

lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
uppers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']

def encrypt(original_text, shift_amount):
    encrypted_text = "".join([lowers[(lowers.index(letter) + shift_amount) % 26] if letter.islower() else uppers[
        (uppers.index(letter) + shift_amount) % 26] if letter.isupper() else letter for letter in original_text])
    print(f"The encoded text is {encrypted_text}")

def decrypt(encrypted_text, shift_amount):
    decrypted_text = "".join([lowers[(lowers.index(letter) - shift_amount) % 26] if letter.islower() else uppers[
        (uppers.index(letter) - shift_amount) % 26] if letter.isupper() else letter for letter in encrypted_text])
    print(f"The decoded text is {decrypted_text}")

def ceaser(original_text, shift_amount, operation):
    if operation == "encode":
        encrypt(text, shift)
    elif operation == "decode":
        decrypt(text, shift)

active = True
while active:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    ceaser(text, shift, direction)
    active = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower() == "yes"







