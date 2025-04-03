def divide_numbers(numerator, denominator):
    try:
        # Attempt division
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        # Handle division by zero
        print("Error: Cannot divide by zero.")
    except TypeError:
        # Handle invalid input types
        print("Error: Invalid input types. Both arguments must be numbers.")
