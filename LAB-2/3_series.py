# WAP to print the series as 3 5 7 11 13 17..........n, where n is given by user
n=int(input("Enter Number: "))
for i in range(3,n+1):
    count=0
    for j in range(2,int(i/2)+1):
        if(i%j==0):
            count=1
            break  
    if(count==0):
        print(i,end=" ")