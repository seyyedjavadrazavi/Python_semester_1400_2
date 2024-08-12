# g = 'Hi. this is a test.'

# for i in range(len(g)):
#     print(i)
#     if i == 'a':
#         print('I found an a.')
#         break

# print('here we are after loop.')

###########################################

# sum_num = 0
# for i in range(10):
#     print(i)
#     sum_num += i

# avg = sum_num/10
# print(avg)


###############################################

# sum_num = 0
# n = int(input('enter the number of courses.'))

# for i in range(n):
#     score = float(input('enter the score of course '+ str(i + 1)+' : '))
#     sum_num += score

# avg = sum_num/n
# print(avg)


######################################################

# n = int(input('Enter the number of student: '))

# while n < 2:
#     print('The number of students is invalid.')
#     n = int(input('Enter the number of student: '))

#     if n == -1:
#         exit()

# student_number_1 = ''
# avg_stdn_1 = 0

# student_number_2 = ''
# avg_stdn_2 = 0

# for i in range(n):
#     sd_id = input('Enter the student id of student ' + str(i + 1) + " : ")
#     sd_avg = float(input('Enter the average score of student ' + str(i + 1) + ' : '))

#     if sd_avg > avg_stdn_1:
#         avg_stdn_1 = sd_avg
#         student_number_1 = sd_id
#     elif sd_avg > avg_stdn_2:
#         avg_stdn_2 = sd_avg
#         student_number_2 = sd_id


# print(student_number_1)
# print(avg_stdn_1)

# print(student_number_2)
# print(avg_stdn_2)

##########################################

# n = int(input('Enter a number: '))

# print(type(n))

# if type(n) == type(1):
#     print(type(n))
