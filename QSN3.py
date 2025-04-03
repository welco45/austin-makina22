def get_valid_number():
    """
    Repeatedly prompts the user for a valid number until a valid integer is entered.

    Returns:
    int: A valid integer input by the user.
    """
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


while True:
    user_input = get_valid_number()
    print("The number is:", classify_number(user_input))
    break  # Exit loop after a valid integer is entered
