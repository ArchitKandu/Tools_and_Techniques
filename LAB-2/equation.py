# WAP to evaluate the equation y=x^n where n is a non-negative integer

x=int(input("Enter x: "))
n=int(input("Enter n: "))
if n>=0:
    y = x**n
    print("\nResult is:-\nn:",n," x:",x," y:",y)
else:
    print("\nInvalid value of n !")