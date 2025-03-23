def calculate_average(*args):
    """
    Calculate the average of a variable number of numeric arguments.

    Parameters:
        *args (float or int): A variable number of numeric arguments.

    Returns:
        float: The average of the provided numbers.


    Raises:
        ValueError: If no arguments are provided.

    Example:
        >>> calculate_average(20, 30, 40)
        20.0
        >>> calculate_average(5, 15, 25, 35)
        20.0
    """
    if not args:
        raise ValueError

    total = sum(args)
    count = len(args)
    return total / count