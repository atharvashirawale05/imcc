arr = list(map(int, input("Enter elements: ").split()))

n = len(arr) + 1

expected = n * (n + 1) // 2
actual = sum(arr)

print("Missing number:", expected - actual)