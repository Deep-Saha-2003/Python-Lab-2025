# Question6 Write a program in Python to print sum of all +ve numbers and all -ve numbers.

# Function to calculate sum of positive and negative numbers
def sum_positive_negative(numbers):
    sum_positive = 0
    sum_negative = 0
    
    for num in numbers:
        if num > 0:
            sum_positive += num
        elif num < 0:
            sum_negative += num
            
    return sum_positive, sum_negative

# Get user input for numbers (space-separated)
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Call the function
positive_sum, negative_sum = sum_positive_negative(numbers)

# Print the result
print(f"Sum of positive numbers: {positive_sum}")
print(f"Sum of negative numbers: {negative_sum}")