from  abc import ABCMeta,abstractmethod

#             or
#from  abc import ABC,abstractmethod


class Shape(metaclass=ABCMeta):

#     or
#class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0




class Rectangle(Shape):
    type="Rectangle"
    sides=4
    def __init__(self):
        self.length=6
        self.breadth=7

    def printarea(self):
        return  self.length * self.breadth



rect1=Rectangle()
print(rect1.printarea())


#we can't make object of abstract base class
#tryobj=Shape()------it will show error