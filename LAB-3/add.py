#1. Write a program to add two lists index-wise
l1=[1,2,3,4,5]
l2=[9,8,7,6,5]
l3=[]
for i in range(0,len(l1)):
    t=l1[i]+l2[i]
    l3.append(t)
print(l3)