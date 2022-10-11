

x = {"company":"네이버","isPartTime": True}
if x.get("company") == "카카오" :
    if x.get("isPartTime"):
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

