
file = open("sample.txt", "r")
content = file.read()

count = 0

for ch in content:
    if ch.lower() in "aeiou":
        count += 1

file.close()

print("Number of vowels:", count)
