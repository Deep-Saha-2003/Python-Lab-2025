# Question8 Write a program to find the octal equivalent of the entered number.

decimal_number = int(input("Enter a decimal number: "))
octal_number = ""

while decimal_number > 0:
    remainder = decimal_number % 8
    octal_number = str(remainder) + octal_number
    decimal_number = decimal_number // 8

if octal_number == "":
    octal_number = "0"

print(f"The octal equivalent is: {octal_number}")
