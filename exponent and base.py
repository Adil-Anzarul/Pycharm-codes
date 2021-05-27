
def power():
    a = int(input("Enter the base\n"))
    b = int(input("Enter the power\n"))
    pro = 1
    if b > 0:
        for i in range(b):
            pro *= a
    elif b < 0:
        b = b * (-1)
        for i in range(b):
            pro *= a
        pro = 1 / (pro)
    print("The required result is ---------\n", pro)

if __name__ == '__main__':
    power()