import time

initial =time.time()
k=0
while(k<45):
    print("This is Adil Anzarul")
    #time.sleep(2)
    k+=1
print("while loop ran in ",time.time()-initial,"seconds")


initial2=time.time()
for i in range(45):
    print("This is Adil Anzarul")
print("for loop ran in ",time.time()-initial2,"seconds")



"""To print local time"""
localtime=time.asctime(time.localtime(time.time()))
print(localtime)