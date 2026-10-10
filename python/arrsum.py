n = int(input("Enter N: "))

arr = list(map(int, input("Enter elements: ").split()))

total = 0

for i in range(n):
    total = total + arr[i]

print("Sum =", total)