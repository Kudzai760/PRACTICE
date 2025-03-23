def get_valid_number():
    """
    Continuously prompt the user for a valid number until one is entered.

    Returns:
        float: The valid number entered by the user.
    """
    while True:
        try:
            # Prompt the user for input
            user_input = input("Enter a number: ")

            # Attempt to convert the input to a float
            number = float(user_input)
            return number  # Return the valid number
        except ValueError:
            # Handle invalid input (non-numeric)
            print("Invalid input. Please enter a valid number.")



# Example usage
if __name__ == "__main__":
    valid_number = get_valid_number()
    print(f"You entered a valid number: {valid_number}")