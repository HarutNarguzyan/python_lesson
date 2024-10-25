# new_dict = {
#     "Harut": 1,
#     "Ero":8,
#     "Hrach":4,
#     "Trdat":2,
#     "Tigran":7,
#     "Sona": 12,
#     "Martin": 3,
#     "Sergo": 777,
#     "Albert": 999
# }
# bad = []
# good = []
# mijin = []
# summ = 0
# summ1 = 0
# for i in new_dict:
#     summ+=new_dict[i]
#     summ1 += 1
# for j in new_dict:
#     if new_dict[j] < summ/summ1:
#         bad.append(j)
#     elif new_dict[j] > summ/summ1:
#         good.append(j)
#     else:
#         mijin.append(j)
# print(f"vat {bad} ,mijin {mijin} , lav{good}")


# new_dict = {
#     "Harut": 1,
#     "Ero":8,
#     "Hrach":4,
#     "Trdat":2,
#     "Tigran":7,
#     "Sona": 12,
#     "Martin": 3,
#     "Sergo": 777,
#     "Albert": 999
# }


# print(new_dict.get('Se', "chka"))


# s = 'a,2,c,4,a,4,e,11,d,20'
# s = s.split(',')
# data = {}
# for i in range(0, len(s) - 1, 2):
#     if s[i] in data:
#         data[s[i]] += int(s[i + 1])
#     else:
#         data[s[i]] = int(s[i + 1])
# print(data)

# new_dict = {}
# a = input("greq bar: ")
# for i in a:
#     if not i in new_dict:
#         b = a.count(i)
#         new_dict[i] = b
# print(new_dict)



# new_list = []
# old_list = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}] 
# for i in old_list:
#     if not i in new_list:
#         new_list.append(i)
# print(new_list)



# ---------------------------------------

# new_dict = {
#     "Harut": 1,
#     "Ero":8,
#     "Hrach":4,
#     "Trdat":2,
#     "Tigran":7,
#     "Sona": 12,
#     "Martin": 3,
#     "Sergo": 777,
#     "Albert": 999
# }

# keys = sorted(new_dict, key=new_dict.get)
# print(keys)




# new_dict = {
#     "Harut": 1,
#     "Ero":8,
#     "Hrach":4,
#     "Trdat":2,
#     "Tigran":7,
#     "Sona": 12,
#     "Martin": 3,
#     "Sergo": 777,
#     "Albert": 999
# }

# user_key = input("text: ")
# user_value = input("text: ")
# new_dict[user_key] = user_value
# print(new_dict)






# new_dict = {
#     "Harut": 1,
#     "Ero":8,
#     "Hrach":4,
#     "Trdat":2,
#     "Tigran":7,
#     "Sona": 12,
#     "Martin": 3,
#     "Sergo": 777,
#     "Albert": 999
# }
# user_input = input("text: ")
# if user_input in new_dict:
#     print("ka")
# else:
#     print("chka:)")







# dict1 = {'a': 50, 'b': 700}
# dict2 = {'c': 400, 'd': 600}
# dict1.update(dict2)
# print(dict1)





# mydict = {'a':1,'b':2,'c':12}
# summ = 1
# for i in mydict:
#     summ*=mydict[i]
# print(summ)







# d = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# keys = sorted(d, key=d.get, reverse=True)[:3]
# test = {}
# for i in keys: 
#     test[i] = d[i]
# print(test)





























# mydict = {
#     1:['.',',','?','!',':'],
#     2:['A','B','C'],
#     3:['D','E','F'],
#     4:['G','H','I'],
#     5:['J','K','L'],
#     6:['M','N','O'],
#     7:['P','Q','R','S'],
#     8:['T','U','V'],
#     9:['W','X','Y','Z'],
#     0:[" "]
# }
# user_input = input("Text: ").upper()

# for i in mydict:
#     for j in user_input:
#         if j in mydict[i]:
#             print(mydict[i].index(j) + 1 * i,end='')


# mydict = {
#     1:'AEILNORSTU',
#     2:'DG',
#     3:'BCMP',
#     4:'FHVWY',
#     5:'K',
#     8:'JX',
#     10:'QZ'
#     }
# count = 0
# user_input = input("text: ").upper()
# for i in mydict:
#     for j in user_input:
#         if j in mydict[i]:
#             count += i
# print(count)



# import random

# toms = {
#     "B":[random.randint(1,15) for i in range(5)],
#     "I":[random.randint(16,30) for i in range(5)],
#     "N":[random.randint(31,45) for i in range(5)],
#     "G":[random.randint(46,60) for i in range(5)],
#     "O":[random.randint(61,75) for i in range(5)]
# }

# while True:
#     input('enter: ')
#     number = random.randint(1,75)
#     for i in toms:
#         if number in toms[i]:
#             toms[i][toms[i].index(number)] = "X"
#         print(f'{i} : {toms[i]}')
#     print(number)
    
