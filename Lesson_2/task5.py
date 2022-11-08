input_list = input('Enter your list: ').split(',')
#List entry
int_list = []
for element in input_list:
    int_list.append(int(element))
#translation of the list for the correct operation of the max, min functions
print('The maximum value is: ' + str(max(int_list)))
print('The minimum value is: ' + str(min(int_list)))

int_list.sort()
summ = sum(int_list[1:-1])
print('Sum equals: ', summ)

