# Updated second attempt

# Added personal touch to calculator name

print("Welcome to Pauls Calculator!")

while True:
    # Get user input
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

    # Show result
    print("Result:", result)
# Added option to continue
    # Ask if user wants to continue
    again = input("Do you want to calculate again? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye!")
        break
