
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

while len(numbers)<6:
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
