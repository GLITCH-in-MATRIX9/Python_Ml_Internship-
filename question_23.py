def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

choice = input("Convert from (C)elsius or (F)ahrenheit? ").upper()
temp = float(input("Enter the temperature: "))

if choice == 'C':
    print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")
elif choice == 'F':
    print(f"{temp}°F is {fahrenheit_to_celsius(temp)}°C")
else:
    print("Invalid choice.")
