# Q2. The distance between two cities (in km.) is input through the keyboard. Write a program to 
# convert and print this distance in meters, feet, inches and centimeters.

distance_between_two_cities = float(input("Enter the distance between two cities(in km): "));

# 1 kilometer = 1000 metres
km_to_m = distance_between_two_cities * 1000;
print(f"Distance between two cities in metres: {km_to_m} m");

# 1 kilometer = 3280.84 feet
km_to_feet = distance_between_two_cities * 3280.84;
print(f"Distance between two cities in feet: {km_to_feet} feet");

# 1 kilometer = 39,370.1 inches
km_to_inches = distance_between_two_cities * 39370.1;
print(f"Distance between the two cities in inches: {km_to_inches} inches")

# 1 kilometer = 100,000 centimeters
km_to_cm = distance_between_two_cities * 100000;
print(f"Distance between two cities in centimetre: {km_to_cm} cm");