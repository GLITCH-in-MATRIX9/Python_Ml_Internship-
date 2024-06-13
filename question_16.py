from collections import Counter

def count_characters(s):
    return Counter(s)

s = input("Enter a string: ")
char_count = count_characters(s)
for char, count in char_count.items():
    print(f"{char}: {count}")
