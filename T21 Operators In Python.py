"""
Operators in python
Arithmetic Operator
Assignment Operator
Comparison Operator
Loginal Operator
Identity Operator
Membership Operator
Bitwise Operator
"""

#Arithmetic Operator
print("5+6 is",5+6)
print("5-6 is",5-6)
print("5*6 is",5*6)
print("5/6 is",5/6)
print("5%6 is",5%6)
print("15//6 is",15//6)
print("5**6 is",5**6)

#Assignment Operator
x=5
print(x)
x+=7
print(x)
x-=7
print(x)
x/=7
print(x)
x%=7    #x=x%7
print(x)


#Comparison Operator
i=8
print(i==5)
#   > >= < <= == !=


#Loginal Operator
a=True
b=False
print(a and b)
print(a or b)

#Identity Operator
print(a is b)
print(a is not b)


#Membership Operator
list=[3,3,2,2,39,35,32]
print(32 in list)
print(32 not in list)

#Bitwise Operator
"""
0=00
1=01
2=10
3=11
"""
print(0 & 1)
print(0 | 1)
