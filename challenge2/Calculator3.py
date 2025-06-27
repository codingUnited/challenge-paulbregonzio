# Calculator attempt 3
# Updated with input validation
print("Welcome to the Paul's Calculator!")

while True:
    try:
        # Get numbers and operation
        num1 = float(input("\nEnter the first number: "))
        operation = input("Enter an operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        # Perform calculation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result = "Error: Cannot divide by zero"
            else:
                result = num1 / num2
        else:
            result = "Error: Invalid operation"

        print("Result:", result)

    except ValueError:
        print("Error: Please enter valid numbers.")

    # Ask if the user wants to go again
    again = input("Do you want to calculate again? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye!")
        break
