# -------------46------------------------
# kent_tar = 'aceg'
# zuyg_tar = 'bdfh'

# user_tar = input("greq tar: ")
# user_tiv = int(input("greq tiv: "))
# if user_tar in kent_tar and user_tiv % 2 == 0:
#     print("spitak")
# else:
#     print("sev")
# ----------------59--------------
# amisner = ['hunvar','petrvar','mart','april','mayis','hunis','hulis','ogostos','september','hoktember','noyember','dektember']
# amisner_30 = ['april','hunis','september','noyember']
# amisner_31 = ['hunvar','mart','mayis','hulis','ogostos','hoktember','dektember']
# while True:
#     user_year = int(input("taretiv: "))
#     user_amis = input("amis: ").lower()
#     user_amsativ = int(input("amsativ: "))
#     if user_amis in amisner_30 and user_amsativ > 30 or user_amis in amisner_31 and user_amsativ > 31:
#         print('out of range')
#     else:
#         if user_year % 4 == 0 and user_amis == 'petrvar':
#             if user_amsativ > 29:
#                 print("sxal")
#             elif user_amsativ == 29:
#                 print(user_year,'mart',1)
#                 break
        
#         elif user_amis == 'petrvar' and user_amsativ == 28:
#             print(print(user_year,'mart',1))
#             break
#         elif user_amsativ < 29 and user_amis == 'petrvar':
#             print(user_year,user_amis,user_amsativ+1)
#             break
#         elif user_amis == amisner[-1] and user_amsativ == 31:
#             print(user_year+1,'hunvar',1) 
#             break
#         elif (user_amis in amisner_30 and user_amsativ == 30) or (user_amis in amisner_31 and user_amsativ == 31):
#             print(user_year,amisner[amisner.index(user_amis)+1],1)
#             break
#         else:
#             print(user_year,user_amis,user_amsativ+1)
#             break
# ---------------62------------------
# import random
# while True:
#     guyn = random.choice(["sev","karmir"])
#     tiv = random.randint(0,37)

#     if tiv % 2 == 0:
#         zuyg = 'ha'
#     elif tiv == 37:
#         tiv = "00"
#     else:
#         zuyg = 'che'
#     if tiv == 0 or tiv == "00":
#         print(f'yngela {tiv}\nhaxtuma {tiv}')
#         break
#     elif tiv <= 18 and guyn == 'sev' and zuyg == 'ha':
#         print(f'yngela {tiv}\nhaxtuma {tiv}\nhaxtuma 1-18\nhaxtuma sev\nhaxtuma zuyg')
#         break
#     elif tiv <= 18 and guyn == "karmir" and zuyg == 'ha':
#         print(f'yngela {tiv}\nhaxtuma {tiv}\nhaxtuma 1-18\nhaxtuma karmir\nhaxtuma zuyg')
#         break
#     elif tiv <= 18 and guyn == 'sev' and zuyg == 'che':
#         print(f'yngela {tiv}\nhaxtuma {tiv}\nhaxtuma 1-18\nhaxtuma sev\nhaxtuma kent')
#         break
#     elif tiv <= 18 and guyn == 'karmir' and zuyg == 'che':
#         print(f'yngela {tiv}\nhaxtuma {tiv}\nhaxtuma 1-18\nhaxtuma karmir\nhaxtuma kent')
#         break
#     elif tiv > 18 and guyn == 'sev' and zuyg == 'ha':
#         print(f'yngela {tiv}\nhaxtuma {tiv}\nhaxtuma 19-36\nhaxtuma sev\nhaxtuma zuyg')
#         break
#     elif tiv > 18 and guyn == 'karmir' and zuyg == 'ha':
#         print(f'yngela {tiv}\nhaxtuma {tiv}\nhaxtuma 19-36\nhaxtuma karmir\nhaxtuma zuyg')
#         break
#     elif tiv > 18 and guyn == 'sev' and zuyg == 'che':
#         print(f'yngela {tiv}\nhaxtuma {tiv}\nhaxtuma 19-36\nhaxtuma sev\nhaxtuma kent')
#         break
#     elif tiv > 18 and guyn == 'karmir' and zuyg == 'che':
#         print(f'yngela {tiv}\nhaxtuma {tiv}\nhaxtuma 19-36\nhaxtuma sev\nhaxtuma kent')
#         break
# ------------------------63---------------------------
# gumar = 0
# qanak = 0
# while True:
#     tiv = int(input("greq tiv "))
#     if tiv == 0 and qanak == 0:
#         print('arajiny chi karox linel 0')
#     elif tiv == 0:
#         print(gumar/qanak)
#         break
#     else:
#         gumar += tiv
#         qanak += 1
# ----------------69------------------------
# gumar = 0
# 3-12/14
# 65-100/18
# 13-64/23
# while True:
#     tariq = input("greq tariqy: ")
#     if tariq == "":
#         break
#     else:
#         if int(tariq) > 100:
#             print("merelneri muitqy argelvume:")
#         if 12 > int(tariq) > 3:
#             gumar += 14
#         elif 64 > int(tariq) > 13:
#             gumar += 23
#         elif int(tariq) > 65:
#             gumar += 18
# print(gumar)
#----------------------77------------
# for i in range(1,11):
#     for j in range(1,11):
#         print(i,end="")
#     print()??????
# ---------------------------------
# import datetime
# date = datetime.datetime(2008, 5 , 26)

# day = date.strftime('%A')

# print(day)
#------------------------83---------
# import random
# maks = 0
# for i in range(100):
#     tiv = random.randint(1,100)
#     if tiv > maks:
#         maks = tiv
#         print(tiv,"poxvec")
#     else:
#         print(tiv)
# -----------------------84--------------
# import random
# xush = 0
# gir = 0
# while True:
#     a = random.choice(["xush","gir"])
#     print(a,end=" ")
#     if xush == 3 or gir == 3:
#         break
#     else:
#         if a == "xush":
#             xush += 1
#             gir = 0
#         else:
#             gir += 1
#             xush = 0
# -------------------------------------------
# a = [3,4,1,2,4,4,1]
# count = 0
# while True:

# import pygame
# import sys
# import random
# import math

# WIDTH, HEIGHT = 800, 600
# FPS = 60

# pygame.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Красивые анимации")
# clock = pygame.time.Clock()

# def random_color():
#     return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# circles = []
# for _ in range(10):
#     radius = random.randint(20, 60)
#     x = random.randint(radius, WIDTH - radius)
#     y = random.randint(radius, HEIGHT - radius)
#     speed_x = random.choice([-1, 1]) * random.uniform(1, 3)
#     speed_y = random.choice([-1, 1]) * random.uniform(1, 3)
#     circles.append({'pos': [x, y], 'radius': radius, 'speed': [speed_x, speed_y], 'color': random_color()})

# def main():
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#         screen.fill((0, 0, 0))

#         for circle in circles:
#             circle['pos'][1] += circle['speed'][1]
#             circle['pos'][1] += circle['speed'][1]

#             if circle['pos'][0] - circle['radius'] < 0 or circle['pos'][0] + circle['radius'] > WIDTH:
#                 circle['speed'][0] = -circle['speed'][0]
#             if circle['pos'][1] - circle['radius'] < 0 or circle['pos'][1] + circle['radius'] > HEIGHT:
#                 circle['speed'][1] = -circle['speed'][1]

#             circle['radius'] = 30 + 20 * math.sin(pygame.time.get_ticks() / 500 + circle['pos'][0] / 100)

#             pygame.draw.circle(screen, circle['color'], (int(circle['pos'][0]), int(circle['pos'][1])), int(circle['radius']))

#         pygame.display.flip()
#         clock.tick(FPS)

# if __name__ == "__main__":
#     main()





# list_=[1,6,7,9,10,20,21,22,23,24,25,26,27,28,29,35,46,54,68,79,82,93,106,222,345,465,565,654,754,845,965,1000]
# n=465
# poqr=0
# mec=len(list_)
# mijin = (mec + poqr) //2
# count = 0
# print(list_.index(n))
# while True:
#     if list_.index(n) + 1>mijin:
#         mijin = (mec+mijin) // 2
#         count +=1
#     elif list_.index(n) +1 < mijin:
#         mijin =  (mijin + poqr) //2
#         count +=1
#         print('aaa')
#     else:
        
#         print(count)
#         break








# num=[2,5,3,7,4,8]
# x = 8
# for i in range(0 , len(num)-1):
#     if num[i] + num[i+1] == x:
#         print(i,i+1)






# user_input = input('greq tiv: ')
# print(user_input==user_input[::-1])



# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
# summ = 0 
# user_input = input("text: ")
# for i in user_input: 
#     if i == 'I':
#         summ += 1
#     elif i == 'V':
#         summ += 5
#     elif i == 'X':
#         summ += 10
#     elif i == 'L':
#         summ += 50
#     elif i == 'C':
#         summ += 100
#     elif i == 'D':
#         summ += 500
#     elif i == 'M':
#         summ += 1000 
# print(summ)



# nums = [0,1,2,2,3,0,4,2]
# tiv = 2
# new_list = [] 
# summ = 0
# for i in nums:
#     if i != tiv:
#         new_list.insert(0,i)
#         summ += 1
#     else:
#         i = '_'
#         new_list.append(i)
# print(summ,new_list)
     
        
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# for i in nums1[::-1]:
#     if i == 0:
#         nums1.remove(0)
# nums1.extend(nums2)
# nums1.sort()
# print(nums1)


# nums = [2,2,1,1,1,2,2]
# for i in nums:
#     if nums.count(i) >= len(nums) / 2:
#         print(i)
#         break
#     else:
#         print('chka')
#         break


# n = int(input())
# s = []
# for i in range(n):
#     s.append(input().lower())
# s = sorted(s)
# print(s)
# for i in s:
#     anagrams = []
#     for j in s:
#         if sorted(list(i)) == sorted(list(j)):
#             anagrams.append(j)
#     if len(anagrams) > 1:
#         print(*anagrams)
#         for j in anagrams:
#             del s[s.index(j)]


    






# def gumar(a,b):
#     return a + b
# def hanum(a,b):
#     return a - b

# def bazmapatkum(a,b):
#     return a * b

# def bajanum(a,b):
#     return a / b


# print(f'gumar {gumar(5,7)},hanum {hanum(5,7)}, bazmapatkum {bazmapatkum(5,7)}, bajanum {bajanum(5,7)}')

# def jumong():
#     tar = 0
#     tiv = 0
#     nshan = 0
#     a = input("Gra text usta: ")
#     for i in a:
#         if i.isdigit():
#             tiv += 1
#         elif i.isalpha():
#             tar += 1
#         else:
#             nshan += 1
#     return f'Tveri qanak {tiv} Tareri qanak {tar} Nshanneri qanak {nshan}'

# print(jumong())


# def parz(number):
#     for i in range(2,int(number**0.5)+1,2):
#         if number % i == 0:
#             return True
#     else:
#         return False        

# def next_prime(number):
#     number += 1
#     while True:
#         if parz(number) == True:
#             return number
#         else:
#             number += 1

# print(next_prime(20))




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


a = {
    1:'a',
    2:'b'
}
for i in a:
    if 'a' in a[i]:
        print(True)