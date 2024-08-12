# test = (1, 2, 3, 4)
# # test[0] = 1
# # test[1] = 2
# print(test[0])
# print(test[1])
# print(test[2])

##################################

# test_1 = {}
# test_1['سلام'] = 'Hello'
# test_1['مشهد'] = 'Mashhad'
# test_1['ایران'] = 'Iran'

# # print(test_1['سلام'])
# # print(test_1)

# test_1['سلام'] = 'Boljogh'

# print(test_1.keys())
# print(test_1.values())
# print(test_1.items)

# test_1.pop('سلام')
# print(test_1)

# del test_1['ایران']
# print(test_1)

# test_1.clear()
# print(test_1)
################################
import copy 

name = []
families = []

in_nme = input('Enter a name: ')
in_fam = input('Enter a falimy: ')

while in_nme != '-1':
    name.append(in_nme)
    families.append(in_fam)

    in_nme = input('Enter a name: ')
    in_fam = input('Enter a falimy: ')

del_name = input('Enter a name to delete it :')

if del_name in name:
    ind_del = name.index(del_name)
else:
    print("khata")
    del_name = input('Enter a name to delete it :')

name.remove(del_name)
families.pop(ind_del)

print(name)
print(families)

tmp_name = []
tmp_name.extend(name) 
tmp_name.sort()

for i in tmp_name:
    ind_search = name.index(i) 
    families[ind_search]
    print(i)
    print(families[ind_search])