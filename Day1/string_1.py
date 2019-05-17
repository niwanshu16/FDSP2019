s=str(input("Enter the string "))
if(ord(s[0])>=65 and ord(s[0])<=97):
    m=ord(s[0])+32
    s2[0]=chr(m)
for i in s[1:]:
    if(ord(i)>=97 and ord(i)<=128):
        s2=chr(ord(i)-32)
print(s2)
