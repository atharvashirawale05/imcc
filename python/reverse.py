while True:
    n=int(input("enter number of elements:"))
    arr=list(map(int,input(f"enter {n} elements:").split()))
    r=arr[::-1]
    print(r)

    choice=input("want to continue:y/n")
    if choice == "n":
        break