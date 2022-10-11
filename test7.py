# #list = [1,2,3,4,5,6,2,3,5,1]
# #뭐는 짝수입니다.
# #뭐는 홀수입니다.


# list1 = [1,2,3,4,5,6,2,3,5,1]
# #for el in list1:
# #    if el % 2 == 0:
#  #       print(f"{el}은 짝수입니다")
#  #   elif el % 2 == 1:
#   #      print(f"{el}은 홀수입니다 ")


# # #i = 0
# # #while i <len(list1):
# #     #if list1[i] % 2 == 0:
# #         print("f{list1} 은 짝수입니다")
# #     elif list1[i] %2==1:
# #         print(i)
# #         continue
# #     i+=1
# #     #print(f"------{list[1]}----------")


# list1 = [1,2,3,4,5,6,2,3,5,1]
# for el in list1:
#     match el %2:
#         case 1:
#             print(f"{el} 은 홀수입니다")
#         case 0:
#             print(f"{el} 은 짝수입니다")
        
#         #if el %1 == 0:
#         #   print(f"{el} 은 홀수입니다")
#         #elif el % 2 == 1:
#             #print("f"{ei} 은 짝수입니다")

# #람다 3.6 
# #예제) list1 의 요소를 *2해서 찍어봐라 
# list1 = [1,2,3,4,5,6,2,3,5,1]
# list2 = []
# for el in list1:
#     list2.append(el * 2)
# print(list2)


# # list1 요소의 합 ?  int(수)
# list1 = [1,2,3,4,5,6,2,3,5,1]
# list2 = []
# list3 = []
# for el in range(0, len(list1)):
#     print (list2)



# # list1 요소의 합 ?  int(수)
# list1 = [1,2,3,4,5,6,2,3,5,1]
# sum = 0 
# for el in list1:
#     sum += el 
# print(sum)

# sum2 = reduce(lambda x,y: x+y el **2, list1)
# print(sum2)


# # map은 새로운 리스트를 만든다 (반환한다)
# list4 =list(map(lambda x: x*2, list1))
# #합께 구할때 사용                                                                                                                                                                                                                                                                   
# print(list4)


list1= [1,2,3,4,5,6,2,3,5,1]
# 4이상 것 만 리스트를 만들려고함 
list0 = []
# 리스트를 만들려고 하니깐 리스트를 선언
# for el in list1:
#     # print(el)
#     if el >= 4 :
#         list0.append(el)
# print(list0)

list01 = list(filter(lambda x: x, list1))
print(list01)








