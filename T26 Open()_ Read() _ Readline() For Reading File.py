f=open("Harry.txt","rt")# open returns file pointers
content=f.read()#it will read the whole file
print(content)
#content=f.read(3) # it will print 3 characters
#print(content)

#content=f.read(3)#it will print next 3 characters
#print(content)


#for printing character line by line
for char in content:
    print(char)

print(f.readline())
print(f.readline())
print(f.readline())

f.close()



#for printing line by line
g=open("Harry.txt")
for line1 in g:
    print(line1,end="")


#print("\n",type(g))
g.close()


"""
if f.read is used 
  then file pointer (here f)
    become empty
     So, be carefull for further use
"""
print()
h=open("Harry.txt")
print(h.readlines())#it will print list of lines
h.close()


