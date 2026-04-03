# Simple calculator
import math

print("==== SIMPLE CALCULATOR ====")

while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nChoose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Result:", num1 + num2)

    elif choice == "2":
        print("Result:", num1 - num2)

    elif choice == "3":
        print("Result:", num1 * num2)

    elif choice == "4":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print("Result:", num1 / num2)

    elif choice == "5":
        num = float(input("Enter number for square root: "))    
        print("Result:", math.sqrt(num))

    else:
        print("Invalid choice")

    again = input("\nDo you want to continue? (yes/no): ")
    if again.lower() != "yes":
        print("Goodbye!")
        break
