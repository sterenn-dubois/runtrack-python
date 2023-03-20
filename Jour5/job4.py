def shift_message(message, shift):
    shifted_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                shifted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            shifted_char = char
        shifted_message += shifted_char
    return shifted_message
message = "Hello, world!"
shift = 3
shifted_message = shift_message(message, shift)
print(shifted_message)