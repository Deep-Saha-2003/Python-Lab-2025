# Question7 Write a program in Python to check whether an inputted number is palindrome.

# Function to check if a number is palindrome
def is_palindrome(number):
    # Convert the number to string to easily compare the original and reversed number
    str_num = str(number)
    # Check if the number is equal to its reverse
    if str_num == str_num[::-1]:
        return True
    else:
        return False

# Get user input
num = int(input("Enter a number to check if it's a palindrome: "))

# Call the function and check if the number is a palindrome
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
