s = input()
for i in range(len(s)):
    if(ord(s[i])==32):
        c=s[i+1:]
        k=s[:i+1]
s = c+" " +k
print(s)
input()
