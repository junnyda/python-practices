
# def gama(cur, myInput):
#     answer=str(cur)
#     for c in str(cur):
#         if c =="3" or c =="6" or c=="9":
#             answer ="c"
#     if myInput == answer:
#         print("맞았다")
#         return True
#     else:
#         print("game over")
#         return False
# i = 0 
# while True:
#     i += 1
#     myInput =input(f"현재 값 {i}")
#     isWin = gama(i+1,myInput)
#     if(not isWin):
#         break



# def solution(phone_number):
#     answer ='***********4444'
#     for i in range (0,len(phone_number)):
#         if i <len(phone_number)-4:
#             answer += "*"
#         else:
#             answer += phone_number[i]
#     return answer
# phone_number =input("번호 000-0000-0000")
# pront(solution(phone+number))




# def solution(phone_number):
#     phone_number_len = len(phone_number)
#     answer = '*'* (phone_number_len-4)

#     answer += phone_number[-4:]
#     return answer


# 파일 입출력 g
# 상대 경로 내위치에서 -> 하고싶은곳 
# . 현재위치 c/test
# .. c(전 경로)
# .현재위치 c/test/test1
# . test12.py




# f.write("""f = open("./test.txt",'r')
# f.write("""hi
#   bye""")
# f.close()





# fr = open("./8888.txt",'r',encoding="UTF-8")
# lines = fr.readlines() 
# # lines = ["빅테이터", "". "AI"]
# for line in lines:
#     # print(line)
# fr.close()



#  c & p

fr = open("./8888.txt",'r',encoding="UTF-8")
lines = fr.readlines() 
fr.close()

fw = open("./8888.txt","w",encoding="UTF-8")
for line in lines:
    line = line.strip()
    if line =="한글":
        fw.write("ML")
    elif lines == "쓰기":
        fw.write("글쓰기\n\\")
    else:
       fw.write(f"{line}")
    fw.write("\n")
fw.close()









fr = open ("./1234.txt","r",encoding="UTF-8")
lines = fr.readlines()
fr.close

fw = open ("./1234.txt','w',encoding="UTF-8")
for line in lines:
    update_text = input(f"전문장 : {line}\n 바꿀 문장(취소는c) :\t")
    if update_text == 'c':
        fw.write(line.strip())
    else:
        fw.write(update_text)
    fw.write("\n")
fw.close() 






# hi = "hi"
# f =open("./test2/ino")
# f.write("""f = open("./test.txt",'r')
# f.write("hi1\n")
# f.close()
# f = open("/test.txt,'r'")
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()





# f = open("/test.txt,'r'")
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close())







