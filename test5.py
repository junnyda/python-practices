# 제어문 
a = 10
b = 5
# print(f"a>b{a>b} = True 크다 false 작다 ")


str1 = ""
if a > b: # 조건이 True면 아래 문장을 실행한다 
    print(f"a > b 크다")
elif a < b: #   elif 위의 조건이 아니면(False)이걸 실행 
    print(f"a>b 작다")
else: # else if도 flase elif fasle 다 아니면 실행 
    print("a = b 같다")

c = [1,2,3,4,5]
if len(c) > 3:
    print(c[3])
    print(c[0])
if len(c) > 2:
    print(c[0])



