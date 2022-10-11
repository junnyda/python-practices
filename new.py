
#2부터 30까지 소수 리스트 뽑아내기

    

# for i in range(2,10) :
#     for num in range(1,10):
#         print(f"{i} * {num} = {num*i}")


# ***


# text = "*"
# for i in range(1,7):
#     st =""
#     for j in range(1, i):
#         st = text*j
#     print(st)



# def GetPrimeNoOpt(n):
#     res = []
#     for i in range(2, 30):
#         is_prime = True
#         for j in range(2, 30):
#             if i % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             res.append(i)
#     return res

# def is_prime
# for i in range(2,30):
#     if is_Prime(i) ==True
#         a.append(i)
# print(a)






# n = 2
# res = []
# while n <= 31:
#   cnt = 0
#   for i in range(2, 30) :
#     if n % i == 0:
#       cnt += 1
#       if cnt > 1 : break
#   if cnt == 1 : print(n)
#   n += 1

# answer = []
# for i in range(2,31):
#     isPrimary = True
#     for j in range(2,i):
#         if i%j ==0:
#             isPrimary = False
#             break
#     if isPrimary:
#         answer.append(i)

# print(answer)






n = int()
for i in range (1, n+1):
    num = str(i)

    count = 0 #369
    count += num.count('3') 
    count += num.count('6') 
    count += num.count('9')
    
    if count == "end":
        print( num,"end")








