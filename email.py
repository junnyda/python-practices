# from random import random
# import re


# reg =re.compile("([A-za-z0-9]+@[A-za-z0-9]+\.[a-za-z]{2,3})")
# print(reg.match("junnyda1004@gmail.com"))

#  check 정규식 


# quiz 
# lotte 1~45 중복 없이 6자리 
# random for
# 5개
# print(random.random()*11+1)


from lib2to3.pgen2.token import NUMBER
import numbers
import random

# random.randrange(0,6)



lotto = []
# for i in range(0,6):
#     num =random.random()*45+1
#     print(int(num))
lotto = []
while len (numbers)<6:
    num = int(random.random()*45+1)
    tmpNumber = numbers.copy()
    tmpNumber.append(num)
    setNumbers =set(tmpNumber.copy())
    if len(setNumbers) == len(tmpNumber):
        numbers.append(num)
    else:
        print(num)
        print(tmpNumber)
    lotto.append(numbers)
for text in lotto:
    print(numbers)



# reg =re.compile("[0-9]{2,5}")
# id = "2ㅇㅇㅇㅇ445"
# id = "ㅇ2445ㅇ"
# print(reg.match(id))
# print(reg.search(id))
