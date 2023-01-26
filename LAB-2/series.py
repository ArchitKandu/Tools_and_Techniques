# WAP to sum the following series S=1+(1+2)+(1+2+3)+...+(1+2+3+...+n)
n=int(input("Enter Number: "))
sum=0
print("Series is: ",end="")
for i in range(1,n+1):
    print("(",end="")
    for j in range(1,i+1):
        sum+=j
        if j<i:
            print(j,end="+")
        else:
            print(j,end="")
    if i<n:
        print(")+",end="")
    else:
        print(")")
print("\nSum is:",sum)