def safe_divide(numerator, denominator):

     try:
         #Performs the division if the right form of data in submitted
       result = float(numerator) / float(denominator)
       return f"The result of the division is {result}"
         
    # Exception blocks for handling ZeroDivisionError, ValueError and TypeError    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
        
    except ValueError:
        return "Error: Please enter numeric values only."

     except TypeError:
        return "Error: Both numerator and denominator must be numbers."


    
