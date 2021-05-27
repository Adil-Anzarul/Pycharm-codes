s1 = input().upper()
s2 = input().upper()
t = ''
for c in s1:
    t+=chr(((ord(c)-ord('A'))+5)%26 +ord('A'))

s2=sorted(s2)
t=sorted(t)

if s2==t:
    print("Yes")
else:
    print("No")



