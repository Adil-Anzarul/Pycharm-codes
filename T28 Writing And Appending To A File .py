"""
#it will first empty the content and then print
#if file doesnt exixt it will create new file
f=open("Harry2.txt","w")
f.write("Harry bhai bahut achhe hai")
f.close()
"""
"""
f=open("Harry2.txt","a")
# simply last ma add ho jaiaga
f.write("Harry bhai bahut achhe hai\n")
f.close()
"""
"""
f=open("Harry2.txt","a")
# simply last ma add ho jaiaga
a=f.write("Harry bhai bahut achhe hai\n")# f.write fxn returns no. of character 
print(a)#it will print no. of character written
f.close()
"""

#to handle read and write both
f=open("Harry2.txt","r+")
print(f.read())
f.write("Thank you")
f.close()

