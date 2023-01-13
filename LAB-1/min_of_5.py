# WAP to check minimum of 5 numbers (user input)
min = 99999
num = []
for i in range(0,5):
    ele = int(input('Enter number: '))
    num.append(ele)
    if min > ele:
        min = ele
print('\nMinimum is: ',min)