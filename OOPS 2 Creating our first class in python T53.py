class Employee:
    no_of_leaves=8
    pass
harry=Employee()
rohan=Employee()

harry.name="Harry"
harry.salary=4587
harry.role="Instructor"

rohan.name="Rohan"
rohan.salary=2854
rohan.role="Student"

print("1-> ",Employee.no_of_leaves)

print("2-> ",rohan.__dict__)
rohan.no_of_leaves=154
print("3-> ",rohan.__dict__)

print("4-> ",Employee.no_of_leaves)
print("5-> ",rohan.no_of_leaves)

Employee.no_of_leaves=41
print(Employee.no_of_leaves)
print("5'-> ",rohan.no_of_leaves)

