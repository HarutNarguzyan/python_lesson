# count = 0
# arr = [4,6,5,7,8,9,8,8,8,4,5,2]
# for i in arr:
#     count += i
# print(count)
# -------------------------------------
# count = 1
# arr = [4,5,2,6]
# for i in arr:
#     count *= i
# print(count)
# -------------------------------------
# a = ""
# arr = ["Harut", "Ero", "Sergo", "Artavazd"]
# for i in arr:
#     erk = len(i)
#     if erk > len(a):
#         a = i
# print(a)
# arr.sort(key=len)
# print(arr[-1])
# ---------------------------------------
# arr1 = ["a", "b", "c"]
# arr2 = ["g", "t", "a"]
# for i in arr1:
#     for j in arr2:
#         if i == j:
#             print(True)
#             break
#     else:
#         print("chka")???????????
# --------------------------------------------
# arr = ["anun","azganun","hayranun",5,7,8]
# ----------------------------------------------
# arr = ["hp","asus","del","mac","lenovo"]
# if "mac" in arr:
#     print("ka")
# else:
#     print("chka")
# ------------------------------------------
# count1 = 0
# count2 = 0
# nshanner = ["$","&","*","%","#"]
# password = input("greq gaxtnabary: ")
# for i in nshanner:
#     for j in password:
#         if i == j:
#             count1 += 1
#     # if i in password:
#     #     count1 += 1
# for j in password:
#     if j.isdigit():
#         count2 += 1
# if len(password) >= 8 and count1 >= 2 and count2 >= 2:
#     print("ujex")
# else:
#     print("tuyl")
# --------------------------------------------------
# user_input = input('greq linky: ')
# if "=" in user_input:
#     a = user_input.index("=")
#     print(user_input[a+1:])
# else:
#     print(":)")
# --------------------------------------------------
# user_input = input("greq bary: ")
# if user_input == user_input[::-1]:
#     print("Open")
# else:
#     print("Trash")
# ----------------------------------------------
# a = "barev"
# b= list(a)
# print(b)
# --------------------------------
# arr = [12,9,15,8,75,45,14]
# for i in arr:
#     if i % 2 ==0:
#         print(f"{i}zuyg",end=" ")
# --------------------------------------
# name = input("greq dzer anuny: ")
# anunner = ["Harut","Ero","Arman","Sergo"]
# while True:
#     if len(anunner) == 1 and name in anunner:
#         print("mnaciq menak duq:")
#         break
#     elif len(anunner) == 0:
#         print("mard chmnac:)")
#         break
#     else:
#         print(anunner)
#         user_input = input("um eq yntrum: ")
#         if user_input != name:
#             if user_input in anunner:
#                 anunner.remove(user_input)
#         else:
#             print("duq dzez cheq karox yntrel")
# -----------------------------------------------------

        
