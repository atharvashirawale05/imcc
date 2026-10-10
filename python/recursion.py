def num(n):
    print(n)
    if n>0:
        num(n-1)
num(8)

def factorial(n):
    fact=1
    for i in range(1,n+1):
         fact=fact * i
    print(fact)
factorial(5)