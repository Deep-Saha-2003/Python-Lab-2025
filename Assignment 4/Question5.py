# Question5 Write a program Python to calculate l.c.m using while loop.

# Get user input for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find the larger of the two numbers
if num1 > num2:
    larger = num1
else:
    larger = num2

# Use a while loop to find the LCM
while True:
    if larger % num1 == 0 and larger % num2 == 0:
        lcm = larger
        break
    larger += 1

# Print the result
print(f"The LCM of {num1} and {num2} is: {lcm}")
