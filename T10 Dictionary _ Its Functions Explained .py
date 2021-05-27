#Dictionary is nothing but key value pairs---a data type
di={}
print(type(di))
d2={"Harry":"Burger","Rohan":"Fish","SkillF":"Roti","Shubham":{"B":"maggi","L":"roti","D":"Chicken"}}
print(d2)
print(d2["Rohan"])  #Case sensetive
print(d2["Shubham"]["B"])   #Dictionary value can bea dictionary , tuple, list
# but keys should be immtable
d2["Ankit"]="Junk Food"
print(d2)
del d2["Ankit"]


print(d2.copy())  # give copy of d2


d3=d2
"""
it will not make any new copy 
    it acts as pointer and points to dictionary  
         like d2 does
            d2 s also a pointer and it points to itself
            
            so, we should do this 
             d3=d2.copy()
                      """
del d3["Harry"]
print(d3)

print(d2.get("Harry"))

d2.update({"Leena":"Toffie"})
print(d2)
print(d2.keys())
print(d2.items())

