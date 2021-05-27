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


#Single inheritance
class Programmer(Employee):
    def __init__(self,a,b,c,languages):
        self.name = a
        self.salary = b
        self.role = c
        self.languages=languages


    def printprog(self):
        return f" The Programmers name is {self.name}, salary is {self.salary} and role is {self.role}  .The languages are {self.languages}"



harry=Employee("Harry",5245,"Instructor")
rohan=Employee("Rohan",5875,"Student")


shubham=Programmer("Shubham",555,"Programmer",["python"])
karan=Programmer("karan",777,"Programmer",["python"])

print(karan.printprog())
