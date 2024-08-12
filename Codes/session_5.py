# day = int(input('enter a number: '))

# if day == 1:
#     print('Sturday')
# elif day == 2:
#     print('Sunday')
# elif day == 3:
#     print('Monday')
# elif day == 4:
#     print('Tuesday')
# elif day == 5:
#     print('Wednsday')
# elif day == 6:
#     print('Thursday')
# elif day == 7:
#     print('Friday')
# else:
#     print('please enter a correct number between 1 and 7.')


########################## 

# code = int(input('Staff Code: '))
# salary = int(input('Salary: '))

# if salary < 0:
#     print('incorrect salary.')
# elif salary < 400000:
#     print('Your final salary is:' + str(salary))
# elif 400001 < salary < 500000:
#     tax = salary * 0.1
#     res = salary - tax
#     print('Your final salary is:' + str(res))
# elif 500001 < salary < 700000:
#     tax = salary * 0.15
#     res = salary - tax
#     print('Your final salary is:' + str(res))
# elif salary > 700000:
#     tax = salary * 0.17
#     res = salary - tax
#     print('Your final salary is:' + str(res))

# ##################################
# def less_than_40000(salary):
#     print('Your final salary is:' + str(salary))

# def between_400000_and_500000(salary):
#     tax = salary * 0.1
#     res = salary - tax
#     print('Your final salary is:' + str(res))

# def between_500000_and_700000(salary):
#     tax = salary * 0.15
#     res = salary - tax
#     print('Your final salary is:' + str(res))

# def more_than_700000(salary):
#     tax = salary * 0.17
#     res = salary - tax
#     print('Your final salary is:' + str(res))

# def main():
#     # code = int(input('Staff Code: '))
#     salary = int(input('Salary: '))

#     if salary < 0:
#         print('incorrect salary.')
#     elif salary < 400000:
#         less_than_40000(salary)
#     elif 400001 < salary < 500000:
#         between_400000_and_500000(salary)
#     elif 500001 < salary < 700000:
#         between_500000_and_700000(salary)
#     elif salary > 700000:
#         more_than_700000(salary)

# main()
##########################################

salary = int(input('Salary: '))

if salary < 0:
    print('incorrect salary.')
elif salary < 400000:
    print('Your final salary is:' + str(salary))
elif (400001 < salary) and (salary < 500000):
    tax = salary * 0.1
    res = salary - tax
    print('Your final salary is:' + str(res))
elif (500001 < salary) or (salary < 700000):
    tax = salary * 0.15
    res = salary - tax
    print('Your final salary is:' + str(res))
elif salary > 700000:
    tax = salary * 0.17
    res = salary - tax
    print('Your final salary is:' + str(res))