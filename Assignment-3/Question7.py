# Question7 Write a program to enter the numbers till the user wants and at the end it should display the count of positive, negative and zeros entered.

positive_count = 0
negative_count = 0
zero_count = 0

while True:
    number = input("Enter a number (or type 'done' to finish): ")
    
    if number.lower() == 'done':
        break
    
    try:
        number = int(number)
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1
        else:
            zero_count += 1
    except ValueError:
        print("Invalid input. Please enter a number.")

print(f"\nYou entered {positive_count} positive number(s), {negative_count} negative number(s), and {zero_count} zero(s).")