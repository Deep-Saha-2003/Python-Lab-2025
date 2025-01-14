# Question2 Write a program in Python to check if a given number is even or odd using the function.

# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Get user input
num = int(input("Enter a number to check if it's even or odd: "))

# Call the function and print the result
result = check_even_odd(num)
print(f"The number {num} is {result}.")
