def print_pattern1(n):
    for i in range(n):
        for j in range(n):
            print(" * ",end="")
        print()



if __name__ =='__main__':
    print("Enter number of rows")
    n=int(input())
    print_pattern1(n)


