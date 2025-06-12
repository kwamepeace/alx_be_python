def perform_operation (num1, num2, operator):
    """
    A simple match catch calculator
    """
    match operator:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "Cannot divide by zero"
            else:
                return num1 / num2






