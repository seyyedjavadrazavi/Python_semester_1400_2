# import math

# print(1 * 1)
# print(2 * 2)
# print(3 * 3)
# print(4 * 4)

# i = 0
# while i < 10:
#     print(math.pow(i, 2))
#     i = i + 1

# print('end of the while.')

# temp = 'this is a string.' # 0 - 16
# temp = temp + ' And it is our first example.'
# temp = 'This is class.' + temp
# print(temp)

# print(temp[0])
# print(temp[5])
# print(temp[10])
# print(temp[15])
# print(temp[16])
# print(temp[17])

##############################################

# temp = 'this is a string.' # 0 - 16

# print(temp[3:11])
# print(temp[:11])
# print(temp[3:])
# print(len(temp))


##############################################

# temp = 'This is an example and we need to find the banana in this sentece'
# temp1 = 'there is orange in this sentence.'

# if 'banana' in temp:
#     print('Banana is find!')
#     index = temp.find('orange')
#     print(index)

# temp = temp.replace('banana', 'blue orange')
# print(temp)

# if 'banana' in temp1:
#     print('Banana is find!')
# else:
#     print('Banana does not exist!')

##########################################################

# temp = 'This is an example and we need to find the banana in this sentece'
# index = temp.find(' bana ')
# print(index)

# temp = temp.replace(' bana ', 'blue orange ')
# print(temp)

##########################################################

# temp = 'This is an example and we need to find the banana in this sentece'
# index = temp.find(' bana ')
# print(index)

# temp = temp.replace(' bana ', 'blue orange ')
# print(temp)

##########################################################

temp = 'This is an EXAMPLE and we need to find the banana in this sentece'

temp = temp.lower()

# print(temp.lower())
# print(temp.upper())

index = temp.find('example')
print(index)

temp = temp.replace('example', 'blue orange ')
print(temp)
