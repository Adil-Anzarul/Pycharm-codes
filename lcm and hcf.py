print("This program is gonna find lcm and hcf of two numbers------------------")
print("Enter two numbers--------------------------")
var1=int(input())
var2=int(input())
a=var1
b=var2
while 1:
    if var1>var2:
        var1=var1-var2
    elif var2>var1:
        var2=var2-var1
    elif var1==var2:
        hcf=var1
        print("The hcf of given two numbers is ",hcf)
        break
for i in range(1,a*b+1):
    if i%a==0 and i%b==0:
        lcm=i
        print("The lcm of given two numbers is ",lcm)
        break