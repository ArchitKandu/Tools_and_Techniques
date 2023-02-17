#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Write a Python program to convert a tuple to a string.
t1=('A','R','C','H','I','T')
s=''
for i in t1:
    s=s+i
print(s)


# In[2]:


# 2. Write a Python program to find the repeated items of a tuple.
tup=(1,2,3,4,3,2,1)
temp=tup
for i in tup:
    if temp.count(i)>1:
        print(i,'REPEATED!')
        list1=list(temp)
        list1.remove(i)
        temp=tuple(list1)


# In[3]:


# 3. Write a Python program to convert a list to a tuple.
l1=[1,2,3,4,5]
t1=tuple(l1)
print(t1)


# In[4]:


# 4. Write a Python program to reverse a tuple.
t1=(1,'a',2,'b',3,'c',4,'d',5,'e')
temp=t1
temp=temp[::-1]
print(temp)


# In[5]:


# 5. Write a Python program to remove an empty tuple(s) from a list of tuples.
l1=[(1,2),(),(3,4),(),(5,6),(),(7,8),(),(9,10)]
l2=[]
print('Original:',l1)
for i in range(0,len(l1)):
    if l1[i]!=():
        l2.append(l1[i])
print('Removing Empty:',l2)


# In[6]:


# 6. Write a Python program to replace middle value of tuples in a list.
l1=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
print('Original:',l1)
for i in range(0,len(l1)):
    new_list=list(l1[i])
    mid=int(len(new_list)/2)
    new_list[mid]=99999
    l1[i]=tuple(new_list)
print('Updated:',l1)


# In[7]:


# 7. Write a Python program to get the 5th element and 5th element from last of a tuple.
t1=(1,2,3,4,5,6,7,8,9,0)
print('5th element:',t1[4])
print('Last 5th element:',t1[-5])


# In[8]:


# 8. Write a Python program to check if two given sets have no elements in common.
s1={'a','b','c'}
s2={'d','e','f'}
s3=s1.intersection(s2)
if s3==set():
    print('No Common Elements!')
else:
    print('Common Elements:',s3)


# In[9]:


# 9. Write a Python program to check whether an element exists within a tuple.
t1=(1,2,3,4,5,6,7,8,9,0)
print(t1)
n=int(input("Enter element to search: "))
if n in t1:
    print(n, " is present in the Tuple")
else:
    print(n," is not present in the Tuple")


# In[10]:


# 10. Write a Python program to check if a given value is present in a set or not.
s1={1,2,3,4,5,6,7,8,9,0}
print(s1)
n=int(input("Enter element to search: "))
if n in s1:
    print(n, " is present in the Set")
else:
    print(n," is not present in the Set")


# In[11]:


# 11. Write a Python program to check if a given set is superset of itself and superset of another given set.
num={1,2,3,4,5}
print("Original set: ",num)
print("If given set is superset of itself:")
print(num.issuperset(num))
num1 = {1,2,3,4,5,7}
print("num1:", num1)
print("If given set is superset of another set:")
print(num.issuperset(num1))


# In[12]:


# 12. Write a Python program to create a union, intersection, difference, symmetric difference of sets.
A = {0, 2, 4, 6, 8}
B = {1, 3, 5, 7, 9}
print("Union :", A | B)
print("Intersection :", A & B)
print("Difference :", A - B)
print("Symmetric difference :", A ^ B)


# In[13]:


# 13. Write a Python program to remove the intersection of a 2nd set from the 1st set.
sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Original sets:")
print(sn1)
print(sn2)
print("Remove the intersection of a 2nd set from the 1st set")
sn1-=sn2
print("sn1: ",sn1)
print("sn2: ",sn2)


# In[14]:


# 14.  Write a Python program to update the first set with items that don’t exist in the second set.
set1 = {10, 20, 30}
set2 = {20, 40, 50}

set1.difference_update(set2)
print(set1)


# In[15]:


# 15.  Write a Python program to remove items from the set at once.
set1={1,2,3,4,5}
print(set1)
set1.clear()
print(set1)


# In[16]:


# 16.  Write a Python program to return a set of elements present in Set A or B, but not both.
set1={1,2,3,4,5}
set2={8,6,5,4,3}
set3=set1.union(set2)
print(set3)


# In[17]:


# 17.  Write a Python program to check if two sets have any elements in common. If yes, display the common elements.
set1={1,2,3,4,5}
set2={8,6,5,4,3}
set3=set1.intersection(set2)
if len(set3)>0:
    print("the hav common value",set3)
else:
    print("none in common")


# In[18]:


# 18.  Write a Python program to update set1 by adding items from set2, except common items.
set1={1,2,3,4,5}
set2={8,6,5,4,3}
set3=set2.difference(set1)
for i in set3:
    set1.add(i)
print(set1)


# In[19]:


# 19.  Write a Python program to remove items from set1 that are not common to both set1 and set2.
set1={1,2,3,4,5}
set2={8,6,5,4,3}
set1.intersection_update(set2)
print(set1)

