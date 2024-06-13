def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        return "Invalid operator"

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")
result = calculator(a, b, operator)
print(f"The result is: {result}")
