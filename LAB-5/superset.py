num={1,2,3,4,5}
print("Original set: ",num)
print("If given set is superset of itself:")
print(num.issuperset(num))
num1 = {1,2,3,4,5,7}
print("num1:", num1)
print("If given set is superset of another set:")
print(num.issuperset(num1))