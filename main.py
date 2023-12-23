alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print(f"\033[1m{'Caeser Cypher':.^50}\033[0m")

def caeser(start_text, shift_amount, cipher_direction):

    end_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            if shift_amount >= 45:
                shift_amount %= 26
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}.")


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()
    text = input("Type your message:\n").lower().strip()
    shift = int(input("Type the sift number:\n"))

    caeser(start_text=text, shift_amount=shift, cipher_direction=direction)

    continue_loop = input("Type 'yes' if you want to go again. Type 'no' to stop. ")
    if continue_loop == "yes":
        continue
    else:
        print("Goodbye ^^")
        break
