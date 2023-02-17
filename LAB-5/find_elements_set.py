s1={1,2,3,4,5,6,7,8,9,0}
print(s1)
n=int(input("Enter element to search: "))
if n in s1:
    print(n, " is present in the Set")
else:
    print(n," is not present in the Set")