sentence = input("Enter a sentence: ")

words = sentence.split()

longest = max(words, key=len)

print("List of words:", words)
print("Longest word:", longest)