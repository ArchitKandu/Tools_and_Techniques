l=[1,2,3,True,False,3.44,"Hello"]
print(l)
print(len(l))
print(type(l))
print(l[2])
print(l[-2])
print(l[2:5])
l[5]="Hi"
print(l)
l[3:5]=4,5,6 #Replace
print(l)
l.insert(6,7) #Insert
print(l)
l.append(40) #Append only appends single value. To do multi value use for loop
print(l)
l2=["new",41,42,43]
print(l+l2) #Method 1
l.extend(l2) #Method 2
print(l)
l3=l.copy()
print(l3)
l4=list(l)
print(l4)
l.remove(40) #removes all 40 if multiple values in list
print(l)
l.pop(5) #Not mention any range last element is removed
print(l)
del l[5]
print(l)
for i in range(1,len(l3)+1,2):
    print(l3[i],end=" ")
print("")
l5=[25,6,0,46,98,79,56,9]
l5.sort()
print(l5)
l5.sort(reverse=True)
print(l5)