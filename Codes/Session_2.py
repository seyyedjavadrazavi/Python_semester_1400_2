name = input("Insert your name: ")
family = input("Your family please? ")
birth_date = input("Enter your birth date: ")

full_name = name + ' ' + family
year = int(birth_date)
Current_year = 1401
age = Current_year - year
print('Your full name is: ' + full_name)
print('Your age is: ' + str(age))

course_1 = input('Input the score 1: ')
weight_1 = input("Weight? ")
course_2 = input('Input the score 2: ')
weight_2 = input("Weight? ")

average = ((int(course_1) * int(weight_1)) + (int(course_2) * int(weight_2))) / (int(weight_1) + int(weight_2))
print('Your average is: ' + str(average))

# 18 * 3 = 54
# 20 * 2 = 40
# 54 + 40 / 5 = 94 / 5 = 18.8