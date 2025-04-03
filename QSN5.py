# Sample list of temperatures in Celsius
celsius_temperatures = [0, 25, 30, 15, -5]

# Lambda function to convert Celsius to Fahrenheit
fahrenheit_temperatures = list(map(lambda c: c * 9/5 + 32, celsius_temperatures))

# Print the converted list
print(fahrenheit_temperatures)
