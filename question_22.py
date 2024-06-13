def min_and_max(numbers):
    return min(numbers), max(numbers)

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
min_val, max_val = min_and_max(numbers)
print(f"The minimum value is: {min_val}")
print(f"The maximum value is: {max_val}")
