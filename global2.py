l=10 # Global

def function1(n):
    global l
    print(l)
    l=5 #Local
    m=8 #local
    #first local variable is considered
    #
    #
    # l=l+45
    print(l,m)
    print(n,"\nI have printed")
function1("This is me")
print(l)
#print(m)--it will show error