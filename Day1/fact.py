'''Factorial of a number '''

a = int(input())
fact=1
while a>=1:
    fact*=a
    a-=1
print("Factorial is {}".format(fact))

input()
