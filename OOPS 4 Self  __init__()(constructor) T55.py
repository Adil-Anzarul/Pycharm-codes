class Employee:
    no_of_leaves=8
    def __init__(self,a,b,c):  #this is constructor
        self.name=a
        self.salary=b
        self.role=c

    def printdetails(self):
        return f" The name is {self.name}, salary is {self.salary} and role is {self.role} "
harry=Employee("Harry",5245,"Instructor")

print(harry.printdetails())


