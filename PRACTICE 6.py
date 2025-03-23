def divide_numbers(numerator, denominator):
    """
    Divide two numbers and handle exceptions for division by zero and invalid input types.

    Parameters:
        numerator (int or float): The numerator in the division.
        denominator (int or float): The denominator in the division.

    Returns:
        float or None: The result of the division if successful, otherwise None.
    """
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Both numerator and denominator must be numbers.")
    return None


# Example usage Print(divide_numbers(10, 2))  # Valid division
print(divide_numbers(20, 0))  # Division by zero
print(divide_numbers(20, "a"))  # Invalid input type