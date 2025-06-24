#first attempt at calculator app

      
# calculator.py

print("Welcome to the Calculator!")

# Get the first number from the user
num1 = float(input("Enter the first number: "))

# Get the operation
operation = input("Enter an operation (+, -, *, /): ")

# Get the second number
num2 = float(input("Enter the second number: "))

# Do the calculation
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

# Show the result
print("Result:", result)
