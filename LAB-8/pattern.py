# WAP to print following output.
# Input: [4237,6389,7257,4216,5784,5467,7234,5789]
# Output: [4239,6387,7217,4256,5484,5767,5234,7789]

n=int(input('Enter digit of number: '))
print('Enter List: ')
l1=[]
rl1=[]
for i in range(0,2*n):
    t=input('Enter number: ')
    l1.append(t)
j = -1
for i in range(0,2*n,2):
    t1=list(l1[i])
    t2=list(l1[i+1])

    t1[j], t2[j] = t2[j], t1[j]
    j-=1

    s1="".join(t1)
    s2="".join(t2)

    rl1.append(s1)
    rl1.append(s2)

print('Original:',l1)
print('Result:',rl1)