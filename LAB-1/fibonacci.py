#WAP to print a fibonacci sequence by taking term input from the user
n = int(input("Number of terms: "))
a=0
b=1
count=0
if n==1:
  print("Fibonacci Series: ")
  print(a)
else:
  print("Fibonacci Series: ")
  while count < n:
    print(a)
    x=a+b
    a=b
    b=x
    count=count+1