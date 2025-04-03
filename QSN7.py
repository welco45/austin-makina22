# Define the custom exception class
class NegativeNumberError(Exception):
    pass

# Function that raises NegativeNumberError if the number is negative
def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Error: The number is negative.")
    else:
        print("The number is positive.")

# Demonstration of usage inside a try block
try:
    check_positive(-5)  # This will raise the custom exception
except NegativeNumberError as e:
    print(e)  # Output: Error: The number is negative.
