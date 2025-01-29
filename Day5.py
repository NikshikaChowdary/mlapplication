def main():
    # Ask the user to enter a positive integer n
    n = int(input("Enter a positive integer n: "))

    # Task 2: Use a for loop to print all numbers from 1 to n on separate lines
    print("Numbers from 1 to n:")
    for i in range(1, n + 1):
        print(i)

    # Task 3: Use a while loop to calculate the sum of all numbers from 1 to n
    total_sum = 0
    current = 1
    while current <= n:
        total_sum += current
        current += 1

    # Print the sum of all numbers from 1 to n
    print(f"The sum of numbers from 1 to {n} is: {total_sum}")

# Call the main function to execute the program
main()







def calculate_square(n):
    """
    This function takes a single argument n and returns its square.
    """
    return n ** 2

def main():
    # Ask the user to input a positive integer
    number = int(input("Enter a positive integer: "))

    # Call the calculate_square function with the user-provided number
    square = calculate_square(number)

    # Display the result
    print(f"The square of {number} is: {square}")

# Call the main function to execute the program
main()







