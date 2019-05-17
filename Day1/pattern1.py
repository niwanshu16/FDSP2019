n=int(input("Enter the number of lines"))
count=0
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=' ')
        count=count+1
        print(count)
    
       
