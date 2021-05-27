list1=["Harry","Larry","Carry","marie"]

for item in list1:
    print(item)
list2=[["Harry",10],["Larry",20],["Carry",52],["marie",100]]
for item, lollypop in list2 :
    print(item," and lollypop is" , lollypop)
dict1=dict(list2)
print(dict1)
for item, lollypop in dict1.items() :
    print(item," and lollypop is" , lollypop)


"""for only printing keys"""
for item in dict1:
    print(item)

"""to print integer ifrom list which are greater than 6"""
items=[int,float,"Harry",2,5,45,85,2225,2225,54,36,-10]
for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)