n=28
i=9
inp=12
indicator=0
print("Maximum 9 Guesses are provided ")
while(i):
    i=i-1
    print("Enter the number")
    inp=int(input())
    if inp>n:
        print("It is greater")
    elif inp<n:
        print("It is lesses")
    elif inp==n:
        print("You won \n You Guessed the correct number\n And no of Gusses you took = ",9-i)
        indicator=1
        break
    print("You are left with ",i," more gusses")
if indicator==0:
    print("GAME OVER")