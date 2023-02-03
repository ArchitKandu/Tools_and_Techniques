list1=[25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
list2,list3,list4=[],[],[]
print('List:',list1)
l=len(list1)-1
list1.sort()
print('Sorted List:',list1)
for i in range(0,len(list1),4):
    if i+3<l:
        o=list1[i+1]+list1[i+3]
        e=list1[i]+list1[i+2]
    elif i==l:
        o=0
        e=list1[i]
    list2.append(o)
    list3.append(e)
print('Odd consecutive:',list2)
print('Even Consecutive:',list3)
for j in range(0,len(list2)):
    p=list2[j]*list3[j]
    list4.append(p)
print('Product: ',list4)