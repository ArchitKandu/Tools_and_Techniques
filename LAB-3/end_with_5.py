#5. Write a program to remove all occurrences of item ending with 5 from a list of roll nos
l=[105,207,308,405,555,674,709,800,915,204]
print('List:',l)
nl=[]
for i in range(0,len(l)):
    t=l[i]
    if t%10!=5:
        nl.append(t)
print('New List: ',nl)