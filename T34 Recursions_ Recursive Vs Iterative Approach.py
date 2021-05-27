def factorial_iterative(n):
    fact=1
    for i in range(n): # i ko zero sa chalu karaga
        fact=fact*(i+1)
    return fact


def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial_recursive(n-1)

number=int(input(" Enter the number\n"))
print("Factorial using iterative method",factorial_iterative(number))
print("Factorial using recursive method",factorial_recursive(number))