"""
object introspection
type()
id()
dir()
"""


class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        #self.email=f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"


    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self,string):
        print("Setting now")
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None


skillF=Employee("Skill","F")
#print(skillF.email)


print(type(skillF))

print(id("this is a string"))
print(id("this is "))
o="Adil Anzarul"
print(dir(o))
print(dir(skillF)) #it gives all methods that are defined for that


import inspect
print(inspect.getmembers(skillF))



