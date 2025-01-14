# Q13. If a five-digit number is input through the keyboard, write a program to print a new number 
# by adding one to each of its digits. For example if the number that is input is 12391 then the 
# output should be displayed as 23402. 

number = int(input("Enter a five-digit number: "))

# Check if the number is a valid five-digit number
if 10000 <= number <= 99999:
    new_number = 0
    place_value = 1  # Used to build the new number by place value

    while number > 0:
        digit = number % 10         # Get the last digit
        new_digit = (digit + 1) % 10  # Add 1 and handle cases where 9 + 1 becomes 0
        new_number = new_digit * place_value + new_number  # Reconstruct the number from the last digit
        place_value *= 10           # Move to the next place value
        number //= 10               # Remove the last digit

    print(f"The new number is: {new_number}")
else:
    print("Please enter a valid five-digit number!")
