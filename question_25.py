def copy_file(src, dest):
    with open(src, 'r') as file:
        content = file.read()
    with open(dest, 'w') as file:
        file.write(content)

src = 'source.txt'  # Change this to your source file path
dest = 'destination.txt'  # Change this to your destination file path
copy_file(src, dest)
print("File copied successfully.")
