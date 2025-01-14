# Question8 Write a program in Python to calculate combinatoric C(n,r) using function.

import math

# Function to calculate combinatoric C(n, r)
def combinatoric(n, r):
    # Calculate C(n, r) using the formula n! / (r! * (n - r)!)
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

# Get user input for n and r
n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

# Call the function and calculate C(n, r)
result = combinatoric(n, r)

# Print the result
print(f"C({n}, {r}) = {result}")
