f=open("harry.txt")
#print(f.tell)#batata hai ki file pointer kaha pa hai ,kaun sa character pa hai
print(f.readline())
#print(f.tell)
print(f.readline())
print(f.tell)
f.seek(10)# reset the file pointer to 10th character
print(f.readline())
print(f.readline())
f.close()
