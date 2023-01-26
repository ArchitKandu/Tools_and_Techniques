#5. WAP to convert a number with base b into its equivalent decimal number. Number with base b & b are the user input

n=input("Enter number: ")
b=int(input("Enter base: "))
print("\nNumber is:",n)
print("Decimal equivalent is:",int(n,b))