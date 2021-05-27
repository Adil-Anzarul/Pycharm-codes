"""MULTIPLE INHERITANCE"""


class Employee:
    var=8
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

class Player:
    var=9
    no_of_games=4
    def __init__(self,name,game):
        self.name=name
        self.game=game

    def printdetails(self):
        return f" The name is {self.name}, Game  is {self.game} "

#class Coolprogrammer(Employee,Player):
class Coolprogrammer(Player,Employee):   #order is important
    #var=10
    language="C++"
    def printlanguage(self):
        print(self.language)
    pass


harry=Employee("Harry",5245,"Instructor")
rohan=Employee("Rohan",5875,"Student")

shubham=Player("Shubham",["Cricket","Football"])
# karan=Coolprogrammer("Karan",2555,"Coolprogrammer")
karan=Coolprogrammer("Karan","WWe")
det=karan.printdetails()
# karan.printlanguage()
# print(det)

print(karan.var)



