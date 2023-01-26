#WAP to form reverse pyramid of numbers for a given number. Ex. for number 4
# 1 2 3 4 3 2 1
#   1 2 3 2 1
#     1 2 1
#       1
n=int(input("Enter Number: "))
space=0
for i in reversed(range(1,n+1)):
    for s in range(1,space+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for k in reversed(range(1,i)):
        print(k,end=" ")
    print("")
    space+=1