def main():
    text = input("Enter some text: ")
    filename = input("Enter the file name to write to: ")
    with open(filename, 'w') as f:
        f.write(text)
    print("Text written to", filename)

if __name__ == "__main__":
    main()
