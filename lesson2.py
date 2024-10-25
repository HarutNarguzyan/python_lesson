# a = -1
# b = 10
# for i in range(0,6):
#     a +=1
#     if a % 2 ==0:
#         b +=2
#     for j in range(a,b,2):
#         print(f"{j:>3}", end="")
#     print()

# tox = 6 
# syun = 6
# for i in range(syun):
#     for j in range(tox):
#         print(i + 2 * j,end='\t')
#     print()
# --------------------------------------------
# for i in range(1,6):
#     for j in range(1,6):
#         if j <= i:
#             print(j,end=" ")
#     print()
#---------------------------------------------
# count = 0
# lenutyun = int(input("greq lenutyuny: "))
# bardzrutyun = int(input("greq bardrutyuny: "))

# for i in range(bardzrutyun):
#     print("|",end="")
#     for j in range(lenutyun):
#         if count == 1:

#             print("-")
#         print("-")
#         count += 1


# erkarutyun="-"
# bardzrutyun="|"
# len=int(input("laynutyun"))
# erk=int(input("erkarutyun"))
# for i in range(len):
#     for j in range(erk):  
#         print(i+j)
# count = 0

# len=int(input("gri Len "))
# bardzr=int(input("gri bzrdzr "))
# for i in range(len):
#     for j in range(bardzr):
#         count+=1
#         if count == 1 or count == bardzr:
#             print("|"+bardzr*"-"+"|")
#         else:
#             print("|"+bardzr*" "+"|")
#             # print("|"+bardzr*"-"+"|")
#             break??????????????????????????
# #------------------------------------------
# tver = int(input("Greq dzer tivy: "))
# for i in range(2,tver // 2+1):
#     if tver % i == 0:
#         print("Dzer tivy parz che")
#         break
#     else:
#         print("dezer tivy parz e")
#         break
#-----------------------------------------------
# tiv = int(input("greq tiv: "))
# b = 0
# for i in range(1,tiv+1):
#     a = 1
#     for j in range(1, i + 1 ):
#         a = a * j
#     b+=a
# print(b)
#-----------------------------------------
# tver = input("greq tver: ")
# a = tver.split()
# b = 0
# for i in a:
#     if i >= b:
#         b = i
#     else:
#         continue??????????????????????
#--------------------------------------------

# count = 0
# number_count = int(input("greq tiv: "))
# for _ in range(number_count):
#     number = int(input("greq tver: "))
#     a = 0
#     for i in str(number+1):
#         a += int(i)
        
#     if a > count:
#         count = int(a)
# print(a)???
#------------------------------------------------
# count = 0
# while True:
#     user_input = int(input("greq dzer tariqe: "))
#     if user_input == 0:
#         break
#     elif user_input <=2:
#         count += 0
#     elif 12 >= user_input >= 3:
#         count += 14
#     elif 65 >= user_input >= 12:
#         count += 23
#     elif user_input >65:
#         count += 18


# print(count)
#---------------------------------







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
#     print(True)
# else:
#     print(False)
#-------------------GIRQ.84------------------
# import random
# count = 0
# b = "xush" , "gir"
# while True:
#     a = random.randint(0,1)
#     print(b[a], end=" ")
#     count += 1
    # if   :
        # break ?????????????????????
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
#     print(b)
#     break