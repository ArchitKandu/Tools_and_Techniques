tup=(1,2,3,4,3,2,1)
temp=tup
for i in tup:
    if temp.count(i)>1:
        print(i,'REPEATED!')
        list1=list(temp)
        list1.remove(i)
        temp=tuple(list1)