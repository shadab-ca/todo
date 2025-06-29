# Create an empty list
numbers = []

# Take 5 inputs from the user
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Calculate the sum of the numbers
total = sum(numbers)

# Display the result
print("The sum of the 5 numbers is:", total)
