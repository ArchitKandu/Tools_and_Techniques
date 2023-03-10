# WAP to print following output.
# Input: [4237,6389,7257,4216,5784,5467,7234,5789]
# Output: [4239,6387,7217,4256,5984,5767,5234,7789]

n=int(input('Enter digit of number: '))
print('Enter List: ')
# l1=[]
l1=['4237', '6389', '7257', '4216', '5784', '5467', '7234', '5789']
# for i in range(0,2*n):
#     t=input('Enter number: ')
#     l1.append(t)
j = -1
for i in range(0,2*n,2):
    t1=l1[i]
    t2=l1[i+1]

    rt=t1[j]
    t1.replace(t1[j],t2[j])
    t2.replace(t2[j],rt)
    
    # l1[i][j], l1[i+1][j]=l1[i+1][j], l1[i][j]
    j-=1

    l1[i]=t1
    l1[i+1]=t2
print('Result: ',l1)