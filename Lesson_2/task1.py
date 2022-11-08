input_list = (input("Enter your string"))
set_list = sorted(set(input_list))
print(set_list)
for index in set_list:
    count_i = input_list.count(index)
    print(index, '=', count_i, end=' ')





