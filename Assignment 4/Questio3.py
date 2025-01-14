# Question3 Write a program in Python to calculate sum of Fibonacci series.

# Function to calculate the sum of Fibonacci series
def fibonacci_sum(n):
    a, b = 0, 1
    total_sum = 0
    for _ in range(n):
        total_sum += a
        a, b = b, a + b
    return total_sum

# Get user input
terms = int(input("Enter the number of terms in Fibonacci series: "))

# Call the function and print the result
result = fibonacci_sum(terms)
print(f"The sum of the first {terms} terms of the Fibonacci series is: {result}")
