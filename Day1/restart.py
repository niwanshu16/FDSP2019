c = 'RESTART'
c=list(c)
a=1
for i in range(len(c)):
    if ord(c[i])==82 and a==0:
        c[i] = chr(36)
    else:
        a=0
for i in c:
    print(i,end='')
input()
