
def sum_of_numbers(numbers):
    return sum(numbers)

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
total = sum_of_numbers(numbers)
print(f"The sum of the numbers is: {total}")
