input_number = int(input('Enter your number: '))
for first_index in range(input_number):
    for second_index in range(input_number-first_index):
        print(input_number-second_index-first_index, end=' ')
    print('')


