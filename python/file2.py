file = open("sample.txt", "r")
lines = file.readlines()
file.close()

print("Total number of lines:", len(lines))

print("Second line:", lines[1].strip())
print("Fourth line:", lines[3].strip())