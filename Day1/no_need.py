import math
def search(L,low,high,key):
    while low < high:
        mid =math.floor((low + high)/2)
        if L[mid] == key:
            return 1
        elif L[mid]<key:
            low = mid
        elif L[mid] > key:
            high = mid
    return 0
n,m = map(int,input().split())
L=list(map(int,input().split()))
h = 0
L = sorted(L)
A = list(map(int,input().split()))
B = list(map(int,input().split()))
for i in A:
    x = search(L,0,n,i)
    h+=x
for i in B:
    x = search(L,0,n,i)
    h-=x
print(h)

