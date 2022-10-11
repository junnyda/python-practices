# # 함수
# # #sum(a,b) -> return




# # # 파이선은 절차 지향 
# # # isPrimary = True cammel case
# # def sum(a,b):
# #     return a+b
# # print(sum(1,2)) # sum(1,2) => 1,2 => 인수
# # print(sum(3,5))

# # def sum1(*args):
# #     print(args)
# #     pppp = 0
# #     for arg in args:
# #         pppp+=arg
# #     return pppp
# # print(sum1(1,1,1,1,1,1,))
# # def printFunc(**kwargs):
# #     print(kwargs)
# # printFunc(a=1, b=1)


# # def makeHuman(name, age):
# #     return{"name":name, "age":age}
# # human1 = makeHuman("kim", 30)
# # human2 =makeHuman("park", 34)
# # print(human1)
# # print(human2)


# # def isPrimaryNumber(num):
# #     isPrimary = True
# #     for j in range(2,num):
# #         if num%j ==0:
# #                 isPrimary = False
# #                 break
# #     if isPrimary:
# #         return f"{num}은 소수입니다"
# #     else:
# #         return f"{num}은 소수가 아닙니다"
# # print(isPrimaryNumber(6))



# from msilib.schema import ODBCDataSource, ODBCDriver


# def sum1(*args):
#     print(args)
#     pppp = 0
#     for arg in args:
#         pppp+=arg
#     return pppp

# def isPrimaryNumber(*nums):
#     for num in nums:
#          isPrimary = True
#          for j in range(2, num):
#             if num%j ==0:
#                 isPrimary = False
#                 break
#          if isPrimary:
#             print(f"{num}은 소수입니다")
#          else:
#             print(f"{num}은 소수가 아닙니다")
# print(isPrimaryNumber(9,4,2,11,6))


# name = "park"
# name1 = "lee" # 전역변수
# def setName1(name): # name = 매개변수
#     print(f"2.{name}") # kim
#     # name1 = name
#     name = name # kim
#     pppp = name # 지역변수
#     pppp = "hi"

#     print(f"3.{name} {name1}") # 3. kim kee
# # print(f"1.name1 : {name1}") #1. name1: 
# # print(f"1.{name}") # pakr
# # setName1("kim") #인자갑
# # print(f"4.{name}") #park, 
# # print(f"2. name1 : {name1}") #2. name1:


# # # 코딩 테스트 (1. 백준 2.프로그래머스)

# # def solution(num) :
# #     answer = ''
# #     return answer
    

# # print(solution(3)) #odd
# # print(solution(4)) # even


# # def solution(num):
# #     answer = ''
# #     if (num % 2) == 0:
# #         answer = "Even"
# #     else:
# #          answer = "Odd"
# #          return answer


# # def sum(a,b):
# #     if a == "짝수":
# #         return #return 한순간 끝 
# #     print("sum after")
# #     for i in range(0,9):
# #         print(i)
# # a = input("입력하세요")
# # b= input("입력하세요")
# # print(sum(a,b))

# # 형변환 

# # def sum(a,b):
# #      try:
# #         if type(a) == int and type(b) == int:
# #             return a + b
# #         else:
# #             return int(a) + int(b)
# #      except:
# #         return f"{a}랑 {b} 중 숫자가 아닌게 있습니다.#
        
# #         print(sum(a,b))
# # while True:
# #     a = input("입력하세요")
# #     if a =="end":
# #         break
# #     b = input("입력하세요")
# #       if a =="end":
# #         break
# #     print(sum(a,b))



# from ast import Num
# from itertools import count


# for i in range(0, 10):
#      a = input("입력하세요")
#      if a =="end":
#         break
#     b = input("입력하세요")
#     if b =="end":
#         break
#     print(sum(a,b))



# # 369  게임 
# # 들어온 숫자  에 3,6,9,가 
# # 짝
# # 계속 지속되어야함 
# # 369369 현재 {i}
# # 입력 다음 할 것 

# #input whiel for 

# n = int(input())
# for i in range(1, n+1):

# n = int(input())
# for i in range(1, n+1):




# for i in range (1, n+1):
#     num = str(i)

#     count = 0 #369
#     count += num.count('3') 
#     count += num.count('6') 
#     count += num.count('9')
    
#     if count == "end":
#         print( num,"end")




   
#     else






# n = int(input())

# for i in range(1, n + 1):
#     num = str(i) 
#     count = 0
#     count += num.count('3')
#     count += num.count('6')
#     count += num.count('9') 
#     if count == 0: 
#         print(num, end = ' ') 
#     else:         
#         print(count * '_', end = ' ')


       

        







    # a = input("clap")
    # if a =="end":
    #     break
    # print(sum(a,b))





# def sum(a,b):
#      try:
#         if type(a) == int and type(b) == int:
#             return a + b
#         else:
#             return int(a) + int(b)
#      except:
#         return f"{a}랑 {b} 중 숫자가 아닌게 있습니다.#
        
#         print(sum(a,b))
# while True:
#     a = input("입력하세요")
#     if a =="end":
#         break
#     b = input("입력하세요")
#       if a =="end":
#         break
#     print(sum(a,b))
