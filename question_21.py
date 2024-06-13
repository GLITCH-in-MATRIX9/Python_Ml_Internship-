def count_occurrences(lst, element):
    return lst.count(element)

lst = list(map(int, input("Enter list elements separated by spaces: ").split()))
element = int(input("Enter the element to count: "))
count = count_occurrences(lst, element)
print(f"The element {element} occurs {count} times in the list.")
