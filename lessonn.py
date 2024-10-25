# def matem():
#     a=int(input('tiv: '))
#     b=int(input('tiv: '))
#     print((a**2+b**2)**0.5)
# matem()

# def taxi():
#     tarif = 4
#     tiv = int(input('greq heravorutyuny(km): '))
#     tarif += tiv * 1000 / 140 * 0.25
#     return round(tarif)
# print(taxi(),'$')



# def qanak():
#     user_input = int(input('greq qanaky: '))
#     summ = 0 
#     if user_input > 0:
#         summ += 10.95 + (user_input - 1) * 2.95
#     return summ
# print(qanak())


# def mijin():
#     tiv1 = int(input('tiv1: '))
#     tiv2 = int(input('tiv2: '))
#     tiv3 = int(input('tiv3: '))
#     return (tiv1 + tiv2 + tiv3) / 3
# print(mijin())



# dictik = {
#         1:'One',
#         2:'Two',
#         3:'Three',
#         4:'Four',
#         5:'Five',
#         6:'Six',
#         7:'Seven',
#         8:'Eight',
#         9:'Nine',
#         10:'Ten',
#         11:'Eleven',
#         12:'Twelve'
#     }


# def func():
#     tiv = int(input('greq tiv: '))

#     print(dictik[tiv])

# func()


            
# dictik = {
#     'hunvar': 31,
#     'petrvar': 28,
#     'mart' : 31,
#     'april' : 30,
#     'mayis' : 31,
#     'hunis' : 30,
#     'hulis' : 31,
#     'ogostos' : 31,
#     'september' : 30,
#     'hoktember' : 31,
#     'noyember' : 30,
#     'dektember' : 31
# }
# summ = 0
# tiv = int(input('tiv: '))
# for i in dictik:
#     if tiv > summ:
#         summ += dictik[i]
#     else:
#         print(i,dictik[i])
#         break
# ???????

# a = int(input("a "))
# b = int(input("b "))
# c = int(input("c "))
# if a + b >= c and a+c >= b and b + c >= a:
#     if a == b == c:
#         print('havasarakoxm')
#     elif a == b or a == c or b == c:
#         print('havasarasrun')
#     else:
#         print('sovorakan')


# else:
#     print('tenc erankyun goyutyun chuni')



# a = ' '
# arr = []
# # user_input = input('greq text: ')
# for i in a:
#     arr.append(i)
# for j in arr:
#     print(arr.index(j))
#     # if i == ' ':
#         # arr.index(i) + 1 = (arr.index(i) + 1).upper()
# print(arr)
# ???


# def calendar(day,month,year):
#     summ = 0
#     day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if year % 4 == 0:
#         day_list[1] = 29
#     for i in range(month-1):
#         summ += day_list[i]
#     summ += day
#     return summ
# print(calendar(31,12,2023))

# def reverse_calendar(year, days):
#     month = 1
#     day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if year % 4 == 0:
#         day_list[1] = 29
#     while True:
#         if days > day_list[0]:
#             days -= day_list[0]
#             month += 1
#             day_list.pop(0)
#         else:
#             break
#     return f'{days}.{month}.{year}'

# print(reverse_calendar(2022, 364))



# -----------harusti kod----------------

# import random

# def random_hamar():
#     hamar_list = 'QWERTYUIOPASDFGHJKLZXCVBNM'
#     my_dict = {}
#     count = 0
#     krknvox = 0
#     print('Loading...')
#     while True:
#         tiv1 =random.randint(0,9)
#         tiv2 = random.randint(0,9)
#         tar1 = random.choice(hamar_list)
#         tar2 = random.choice(hamar_list)
#         tiv3 = random.randint(0,9)
#         tiv4 = random.randint(0,9)
#         tiv5 = random.randint(0,9)
#         hamar = (str(tiv1) +str(tiv2) + tar1+tar2 + str(tiv3)+str(tiv4)+str(tiv5))
#         for i in my_dict:
#             if hamar in my_dict[i]:
#                 krknvox += 1 
#         my_dict[count] = hamar
#         count += 1
#         if tiv1 == 2 and tiv2 == 2 and  tiv3 == 1 and  tiv4 == 0 and tiv5 == 1 :#and tar1 == tar2:
#             print(f'{tiv1}{tiv2} {tar1}{tar2} {tiv3}{tiv4}{tiv5}')
#             print(count,krknvox)
#             break
        
# random_hamar()


# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# nums1[m:m+n] = nums2[:n]
# nums1.sort()
# print(nums1)

# def func(nums):
#     val = 3
#     while True:
#         if val in nums:
#             nums.remove(val)        
#         else:
#             print(nums)
#             break

    
# func([3,2,2,3])

# nums = [0,0,1,1,1,3,3,3,3,3,3,3,3,3,2,2,3,7,7,7,7,7,7,3,4]
# for i in nums[::-1]:
#     if nums.count(i) > 1:
#         nums.remove(i)
# print(nums)


# a = input('text: ')
# print(len(a.split(' ')[-1]))


# nums = [2,7,13,15,3,3,3,3,3,3,4]
# target = 18
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] + nums[j] == target:
#             print(i,j)
#             break


# strs = ['flower','flow','flight']
# strs.sort(key=len)
# count = 1
# while count < len(strs):
#     if strs[0] == strs[count][:len(strs[0])]:
#         count += 1
#     else:
#         strs[0] = strs[0][:-1]

# print(strs[0])