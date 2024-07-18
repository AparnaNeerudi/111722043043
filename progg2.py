# This program calculates the area of a rectangle

# Function to calculate area
def calculate_area(length, width):
    return length * width

# Input length and width from user
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

# Calculate area
area = calculate_area(length, width)

# Output the area
print(f"The area of the rectangle with length {length} and width {width} is {area}")
