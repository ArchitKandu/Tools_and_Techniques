# WAP to print the following pattern for n rows. (n to be taken from user)

# A
# C B A
# E D C B A

n=int(input("Enter rows: "))
n*=2
for i in range(1,n+1,2):
    for j in reversed(range(0,i)):
        print(chr(65 + j),end=" ")
    print("")
print("")