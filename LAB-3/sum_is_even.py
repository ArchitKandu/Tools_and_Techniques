#10. WAP to display all integers within the range 240-800 whose sum of digits is an even number
print("Numbes are: ")
for i in range(240,801):
    sum=0
    t=i
    while t>0:
        sum+=t%10
        t=t//10
    if sum%2==0:
        print(i,end=' ')