print("CALCULATOR")

def calc(a, b, operation):
    if operation == '+':
        return f"{a} + {b} = {a + b}"
    elif operation == '-':
        return f"{a} - {b} = {a - b}"
    elif operation == '*':
        return f"{a} * {b} = {a * b}"
    elif operation == '/':
        return f"{a} / {b} = {a / b}"
    else:
        return "Invalid operation"

def start(number1):
    print(" +\n -\n * \n /\n")
    operation = input("Pick an operation: ")
    number2 = float(input("What is the second number? \n"))
    result = calc(number1, number2, operation)  # Pass 'operation' to the calc function
    print(result)
    result_val = float(result.split("=")[-1].strip())  # Extract result value from the string
    return result_val  # Return result_val for use in the main loop

# Start the calculator by asking for the first number
number1 = float(input("What is the first number?\n"))
while True:
    result_val = start(number1)  # Get the result value from the start() function
    decide = input(f"Type 'y' to continue calculating with {result_val} or type 'n' to start a new calculation: ").lower()

    if decide == 'y':
        number1 = result_val  # Use the result of the previous calculation as the first number
    elif decide == 'n':
        number1 = float(input("What is the first number?\n"))  # Start a new calculation
    else:
        print("Invalid input. Please type 'y' or 'n'.")




