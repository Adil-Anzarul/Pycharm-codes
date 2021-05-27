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

    @classmethod
    def from_dash(cls,string):
        params=string.split("-")
        print(params)
        return cls(params[0],params[1],params[2])

    @staticmethod
    def printgood(str):
        print("This is good "+str)
        return 89

karan=Employee.from_dash("Karan-5845-student")
print(karan.printgood("Adil Anzarul"))
Employee.printgood("Adil Anzarul")
