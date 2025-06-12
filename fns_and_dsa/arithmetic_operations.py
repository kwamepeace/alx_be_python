def perform_operation(num1, num2, operation):
    """
    A simple match catch calculator
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Cannot divide by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operation choice. Please choose from add, subtract, multiply, or divide."






