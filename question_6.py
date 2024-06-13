def main():
    filename = input("Enter the file name to read from: ")
    with open(filename, 'r') as f:
        content = f.read()
        print(content)

if __name__ == "__main__":
    main()
