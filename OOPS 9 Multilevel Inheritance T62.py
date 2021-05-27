"""Multilevel inheritance"""


class Dad:
    basketball=1

class Son(Dad):
    dance=1
    basketball = 25
    def isDance(self):
        return f"Yes i dance {self.dance} no of times"

class Grandson(Son):


    dance =6
    def isDance(self):
        return f"Jackson yeah! \nYes i dance very awesomely {self.dance} no of times"

darry=Dad()
larry=Son()
harry=Grandson()


print(harry.isDance())
print(harry.basketball)
print(harry.dance)
