# WAP to convert a decimal number into its equivalent number with base b. Decimal number and b are the user input.

d=int(input("Enter number: "))
b=int(input("Enter base: "))
print("\nDecimal is: ",d)
r=""
while d>0:
    rem=d%b
    r=str(rem)+r
    d=d//b
print("Result is: ",r)