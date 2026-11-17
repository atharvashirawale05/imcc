
def longest_string(*args):
    longest = max(args, key=len)
    print("Longest string:", longest)
    print("Length:", len(longest))

longest_string("Python", "Programming", "Java", "Computer Science")

