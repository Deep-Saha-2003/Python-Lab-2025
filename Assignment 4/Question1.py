# Question1 Write a program in Python to find the square of any number using the function.

# Function to calculate the square of a number
def square(number):
    return number ** 2

# Get user input
num = float(input("Enter a number to find its square: "))

# Call the function and print the result
result = square(num)
print(f"The square of {num} is {result}")
