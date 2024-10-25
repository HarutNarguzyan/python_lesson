# user_input = int(input("greq tiv: "))
# for i in range(user_input+1):
#     print(i**3)
#------------------------------------------
# user_name = input("greq partqatiroj anuny: ")
# partq = int(input("greq partqy: "))
# a = partq
# while True:
#     if partq != 0:
#         hanum = int(input(f"dzer partqy {partq},inchqan eq uzum hanel partqic: "))
#         partq -= hanum
#     else:
#         print("duq pakel eq partqy,shnorhakalutyun")
#         break
#------------------------------------------------------------------------------
# user_input = input("greq tiv: ")
# print(len(user_input))

# count = 0
# user_input = input("greq tiv: ")
# for i in user_input:
#     count += 1
# print(count)
#-------------------------------------------------------
# bacasakan = 0
# drakan = 0
# while True:
#     user_input = int(input("greq dzer gnahatakany: "))
#     if -100 <user_input < 100:
        
#         if user_input == 0:
#             break
#         elif user_input<0:
#             bacasakan +=1
#         else:
#             drakan+=1
#     else:
#         print("greq -100:100 mijakayqum")
# print(f"{drakan}drakan\n{bacasakan}bacasakan")

#---------------------------------------------------------------------------


# jam = -1
# zadaniya=0
# knoj_zang=0
# while True:
#     jam+=1
#     maksim=int(input(f"jam{jam})\n vercnel zangy(1) te che(0):   "))
#     if jam >= 8:
#         print(f"duq avarteciq ory ev areciq {zadaniya}arajadranq ev {knoj_zang}zang")
#         break
#     else:
#         if maksim == 1:
#             knoj_zang += 1
#             print(f"jam{jam})\n duq verceciq zangy gnaceq xanut))\n{knoj_zang} zang, {zadaniya} arajadranq")
#         else:
#             zadaniya += 1
#             print(f"jam{jam})\n duq cheq vercrel zangy:)\n{zadaniya} arajadranq, {knoj_zang}zang")
    
#-------------------------------------------------------------------------------
# import math
# count = 0
# tiv = int(input("greq hasvi gumary: "))
# tokos = int(input("Greq tokosy: "))
# tari = int(input("greq tarinery: "))
# while True:
#     tiv =tiv + tiv * tokos / 100
#     count +=1
#     if count == tari:
#         break
# print(round(tiv))
#---------------------------------------------------------------
# import random
# count = 1
# tiv = random.randint(0,10)
# while True:
#     user_input = int(input("greq dzer tivy: "))
#     if user_input == tiv:
#         print(f"shnorhavorum em,duq gushakeciq {count} angamic:")
#         break
#     else:
#         if tiv > user_input:
#             print("dzer tivy poqr e")
#         else:
#             print("dzer tivy mec e")
#         count +=1
#--------------------------------------------------------------------
# c = 0
# a = 0
# b = 100
# User_input = int(input("greq dzer tivy(1,100): "))
# if 0<User_input <101:
#     a = (a+b)//2
#     print(a)
#     while True:
#         patasxan = int(input("havasar(1),mec(2),poqr(3): "))
#         if patasxan == 1:
#             print("chisht")
#             break
#         elif patasxan == 2:
#             a = (a+b)//2
#             print(a)
#             if patasxan == 1:
#                 print("gushakecir")
#         elif patasxan == 3:
#             a = (a+c)//2
#             print(a)
#             if patasxan == 1:
#                 print("gushakecir") ?????
#------------GIRQ.63------------------------
# count = 0
# count1 = 0
# while True:
#     user_input = int(input("greq tiv: "))
#     if user_input == 0 and count ==0:
#         print("araji tivy chi karox linel 0:")
#     elif user_input != 0:
#         count += user_input
#         count1 += 1
#     elif user_input == 0:
#         print(f"{count / count1}")
#         break
#-----------------GIRQ.69--------------------------
# count = 0
# while True:
#     user_input = int(input('greq tariqy: '))
#     if 0 <= user_input < 101:
#         if user_input == 0:
#             break
#         elif user_input <= 2:
#             count += 0
#         elif 2 < user_input <= 12:
#             count += 14
#         elif 12 < user_input <= 65:
#             count += 23
#         else:
#             count += 18
# print(f"yndhanur arjeqy {count}")

#-------------------GIRQ.75-----------------------
# user_input = input("greq bary: ")
# if user_input == user_input[:: -1]:
#     print("chisht")
# else:
#     print("sxal")
#-------------------GIRQ.84------------------
# import random
# for i in range(10):
#     xush = 0
#     gir = 0
#     count = 0
#     b = "xush" , "gir"
#     while True:
#         a = random.randint(0,1)
#         print(b[a], end=" ")
#         count += 1
#         if a == 0:
#             xush +=1
#             gir = 0
#         else:
#             gir += 1
#             xush = 0
#         if xush == 3 or gir == 3:
#             break
#     print(f"\navart,{count} angamic")
#-----------------------GIRQ------------------
# count = 0
# User_input = input("greq tivy: ")
# a = len(User_input) 
# for i in User_input:
#     b = int(i) * (2 ** (a -1))
#     a-=1
#     count += b
# print(count)      
# ---------------------GIRQ---------------------------
# user_input = int(input("greq tiv: "))
# while True:
#     a = user_input // 2
#     b = user_input % 2
#     user_input = a
# print(b)
#     break
#--------------------------------------------
# sharq = int(input("greq sharqeri qanaky: "))
# laynutyun = int(input("greq laynutyuny: "))
# bac = int(input("greq bac toxnvac texeri qanaky: "))
# for i in range(sharq):
#     print(laynutyun*"="+bac*"*"+laynutyun*"=")
# #------------------------------------------------
# count = 0
# mijakayq = int(input("greq mijakayq: "))
# for tiv in range(2,mijakayq+1):
#     for i in range(2,int(tiv**0.5)+1):
#         if tiv % i == 0:
#             break
#     else:
#         count += 1
# print(count)
#----------------------------------------
# user_input = int(input("greq baredzrutyuny: "))
# for i in range(user_input):
#     print("*")


# count = 0 
# count1 = 0
# while True:
#     a = int(input('enter number:  '))
#     if a==0:
#         break
#     elif a!=0:
#         count+=a
#         count1 += 1
# print(count / count1)
