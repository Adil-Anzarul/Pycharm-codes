while 1:
    print("Enter a number to find weather its prime or not")
    n=int(input())
    indicator=0
    for i in range(2,n):
        if n%i==0:
            indicator=1
            break
    if indicator==0:
        print(f"{n} is prime number\n\n")
    elif indicator==1:
        print(f"{n} is not prime number\n\n")