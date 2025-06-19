def safe_divide(float(numerator), float(denominator)):

    try:
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        elif not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
            raise ValueError
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Both numerator and denominator must be numbers."



    
