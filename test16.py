# 머신러닝 딥러닝 텐서플로(12/14 python)

##파이썬 = 절차지향  / 자바 = 객체지향 
# type 
# int, str , list , set , tuple, dict
# a =1  int
# a = "stt" str
# a = [] list
# a = {} set
# a = () tuple
#  a = {key:value} dict

#  동적 타이핑 
#  장정: 타입을 지정 안해도 가능
#  단점: 오류 발생 가능 


# 스크립트 언어  
# 소스 코드를 한 줄로 읽어서 곧 바로 실행
# eg. ZIP파일 풀지않고 바로 실행 가능 


# 플랫폼 독립적 : os 상관없다 (window, mac, linux)

##제어문 
# if elif else
# match - case

##반복문 
# for in:
# while :
# break continue
# 람다lambda (map, reduce, filter)

## lambda eg.
# from functools import reduce
# from unicodedata import name


# list1 = [9,1,2,4,3]
# def sum (x,y):
#     print(f"{x} {y}") # f = format
#     return x+y
# a = reduce(lambda x,y: sum(x,y), list1)

# user = {"id":"id","pass":"pass","name":""}
# names = ["kim", "lee", "park","kim", "lee", "park"]
# namelist = list(map(lambda x : {"id":"id","pass":"pass","name":x,"age":30}))
# print(namelist)


# findUser = list(filter(lambda x : x.get("name") == "park", namelist))
# print(findUser)
# avaAge = reduce(lambda x,y: x+y.get("age"),namelist,0)
# print(avaAge/len(namelist))





## 함수
# def :
# def sum(a,b): a,b
#    return a+b
# sum(1,2)) 1,2 인수

# def sum(*a): *a tuple
# sum (1,2,3,4)
# def sum(**a) : **a dict
# sum(name= kim, age = 56)

# name = "kim" 전역 변수
# def printName(name):
#   name = "lee" 지역 변수

## 파일 입출력
#  f = open(파일, mode,)
# endcoring = UTF-8

# 입력 받고 싶을때: input

## Class 
# 중복되는 것을 한번에 처리하려 씀
# 객체지향 
# class name(상속):
#   def __init__:
#  상속 접근 할때 super()
#   def__init__(self):

## import-현재 파일 외 다른곳에서 불러올 떄 

## 정규식 개념 search match
#  bae@gmail.com
#  이메일 형식이 맞음?
# import re

## import random


## 오늘 
# from date.time import date
# print(date.today())


#c:\test ->c:=test=test2
# 상대경로
# ./test2
# .. 상위 폴더 
# 절대경로
# c:\test\test2


# cd /
# test
# python (filename)




#  1. 자연수 뒤집어 배열로 만들기 
#  2. 제일 작은수  수 제거하기 
#  3. 두 정수 사이의 합 
#  4. 




# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.
# return = reversed 였던것 같음?
# len - 1
# 




# def solution(n):
#     n = [1,2,3,4,5]
#     reversed(n)
#     answer = ()
#     return n


# a = 123 #백이십삼
# a = '123'#일 이 삼

# def solution(n):
#     answer =list(str(n)) #분리
#     print(answer)
#     answer.reverse() # 역순 
#     print(answer)
#     answer = list(map(int,answer)) # int 재배치 
#     answer1=[]
#     for x in answer:
#         answer1.append(int(x))
#     print(answer)
#     print(answer1)
#     return answer
# print(solution(12345))



     
# a = '1234'
# a[0]='1'




# def solution(n):

#     n = str(n)[::-1] 
#     answer = list(map(int, n))
#     return answer






# # 2. 제일 작은수  수 제거하기 
# def solution(arr):
#     answer = []
#     if len(arr)==1:
#         return[-1]
#     #제일 작은수
#     minNumber = 1000000
#     for a in arr:
#         if a < minNumber:
#             minNumber = a
#     #제거하기
#     for a in arr:
#         if minNumber != a:
#             answer.append(a)
#     return answer
# print(solution([10]))
# print(solution([4,3,2,1]))



#  3. 두 정수 사이의 합

# def solution(a, b):
#     answer = 0
#     if b>a:
#         list=list1(range(a,b+1))
#         answer =sum(list1) 
#     elif a>b:
#           list=list(range(a,b+1))
#         answer =sum(list1) 
#     else:1
#         answer = a
#     return answer
# print(solution(10,5))





##  4 정수 제곱근 판별
#  임의의 양의 정수 n에 대해, 
#  n이 어떤 양의 정수 x의 제곱인지 
#  아닌지 판단하려 합니다.
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고,
#  n이 양의 정수 x의 제곱이 아니라면 
#  -1을 리턴하는 함수를 완성하세요.


# def solution(n):
#     answer = 0
#     for i in range(1,n):
#         if i * i ==n:
#             answer =(i+1)*(i+1)
#             break
#         elif i * i > n: # 144> 123
#             break
#     if answer ==0:
#         return -1
#     return (answer+1)*(answer+1)
# print(solution(121))
# print(solution(3))


## 피보나치
# 피보나치 수는 F(0) = 0, 
# F(1) = 1일 때, 
# 1 이상의 n에 대하여 
# F(n) = F(n-1) + F(n-2) 
# 가 적용되는 수 입니다.
# 예를들어
# F(2) = F(0) + F(1) = 0 + 1 = 1
# F(3) = F(1) + F(2) = 1 + 1 = 2
# F(4) = F(2) + F(3) = 1 + 2 = 3
# F(5) = F(3) + F(4) = 2 + 3 = 5
# 와 같이 이어집니다.
# 2 이상의 n이 입력되었을 때, 
# n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수,
# solution을 완성해 주세요.

def solution(n:int):
    answer = 1 
    first = 0
    second = 1
    # answer = first + second
    # F(2) = F(0) + F(1) = 0 + 1 = 1
    for i in range(2,n+1): # 2<= i < 5+1
        tmp =second 
        answer = first + second # 0 + 1
        first = tmp
        second = answer
    return answer % 1234567
# def main()
print(solution(3))
print(solution(5))

# def arrAppend(arr:list):
#     arr.append()
# a =[]
# a.append

