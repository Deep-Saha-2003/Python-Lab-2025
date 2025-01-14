# Question10 Write a program in Python to calculate factorial of a natural number.

# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Get user input for the number
num = int(input("Enter a natural number to calculate its factorial: "))

# Check if the number is non-negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Call the function and calculate factorial
    result = factorial(num)
    # Print the result
    print(f"The factorial of {num} is: {result}")
