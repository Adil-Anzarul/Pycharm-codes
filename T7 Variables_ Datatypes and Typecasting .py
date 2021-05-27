var1="Hellow world"
var2=4
var3=36.7
#Python automatically assign datatype to variable  >> intelligent
print(var1)
print(type(var1))
print(type(var2))
print(type(var3))
print(var2+var3)
var4="Adil"
print(var1+var4)
"""Concatinate string"""
var5="40"
var6="100"
print(var5+var6)
print(int(var5)+int(var6))
"""
int()
str()
float()
for Typecasting
"""
"""if u wanna print hellow world 10 times then """
print(10*"Hellow world\n")
# now
print(10*str(int(var5)+int(var6)))
print(10*int(var5)+int(var6))
print(10*(str(int(var5)+int(var6))+"\n"))
"""to take input from user"""
print("Enter your number")
inpnum=input()
""" inpnum is a variable 
        input is stored as string"""
print(type(inpnum))
#print(inpnum+10) <<It will shoe error
print(int(inpnum)+10)