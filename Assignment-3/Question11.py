# Question11 Write a program to fill the entire screen with a smiling face. The smiling face has an ASCII value 1

# Importing sys and os modules to control screen output
import os
import sys

# Get the dimensions of the terminal
rows, columns = os.get_terminal_size()

# Smiling face character using ASCII value 1
smiling_face = chr(1)

# Fill the screen with the smiling face
for _ in range(rows):
    for _ in range(columns):
        sys.stdout.write(smiling_face)
    sys.stdout.write('\n')
