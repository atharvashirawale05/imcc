arr=[]
n=int(input("enter size of array:"))
for i in range(n):
    element=int(input("enter elements:"))
    arr.append(element)
max=arr[0]
for i in range(n):
    if arr[i]>max:
        max=arr[i]
print("maximum:",max)