class A:
    classvar1="I am a class variable in class A"
    def __init__(self):
        self.var1="I am inside class A's constructor"
        #self.classvar1="Instance var in class A"

class B(A):
    pass
    #classvar1 = "I am in class B"

""" First of all it looks for instance variables (first of B than A) and then class variable (B then A)
This is overriding"""
a=A()
b=B()

print(b.classvar1)
