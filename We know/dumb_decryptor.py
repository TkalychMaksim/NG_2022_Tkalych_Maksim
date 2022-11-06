alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
input_text = input('Input text to decoding: ').upper()
#Entering text with uppercase translation to avoid errors
encoder_step = int(input('Choose the step of encoder: '))
decoded_text = ''
for i in input_text:
    place = alphabet.find(i)
    new_place = place + encoder_step
    if i in alphabet:
        decoded_text += alphabet[new_place]
    else:
        decoded_text += i
print(decoded_text)

