number = int(input('Enter a number to calculate the factorial: '))
factorial = 1
while number > 1:
    factorial *= number
    number = number -1
print(factorial)