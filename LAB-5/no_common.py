s1={'a','b','c'}
s2={'d','e','f'}
s3=s1.intersection(s2)
if s3==set():
    print('No Common Elements!')
else:
    print('Common Elements:',s3)