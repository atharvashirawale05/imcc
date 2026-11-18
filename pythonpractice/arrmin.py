arr=[]
n=int(input("enter the size of array:"))
for i in range(n):
    element=int(input("enter the elements:"))
    arr.append(element)
min=arr[0]
for i in range(n):
    if arr[i]<min:
        min=arr[i]
print(arr)
print("minimum:",min)