#8. Write a program to count the length of each component of a list and present it in a new list
l=['STRING1','STRING2','','','STRING3','','STRING4','','','STRING5']
lengths=[]
for i in range(0,len(l)):
    t=len(l[i])
    lengths.append(t)
print('List:',l)
print('Lengths:',lengths)