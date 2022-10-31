print("To work with the program, enter 2 numbers and select an operation from the list")
print("For operations ^,√ enter only one number, instead of the second number enter '0'")
print("To enter √ sign use the key combination (alt+251)")
firstnumber = int(input("Input first number:"));
secondnumber = int(input("Input second number:"));
#Request numbers from user and translation to int
action = input("Choose the operation from list(+,-,*,/,^,√)");
#Reuest action from user


if action == "+":
     result = firstnumber + secondnumber
     print("Result: " + str(result))

if action == "-":
    result = firstnumber - secondnumber
    print("Result: " + str(result))

if action == "*":
    result = firstnumber * secondnumber
    print("Result: " + str(result))

if action == "/":
    result = firstnumber / secondnumber
    print("Result: " + str(result))

if action == '^':
    result = firstnumber * firstnumber
    print("Result:" + str(result))
if action == "√":
    result = (firstnumber ** 0.5)
    print("Result:  " + str(result))
