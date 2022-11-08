alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
input_text = input('Input text to decoding: ').upper()
#Entering text with uppercase translation to avoid errors
encoder_step = int(input('Choose the step of encoder: '))
decoded_text = ''
for letter in input_text:
    place = alphabet.find(letter)
    new_place = place + encoder_step
    if letter in alphabet:
        decoded_text += alphabet[new_place]
    else:
        decoded_text += letter
print(decoded_text)

