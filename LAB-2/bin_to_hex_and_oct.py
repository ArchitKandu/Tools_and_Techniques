#6. WAP to convert a binary number to its equivalent octal & hexa-decimal number system

bin=input("Enter binary: ")
dec=int(bin,2)
print("\nBinary:",bin)
print("Octal:",oct(dec))
print("Hexadecimal:",hex(dec))