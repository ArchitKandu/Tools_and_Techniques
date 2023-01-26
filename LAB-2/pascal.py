#2. WAP to generate the pascal triangle pyramid of numbers for a given number. Ex. for number 4
    #     1
    #    1 1
    #   1 2 1
    #  1 3 3 1
    # 1 4 6 4 1
n=int(input("Enter rows: "))
for i in range(0,n):
    for s in range(1,(n-i)+1):
        print(end=" ")
    result = ' '.join(str(11**i))
    print(result)