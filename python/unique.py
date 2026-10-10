while True:
    n=int(input("enter number of elements:"))
    arr=[]
    for i in range(n):
     x=int(input("enter elements:"))
     arr.append(x)
    print(arr)
    unique=[]
    for x in arr:
     if x not in unique:
        unique.append(x)
    print(unique)

    choice=input("continue?:y/n")
    if choice=="n":
      break
