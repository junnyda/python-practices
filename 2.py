#복습
#80이 짝수인가
#print()


print(f"80은짝수인가{80%2==0}")


#리스트 [2,1,4,6,2,40,50,2,5,32] 와 리스트 [4,6,2,3,9,10,2,3,42,5,4,63]의 교집합 중 
최대값 출력 

# list a =  [2,1,4,6,2,40,50,2,5,32] 
# list b =  [2,1,4,6,2,40,50,2,5,32] 
#set(list a)
#set(list b)
#a.sort()
#b.sort()
#print()


list1 =  [2,1,4,6,2,40,50,2,5,32] 
list2 =  [2,1,4,6,2,40,50,2,5,32] 
union = list(set(list1) & set(list2))
print(union)
union.sort()
print(union[len(union)-1])




#union 합집합

#sort () 라는 메소드를 가지고 이 메소드는 리스트를 정렬된 상태로 변경한다.


