# Question4 Write a program in Python to calculate H.C.F using while loop.

# Get user input for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Initialize the smaller number to start checking for HCF
if num1 > num2:
    smaller = num2
else:
    smaller = num1

# Using a while loop to find HCF
while smaller > 0:
    if num1 % smaller == 0 and num2 % smaller == 0:
        hcf = smaller
        break
    smaller -= 1

# Print the result
print(f"The HCF of {num1} and {num2} is: {hcf}")
