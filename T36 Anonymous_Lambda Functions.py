#Lambda functions and anonymous function
def add(a,b):
    return a+b


minus=lambda x,y:x-y   # lambda creates one liner function
       #or
#def minus(x,y):
#   return x-y



print(minus(9,4))


def a_first(a):
    return a[1]


a=[[1,4],[5,60],[8,23]]
a.sort(key=a_first)
     #or
#a.sort(key=lambda x:x[1])
print(a)
