################# question 3

# num = float(input('Enter a number.'))

# maximum = 0
# minimum = 10000000000

# while(num != -1):
#     if num > maximum:
#         maximum = num
    
#     if num < minimum:
#         minimum = num

#     num = float(input('Enter a number.'))

# print(maximum)
# print(minimum)

###################### question 5

def check(reshte):
    ind_a = -1
    ind_b = -1
    ind_c = -1
    
    if 'a' in reshte:
        for char in reshte:
            ind_a += 1  # This is a reshte. -> index_ a = 0 -> 1 -> 2 -> 3 -> 4 -> 5
            if char == 'a':
                break
    
    if 'b' in reshte:
        for char in reshte:
            ind_b += 1
            if char == 'b':
                break

    if 'c' in reshte:
        for char in reshte:
            ind_c += 1
            if char == 'c':
                break
    
    return [ind_a, ind_b, ind_c]

def main():
    reshte = input('Enter a string:')
    res = check(reshte)

    if res[0] != -1:
        print('a exist and the index a is :', res[0])
    else:
        print('a does not exist.')

    if res[1] != -1:
            print('b exist and the index a is :', res[1])
    else:
        print('b does not exist.')

    if res[2] != -1:
        print('c exist and the index a is :', res[2])
    else:
        print('c does not exist.')

main()