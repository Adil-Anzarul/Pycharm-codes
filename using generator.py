"""To find fatorial and fibonacci seris using generator"""


def fact(n):
    pro=1
    for i in range(1,n+1):
        pro=pro*i
    yield pro

# 0 1 1 2 3 5 8 13
def fib(n):
    ls=[0,1]
    for i in range(2,n):
        ls.append(ls[i-1]+ls[i-2])
    yield ls[n-1]



n=int(input("Enter a number\n"))
f1=fact(n)
print(f1.__next__())
f2=fib(n)
print(f2.__next__())


