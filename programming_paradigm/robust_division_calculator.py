def safe_divide(numerator, denominator):

    try:
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        elif not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
            raise ValueError
        result = float(numerator) / float(denominator)
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."



    
