#3. WAP to display the following style o/p for a given string input through keyboard.(Ex.for a string “KIITCSIT”)
    # KIITCSITTISCTIIK
    # KIITCSI  ISCTIIK
    # KIITCS    SCTIIK
    # KIITC      CTIIK
    # KIIT        TIIK
    # KII          IIK
    # KI            IK
    # K              K
    # KI            IK
    # KII          IIK
    # KIIT        TIIK
    # KIITC      CTIIK
    # KIITCS    SCTIIK
    # KIITCSI  ISCTIIK
    # KIITCSITTISCTIIK

s=input("Enter String: ")
rs=s[::-1]
spc1=0
print("")
for i in range(len(s)+1,1,-1):
    print(s[0:i-1],end="")
    for bl1 in range(1,spc1+1):
        print(end=" ")
    print(rs[len(rs)-i+1:len(rs)])
    spc1+=2
spc2=spc1-4
for j in range(2,len(s)+1):
    print(s[0:j],end="")
    for bl2 in range(1,spc2+1):
        print(end=" ")
    print(rs[len(rs)-j:len(rs)])
    spc2-=2
print("")