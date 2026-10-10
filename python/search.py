while True:
    n=int(input("enter number of elememts:"))
    arr=list(map(int,input(f"enter{n} elements:").split()))
    x=int(input("enter number to search:"))
    if x in arr:
        print(f"element {x} found")
    else:
        print("element not found")
    choice=input("do you want to continue: y/n")

    if choice == "n":
        break

