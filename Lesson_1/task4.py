import math
#Import necessary Library
while True:
    first_coef = int(input('Input first coefficient of equation:'))
    second_coef = int(input('Input second coefficient of equation:'))
    third_coef = int(input('Input third coefficient of equation:'))

    if (second_coef>0) and (third_coef>0):
        print('============================')
        print("Your equation:", str(first_coef) + 'x^2', '+' + str(second_coef) + 'x', '+' + str(third_coef), '=0')
        print('============================')
    elif (second_coef<0) and (third_coef>0):
        print('============================')
        print("Your equation:", str(first_coef) + 'x^2', str(second_coef) + 'x', '+' + str(third_coef), '=0')
        print('============================')
    elif (second_coef>0) and (third_coef<0):
        print('============================')
        print("Your equation:", str(first_coef) + 'x^2', '+' + str(second_coef) + 'x', str(third_coef), '=0')
        print('============================')
    elif (second_coef<0) and (third_coef<0):
        print('============================')
        print("Your equation:", str(first_coef) + 'x^2', str(second_coef) + 'x', str(third_coef), '=0')
        print('============================')
#Loop for correct representation of the equation
    discriminant = math.pow(second_coef, 2)-(4*first_coef * third_coef)
    if (discriminant<0):
        print('Equation Error: discriminant<0')
    else:
        print(discriminant)
        print(math.sqrt(discriminant))
        x1 = ((-second_coef) - math.sqrt(float(discriminant))) / (2 * first_coef)
        x2 = ((-second_coef) + math.sqrt(float(discriminant))) / (2 * first_coef)
        print('Your answers:', x1, x2)
