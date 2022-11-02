current_number = int(input('Enter your number: '))
for i in range(current_number):
    for j in range(current_number-i):
        print(current_number-j-i, end=' ')
    print('')


