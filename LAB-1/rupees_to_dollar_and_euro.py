#WAP to take input from user in rupees and find its equivalent in dollar and factorial of it in euro
rups=int(input("Rupees: "))
dollar = rups * 0.012
fac = 1
for i in range(1,rups+1):
  fac = fac*i
euro = fac * 0.011
print("Dollar: ",dollar)
print("Euro: ",euro)