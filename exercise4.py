print("Enter no of Rows u wanna print")
var1=int(input())
print("Type 0 or 1")
var2=int(input())
if var2 ==0 :
    for i in range(1,var1+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()

elif var2==1 :
    for i in range(var1,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()