def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def main():
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    fib_numbers = fibonacci(n)
    print("The first {} Fibonacci numbers:".format(n), fib_numbers)

if __name__ == "__main__":
    main()
