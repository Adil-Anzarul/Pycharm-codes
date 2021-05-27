def trans():
    list1 = []
    a = []
    print("Enter n and m of nXm matrix ")
    n, m = input(), input()
    n = int(n)
    m = int(m)
    print("Enter the elements of matrix")
    for i in range(0, n):
        a = input().split()
        list1.append(a)
        a = []

    print("Original matrix")
    for i in range(n):
        for j in range(m):
            print(list1[i][j], end=" ")
        print()

    print("Transpose matrix")
    for i in range(m):
        for j in range(n):
            print(list1[j][i], end=" ")
        print()

if __name__ == '__main__':
    trans()