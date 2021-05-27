def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
num=input("Enter the term of fibonacci series:\n")
print(fibonacci(int(num)))