# WAP to print all combination by swapping characters.
#Input: ABC
#Output: ABC, BAC, CBA

def swapcomb(s):
    rl=[s]
    for i in range(1,len(s)):
        tl=list(s)
        tl[0], tl[i] = tl[i], tl[0]
        t = "".join(tl)
        rl.append(t)
    return rl

s=input('Enter String: ')
result=swapcomb(s)
print('Result: ',end='')
for i in result:
    print(i,end=' ')