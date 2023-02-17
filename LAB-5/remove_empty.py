l1=[(1,2),(),(3,4),(),(5,6),(),(7,8),(),(9,10)]
l2=[]
print('Original:',l1)
for i in range(0,len(l1)):
    if l1[i]!=():
        l2.append(l1[i])
print('Removing Empty:',l2)