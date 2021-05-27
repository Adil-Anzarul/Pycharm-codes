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

harry=Employee("Harry",5245,"Instructor")
rohan=Employee("Rohan",5875,"Student")

rohan.change_leaves(45)
print(harry.no_of_leaves)

Employee.change_leaves(852)
print(harry.no_of_leaves)
print(rohan.no_of_leaves)
