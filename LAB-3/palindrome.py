#11. Python program to check whether elements of the list is palindrome or not
l=[1,2,3,4,5,5,4,3,2,1]
nl=l[::-1]
if nl==l:
    print('List is Palindrome')
else:
    print('List is not Palindrome')