def main():
    string = input("Enter a string: ")
    substring = input("Enter a substring to check: ")
    
    if substring in string:
        print("Substring '{}' is present in the string.".format(substring))
    else:
        print("Substring '{}' is not present in the string.".format(substring))

if __name__ == "__main__":
    main()
