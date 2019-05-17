n1=str(input("Enter the string : "))
n2=str(input("Enter the substring : "))
count=0
while True:
    m=n1.find(n2)
    n=m+len(n2)
    n1=n1[n:]
    if(m>=0):
      count=count+1
    else:
        break
print("Substring is repeated by ",count,"times")
