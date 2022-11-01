string =list(input("Enter your string:" ))
list.sort(string)
for elements in range(len(string)):
#count_e-count of elements
    count_e = 0
    if string[elements] != string[elements-1]:
        for letters in range(len(string)):
            if string[elements] == string[letters]:
                count_e = count_e + 1
#character count
            if letters + 1 == len(string):
                print(string[elements], '-', count_e)



