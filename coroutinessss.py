# this prog. is to search a character from list
#   by using coroutines

def search():
    import time
    time.sleep(5)
    list1=[chr(i) for i in range(ord('A'),ord('Z')+1) ]
    # print(list1)

    while 100:
        text=(yield )
        if text in list1:
            print("Text Found")
        else:
            print("Text not found")


def input_text():
    print("Enter a character u wanna search")
    c=input().upper()
    return c

s=search()
next(s)
s.send(input_text())
s.send(input_text())
s.send(input_text())
s.close()


