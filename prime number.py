def prime():
    n = int(input("Enter a number\n"))
    flag = 0
    for i in range(2, n):
        if (n % i) == 0:
            flag = 1
            break
    if flag == 0:
        print(n, " is prime number")
    elif flag == 1:
        print(n, " is not prime")

if __name__=='__main__':
    prime()