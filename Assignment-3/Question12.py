# Question12 Write a program to add first seven terms of the following series using a for loop: 11!+22!+33!+⋯ +nn!

# Initialize the sum to 0
total_sum = 0

# Loop through the first 7 terms
for n in range(1, 8):
    # Calculate factorial of n
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    
    # Add n/n! to the total sum
    total_sum += n / factorial

# Print the result
print(f"The sum of the first 7 terms of the series is: {total_sum}")
