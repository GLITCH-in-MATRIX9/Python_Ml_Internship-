def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

def main():
    number = int(input("Enter a number: "))
    digit_sum = sum_of_digits(number)
    print("Sum of digits:", digit_sum)

if __name__ == "__main__":
    main()
