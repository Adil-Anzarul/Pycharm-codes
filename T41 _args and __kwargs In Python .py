def function_name_print(a,b,c,d,e):
    print(a,b,c,d,e)
function_name_print("harry","arohan","adil","imran","rima")


#args  aur kwargs ka place ma koi aur name v likh sahta hai
def funargs(normal,*args,**kwargs):
    print(type(args))
    print(normal)
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(key,value)

har=["harry","arohan","adil","imran","rima"]
normal="I am a normal argument"
funargs(normal,*har)
"""By convension as tuple is passed
By convension pehla normal argument uska baad args and then kwargs
args and kwargs are optional
i.e funargs(normal) --- will not show error
"""
kw={"Rohan":"monitor","Adil":"Fitness instructor","Harry":"Coordinator"}
funargs(normal,*har,**kw)