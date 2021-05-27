# PUBLIC
# can be accesed easily
#
# PROTECTED
# class+child class
#
# PRIVATE
# only inside class
# it is done by name mangling
# variable is given name as
#       _Classname__varname


class Employee:
    var=8 #public variable
    _protec=9#protected variable
    __private=98#private variable

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

    @classmethod
    def from_dash(cls,string):
        params=string.split("-")
        print(params)
        return cls(params[0],params[1],params[2])

    @staticmethod
    def printgood(str):
        print("This is good "+str)
        return 89

emp=Employee("harry",1452,"programmer")
print(emp._protec)

# print(emp.__private)
print(emp._Employee__private)  #name mangling
