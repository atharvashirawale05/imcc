n=int(input("enter number of elements:"))
arr=list(map(int,input("enter numbers:").split()))
even=[]
odd=[]
for x in arr:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
print(even)
print(odd)

print("even count:",len(even))
print("odd count:",len(odd))