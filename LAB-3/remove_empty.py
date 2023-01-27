#4. WAP to Remove empty strings from the list of strings and display their position
l=['STRING1','STRING2','','','STRING3','','STRING4','','','STRING5']
print('List:',l)
nl=[]
postions=[]
for i in range(0,len(l)):
    if l[i]=='':
        postions.append(i)
    else:
        nl.append(l[i])
print('Removed Position: ',postions)
print('New List:',nl)