l1=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
print('Original:',l1)
for i in range(0,len(l1)):
    new_list=list(l1[i])
    mid=int(len(new_list)/2)
    new_list[mid]=99999
    l1[i]=tuple(new_list)
print('Updated:',l1)