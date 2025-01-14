# Question9 Write a program in Python to calculate Power(a,b) using function.

# Function to calculate power a^b
def power(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

# Get user input for a and b
a = float(input("Enter the base number (a): "))
b = int(input("Enter the exponent (b): "))

# Call the function and calculate power(a, b)
result = power(a, b)

# Print the result
print(f"{a} raised to the power {b} is: {result}")
