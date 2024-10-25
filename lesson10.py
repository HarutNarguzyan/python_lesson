#----------------110---------------------------
# arr = []
# while True:
#     user_input = int(input("greq tiv: "))
#     if user_input == 0:
#         break
#     else:
#         arr.append(user_input)
# arr.sort()
# # print(arr)
# for i in arr:
#     print(i)
#------------------111--------------------
# arr = []
# while True:
#     user_input = int(input("greq tiv: "))
#     if user_input == 0:
#         break
#     else:
#         arr.append(user_input)
# arr.sort(reverse=True)
# print(arr)
#-------------------113----------------------
# arr = []
# while True:
#     user_input = input("greq bar: ")
#     if user_input == "":
#         break
#     elif arr.count(user_input) == 0: 
#         arr.append(user_input)

# # print(arr)
# # --------------------114--------------
# bacasakan = 0
# zro = 0
# drakan = 0
# arr = []
# while True:
#     user_input = input("greq tver: ")
#     if user_input == "":
#         break
#     elif int(user_input) < 0:
#         arr.insert(bacasakan,user_input)
#         bacasakan += 1
#     elif int(user_input) == 0:
#         arr.insert(bacasakan+zro,user_input)
#         zro += 1
#     else:
#         arr.insert(bacasakan+zro+drakan,user_input)
#         drakan += 1
# print(arr)
#-----------------116-----------------------------

# for j in range(1,1000000):
#     count = 0

#     for i in range(1,int(j//2+1)):
#         if j % i == 0:
#             count += i
#     if count == j:
#         print(j)
#-----------------117-------------------------
# count = 0
# alist = []
# text = input("greq text: ")
# for i in text:
#     if i == " ":
#         a = text.index(i)
#         alist.append(text[count:a])
#         count += a
# print(alist)
# ??????????????
# -----------------------------------
# arr = []
# count = 0
# count1 = 0
# while True:
#     tiv = input("greq tiv: ")
#     if tiv == "":
#         break
#     else:
#         arr.append(tiv)
#         count += 1
#         count1 += int(tiv)
# mijin = count1 / count
# for i in arr:
#     if int(i) < mijin:
#         print(i,"poqr mijinic",end="")
#     elif int(i) == mijin:
#         print(i,"mijin",end="")
#     else:
#         print(i,"mec mijinic",end="")
#--------------------------------------------
# arr = []
# while True:
#     user_input = input("Greq barer: ")
#     if user_input == "":
#         break
#     else:
#         arr.append(user_input)
# for i in arr:
#     if arr(i) == arr[-2]:
#         ("u", i,)
#     else:
#         print(i,",",end="")
