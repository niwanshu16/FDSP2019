c = input().lower()
c=list(c)
for i in range(len(c)):
    if not i%2:
        c[i] = chr(ord(c[i])-32)
for i in c:
    print(i,end='')

input()
