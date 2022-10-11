import calendar

import random
import re


calendar.prmonth(2022,10)
print(random.random()*11+1)


#정규식
reg =re.compile("[0-9]{2,5}")
id = "2ㅇㅇㅇㅇ445"
id = "ㅇ2445ㅇ"
print(reg.match(id))
print(reg.search(id))


st = """
돈돈돈다다다발발"""
reg = re.compile("돈")
print(len(reg,re.findall(st)))




