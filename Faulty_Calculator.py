print("Enter first number")
var1=int(input())
print("Enter second number")
var2=int(input())
print("Enter operator")
op=input()
list1=[45,56]
list2=[3,9,6]
if var1 in list1:
    var1=2*var1-var1*var1
if var2 in list2:
    var1=2*var1-var1*var1

result=0.0
if op=='+':
      result=var1+var2
elif op=='*':
      result=var1*var2
elif op=="/" :
    result=var1/var2
print(result)