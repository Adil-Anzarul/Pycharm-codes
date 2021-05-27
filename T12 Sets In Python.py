s=set()
print(type(s))
l=[1,2,3]
s_from_list=set(l)   #it is set
"""
the above two lines can also be written as
s_from_list=set([1,2,3])
"""
print(s_from_list)
print(type(s_from_list))
S=set()
S.add(1)
S.add(1)
S.add(2)
"""Set retains unique value"""
print(S)

#s1=S.intersection({1,2,3,4})
s1=S.union({1,2,3,4})
print(S,s1)


print(max(S))#len max min


print(s.isdisjoint(s1))
S.remove(2)
print(S)