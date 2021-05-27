def print_pattern():
    var1=int(input("Enter the number of rown u wanna print\n"))
    for i in range(1,var1+1):
        for j in range(1,i+1):
            print(i,end="")
        print()

print_pattern()