file = open("sample.txt", "r")
content = file.read()
file.close()

words = content.split()

print("Total number of words:", len(words))

unique_words = set(words)

print("Unique words:", unique_words)