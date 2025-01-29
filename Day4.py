# Take input for the positive integer n
n = int(input("Enter a positive integer: "))

# Initialize a variable to store the sum
even_sum = 0

# Calculate the sum of all even numbers between 1 and n
for num in range(2, n + 1, 2):  # Start at 2, step by 2 to get even numbers
    even_sum += num

# Print the result
print("The sum of all even numbers between 1 and", n, "is:", even_sum)
