
class NegativeNumberError(Exception):
    def __init__(self, number):
        self.number = number
        super().__init__(f"Error: Negative number ({number}) is not allowed.")

def check_positive(number):
    """
    Check if a number is positive. If not, raise NegativeNumberError.

    Parameters:
        number (int or float): The number to check.



    if number < 0:
        raise NegativeNumberError(number)
    print(f"{number} is a positive number.")

    check_positive(10)  # Valid positive number
    check_positive(-5)  # Negative number (will raise an exception)
except NegativeNumberError as e:
    print(e):
    