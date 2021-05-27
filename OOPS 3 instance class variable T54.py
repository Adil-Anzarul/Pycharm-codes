class Employee:
    no_of_leaves=8
    def printdetails(self):
        return f" The name is {self.name}, salary is {self.salary} and role is {self.role} "
harry=Employee()
rohan=Employee()

harry.name="Harry"
harry.salary=4587
harry.role="Instructor"

rohan.name="Rohan"
rohan.salary=2854
rohan.role="Student"

print(harry.printdetails())
