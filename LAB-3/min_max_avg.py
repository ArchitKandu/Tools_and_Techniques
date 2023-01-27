#6. Write a program to find maximum, minimum and average of all elements of a list
l=[26,54,96,76,43,32,1,19,62,89]
min=999
max=0
sum=0
for i in range(0,len(l)):
    if l[i]<min:
        min=l[i]
    if l[i]>max:
        max=l[i]
    sum+=l[i]
print('List:',l)
print('Minimun:',min,' Maximum:',max,' Average:',float(sum/len(l)))