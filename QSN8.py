import random

# Function to generate a list of 10 random integers between 1 and 100
def generate_random_numbers():
    return [random.randint(1, 100) for _ in range(10)]

# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# Generate random numbers
random_numbers = generate_random_numbers()

# Calculate the average
average = calculate_average(random_numbers)

# Print the generated numbers and the average
print("Random Numbers:", random_numbers)
print("Average:", average)
