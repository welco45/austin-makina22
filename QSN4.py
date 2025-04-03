# List of names
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Write names to a file
with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

# Read and print names from the file
with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())