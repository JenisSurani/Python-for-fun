# - This equation ((x * 0.04)^2 + (y * 0.1)^2 - 1)^3 - (x * 0.04)^2 * (y * 0.1)^3 <= 0
#   defines a heart shape mathematically.

print('\n'.join(  # Join all rows with a newline to create the shape
    [''.join(  # Join all characters in a row to form a line
        [
            # Heart shape equation: Derived from a mathematical heart curve formula
            # "LoveU" is repeated inside the heart shape using modulus to distribute letters
            ('LoveU'[(x - y) % 5] if ((x * 0.04) ** 2 + (y * 0.1) ** 2 - 1) ** 3 
             - (x * 0.04) ** 2 * (y * 0.1) ** 3 <= 0 else ' ')
            for x in range(-30, 30)  # Moving left to right
        ]
    ) for y in range(15, -15, -1)]  # Moving top to bottom
))

# If a coordinate satisfies the heart equation, we print a letter from "LoveU".
# - Otherwise, we print a space, ensuring the shape looks like a heart.



# Author: Jenis Surani
# Topic: Heart_Shape with LoveU inside it
# Date: 08/02/2025