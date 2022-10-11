#  회원 가입 
# 비밀번호 특수문자. 영어 대문자
# AI 
# 자연어 처리 예시) 나는 기분이좋다(감정 처리)


import re
from tokenize import Number

reg =re.compile("[0,9]{3}-[0,9]{3,4}-[0,9]{4}")
phone_number = "010-2222-3333"
print(reg.match(phone_number))


                 