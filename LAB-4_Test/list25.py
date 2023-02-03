list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
list2,list3,list4=[],[],[]
print('Enter list: ')
print('List:',list1)
l=len(list1)-1
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