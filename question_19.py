import string

def remove_punctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation))

s = input("Enter a string: ")
no_punctuation_string = remove_punctuation(s)
print(no_punctuation_string)
