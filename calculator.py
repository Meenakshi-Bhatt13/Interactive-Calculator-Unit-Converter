
# 1. BASIC ARITHMETIC OPERATIONS

def calculator():
    print("\n--- BASIC CALCULATOR ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter your choice (1-4): ")

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice!")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", num1 + num2)

        elif choice == "2":
            print("Result:", num1 - num2)

        elif choice == "3":
            print("Result:", num1 * num2)

        elif choice == "4":
            if num2 == 0:
                print("Error! Division by zero is not allowed.")
            else:
                print("Result:", num1 / num2)

    except ValueError:
        print("Invalid input! Please enter numbers only.")


# 2. CURRENCY CONVERTER

def currency_converter():
    print("\n--- CURRENCY CONVERTER ---")
    print("1. INR to USD")
    print("2. USD to INR")

    choice = input("Enter your choice (1-2): ")

    if choice not in ["1", "2"]:
        print("Invalid choice!")
        return

    try:
        amount = float(input("Enter amount: "))

        if amount < 0:
            print("Amount cannot be negative.")
            return

        rate = float(input("Enter current USD to INR exchange rate: "))
        if rate <= 0:
            print("Exchange rate must be greater than zero.")
            return

        if choice == "1":
            result = amount / rate
            print(f"{amount:.2f} INR = {result:.2f} USD")

        elif choice == "2":
            result = amount * rate
            print(f"{amount:.2f} USD = {result:.2f} INR")

    except ValueError:
        print("Invalid input! Please enter numbers only.")


# 3. DISTANCE UNIT CONVERTER

def distance_converter():
    print("\n--- DISTANCE CONVERTER ---")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")

    choice = input("Enter your choice (1-2): ")

    if choice not in ["1", "2"]:
        print("Invalid choice!")
        return

    try:
        distance = float(input("Enter distance: "))

        if distance < 0:
            print("Distance cannot be negative.")
            return

        if choice == "1":
            result = distance * 0.621371
            print(f"{distance} KM = {result:.2f} Miles")

        elif choice == "2":
            result = distance / 0.621371
            print(f"{distance} Miles = {result:.2f} KM")

    except ValueError:
        print("Invalid input! Please enter a number.")

# 4. TEMPERATURE CONVERTER

def temperature_converter():
    print("\n--- TEMPERATURE CONVERTER ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter your choice (1-2): ")

    if choice not in ["1", "2"]:
        print("Invalid choice!")
        return

    try:
        temperature = float(input("Enter temperature: "))
        if choice == "1":
            result = (temperature * 9/5) + 32
            print(f"{temperature}°C = {result:.2f}°F")

        elif choice == "2":
            result = (temperature - 32) * 5/9
            print(f"{temperature}°F = {result:.2f}°C")

    except ValueError:
        print("Invalid input! Please enter a number.")


# 5. MAIN MENU

def main():

    while True:

        print("\n====================================")
        print("   INTERACTIVE CALCULATOR")
        print("       & UNIT CONVERTER")
        print("====================================")

        print("1. Basic Calculator")
        print("2. Currency Converter")
        print("3. Distance Converter")
        print("4. Temperature Converter")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            calculator()

        elif choice == "2":
            currency_converter()

        elif choice == "3":
            distance_converter()

        elif choice == "4":
            temperature_converter()

        elif choice == "5":
            print("\nThank you for using the program!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please select between 1 and 5.")


# PROGRAM EXECUTION


main()
