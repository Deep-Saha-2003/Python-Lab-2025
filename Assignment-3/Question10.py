# Question10 Write a program to find the range of a set of numbers. Range is the difference between the smallest and biggest number in the list.

numbers = []
print("Enter numbers one by one. Type 'done' to finish:")

while True:
    number = input()
    if number.lower() == 'done':
        break
    try:
        number = int(number)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if numbers:
    smallest = numbers[0]
    largest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    range_value = largest - smallest
    print(f"The range of the entered numbers is: {range_value}")
else:
    print("No numbers were entered.")
