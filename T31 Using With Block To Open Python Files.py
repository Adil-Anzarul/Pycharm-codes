with open("harry.txt") as f:
    a=f.readlines()
    print(a)
"""when opened with with block no need to close the fine
with block is equivalent to 
fopen and fclose

"""


f=open("harry.txt")
print(f.readlines())
f.close()