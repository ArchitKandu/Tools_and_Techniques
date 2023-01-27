#9. WAP to find the average of consecutive elements of a list and display its square in a new list.(min 10 elements)
l=[1,3,5,7,9,11,13,15,17,19]
nl=[]
for i in range(0,len(l),2):
    t=(l[i]+l[i+1])/2
    nl.append(t)
print('List:',l)
print('New List:',nl)
sl=[]
for j in range(0,len(nl)):
    t=nl[j]**2
    sl.append(t)
print('Square:',sl)