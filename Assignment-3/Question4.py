# Question4 Write a program to print all the ASCII values and their equivalent characters using a while loop.The ASCII values vary from 0 to 255[chr(110) will print ascii character of the value 110. ord('A') will print corresponding ASCII value of 'A']

i = 0

while i <= 255:
    print(f"ASCII value: {i}, Character: {chr(i)}")
    i += 1

# ASCII values and their corresponding characters:
# 0: 
# 1: ☺
# 2: ☻
# 3: ♥
# 4: ♦
# ...
# 65: A
# 66: B
# 67: C
# ...
# 97: a
# 98: b
# 99: c
# ...
# 255: ÿ