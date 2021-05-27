a=4
b=9
#built in fxn
c=sum((a,b))   # it should have a list or tuple
# i,e c=sum(a,b) -- it will show error
print(c)

"""
def keyword is used to create functions
"""

def function1(a,b):
    print("Hello You are in function1",a+b)
#print(function1())
function1()
function1()
def function2(a,b):
    """ This is afunction which will calculate average of two numbers """
    average =(a+b)/2
    return average
v=function2(5,2)
print(v)
print(function2.__doc__)
# first line written as comment in function is doc string--gives info. about fxn

