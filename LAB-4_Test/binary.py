list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
target=int(input('Enter Target: '))
left, right = 0, len(list1)-1
while left<=right:
    mid=(left+right)//2
    if list1[mid]==target:
        print('Found at:',mid)
        break
    elif list1[mid]<target:
        left=mid+1
    else:
        right=mid-1
if left>right:
    print('Target not Found')