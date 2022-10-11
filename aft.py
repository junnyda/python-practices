# 제어문
from os import cpu_count
from webbrowser import get


a = 2
b = 5
if a > b :
    print(f"{a}는{b}보다 크다")
    print("2")
    print("3")
elif a < b:
    print(f"{a}는{b}보다 작다")
else: #위 조건이 다 아니면 마지막
    print("else")




x = {"company":"카카오"}
if x.get("company") == "카카오" :
    print("대기업 직원이시네요")
elif x.get("company") == "네이버":
    print("대기업 직원이시네요")
else:
    print("중견기업 직원이시네요")



match x.get("company") :
    case "카카오":
        print("대기업 직원이시네요")
    case "네이버":
        print("대기업 직원이시네요")
    case _:
        print("대기업 직원이시네요")
    

    # phone = {"name":"갤럭시", "version": "플립"}
    # phone 이 애플이면 와우 
    # 갤럭시면 version을 보고 
    # 플립이면 접히네요
    # 아니면 좋네요



phone = {"name":"갤럭시", "version" : "플립"}
if x.phone("name") == "아이폰":
    print("와우")
elif x.phone("phone") =="갤럭시":
    if phone.get("version") =="플립":
     print("version을 보고)"

else:
    print(와우)


phone = {"name":"갤럭시", "version" : "플립"}
if x phone("name") == "갤럭시":
    print("v")
    
elif x.phone()