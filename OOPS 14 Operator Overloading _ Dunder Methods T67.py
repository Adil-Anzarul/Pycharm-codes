"""opertor overloading"""


class Employee:
    no_of_leaves=8
    def __init__(self,a,b,c):  #this is constructor
        self.name=a
        self.salary=b
        self.role=c

    def printdetails(self):
        return f" The name is {self.name}, salary is {self.salary} and role is {self.role} "

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    def __add__(self, other): #Dunder method
        return self.salary+other.salary
    def __truediv__(self, other):
        return self.salary/other.salary
    def __repr__(self):
        return f"Employee('{self.name}', {self.salary} ,' {self.role}')"
    def __str__(self):
        return f" The name is {self.name}, salary is {self.salary} and role is {self.role} "

emp1=Employee("Harry",345,"Programmer")
emp2=Employee("Rohan",5,"Cleaner")

print(emp1+emp2)
"""mapping operators to functions"""
print(emp1)   #first __str is considered

print(str(emp1))
print(repr(emp1))
