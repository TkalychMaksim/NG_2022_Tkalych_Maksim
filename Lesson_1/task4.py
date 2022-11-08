
while True:
    first_coef = int(input('Input first coefficient of equation:'))
    second_coef = int(input('Input second coefficient of equation:'))
    third_coef = int(input('Input third coefficient of equation:'))
    discriminant = (second_coef ** 2)-(4*first_coef * third_coef)
    if (discriminant<0):
        print('Equation Error: discriminant<0')
    else:
        x1 = ((-second_coef) - (float(discriminant ** 0.5))) / (2 * first_coef)
        x2 = ((-second_coef) + (float(discriminant ** 0.5))) / (2 * first_coef)
        print('Your answers:', x1, x2)
