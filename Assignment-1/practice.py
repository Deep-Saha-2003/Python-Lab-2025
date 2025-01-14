# If a five-digit number is input through the keyboard, write a program to reverse the number.

num = int(input("Enter a five-digit number: "))

if 10000 <= num <= 99999:
    rev_num = 0
    while num > 0:
        last_digit = num % 10
        rev_num = (rev_num * 10) + last_digit
        num //= 10

    print(f"Reversed number: {rev_num}")
else:
    print("Enter a valid five-digit number!")
