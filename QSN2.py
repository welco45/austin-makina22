def calculate_average(*args):
    """
    Calculates the average of a variable number of numeric arguments.

    Parameters:
    *args (float or int): A variable number of numeric values.

    Returns:
    float: The average of the provided numbers, or None if no numbers are given.
    """
    if not args:
        return None
    return sum(args) / len(args)